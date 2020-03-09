import numpy as np
import pandas as pd

hair_dryer_df = pd.read_csv('Processed/Stats_Processed/hair_dryer_NLP_processed.tsv', sep=',')
microwave_df = pd.read_csv('Processed/Stats_Processed/microwave_NLP_processed.tsv', sep=',')
pacifier_df = pd.read_csv('Processed/Stats_Processed/pacifier_NLP_processed.tsv', sep=',')
df_all = [hair_dryer_df, microwave_df, pacifier_df]

# organized_hair = [[hair_dryer_df.loc[index, 'product_id'], hair_dryer_df.loc[index, 'evaluation_score'], hair_dryer_df.loc[index, ]]]


