import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#path
df = pd.read_csv('"D:\random\tmdb_5000_credits.csv"')

# 3 primeiras linhas
df.head(3)

#info do data set
df.info()

#manipulação da data
df['profit'] = df['revenue'] - df['budget']
df['profit_margin'] = df['profit']/df['revenue']*100

df.describe()

#+budget = +revenue?
budget = df.query('budget > 0')
budget.describe()

#budget
x_ticks = np.arange(1.000000e+00,5.000000e+08,5.000000e+07)

budget['budget'].hist(bins=x_ticks)
plt.title("Bar Chart of TMDB Movie Budget")
plt.xlabel("Budget (hundred million)")
plt.xticks(x_ticks)
plt.ylabel("Number of TMDB Movie");

# Revenue
x_ticks = np.arange(0.000000e+00,3.000000e+09,5.000000e+08)

budget['revenue'].hist(bins=x_ticks)
plt.title("Bar Chart of TMDB Movie Revenue")
plt.xlabel("Revenue (billion)")
plt.xticks(x_ticks)
plt.ylabel("Number of TMDB Movie");

# Budget vs Revenue
budget.plot(y='revenue',x='budget',kind='scatter')

plt.title("Scatter Plot of TMDB Movie Budget vs. Revenue")
plt.xlabel("Budget (100 million)")
plt.ylabel("Revenue (100 million)");

# Budget vs Profit
budget.plot(y='profit',x='budget',kind='scatter')

plt.title("Scatter Plot of TMDB Movie Budget vs. Profit")
plt.xlabel("Budget (100 million)")
plt.ylabel("Profit (100 million)");

# > 100million
blockbuster = budget.query('budget > 1.000000e+08')
blockbuster.describe()

blockbuster.shape

blockbuster.plot(y='profit',x='budget',kind='scatter')

plt.title("Scatter Plot of TMDB Movie Budget vs. Profit")
plt.xlabel("Budget (hundred million)")
plt.ylabel("Profit (billion)");

# Group by Movie Title and Budget, Revenue and Profit for Top 10 Movies
blockbuster_grouped = blockbuster.groupby('original_title')[['budget','revenue','profit']].sum().sort_values('budget',ascending=False).iloc[:10,:]
blockbuster_grouped