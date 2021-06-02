import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


vectorizer=CountVectorizer(ngram_range=(1,2))
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
    "Is this"
]
x = vectorizer.fit_transform(corpus)
print(x.toarray().shape)
transformer=TfidfTransformer(smooth_idf=False)
tf=transformer.fit_transform(x.toarray())
print(tf.toarray().shape)
print(x.toarray())
print(tf.toarray())

