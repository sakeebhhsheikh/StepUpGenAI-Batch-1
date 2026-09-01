import pandas as pd

li = [2,4,6,8,6,4,7,3,1,5]
# ser = pd.Series(li)
ser = pd.Series(li, index=['a','b','c','d','e','f','g','h','i','j'])
# print(ser)
# print(ser[3])

# print(ser[3:4], ser['d'])
# print(ser[0:4])
# print(ser['a':'d'])

# print(ser.min())
# print(ser.max())
# print(ser.sum())
# print(ser.mean())
# print(ser.median())
# print(ser.var())
# print(ser.std())
# print(ser.quantile([0.25, 0.50, 0.75]))
# print(ser.count())
# print(ser.unique())

#-----------------------------------------------------------------

#Pandas DataFrame

#--> Using List like datastructure : 
# li = [[100,'sakeeb', 1000.5],[101,'rahul',1230],[102,'snehal',2345.0]]
# df = pd.DataFrame(li, columns=['eno','ename','esal'])
# print(df)

#--> Using dict datastructure : 
# dic = {'eno':[100,101,102], 'ename':['sakeeb','rahul','snehal'], 'esal':[1000.5, 1230, 2345.0]}
# dic = [
#     {'eno':100,'ename':'sakeeb', 'esal':1000.5},
#     {'eno':101,'ename':'rahul','esal':1230},
#     {'eno':102,'ename':'snehal','esal':2345.0}]
# df = pd.DataFrame(dic)
# print(df)

#-> By Reading files : 
# df = pd.read_csv('empdata.csv')
# print(df)

#-----------------------------------------------
#==> Attributes
#- ndim
#- shape
#- size
#- dtypes
#- index
#- columns
#- axes
#- values

# print(df.ndim)
# print(df.shape)
# print(df.size)
# print(df.dtypes)
# print(df.index)
# print(df.columns)
# print(df.axes)
# print(df.values)

#---------------------------------
# print(df.info())
# print(df.describe())
# print(df.describe(include='str'))

#----------------------------------------
# df = pd.read_csv('mtcars.csv')
# print(df)

#--> head(nrow), tail(nrows)
# print(df.head())
# print(df.tail())

#---------------------------------------
#Slicing 

# df = pd.read_csv('mtcars.csv')

#range of rows for all columns
# print(df[2:5])
# print(type(df['#model']))
# print(df['#model'])

#-> all rows and selected columns : 
# print(df[['#model','mpg','wt','gear']])

#-> Specific rows and Specific columns
#-> based on labels --> df.loc[]
#-> based on index pos --> df.iloc[]

# print(df.loc[0:4, ['#model','mpg','hp']])

# print(df.iloc[0:4, [0,1,4]])

#==> COnditional Slicing : 

# df = pd.read_csv('mtcars.csv')

# print(df['gear']==4)

# print(df[df['gear']==4])

# print(df[(df['gear']==4) & ((df['cyl']==4) | (df['carb']==4))])

#==================================================================
#Sorting based on specific columns ; 

# df = pd.read_csv('mtcars.csv')

# newdf = df.sort_values(by='mpg', ascending=True)
# print(newdf.head())

# newdf = df.sort_values(by=['mpg','hp'], ascending=True)
# print(newdf.head())

#------------------------------------------

#Statistical operations
#Adding updated data(cols, rows) in DF
#Group By and Stistics
#Concatination
#merge ( like join in sql)
#Dealing with missing elements
#pivot
#String and Datetime operations on DF

#------------------------------------------
#==========================================

# dic = {
#     'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
#     'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
#     }
# df = pd.DataFrame(dic)
# print(df)

#--> Set_index
#reset_index

# print(df[1:5])

# df.set_index('City', inplace=True)
# print(df.head())

# print(df.loc['Pune', :])

#--> reset_index()
# df.reset_index(inplace=True)
# print(df.head())

#==> Multiindex ( Hierarchical Indexing)
# df.set_index(['City','Year'], inplace=True)
# print(df.head())

# print(df.loc['Pune', :])
# print(df.loc[('Pune', 2023), :])

#--------------------------------------------------------
#==> Statistical Operation 

df = pd.read_csv('mtcars.csv')
# print(df.head())
# print(df.dtypes)
# print(df.iloc[:, 1:].mean())


# import numpy as np
# # res = df[['mpg','hp','wt','drat']].agg(['sum', 'mean', 'median'])
# res = df[['mpg','hp','wt','drat']].agg([np.sum, np.mean, np.median, 'var', 'std'])
# print(res)

# res = df[['mpg','hp','wt','drat']].quantile([0.25, 0.5, 0.75])
# print(res)

# res = df[['mpg','hp','wt','drat']].corr()
# print(res)

#----------------------------------------------------
#Adding updating deleting columns in df

dic = {
    'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
    'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
    'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
    }

# dic['Status'] = [True] * 10
# print(dic)

# df = pd.DataFrame(dic)
# df['Status'] = True

# df.insert(0, 'Country', 'India')

# print(df)

#----------------------------------------
import numpy as np

# arr1 = np.array([[1,2,3],[4,5,6]])  #2X3
# arr2 = np.array([[5,6],[8,9]])
# print(arr1)
# print(arr2)

# print(np.hstack((arr1, arr2)))


# arr1 = np.array([[1,2,3],[4,5,6]])  #2X3
# arr2 = np.array([[5,6,4],[8,9,11]])
# print(arr1)
# print(arr2)

# print(np.vstack((arr1, arr2)))

# arr1 = np.array([[1,2,3],[4,5,6]])  #2X3
# arr2 = np.array([[5,6,4],[8,9,11]])
# print(arr1)
# print(arr2)

# print(np.concatenate((arr1, arr2)))
# print(np.concatenate((arr1, arr2), axis=1))

#----------------------------------------------------
# dic1 = {
#     'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
#     'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
#     }

# dic2 = {
#     'City':['Banglore','Banglore','Indore','Indore','Ahemdabad','Ahemdabad'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024 ], 
#     'Population':[170, 250, 210, 220, 300, 350]
#     }

# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)

# df = pd.concat([df1, df2])
# print(df)

#-----------------------------------------------------
# dic1 = {
#     'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
#     'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
#     }

# dic2 = {
#     'City':['Banglore','Banglore','Indore','Indore','Ahemdabad','Ahemdabad'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024 ], 
#     }

# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)

# df = pd.concat([df1, df2])
# print(df)
#-----------------------------------------------------
# dic1 = {
#     'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
#     'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
#     }

# dic2 = {
#     'State' : ['KA','KA','MP','MP','GJ','GJ'],
#     'City':['Banglore','Banglore','Indore','Indore','Ahemdabad','Ahemdabad'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024 ],
#     'Population':[170, 250, 210, 220, 300, 350]
#     }

# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)

# df = pd.concat([df1, df2])
# print(df)

#-----------------------------------------------
#==>  Horizontal Concat : 
# df1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
# df2 = pd.DataFrame([[7,6],[8,7],[7,9]])
# print(df1)
# print(df2)

# df = pd.concat([df1, df2], axis=1)
# print(df)
# #--------------------------------------------

# dic1 = {
#     'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
#     'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
#     }

# dic2 = {
#     'City':['Banglore','Banglore','Indore','Indore','Ahemdabad','Ahemdabad'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024 ],
#     'Population':[170, 250, 210, 220, 300, 350]
#     }

# dic3 = {'State' : ['MH','MH','MH','MH','MH','MH','MH','MH','UT','UT','KA','KA','MP','MP','GJ','GJ'],
#         'Status' : [True]*16}

# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)
# df3 = pd.DataFrame(dic3)

# df = pd.concat([df1, df2])
# df.reset_index(drop=True, inplace=True)
# print(df.shape)
# print(df3.shape)
# newdf = pd.concat([df, df3], axis=1)
# print(newdf)

#--------------------------------------------

# dic1 = {
#     'City':['Pune','Pune','Mumbai','Mumbai','Nagpur','Nagpur','Nashik','Nashik','Delhi','Delhi'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024], 
#     'Population':[100, 150, 200, 250, 170, 250, 210, 220, 300, 350]
#     }

# dic2 = {
#     'City':['Banglore','Banglore','Indore','Indore','Ahemdabad','Ahemdabad'], 
#     'Year':[2023, 2024, 2023, 2024, 2023, 2024 ],
#     'Pop_index':[170, 250, 210, 220, 300, 350]
#     }

# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)

# df = pd.concat([df1, df2])
# print(df)

#----------------------------------------------------------
# Groupby ==>

df = pd.read_csv('mtcars.csv')
# print(df.head())

# print(df.mpg.mean())

# print(df[df['gear']==3].mpg.mean())
# print(df[df['gear']==4].mpg.mean())
# print(df[df['gear']==5].mpg.mean())

# print(df.groupby(by='gear')['mpg'].mean())

# print(df.groupby(by=['am','gear']))
# print(df.groupby(by=['am','gear'])['mpg'].mean())

# print(df.groupby(by=['am','gear'])[['mpg','wt','hp']].mean())
# print(df.groupby(by=['am','gear'])[['mpg','wt','hp']].count())

# df.drop('cyl', axis=1, inplace=True)
#=============================================
#merge ( like join in sql)
#Dealing with missing elements
#pivot
#String and Datetime operations on DF
#-------------------------------------------

#==> Merge Operation : 
accdf = pd.read_csv('datasets/account.csv')
loandf = pd.read_csv('datasets/loan.csv')
# print(accdf.head())
# print(loandf.head())

#--> Inner Join
# df = pd.merge(left=accdf, right=loandf, left_on='acno',  right_on='acnum')
# print(df)

#--> left join
# df = pd.merge(left=accdf, right=loandf, left_on='acno',  right_on='acnum', how='left')
# print(df)

#--> right join
# df = pd.merge(left=accdf, right=loandf, left_on='acno',  right_on='acnum', how='right')
# print(df)

#--> right join
# df = pd.merge(left=accdf, right=loandf, left_on='acno',  right_on='acnum', how='outer')
# print(df)

#------------------------------------------------------------
#Example : 

#--> Which Site, Who dit it,  What is the reading, When it was done ?
# person = pd.read_csv('datasets/survey_person.csv')
# site = pd.read_csv('datasets/survey_site.csv')
# survey = pd.read_csv('datasets/survey_survey.csv')
# visited = pd.read_csv('datasets/survey_visited.csv')

# df1 = pd.merge(left=survey, right=visited, left_on='taken', right_on='ident')
# df2 = pd.merge(left=df1, right=site, left_on='site', right_on='name')
# df3 = pd.merge(left=df2, right=person, left_on='person', right_on='ident')
# df3 = df3[['taken','site','lat','long','quant','reading','dated','person', 'personal','family']]
# print(df3)

#-----------------------------------------
# Df1 =>  First  middle last marks

# Df2 =>  First  middle last contact address

# df = pd.merge(left=Df1, right=Df2, left_on=['First','middle','last'],  right_on=['First','middle','last'], how='outer')
# df = pd.merge(left=Df1, right=Df2, on=['First','middle','last'], how='outer')
#-------------------------------------------------------------------------------------
#--> Finding and dealing with duplicate records:

# df  = pd.read_csv('datasets/duplicated.csv')
# print(df)

# print(df.duplicated(keep='first'))
# print(df.duplicated(subset=['acno','cname'], keep='first'))

# df.drop_duplicates(subset=['acno','cname'], keep='last', inplace=True)
# df.reset_index(drop=True, inplace=True)
# print(df)
#----------------------------------------------------------
# Dealing with Missing elements : 
# NaN
#-> dropna
#-> fillna
#-> isnull() => True/ False
#-> notnull() => True/ False

#
# df = pd.read_csv('datasets/titanic.csv')
# print(df)
# print(df.info())

import numpy as np
import pandas as pd

# arr = np.array([1,2,3,4,5,6,np.nan,7,8,9,10])
# print(arr)
# print(arr.sum())
# print(arr.mean())

# ser = pd.Series([1,2,3,4,5,6,5.5,7,8,9,10])
# print(ser.mean())
#===============================================================
#==> Dealing with missing elements
#-> fillna()
#-> dropna(how, thresh, inplace, axis)
#-> info()
#-> isnull()
#-> notnull()

# df = pd.read_csv('datasets/titanic.csv')
# print(df)
# print(df.info())
# print(sum([True, False, True, True, False, True]))

# print(df.isnull().head())

# print(df.isnull().sum())

# print(df.isnull().sum(axis=1)==11)
# print(df[df.isnull().sum(axis=1)==11])


#==> Dropping rows that are completely empty : 

# df.dropna(how='all', inplace=True)
# print(df.head(7))

# df.dropna(how='all', axis=1, inplace=True)

# print(df.shape)
# print(df.isnull().sum())

# df.drop('cabin', axis=1, inplace=True)

# print(df.isnull().sum())

# quantity(mean, median), category(mode)

# df.dropna(thresh=5, inplace=True)


# ser = pd.Series([1,2,3,4,5,6,np.nan,7,8, np.nan ,9,10])
# print(ser.mean())
# print(ser.fillna(ser.mean()))
# print(ser.ffill())

# df['age'] = df['age'].ffill().isnull().sum()

# print(df.isnull().sum())

# print(df['embarked'].unique())
# df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
# print(df['embarked'].unique())

# df.dropna(inplace=True)

# print(df.isnull().sum())

#1. Groupby pclass and count on survived
# print(df.groupby(by='pclass')['survived'].count())

# print(df.groupby(by=['pclass','survived'])['survived'].count())
# print(df.groupby(by=['pclass','survived','sex'])['survived'].count())

# multiindexdf = df.groupby(by=['pclass','survived','sex'])['survived'].count()

# print(multiindexdf[(1.0, 00., 'male')])


# print(pd.crosstab([df['pclass'],df['sex'],df['embarked']], df['survived']))
#=======================================================================

df = pd.read_csv('datasets/Iris_data_sample.csv', na_values=['??', '###']).iloc[:, 1:]
# print(df.head(10))
# print(df.tail(10))

# print(df.isnull().sum())

# print(df.info())

# for colname in df.columns:
#     print(df[colname].unique())

# SepalLengthCm    1
# SepalWidthCm     1
# PetalLengthCm    2
# Species          1

# df['SepalLengthCm'] = df['SepalLengthCm'].fillna(df['SepalLengthCm'].mean())

# print(df.groupby(by='Species').mean())
# print(df['SepalLengthCm'].mean())

# print(df[df.isnull().sum(axis=1)>0])

# print(df.groupby(by='Species').agg([min, max]))

santosadf = df[df['Species']=='Iris-setosa']
# print(santosadf['SepalLengthCm'].mean())
# print(santosadf.shape)
santosadf.fillna(round(santosadf['SepalLengthCm'].mean(),2), inplace=True)
df[df['Species']=='Iris-setosa'] = santosadf
# print(df.head())

# print(df['Species'].mode())
# df['Species'] = df['Species'].fillna(df['Species'].mode())
df['Species'] = df['Species'].fillna('Iris-setosa')

santosadf = df[df['Species']=='Iris-setosa']
santosadf.fillna(round(santosadf['SepalWidthCm'].mean(),2), inplace=True)
df[df['Species']=='Iris-setosa'] = santosadf

# print(df.head())
# print(df.isnull().sum())

# print(df['Species'].unique())

# newdf = df.copy()
#---> Encoding-> replace, map, get_dummies(one hot encoding)
# newdf['Species'] = newdf['Species'].replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0,1,2], inplace=True)
# print(newdf.head())

newdf = df.copy()
dic = dict(zip(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0,1,2]))
# print(dic)
newdf['Species'] = newdf['Species'].map(dic)
# print(newdf.head())

#Statistically : 

# print(newdf.groupby(by='Species').mean().sum(axis=1))

#Visually
# import matplotlib.pyplot as plt

# plt.scatter(newdf['PetalLengthCm'],newdf['PetalWidthCm'], c=newdf['Species'])
# plt.show()
#==============================================================================================
#File reading and Writing in Pandas DF

# df.read_csv
# df.read_excel
# df.read_json
# df.read_html
# df.read_sql(query, connection)

# df.to_csv()
# df.to_excel()
# df.to_json()
# df.to_dict()

# pd.ExcelWriter(filename)
# pd.ReadExcel(filename)

#--------------------------------------------

#==> Reading, Processing, and writing data to file
# df = pd.read_csv('datasets/Iris_data_sample.csv', na_values=['??', '###']).iloc[:, 1:]

# df['Species'] = df['Species'].fillna('Iris-setosa')

# for colname in df.iloc[:,:-1].columns:
#     tempdf = df[df['Species']=='Iris-setosa'][colname].copy()
#     mean_val = tempdf.mean()
#     df[df['Species']=='Iris-setosa'][[colname]] = df[df['Species']=='Iris-setosa'][[colname]].fillna(mean_val)




    # df[df['Species']=='Iris-setosa'][colname] = df[df['Species']=='Iris-setosa'][colname].fillna(mean_val)
    # print(df[df['Species']=='Iris-setosa'][colname].head())
    # coldf = coldf.fillna(round(coldf.mean(),2), inplace=True)
    # df[df['Species']=='Iris-setosa'][colname] = coldf
    
# print(df.isnull().sum())

# df = pd.read_csv('datasets/Iris_data_sample.csv', header=None, na_values=['??', '###']).iloc[:, 1:]
# print(df.head())
# df.to_excel('Processed_iris.xlsx', sheet_name='iris_data', index=False, header=False)
# df.to_csv('Processed_iris.csv', index=False, header=False)

# df = pd.read_clipboard()
# print(df.head())
# print(df.shape)

#---------------------------------------------------------------------------------------
import os
import re
# print(os.listdir('datasets/fortune500/'))
# df_li = []
# for fname in os.listdir('datasets/fortune500/'):
#     year = re.findall(r'(\d{4})', fname)[0].strip()
#     df = pd.read_excel(f'datasets/fortune500/{fname}')

#     for colname in df.columns:
#         if 'billion' in colname.strip().lower():
#             df[colname] = df[colname] * 1000

#     df.columns = ['Rank','Company','Revenues ($ millions)','Profits ($ millions)']

#     df.insert(0, 'Year', year)
#     df_li.append(df.copy())
# finaldf = pd.concat(df_li)
# finaldf.to_excel('allFortune500.xlsx', index=False)

#==> One file multiple sheets

# writer = pd.ExcelWriter('allFortune500.xlsx')
# df.to_excel(writer, sheet_name=''sheetname'', index=False)
# writer.save()

# with pd.ExcelWriter('allFortune500.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='sheet1', index=False)
#     df2.to_excel(writer, sheet_name='sheet2', index=False)

# with pd.ExcelWriter('allFortune500.xlsx') as writer:
#     for fname in os.listdir('datasets/fortune500/'):
#         year = re.findall(r'(\d{4})', fname)[0].strip()
#         df = pd.read_excel(f'datasets/fortune500/{fname}')

#         for colname in df.columns:
#             if 'billion' in colname.strip().lower():
#                 df[colname] = df[colname] * 1000

#         df.columns = ['Rank','Company','Revenues ($ millions)','Profits ($ millions)']

#         df.insert(0, 'Year', year)

#         df.to_excel(writer, sheet_name=year, index=False)


#==> Reading all sheet_name of a files : 
# fobj = pd.ExcelFile('allFortune500.xlsx')
# # print(fobj.sheet_names)
# for sheetname in fobj.sheet_names:
#     df = pd.read_excel('allFortune500.xlsx', sheet_name=sheetname)
#     print(df.head())
#-----------------------------------------------------------------------
#=======================================================================

# df.value_counts()
#------------------------------------------------------------------------
#---------------------------------------
'''
pd.pivot_table(
    df,
    values=None (column to aggregate),
    index=None (Row labels),
    columns=None (Column labels),
    aggfunc="mean"/['mean','std'],
    fill_value=None (fillvalue for missing elements)
)
'''

dic = {
    "Dept":["HR","HR","IT","IT","Sales","Sales"],
    "Employee":["Amar","Raj","Shiv","Max","Alice","Bob"],
    "Salary":[50000, 40000, 55000,70000,65000,62000],
    "Gender":["M","M","M","F","F","M"]
}
df = pd.DataFrame(dic)
# print(df.head())

# pivot = pd.pivot_table(
#     df,
#     values="Salary",
#     index="Dept",
#     columns="Gender",
#     aggfunc=["mean", "min", "max"]
# )
# print(pivot)

#--> Total Salary in each Dept
# pivot = pd.pivot_table(
#     df,
#     values="Salary",
#     index="Dept",
#     aggfunc="sum",
#     fill_value=0
# )
# print(pivot)

#--> Total Salary in each Dept Gender wise
# pivot = pd.pivot_table(
#     df,
#     values="Salary",
#     index="Dept",
#     columns="Gender",
#     aggfunc="sum",
#     fill_value=0
# )
# print(pivot)

#---------------------------------------------
# df = pd.read_csv('datasets/mtcars.csv')
# print(df.head())

# pivot = pd.pivot_table(
#     df,
#     values="mpg",
#     index="gear",
#     columns="cyl",
#     aggfunc="mean",
#     fill_value=0
# )
# print(pivot)

#----------------------------------------------------------
# df = pd.read_csv('datasets/mtcars.csv')
# # print(df.head())

# newdf = df.sample(15, random_state=2)
# print(newdf)
#----------------------------------------------------------
df = pd.read_csv('datasets/ebola_country_timeseries.csv')
# print(df.head())
# print(df.isnull().sum())

df.fillna(0, inplace=True)
# print(df.isnull().sum())

df["Date"] = pd.to_datetime(df["Date"])

df.set_index("Date", inplace=True)
# print(df.head())

# print(df.index.year)
# print(df.index.month)

# df.index.year
# df.index.month
# df.index.day
# df.index.day_name()

print(df.head(10))

#--> Filter based on date : 
# print(df.loc["2015-01-05"])

df = df.sort_index()

#--> Filter based on range of dates
print(df.loc["2014-12-24":"2015-01-05"])

#==> To have monthly total out of daily data
# monthly_total = df.resample("ME").sum()
# print(monthly_total)

#--------------------------------------------------
#==> To get the cumulative sum

# newdf = df.cumsum()
# print(newdf.tail(1))

#---------------------------------------------
#==> Rolling avg

# df['rolling_Cases_Guinea'] = df['Cases_Guinea'].rolling(window=3).mean()
# print(df[['Cases_Guinea','rolling_Cases_Guinea']])
#---------------------------------------------

#--> Percentage Change : 

# df['percent_Cases_Guinea'] = df['Cases_Guinea'].pct_change() * 100
# print(df[['Cases_Guinea','percent_Cases_Guinea']])

#---------------------------------------------------------
#-> Compare today's cases count with yesterday's

# df['previous_Cases_Guinea'] = df['Cases_Guinea'].shift(1)
# print(df[['Cases_Guinea','previous_Cases_Guinea']])

#----------------------------------------------------------

# df['diff_Cases_Guinea'] = df['Cases_Guinea'].diff()
# print(df[['Cases_Guinea','diff_Cases_Guinea']])

#----------------------------------------------------------

#-> Line chart

import matplotlib.pyplot as plt

df['Cases_Guinea'].plot(figsize=(8,4), title='Guinea Cases Pattern')

plt.xlabel("Date")
plt.ylabel("Cases")
plt.show()