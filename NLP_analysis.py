import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def nlp():
    sid = SentimentIntensityAnalyzer()

    hair_dryer_df = pd.read_csv('Processed/hair_dryer_preprocessed.tsv', sep=',')
    microwave_df = pd.read_csv('Processed/microwave_preprocessed.tsv', sep=',')
    pacifier_df = pd.read_csv('Processed/pacifier_preprocessed.tsv', sep=',')
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

    for df in df_all:
        generate_score(df)

    # Output csv
    hair_dryer_df.to_csv(open('Processed/NLP_Processed/hair_dryer_NLP_processed.tsv', 'w'), index=False)
    microwave_df.to_csv(open('Processed/NLP_Processed/microwave_NLP_processed.tsv', 'w'), index=False)
    pacifier_df.to_csv(open('Processed/NLP_Processed/pacifier_NLP_processed.tsv', 'w'), index=False)
