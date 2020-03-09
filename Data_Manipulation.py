import pprint

import numpy as np
import pandas as pd


def data_manipulate():
    hair_dryer_df = pd.read_csv('Processed/NLP_Processed/hair_dryer_NLP_processed.tsv', sep=',')
    microwave_df = pd.read_csv('Processed/NLP_Processed/microwave_NLP_processed.tsv', sep=',')
    pacifier_df = pd.read_csv('Processed/NLP_Processed/pacifier_NLP_processed.tsv', sep=',')
    df_all = [hair_dryer_df, microwave_df, pacifier_df]
    statistics = {}

    def generate_normalized_data(dataframe):
        for index in range(len(dataframe.index)):
            # Generate normalized vote ratio all
            max_vote_ratio = np.max(dataframe['vote_ratio_total_product_total'])
            min_vote_ratio = np.min(dataframe['vote_ratio_total_product_total'])
            votes_ratio = dataframe.loc[index, 'vote_ratio_total_product_total']
            normalized_vote_ratio = (votes_ratio - min_vote_ratio) / (max_vote_ratio - min_vote_ratio)
            dataframe.at[index, 'normalized_vote_ratio_total_product_total'] = normalized_vote_ratio / 12

            # Generate normalized vote ratio product
            max_product_vote_count = np.max(dataframe['product_vote_count'])
            min_product_vote_count = np.min(dataframe['product_vote_count'])
            product_vote_count = dataframe.loc[index, 'product_vote_count']
            normalized_product_vote_count = (product_vote_count - min_product_vote_count) / (
                    max_product_vote_count - min_product_vote_count)
            dataframe.at[index, 'normalized_product_vote_count'] = normalized_product_vote_count / 12

            # Generate normalized review type
            max_review_type = np.max(dataframe['review_type'])
            min_review_type = np.min(dataframe['review_type'])
            review_type = dataframe.loc[index, 'review_type']
            normalized_review_type = (review_type - min_review_type) / (
                    max_review_type - min_review_type)
            dataframe.at[index, 'normalized_review_type'] = normalized_review_type / 6

            # Generate normalized vine
            vine = dataframe.loc[index, 'vine']
            dataframe.at[index, 'normalized_vine'] = vine / 6

            # Generate normalized verified purchase
            verified_purchase = dataframe.loc[index, 'verified_purchase']
            dataframe.at[index, 'normalized_verified_purchase'] = verified_purchase / 6

            # Generate normalized vote ratio for helpful vs product total
            max_vote_ratio_helpful_product_total = np.max(dataframe['vote_ratio_helpful_product_total'])
            min_vote_ratio_helpful_product_total = np.min(dataframe['vote_ratio_helpful_product_total'])
            vote_ratio_helpful_product_total = dataframe.loc[index, 'vote_ratio_helpful_product_total']
            normalized_vote_ratio_helpful_product_total = (
                                                                  vote_ratio_helpful_product_total - min_vote_ratio_helpful_product_total) / (
                                                                  max_vote_ratio_helpful_product_total - min_vote_ratio_helpful_product_total)
            dataframe.at[
                index, 'normalized_vote_ratio_helpful_product_total'] = normalized_vote_ratio_helpful_product_total / 3 - 1 / 6

            # Generate normalized page number
            dataframe.at[index, 'normalized_page_number'] = (1 / 6) / dataframe.loc[index, 'page_number']

            # Generate normalized keyword count
            max_keyword_count = np.max(dataframe['keyword_count'])
            min_keyword_count = np.min(dataframe['keyword_count'])
            keyword_count = dataframe.loc[index, 'keyword_count']
            normalized_keyword_count = (keyword_count - min_keyword_count) / (max_keyword_count - min_keyword_count)
            dataframe.at[index, 'normalized_keyword_count'] = normalized_keyword_count / 12

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

    def generate_evaluation_score(dataframe):
        product_evaluation_score = {}

        for index in range(len(dataframe.index)):
            product_id = dataframe.loc[index, 'product_id']
            I1 = dataframe.loc[index, 'normalized_keyword_count']
            I2 = dataframe.loc[index, 'normalized_vote_ratio_total_product_total']
            L = dataframe.loc[index, 'normalized_review_type']
            A = dataframe.loc[index, 'normalized_vine']
            V = dataframe.loc[index, 'normalized_verified_purchase']
            H = dataframe.loc[index, 'normalized_vote_ratio_helpful_product_total']
            P = dataframe.loc[index, 'normalized_page_number']
            evaluation_score = I1 + I2 + L + A + V + H + P
            evaluation_score = evaluation_score if evaluation_score > 0 else 0
            dataframe.at[index, 'evaluation_score'] = evaluation_score

            if product_id not in product_evaluation_score:
                product_evaluation_score.update({product_id: evaluation_score})
            else:
                product_evaluation_score.update(
                    {product_id: product_evaluation_score.get(product_id) + evaluation_score})

        for index in range(len(dataframe.index)):
            product_id = dataframe.loc[index, 'product_id']
            dataframe.at[index, 'product_avg_evaluation_score'] = product_evaluation_score.get(product_id) / \
                                                                  dataframe.loc[index, 'review_count']

    for df in df_all:
        generate_statistics(df)
        generate_normalized_data(df)
        generate_evaluation_score(df)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(statistics)

    hair_dryer_df.to_csv(open('Processed/Stats_Processed/hair_dryer_stats_processed.tsv', 'w'), index=False)
    microwave_df.to_csv(open('Processed/Stats_Processed/microwave_stats_processed.tsv', 'w'), index=False)
    pacifier_df.to_csv(open('Processed/Stats_Processed/pacifier_stats_processed.tsv', 'w'), index=False)


if __name__ == '__main__':
    data_manipulate()
