import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('datasets/iris.csv').iloc[:,1:]
df['Species'] = df['Species'].replace(['setosa','versicolor','virginica'],[0,1,2]).astype(int)

print(df.info())

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=2)

model = GaussianNB()
model.fit(xtrain, ytrain)

ypred = model.predict(xtest)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print(accuracy_score(ytest, ypred))
print(confusion_matrix(ytest, ypred))
print(classification_report(ytest, ypred))