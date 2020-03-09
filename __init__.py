import Data_Preprocess as dp
import NLP_analysis as nlp
import Data_Manipulation as dm
import pandas as pd

if __name__ == '__main__':
    dp.data_preprocess()
    print('------------ Data Preprocessed ------------')
    nlp.nlp()
    print('--------- Data Sentiment Calculated ---------')
    dm.data_manipulate()
    df = pd.read_csv('Processed/Stats_Processed/pacifier_stats_processed.tsv', sep=',')
