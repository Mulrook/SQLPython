import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#path
df = pd.read_csv('"D:\random\tmdb_5000_credits.csv"')

#diretores
df['director'].value_counts()

#primeiro diretor
df['director'] = df['director'].str.split("|")
df.head(1)

directors_df = df.explode('director')
directors_df.head(1)

# grupo de diretores
directors_df['director'].value_counts()
#valor
directors_df.groupby('director')[['revenue','profit']].mean().sort_values('revenue', ascending=False).head(5)
#lucro
directors_df.groupby('director')[['revenue','profit']].mean().sort_values('profit', ascending=False).head(5)

# achar um filme do Pierre Coffin
directors_df.query('director == "Pierre Coffin"').sort_values('profit', ascending=False).head(3)