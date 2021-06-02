import pandas as pd
import re

x=pd.read_csv("movies_dataset.csv")
print(x[x["runtime"]==0])
# print(x.columns)