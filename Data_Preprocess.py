import re

import pandas as pd
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
        cleaned_body = str(data['review_body']).strip().replace('<BR>', ' ').replace('<br />', ' ').replace('\r', '')
        cleaned_body = emoji_pattern.sub(r'', cleaned_body)
        cleaned_title = str(data['review_headline']).strip().replace('<BR>', ' ').replace('<br />', ' ').replace('\r', '')
        cleaned_title = emoji_pattern.sub(r'', cleaned_title)
        df.at[i, 'review_body'] = cleaned_body
        df.at[i, 'review_headline'] = cleaned_title

    # Adding empty columns
    df.insert(loc=len(df.columns), column='keywords', value="")  # Adding keywords column
    df.insert(loc=len(df.columns), column='word_count', value=0)  # Adding wordcount column
    df.insert(loc=2, column='review_weight', value=0)  # Adding review weight (for each review for the same prod)
    df.insert(loc=4, column='product_weight', value=0)  # Adding product weight column
    df.insert(loc=7, column='rating_weight', value=0)  # Adding rating weight column
    df.insert(loc=16, column='keyword_count', value=0)  # Adding keyword count column


#
#  Generating new attributes
#

def generate_attribute(word_bank, dataframe):
    word_bank = set(word_bank)
    for index in range(len(dataframe.index)):
        review_headline = dataframe.loc[index, 'review_headline']
        review_body = dataframe.loc[index, 'review_body']
        review_words = re.split(r'\W+', review_body)
        if '' in review_words:
            review_words.remove('')

        # Generate keywords
        contain_keyword = set(review_words).intersection(word_bank)
        if contain_keyword:
            dataframe.at[index, 'keywords'] = set(contain_keyword)
            dataframe.at[index, 'keyword_count'] = len(contain_keyword)

        # Generate review length
        dataframe.at[index, 'word_count'] = len(review_words)


bank = ['love', 'good', 'awesome']
# Insert word count column
for df in df_all:
    generate_attribute(bank, df)

# Output csv
hair_dryer_df.to_csv(open('Sorted/hair_dryer_sorted.tsv', 'w'), index=False)
microwave_df.to_csv(open('Sorted/microwave_sorted.tsv', 'w'), index=False)
pacifier_df.to_csv(open('Sorted/pacifier_sorted.tsv', 'w'), index=False)
