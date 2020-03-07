import re
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download Sentiment Analysis tools
sid = SentimentIntensityAnalyzer()

hair_dryer_df = pd.read_csv('hair_dryer.tsv', sep='\t')
microwave_df = pd.read_csv('microwave.tsv', sep='\t')
pacifier_df = pd.read_csv('pacifier.tsv', sep='\t')
df_all = [hair_dryer_df, microwave_df, pacifier_df]


#
#  Data Preprocessing
#

for df in df_all:
    # Sort by date
    df['review_date'] = pd.to_datetime(df['review_date'])
    df.sort_values(by=['review_date', 'review_id'], ascending=True, inplace=True)

    # Removing unnecessary columns
    df.drop(columns=['marketplace', 'product_parent', 'product_category'], inplace=True)

    # Converting binary data
    df['vine'].replace({'Y': 1, 'N': 0, 'y': 1, 'n': 0}, inplace=True)
    df['verified_purchase'].replace({'Y': 1, 'N': 0, 'y': 1, 'n': 0}, inplace=True)

    # Cleaning comments
    for i, data in df.iterrows():
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   r"$&#(.*?)#&^"
                                   "]+", flags=re.UNICODE)
        cleaned_body = str(data['review_body']).strip().replace('<BR>', ' ').replace('<br />', ' ')
        cleaned_body = emoji_pattern.sub(r'', cleaned_body)
        cleaned_title = str(data['review_headline']).strip().replace('<BR>', ' ').replace('<br />', ' ')
        cleaned_title = emoji_pattern.sub(r'', cleaned_title)
        df.at[i, 'review_body'] = cleaned_body
        df.at[i, 'review_headline'] = cleaned_title

    # Adding empty columns
    df.insert(loc=len(df.columns), column='keywords', value="")  # Adding keywords column
    df.insert(loc=len(df.columns), column='word count', value=0)  # Adding wordcount column
    df.insert(loc=2, column='review_weight', value=0)  # Adding review weight (for each review for the same prod)
    df.insert(loc=4, column='product_weight', value=0)  # Adding product weight column
    df.insert(loc=7, column='rating_weight', value=0)  # Adding rating weight column
    df.insert(loc=16, column='keyword_count', value=0)  # Adding keyword count column


#
#  Generating new attributes
#

def count_keywords(word_bank, dataframe):
    word_bank = set(word_bank)
    for index in range(len(dataframe.index)):
        review_body = dataframe.loc[index, 'review_body']
        review_words = re.split(r'\W+', review_body)
        if '' in review_words:
            review_words.remove('')
        contain_keyword = set(review_words).intersection(word_bank)
        if contain_keyword:
            dataframe.at[index, 'keywords'] = set(contain_keyword)
            dataframe.at[index, 'keyword_count'] = len(contain_keyword)


def count_words(dataframe):
    for index in range(len(dataframe.index)):
        review_body = dataframe.loc[index, 'review_body']
        review_words = re.split(r'\W+', review_body)
        if '' in review_words:
            review_words.remove('')
        if dataframe is microwave_df and index == 0:
            print(review_words)
            print(len(review_words))
        dataframe.at[index, 'word count'] = len(review_words)


# def generate_freq_list(dataframe):
#     # Generate Frequency Map
#     word_mapping = {}
#     for data in dataframe.iterrows():
#         review = set(re.split(r'\W+', data[1]['review_body']))
#         if '' in review:
#             review.remove('')
#         for word in review:
#             if word not in word_mapping:
#                 word_mapping.update({word: 1})
#             else:
#                 word_mapping.update({word: word_mapping.get(word) + 1})
#
#     # Sort Frequency Map
#     word_mapping = {k: v for k, v in sorted(word_mapping.items(), key=lambda item: item[1], reverse=True)}
#     return word_mapping

# Output word frequency mapping
# output_names = ['hair_dryer', 'microwave', 'pacifier']
# for df in df_all:
#     wordmap = generate_freq_list(df)
#     count = 0
#     with open('%s_word_freq.csv' % output_names[count], 'w') as file:
#         for word in wordmap.keys():
#             file.write('%s, %s\n' % (word, wordmap[word]))
#     count += 1

# Insert word count column
for df in df_all:
    count_words(df)

# Output csv
hair_dryer_df.to_csv(open('Sorted/hair_dryer_sorted.csv', 'w'), index=False)
microwave_df.to_csv(open('Sorted/microwave_sorted.csv', 'w'), index=False)
pacifier_df.to_csv(open('Sorted/pacifier_sorted.csv', 'w'), index=False)

# wordbank = ['bought', 'however', 'love']
# filter_keywords(wordbank, hair_dryer_df)
