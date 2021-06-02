import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
################################################
#
#     Task 1 - predict movies revenue & ranking
#
################################################


def predict(csv_file):
    """
    This function predicts revenues and votes of movies given a csv file with movie details.
    Note: Here you should also load your model since we are not going to run the training process.
    :param csv_file: csv with movies details. Same format as the training dataset csv.
    :return: a tuple - (a python list with the movies revenues, a python list with the movies avg_votes)
    """

    data = pd.read_csv(csv_file)
    return data


data = predict("movies_dataset.csv")
data["hasHomepage"] = np.where(data["homepage"].isna(), 1, 0)
data = data.drop(columns=['id'])
data = data[data.runtime.notna()]
data.insert(0, 'intercept', 1, True)
# data.info()


# data.corr()
# data["hasHomePage"] = np.where(type(data["homepage"]) == str, 1, 0)
# fig, ax = plt.subplots(figsize=(22, 22))
# plot heatmap

# sns.heatmap(data.corr(), cmap='YlGnBu', annot=True, linewidths = 0.2);

# plt.show()



