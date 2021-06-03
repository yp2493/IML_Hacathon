import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectPercentile



vectorizer=TfidfVectorizer(ngram_range=(1,2), decode_error="replace")
data=pd.read_csv("movies_dataset.csv")
# x=vectorizer.fit_transform(data["overview"])
print(x.shape)
# print(data["overview"])
x=vectorizer.fit_transform(data["title"])



def bagOfWords(column, movies):
    data=movies[column]
    vectorizer=TfidfVectorizer(ngram_range=(1,2), decode_error="replace")
    return vectorizer.fit_transform(data).toarray()


def dim_reduction(bag_of_words):
    p=SelectPercentile( percentile=50)
    return p.fit_transform(bag_of_words)


def join_bag_of_words(bag_of_words, data, column):
    data=data[:column].join(bag_of_words).join(data[column:])
    data.pop("column")
    return data



words=bagOfWords("title", data)
words2=dim_reduction(words)
print(words2.shape)
print(words.shape)
# d=join_bag_of_words(words, data, "title")