import pandas as pd


def data_reorganize():
    def reorganized_all():
        hair_dryer_df = pd.read_csv('Processed/Stats_Processed/hair_dryer_stats_processed.tsv', sep=',')
        microwave_df = pd.read_csv('Processed/Stats_Processed/microwave_stats_processed.tsv', sep=',')
        pacifier_df = pd.read_csv('Processed/Stats_Processed/pacifier_stats_processed.tsv', sep=',')
        df_all = [hair_dryer_df, microwave_df, pacifier_df]

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
        output_df.drop_duplicates(subset='product_id')

        output_df.to_csv(open('Processed/Reorganized/output_reorganized.csv', 'w'), index=False)

    # def reorganized_month():
    reorganized_all()


if __name__ == '__main__':
    data_reorganize()
