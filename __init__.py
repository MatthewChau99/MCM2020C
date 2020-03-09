import Data_Preprocess as dp
import NLP_analysis as nlp
import Data_Manipulation as dm
import Data_Reorganize as dr
import pandas as pd
import numpy as np

if __name__ == '__main__':
    dp.data_preprocess()
    print('------------ Data Preprocessed ------------')
    nlp.nlp()
    print('--------- Data Sentiment Calculated ---------')
    dm.data_manipulate()
    print('------------ Data Calculated ------------')
    dr.data_reorganize()
    print('------------ Data Reorganized ------------')
    df = pd.read_csv('Processed/Reorganized/output_reorganized.csv')
    print(np.max(df['evaluation_score']))
    print(np.min(df['evaluation_score']))
