# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.model_selection import train_test_split

# df = pd.read_csv('datasets/iris.csv').iloc[:,1:]
# df['Species'] = df['Species'].replace(['setosa','versicolor','virginica'],[0,1,2]).astype(int)

# print(df.info())

# X = df.iloc[:, :-1].values
# y = df.iloc[:, -1].values

# xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=2)

# model = KMeans(n_clusters=3)
# model.fit(xtrain)

# # print(model.cluster_centers_)
# centroids = model.cluster_centers_

# ypred = model.predict(xtest)
# print(ytest)
# print(ypred)

# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

# ax1.scatter(x=xtest[:,[0,1]].sum(axis=1), y=xtest[:,[2,3]].sum(axis=1), c=ytest)
# ax1.scatter(x=centroids[:,[0,1]].sum(axis=1), y=centroids[:,[2,3]].sum(axis=1), c='RED')
# ax1.set_title('Actual')

# ax2.scatter(x=xtest[:,[0,1]].sum(axis=1), y=xtest[:,[2,3]].sum(axis=1), c=ypred)
# ax2.scatter(x=centroids[:,[0,1]].sum(axis=1), y=centroids[:,[2,3]].sum(axis=1), c='RED')
# ax2.set_title('Predicted')
# plt.show()


# Ridge, Lasso, SVR, SVC, DecisionTreeClassifier, DecisionTreeRegressor, RandomForest, DBSCAN

# from sklearn.datasets import load_iris

# iris = load_iris()

# print(iris.data)
# print(iris.target)
# print(iris.feature_names)
# print(iris.target_names)
