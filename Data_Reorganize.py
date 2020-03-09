import pprint

import numpy as np
import pandas as pd
from dateutil.relativedelta import *

pp = pprint.PrettyPrinter(indent=2)


def data_reorganize():
    hair_dryer_df = pd.read_csv('Processed/Stats_Processed/hair_dryer_stats_processed.tsv', sep=',')
    microwave_df = pd.read_csv('Processed/Stats_Processed/microwave_stats_processed.tsv', sep=',')
    pacifier_df = pd.read_csv('Processed/Stats_Processed/pacifier_stats_processed.tsv', sep=',')
    df_all = [hair_dryer_df, microwave_df, pacifier_df]
    products_abrev = ['h', 'm', 'p']


    def reorganized_all():
        #       Generate a table with the following data:
        #
        #       Product ID      Avg Rating      Evaluation Score        Product Type
        #
        #       B003FBG88E        4.4                 2.90               hair_dryer
        #          ...            ...                 ...                   ...

        hair_data = []
        microwave_data = []
        pacifier_data = []
        data_all = [hair_data, microwave_data, pacifier_data]
        data_filename_all = ['hair_dryer', 'microwave', 'pacifier']
        output_df_all = []

        for index1 in range(len(data_all)):
            for index2 in range(len(df_all[index1])):
                product_id = df_all[index1].loc[index2, 'product_id']
                avg_rating = df_all[index1].loc[index2, 'product_average_rating']
                evaluation_score = df_all[index1].loc[index2, 'normalized_product_evaluation_score']
                product_type = data_filename_all[index1]
                data_all[index1].append([product_id, avg_rating, evaluation_score, product_type])

            output_df_all.append(
                pd.DataFrame(data_all[index1],
                             columns=['product_id', 'avg_rating', 'evaluation_score', 'product_type']))

        output_df = pd.concat(output_df_all)
        output_df.drop_duplicates(subset='product_id', inplace=True)

        output_df.to_csv(open('Processed/Reorganized/output_reorganized.csv', 'w'), index=False)

    def reorganized_month():
        """
            Generate a table showing the relation between star rating and review rating(evaluation score) as time passes
            with the following format:

            Product ID      Product Type     2015-08 Star     2015-08 Review     2014-08 Star     2014-08 Review
        """

        year, month = '2015', '08'

        def get_product_data(df_name, df):
            """

            :param df_name: product type; chosen from ['h', 'm', 'p']
            :param df: the dataframe filtered by date
            :return: a dictionary { Product ID : (Product Average Star Rating, Prouduct Average Review Rating)
            """
            data_mapping = {}
            processed_df = df_all[products_abrev.index(df_name)]

            for idx in range(len(df.index)):
                _product_id = df.loc[idx, 'product_id']
                review_id = df.loc[idx, 'review_id']
                product_rating = df.loc[idx, 'star_rating']
                review_eval_score = processed_df.loc[
                    processed_df['review_id'] == review_id, 'review_evaluation_score'].tolist()[0]

                if _product_id not in data_mapping:
                    data_mapping.update({_product_id: [1, product_rating, review_eval_score]})
                else:
                    count = data_mapping.get(_product_id)[0] + 1
                    product_rating = data_mapping.get(_product_id)[1] + product_rating
                    review_eval_score = data_mapping.get(_product_id)[2] + review_eval_score
                    data_mapping.update({_product_id: [count, product_rating, review_eval_score]})

            for key in data_mapping.keys():
                avg_product_rating = data_mapping.get(key)[1] / data_mapping.get(key)[0]
                avg_eval_score = data_mapping.get(key)[2] / data_mapping.get(key)[0]
                data_mapping.update({key: [avg_product_rating, avg_eval_score]})

            min_eval_score = np.min([data_mapping.get(key)[1] for key in data_mapping.keys()])
            max_eval_score = np.max([data_mapping.get(key)[1] for key in data_mapping.keys()])

            for key in data_mapping.keys():
                eval_score = data_mapping.get(key)[1]
                data_mapping.update({key: [data_mapping.get(key)[0],
                                           (eval_score - min_eval_score) * 4 / (max_eval_score - min_eval_score) + 1]})

            return data_mapping

        for product in products_abrev:
            input_df = pd.read_csv('Time/Input/%s%s%s.csv' % (product, year, month), sep=',')
            input_df['review_date'] = pd.to_datetime(input_df['review_date'])

            output_df = pd.DataFrame(input_df['product_id'], columns=['product_id'])
            output_df.drop_duplicates(inplace=True)
            output_df.set_index('product_id')
            output_df['product_type'] = product

            current_date = input_df['review_date'][0]
            current_year, current_month = current_date.dt.year, current_date.dt.month
            input_filtered_df = input_df.loc[input_df['review_date'] <= current_date]
            input_filtered_df.reset_index(inplace=True)

            #   Generate column with decreasing date
            while not input_filtered_df.empty:
                data_in_this_month = get_product_data(product, input_filtered_df)

                for index in range(0, len(input_filtered_df)):
                    product_id = input_filtered_df.loc[index, 'product_id']
                    column_star_rating = '%d_%d_star_rating' % (current_year, current_month)
                    column_eval_score = '%d_%d_eval_score' % (current_year, current_month)
                    output_df.at[output_df['product_id'] == product_id, column_star_rating] = \
                        data_in_this_month.get(product_id)[0]
                    output_df.at[output_df['product_id'] == product_id, column_eval_score] = \
                        data_in_this_month.get(product_id)[1]

                print('---- %s %s Done ----' % (current_year, current_month))

                #   Update current_date
                if current_month == 1:
                    current_year -= 1
                    current_date = current_date + relativedelta(years=-1, month=12, day=31)
                else:
                    current_date = current_date + relativedelta(months=-1, day=31)
                current_month = current_month - 1 if current_month > 1 else 12

                input_filtered_df = input_df.loc[(input_df['review_date'] < current_date)]
                input_filtered_df.reset_index(inplace=True)

            print('-------- %s%s%s Done --------' % (product, year, month))

            output_df.to_csv('Time/Output/%s%s%s.csv' % (product, year, month))

    def reorganized_month_separate():
        for product in products_abrev:
            input_df = pd.read_csv('Time/Output/%s201508.csv' % product, sep=',')
            input_df.drop(columns='Unnamed: 0', inplace=True)
            input_df.set_index('product_id', inplace=True)

            eval_columns = [col for col in input_df.columns if 'eval' in col]
            star_columns = [col for col in input_df.columns if 'star' in col]

            star_df = input_df.drop(columns=eval_columns)
            eval_df = input_df.drop(columns=star_columns)

            star_df.to_csv(open('Time/Output/Star/%s_star.csv' % product, 'w'), index=True)
            eval_df.to_csv(open('Time/Output/Eval/%s_eval.csv' % product, 'w'), index=True)

    def reorganized_month_with_dup():
        for product in products_abrev:
            eval_df = pd.read_csv('Time/Output/Eval/%s_eval.csv' % product, sep=',')
            output_df = pd.DataFrame(columns=['product_id', 'eval_score', 'date'])

            for index in range(len(eval_df.index)):
                product_id = eval_df.loc[index, 'product_id']
                for date_index in range(2, len(eval_df.columns)):
                    eval_score = eval_df.loc[index, eval_df.columns[date_index]]
                    if not pd.isna(eval_score):
                        date = eval_df.columns[date_index]
                        add_dict = {'product_id': product_id, 'eval_score': eval_score, 'date': date[0:len(date) - 11]}
                        output_df = output_df.append(add_dict, ignore_index=True)

            output_df.to_csv(open('Time/Output/Eval/%s_eval_date.csv' % product, 'w'), index=True)

    # reorganized_month_separate()
    reorganized_month_with_dup()


if __name__ == '__main__':
    data_reorganize()
