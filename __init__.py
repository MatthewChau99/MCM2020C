import Data_Preprocess as dp
import NLP_analysis as nlp
import Data_Manipulation as dm

if __name__ == '__main__':
    dp.data_preprocess()
    nlp.nlp()
    dm.generate_statistics()
    dm.generate_normalized_data()