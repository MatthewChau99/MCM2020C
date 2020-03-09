import pprint

import numpy as np
import pandas as pd
from dateutil.relativedelta import *

pp = pprint.PrettyPrinter(indent=2)


def data_reorganize():
    hair_dryer_df = pd.read_csv('Processed/Stats_Processed/hair_dryer_stats_processed.tsv', sep=',')
    microwave_df = pd.read_csv('Processed/Stats_Processed/microwave_stats_processed.tsv', sep=',')
    pacifier_df = pd.read_csv('Processed/Stats_Processed/pacifier_stats_processed.tsv', sep=',')
    df_all = [pacifier_df]

    def reorganized_all():
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
        products_abrev = ['p']
        years = ['2015']
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

        def get_product_data(df_name, df):
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
            for year in years:
                for month in months:
                    if year == '2015' and months.index(month) >= 8 or year == '2012' and month == '01':
                        continue

                    input_df = pd.read_csv('Time/Input/%s%s%s.csv' % (product, year, month), sep=',')
                    input_df['review_date'] = pd.to_datetime(input_df['review_date'])
                    output_df = pd.DataFrame(input_df['product_id'], columns=['product_id'])
                    output_df['product_type'] = product

                    initial_date = input_df['review_date'][0]
                    initial_year, initial_month = input_df['review_date'][0].year, input_df['review_date'][
                        0].month

                    input_filtered_df = input_df.loc[input_df['review_date'] < initial_date]
                    input_filtered_df.reset_index(inplace=True)
                    current_date = initial_date
                    current_year, current_month = initial_year, initial_month

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

                        if current_month == 1:
                            current_year -= 1
                            current_date = current_date + relativedelta(years=-1, month=12, day=31)
                        else:
                            current_date = current_date + relativedelta(months=-1, day=31)
                        current_month = current_month - 1 if current_month > 1 else 12

                        input_filtered_df = input_df.loc[(input_df['review_date'] < current_date)]
                        input_filtered_df.reset_index(inplace=True)

                    print('---- %s%s%s Done ----' % (product, year, month))
                    output_df.to_csv('Time/Output/%s%s%s.csv' % (product, year, month))

    # reorganized_all()
    reorganized_month()


if __name__ == '__main__':
    data_reorganize()
