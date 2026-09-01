from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
import pandas as pd

data = '''
Outlook	Temperature	Humidity	Windy	Play
Rainy	Hot	High	FALSE	No
Rainy	Hot	High	TRUE	No
Overcast	Hot	High	FALSE	Yes
Sunny	Mild	High	FALSE	Yes
Sunny	Cool	Normal	FALSE	Yes
Sunny	Cool	Normal	TRUE	No
Overcast	Cool	Normal	TRUE	Yes
Rainy	Mild	High	FALSE	No
Rainy	Cool	Normal	FALSE	Yes
Sunny	Mild	Normal	FALSE	Yes
Rainy	Mild	Normal	TRUE	Yes
Overcast	Mild	High	TRUE	Yes
Overcast	Hot	Normal	FALSE	Yes
Sunny	Mild	High	TRUE	No
'''
dli = []
for line in data.strip().splitlines():
    dli.append(line.strip().split())

# print(dli)

df = pd.DataFrame(dli[1:], columns=dli[0])
print(df)

newdf = pd.DataFrame()
for col in df.columns:
    dic = dict(zip(df[col].unique(), range(len(df[col].unique()))))
    print(dic)
    newdf[col] = df[col].map(dic)
print(newdf)

X,y = newdf.iloc[:,:-1].values, newdf.iloc[:,-1].values

model = DecisionTreeClassifier()
model.fit(X, y)

ypred = model.predict(X)
print(ypred)

# from sklearn.metrics import accuracy_score
# print(accuracy_score(y, ypred))

# import matplotlib.pyplot as plt

# plot_tree(model, feature_names=['Outlook','Temperature','Humidity','Windy'], class_names=['Yes', 'No'], filled=True, impurity=True, proportion=True, rounded=True, fontsize=10)
# plt.show()



