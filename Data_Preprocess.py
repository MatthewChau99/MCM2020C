import re

import numpy as np
import pandas as pd

hair_dryer_df = pd.read_csv('hair_dryer.tsv', sep='\t')
microwave_df = pd.read_csv('microwave.tsv', sep='\t')
pacifier_df = pd.read_csv('pacifier.tsv', sep='\t')
df_all = [hair_dryer_df, microwave_df, pacifier_df]

hairdryer_wordbank = open('hairdryer_wordbank.txt', 'r', encoding='utf-8').read().split('\n')
microwave_wordbank = open('microwave_wordbank.txt', 'r', encoding='utf-8').read().split('\n')
pacifier_wordbank = open('pacifier_wordbank.txt', 'r', encoding='utf-8').read().split('\n')

#
#  Data Preprocessing
#

for df in df_all:
    # Sort by date
    df['review_date'] = pd.to_datetime(df['review_date'])
    df.sort_values(by=['review_date', 'review_id'], ascending=False, inplace=True, ignore_index=True)

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
        cleaned_title = str(data['review_headline']).strip().replace('<BR>', ' ').replace('<br />', ' ').replace('\r',
                                                                                                                 '')
        cleaned_title = emoji_pattern.sub(r'', cleaned_title)
        df.at[i, 'review_body'] = cleaned_body
        df.at[i, 'review_headline'] = cleaned_title

    # Adding empty columns
    df.insert(loc=len(df.columns), column='page_number', value=0)  # Adding page number column
    df.insert(loc=len(df.columns), column='keywords', value="")  # Adding keywords column
    df.insert(loc=len(df.columns), column='keyword_count', value=0)  # Adding keyword count column
    df.insert(loc=len(df.columns), column='normalized_keyword_count', value=0.0)  # Adding normalized keyword count
    df.insert(loc=len(df.columns), column='word_count', value=0)  # Adding wordcount column
    df.insert(loc=len(df.columns), column='review_type', value=0)  # Adding review type column
    df.insert(loc=2, column='review_weight', value=0)  # Adding review weight (for each review for the same prod)
    df.insert(loc=4, column='review_count', value=0)  # Adding review count for each product
    df.insert(loc=5, column='product_weight', value=0)  # Adding product weight column
    df.insert(loc=8, column='rating_weight', value=0)  # Adding rating weight column
    df.insert(loc=11, column='vote_ratio', value=0.0)  # Adding vote ratio column
    df.insert(loc=12, column='normalized_vote_ratio', value=0.0)  # Adding normalized vote ratio column


#
#  Generating new attributes
#

def generate_attribute(word_bank, dataframe):
    word_bank = set(word_bank)
    total_votes = np.sum(df['total_votes'])
    review_count = {}

    for index in range(len(dataframe.index)):
        review_body = dataframe.loc[index, 'review_body']
        review_words = re.split(r'\W+', review_body)
        if '' in review_words:
            review_words.remove('')

        # Generating page number
        dataframe.at[index, 'page_number'] = np.ceil((index + 1) / 10)

        # Generate keywords
        contain_keyword = set()
        for word1 in review_words:
            for word2 in word_bank:
                if word2 in word1:
                    contain_keyword.add(word2)
        if contain_keyword:
            dataframe.at[index, 'keywords'] = set(contain_keyword)
            dataframe.at[index, 'keyword_count'] = len(contain_keyword)

        # Generate review length
        dataframe.at[index, 'word_count'] = len(review_words)

        # Generate review types according to its length
        review_length = dataframe.loc[index, 'word_count']
        if 0 <= review_length < 20:
            dataframe.at[index, 'review_type'] = 0  # Sentence
        elif 20 <= review_length < 80:
            dataframe.at[index, 'review_type'] = 1  # Paragraph
        elif review_length >= 80:
            dataframe.at[index, 'review_type'] = 2  # Long Review

        # Generate vote ratio
        dataframe.at[index, 'vote_ratio'] = dataframe.loc[index, 'total_votes'] * 1000 / total_votes

        # Generate review count for each product
        product_id = dataframe.loc[index, 'product_id']
        if product_id not in review_count:
            review_count.update({product_id: 1})
        else:
            review_count.update({product_id: review_count.get(product_id) + 1})

    for index in range(len(dataframe.index)):
        # Generate normalized keyword count
        max_keyword_count = np.max(dataframe['keyword_count'])
        min_keyword_count = np.min(dataframe['keyword_count'])
        keyword_count = dataframe.loc[index, 'keyword_count']
        normalized_keyword_count = (keyword_count - min_keyword_count) / (max_keyword_count - min_keyword_count)
        dataframe.at[index, 'normalized_keyword_count'] = normalized_keyword_count

        # Generate normalized vote ratio
        max_vote_ratio = np.max(dataframe['vote_ratio'])
        min_vote_ratio = np.min(dataframe['vote_ratio'])
        votes_ratio = dataframe.loc[index, 'vote_ratio']
        normalized_vote_ratio = (votes_ratio - min_vote_ratio) / (max_vote_ratio - min_vote_ratio)
        dataframe.at[index, 'normalized_vote_ratio'] = normalized_vote_ratio

        # Generate review count for each product
        dataframe.at[index, 'review_count'] = review_count.get(dataframe.loc[index, 'product_id'])


generate_attribute(hairdryer_wordbank, hair_dryer_df)
generate_attribute(microwave_wordbank, microwave_df)
generate_attribute(pacifier_wordbank, pacifier_df)

# Output csv
hair_dryer_df.to_csv(open('Sorted/hair_dryer_sorted.tsv', 'w'), index=False)
microwave_df.to_csv(open('Sorted/microwave_sorted.tsv', 'w'), index=False)
pacifier_df.to_csv(open('Sorted/pacifier_sorted.tsv', 'w'), index=False)
hair_dryer_df.to_csv(open('Sorted/hair_dryer_sorted.csv', 'w'), index=False)
microwave_df.to_csv(open('Sorted/microwave_sorted.csv', 'w'), index=False)
pacifier_df.to_csv(open('Sorted/pacifier_sorted.csv', 'w'), index=False)
