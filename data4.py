import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#path
df = pd.read_csv('"D:\random\tmdb_5000_credits.csv"')

# WORK IN PROGRESS

#popularidade de ator
df['cast'].value_counts()

df['cast'].describe()


df['cast'] = df['cast'].astype(str)
df.head(1)