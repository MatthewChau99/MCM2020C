import re

import pandas as pd

hair_dryer_df = pd.read_csv('hair_dryer.tsv', sep='\t')
microwave_df = pd.read_csv('microwave.tsv', sep='\t')
pacifier_df = pd.read_csv('pacifier.tsv', sep='\t')
df_all = [hair_dryer_df, microwave_df, pacifier_df]

# Sort by date
# for df in df_all:
#     df['review_date'] = pd.to_datetime(df['review_date'])
#     df.sort_values(by=['review_date', 'review_id'], ascending=True, inplace=True)

# Removing unnecessary columns
for df in df_all:
    df.drop(columns=['marketplace', 'product_parent', 'product_category'], inplace=True)

# Converting binary data
for df in df_all:
    df['vine'].replace({'Y': 1, 'N': 0}, inplace=True)
    df['verified_purchase'].replace({'Y': 1, 'N': 0}, inplace=True)

# Cleaning comments
for df in df_all:
    for i, data in df.iterrows():
        cleaned_body = str(data['review_body']).strip().replace('<BR>', ' ').replace('<br />', ' ')
        df.at[i, 'review_body'] = cleaned_body

# Adding keywords column
for df in df_all:
    df.insert(loc=len(df.columns), column='keywords', value="")

# Adding wordcount column
for df in df_all:
    df.insert(loc=len(df.columns), column='word count', value=0)


def generate_freq_list(dataframe):
    # Generate Frequency Map
    word_mapping = {}
    for data in dataframe.iterrows():
        review = set(re.split(r'\W+', data[1]['review_body']))
        if '' in review:
            review.remove('')
        for word in review:
            if word not in word_mapping:
                word_mapping.update({word: 1})
            else:
                word_mapping.update({word: word_mapping.get(word) + 1})

    # Sort Frequency Map
    word_mapping = {k: v for k, v in sorted(word_mapping.items(), key=lambda item: item[1], reverse=True)}
    return word_mapping


def filter_keywords_and_count_words(word_bank, dataframe):
    word_bank = set(word_bank)
    index = 0
    for data in dataframe.iterrows():
        review_words = set(re.split(r'\W+', data[1]['review_body']))
        if '' in review_words:
            review_words.remove('')
        contain_keyword = review_words.intersection(word_bank)
        if contain_keyword:
            dataframe.at[index, 'keywords'] = contain_keyword
        index += 1


def count_words(dataframe):
    index = 0
    for data in dataframe.iterrows():
        review_words = set(re.split(r'\W+', data[1]['review_body']))
        if '' in review_words:
            review_words.remove('')
        dataframe.at[index, 'word count'] = len(review_words)
        index += 1


word_mapping = generate_freq_list(pacifier_df)
with open('pacifier_freq.csv', 'w') as file:
    for word in word_mapping.keys():
        file.write('%s, %s\n' % (word, word_mapping[word]))

# Output word frequency mapping
output_names = ['hair_dryer', 'microwave', 'pacifier']
for df in df_all:
    wordmap = generate_freq_list(df)
    count = 0
    with open('%s_word_freq.csv' % output_names[count], 'w') as file:
        for word in wordmap.keys():
            file.write('%s, %s\n' % (word, wordmap[word]))
    count += 1

# Insert word count column
for df in df_all:
    count_words(df)


# Output csv
hair_dryer_df.to_csv(open('hair_dryer_sorted.csv', 'w'), index=False)
microwave_df.to_csv(open('microwave_sorted.csv', 'w'), index=False)
pacifier_df.to_csv(open('pacifier.sorted.csv', 'w'), index=False)

# wordbank = ['bought', 'however', 'love']
# filter_keywords(wordbank, hair_dryer_df)
