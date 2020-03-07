import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

hair_dryer_df = pd.read_csv('Sorted/hair_dryer_sorted.tsv', sep=',')
microwave_df = pd.read_csv('Sorted/microwave_sorted.tsv', sep=',')
pacifier_df = pd.read_csv('Sorted/pacifier_sorted.tsv', sep=',')
df_all = [hair_dryer_df, microwave_df, pacifier_df]
statistics = {}


def generate_score(dataframe):
    for index in range(len(dataframe.index)):
        review_headline = str(dataframe.loc[index, 'review_headline'])
        review_body = str(dataframe.loc[index, 'review_body'])

        # Generate sentiment score
        polarity_scores_body = sid.polarity_scores(review_body)
        polarity_scores_head = sid.polarity_scores(review_headline)
        dataframe.at[index, 'sentiment_pos'] = polarity_scores_body['pos'] * 0.2 + polarity_scores_head['pos'] * 0.8
        dataframe.at[index, 'sentiment_neu'] = polarity_scores_body['neu'] * 0.2 + polarity_scores_head['neu'] * 0.8
        dataframe.at[index, 'sentiment_neg'] = polarity_scores_body['neg'] * 0.2 + polarity_scores_head['neg'] * 0.8
        dataframe.at[index, 'sentiment_compound'] = polarity_scores_body['compound'] * 0.2 + polarity_scores_head[
            'compound'] * 0.8


def generate_statistics(dataframe):
    attributes = ['pos', 'neu', 'neg', 'compound']
    stats = {}
    for attribute in attributes:
        mean = np.average(df['sentiment_%s' % attribute])
        sd = np.average(df['sentiment_%s' % attribute])
        stats.update({('%s_mean' % attribute): mean, ('%s_sd' % attribute): sd})
    if dataframe is hair_dryer_df:
        statistics.update({'hair': stats})
    elif dataframe is microwave_df:
        statistics.update({'microwave': stats})
    else:
        statistics.update({'pacifier': stats})


for df in df_all:
    generate_score(df)
    generate_statistics(df)

# Output csv
hair_dryer_df.to_csv(open('Processed/hair_dryer_processed.csv', 'w'), index=False)
microwave_df.to_csv(open('Processed/microwave_processed.csv', 'w'), index=False)
pacifier_df.to_csv(open('Processed/pacifier_processed.csv', 'w'), index=False)
