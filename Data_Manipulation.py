import pprint

import numpy as np
import pandas as pd

hair_dryer_df = pd.read_csv('Processed/NLP_Processed/hair_dryer_NLP_processed.tsv', sep=',')
microwave_df = pd.read_csv('Processed/NLP_Processed/microwave_NLP_processed.tsv', sep=',')
pacifier_df = pd.read_csv('Processed/NLP_Processed/pacifier_NLP_processed.tsv', sep=',')
df_all = [hair_dryer_df, microwave_df, pacifier_df]
statistics = {}


def generate_normalized_data(dataframe):
    for index in range(len(dataframe.index)):
        # Generate normalized keyword count
        max_keyword_count = np.max(dataframe['keyword_count'])
        min_keyword_count = np.min(dataframe['keyword_count'])
        keyword_count = dataframe.loc[index, 'keyword_count']
        normalized_keyword_count = (keyword_count - min_keyword_count) / (max_keyword_count - min_keyword_count)
        dataframe.at[index, 'normalized_keyword_count'] = normalized_keyword_count

        # Generate normalized vote ratio product


        # Generate normalized vote ratio all
        max_vote_ratio = np.max(dataframe['vote_ratio'])
        min_vote_ratio = np.min(dataframe['vote_ratio'])
        votes_ratio = dataframe.loc[index, 'vote_ratio']
        normalized_vote_ratio = (votes_ratio - min_vote_ratio) / (max_vote_ratio - min_vote_ratio)
        dataframe.at[index, 'normalized_vote_ratio'] = normalized_vote_ratio


def generate_statistics(dataframe):
    attributes = ['star_rating', 'sentiment_pos', 'sentiment_neu', 'sentiment_neg', 'sentiment_compound']
    stats = {}
    for attribute in attributes:
        mean = np.average(df[attribute])
        sd = np.std(df[attribute])
        stats.update({('%s_mean' % attribute): mean, ('%s_sd' % attribute): sd})
    if dataframe is hair_dryer_df:
        statistics.update({'hair': stats})
    elif dataframe is microwave_df:
        statistics.update({'microwave': stats})
    else:
        statistics.update({'pacifier': stats})


for df in df_all:
    generate_statistics(df)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(statistics)

hair_dryer_df.to_csv(open('Processed/Stats_Processed/hair_dryer_stats_processed.tsv', 'w'), index=False)
microwave_df.to_csv(open('Processed/Stats_Processed/microwave_stats_processed.tsv', 'w'), index=False)
pacifier_df.to_csv(open('Processed/Stats_Processed/pacifier_stats_processed.tsv', 'w'), index=False)
