
################################################
#
#     Task 1 - predict movies revenue & ranking
#
################################################

from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
import json
from ast import literal_eval
import category_encoders as ce


def get_json_names(json_dicts):
    return str([dict['name'] for dict in json_dicts])

def json_to_dummies(df):
    """
    This function converts columns with json values in to dummy vars
    :param df: original pandas data frame
    :return:
    """
    columns = ['production_countries', 'genres', 'production_companies']
    for col in columns:
        mlb = ce.BinaryEncoder()
        df1 = pd.DataFrame(mlb.fit_transform(df.pop(col).apply(
            get_json_names)),
                        columns=mlb.get_feature_names())
        df = df.join(df1)
    return df

def preprocess(df):
    # Transform json columns to dummy vars using binary encoding
    df = json_to_dummies(df)
    return df

def predict(csv_file):
    """
    This function predicts revenues and votes of movies given a csv file with movie details.
    Note: Here you should also load your model since we are not going to run the training process.
    :param csv_file: csv with movies details. Same format as the training dataset csv.
    :return: a tuple - (a python list with the movies revenues, a python list with the movies avg_votes)
    """

    #your code goes here...

    pass


