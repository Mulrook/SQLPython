import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#path
df = pd.read_csv('"D:\random\tmdb_5000_credits.csv"')

df['popularity'].describe()

# mediana
df['popularity'].mean()

#Split de gêneros
df['genres'] = df['genres'].str.split("|")
df.head(1)

#mostrar gêneros
genre = df.explode('genres')
genre.head(3)

#Número de gêneros
genre['genres'].value_counts()

#gráfico
plt.figure(figsize=[8,6])
genre['genres'].value_counts().plot.barh()
plt.title("Bar Chart of Genre Count in TMBd Movies")
plt.ylabel("Genres")
plt.xlabel("Count");

#Gênero mais popular
genre_mean = genre.groupby('genres')[['popularity','revenue','profit']].mean().sort_values('popularity', ascending=False)
genre_mean.iloc[:10,:].query("popularity > 0.6464455549010583")

