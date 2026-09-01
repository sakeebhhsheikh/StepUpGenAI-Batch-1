import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
1. Line -> Frequency Polygon : Timeseries analysis : Quntity(contineous)
2. Bar -> Frequency Distribution : Categorical(Discrete) - Univariate analysis
3. Pie -> Frequency Distributon : Categorical(Discrete) - Percentage analysis
4. Hist / Density -> Frequency Distribution : Quantity(contineous) - Univariate analysis
5. scatter -> Group / Cluster analysis : EDA : 
6. box -> Quantile information, Box and Wiskers -> 5 number summary -> 25%, 50%, 75%, lowerlimit, upperlimit, outlier : QUnatity (Contineous)
'''

#1. Line Chart : Used to show trend
# x = [1,2,3,4,5,6,7,8,9,10]
# # y = [5,8,4,7,9,2,10,3,6,12]
# y = [3,4,8,9,9,10,11,23,24,32]
# # arr = np.array([x, y])
# print(np.corrcoef(x, y))
# plt.plot(x, y,
#          color='red',
#          linestyle='--',
#          marker='o',
#          linewidth=3)
# plt.title("Sales Record Trend")
# plt.xlabel("Months in 2025")
# plt.ylabel("Profit")

# plt.xticks(x)

# plt.grid(True)

# # plt.show()

# plt.savefig('Line.jpg', dpi=300)

##Using Pandas DF
df = pd.read_csv('datasets/mtcars.csv')
# print(df.head())

# df[['mpg','hp','wt']].plot()
# plt.show()
# df[['mpg','wt']].plot()
# plt.show()
# df[['hp','wt']].plot()
# plt.show()


df['hp_nomal'] = (df['hp']-df['hp'].min()) / (df['hp'].max()-df['hp'].min())
df['wt_nomal'] = (df['wt']-df['wt'].min()) / (df['wt'].max()-df['wt'].min())

# df[['hp_nomal','wt_nomal']].plot()
# plt.show()

#---------------------------------------------------------------------------------

# plt.plot(df.index, df.mpg,
#          color='red',
#          linestyle='--',
#          linewidth=2)

# plt.plot(df.index, df.hp,
#          color='orange',
#          linestyle='-.',
#          linewidth=2)

# plt.plot(df.index, df.wt,
#          color='blue',
#          linewidth=2)
# plt.legend(['mpg','hp','wt'])

# plt.show()

#---------------------------------------------------------------------------------
#==> Bar Chart

# travel_mode = ['car','bus','train','bike','cycle','walk']
# freq = [100, 150, 150, 50, 20, 30]

# # plt.bar(travel_mode, freq)
# # plt.show()

# plt.barh(travel_mode, freq)
# plt.show()
#---------------------------------------------------------------------------------
# ==> Pie Chart

# travel_mode = ['car','bus','train','bike','cycle','walk']
# freq = [100, 150, 150, 50, 20, 30]

# plt.pie(freq, labels=travel_mode, autopct="%1.1f%%", explode=[0,0,0,0,0.1,0])
# plt.show()

#---------------------------------------------------------------------------------
# ==> Hist plot

# x = [60, 65, 70, 72, 80, 85, 90, 95, 100]
# plt.hist(x, bins=6)
# plt.show()


# plt.hist(df.mpg)
# plt.show()

#---------------------------------------------------------------------------------
# ==> Scatter plot

# plt.scatter(df.mpg, df.wt)
# plt.show()

# plt.scatter(df.hp, df.wt)
# plt.show()
#---------------------------------------------------------------------------------
# ==> Box plot

# print(df.mpg.describe())

# plt.boxplot(df.mpg)
# plt.show()

# x = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,5,6,6,6,6,6,6,7,7,7,7,8,8,8,9,9,9,9,10,10,10,10,10,50,150,500]
x = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,5,6,6,6,6,6,6,7,7,7,7,8,8,8,9,9,9,9,10,10,10,10,10]
y = [10,10,10,9,9,9,9,8,8,8,7,7,7,6,6,6,6,5,5,5,5,4,4,4,3,3,3,2,2,2]
# print(np.median(x))
# print(np.quantile(x, [0.25,0.5,0.75]))

# plt.boxplot(x)
# plt.show()

#=================================================================================================

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data:
# np.random.seed(10)
# D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))

# plot
# fig, ax = plt.subplots()
# VP = ax.boxplot(df[['mpg','hp','wt']], positions=[2, 4, 6], widths=1.5, patch_artist=True,
#                 showmeans=False, showfliers=False,
#                 medianprops={"color": "white", "linewidth": 0.5},
#                 boxprops={"facecolor": "C0", "edgecolor": "white",
#                           "linewidth": 0.5},
#                 whiskerprops={"color": "C0", "linewidth": 1.5},
#                 capprops={"color": "C0", "linewidth": 1.5})

# # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
# #        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

#------------------------------------------------------------------
#==> Ploting mulitple graphs on the same plot

# travel_mode = ['car','bus','train','bike','cycle','walk']
# freq = [100, 150, 150, 50, 20, 30]


# fig, (ax1,ax2) = plt.subplots(1,2)

# ax1.bar(travel_mode, freq)
# ax1.set_title('Bar Chart')


# ax2.pie(freq, labels=travel_mode, autopct="%1.1f%%", explode=[0,0,0,0,0.1,0])
# ax2.set_title('Pie Chart')
# ax2.set_xlabel('Pie Chart')
# plt.show()

#-----------------------------------------------------------------------
import seaborn as sns

#Line plot
# sns.lineplot(data=df, x=df.index, y='mpg')
# plt.show()

#Scatter plot
# sns.scatterplot(data=df, x='mpg', y='wt', hue=df['gear'])
# plt.show()


#Boxplot
# df.groupby(by='gear')['mpg']

# sns.boxplot(data=df, x="gear", y="mpg")
# plt.show()

#Bar plot
# sns.barplot(data=df, x="gear", y="gear")
# sns.barplot(data=df, x="gear", y="gear", hue="cyl")
# plt.show()

#hist plot

# sns.histplot(data=df, x='mpg', bins=5)
# sns.histplot(data=df, x='mpg')
# plt.show()

#heatmap

# sns.heatmap(data=df[['mpg','hp','wt']],  cmap="coolwarm")
# plt.show()

# regplot
# voilinplot
# pairplot
# catplot
#-----------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datasets/Salaries.csv', skiprows=1)
print(df.head())

print(df.info())

print(df['rank'].unique())
print(df['discipline'].unique())
print(df['sex'].unique())

#describe()
# print(df.describe())
# print(df.describe(include=str))
# print(df.describe(include='all'))
# Attrubutes : ndim, shape, size, dtypes, itemsize

#Check missing elements : 
# df.isnull()
# # df.notnull()
# print(df.isnull().sum())
# print(df.isnull().mean()*100)

#-> Sort dataframe:
# df.sort_values(by=='colname', ascending=False)


#-> Check duplicated rows

# print(df.duplicated().sum())

# print(df[df.duplicated()])

# print(df.drop_duplicates())

#=> find unique element in each categorical column
#=> Frequency Distribution
print(df['rank'].value_counts())

#For Numerical COlumns : 
#Statistical Analysis : mean, mode, median, quantile, std, var, count, min, max, corr, cov, hist

# plt.figure(figsize=(10,6))

# df['rank'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')

# # Customize using Matplotlib commands
# plt.title('Ranking')
# plt.xlabel('Rank')
# plt.ylabel('Count')
# plt.xticks(rotation=60)  # Keeps text horizontal
# plt.tight_layout()
# plt.show()

#---------------------------------------------------------------------

# plt.figure(figsize=(10,6))
# df['salary'].plot(kind='density')
# plt.tight_layout()
# plt.show()

# fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,6))

# # df['salary'].plot(kind='hist')
# # df['salary'].plot(kind='density')

# ax1.hist(df['salary'])
# # ax2.hist(df['salary'], density=True)

# sns.kdeplot(data=df, x="salary")

# plt.tight_layout()
# plt.show()

##=> Plot a graph to show comparison of count between Male and Female employees

#==> Hist Plot

# plt.figure(figsize=(10,8))

# sns.boxplot(data=df, x='salary', hue='sex')

# plt.tight_layout()
# plt.show()
##=> 

# print(df.groupby(by='sex')['salary'].mean())

# print(df.groupby(by=['rank','sex'])[['service','phd','salary']].mean())
print(df.groupby(by=['rank','sex'])[['service','phd','salary']].agg(["count","mean"]))
# sns.barplot(df, x="rank", y="sex", hue="sex")
# plt.tight_layout()
# plt.show()
