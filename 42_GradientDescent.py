import pandas as pd
import numpy as np

df = pd.read_csv('houseprice.csv')
# print(df)

X = df.iloc[:,0].values
y = df.iloc[:,1].values

# print(X)
# print(y)

print(X.tolist())
print(y.tolist())

X = np.array([round((xval-min(X))/(max(X)-min(X)),2) for xval in X])
y = np.array([round((yval-min(y))/(max(y)-min(y)),2) for yval in y]) 

print(X.tolist())
print(y.tolist())

#y = mx + c

def gradient_descent(x, y):
    m_gradient = 0.75
    c_gradient = 0.45
    learning_rate = 0.0001
    iterations = 10
    # print(x)
    # print(y)
    for i in range(iterations):
        ypred = (m_gradient * x) + c_gradient
        # print(ypred)
        sse = (((y-ypred)**2)/2).sum()
        print(sse)

        m_gradient = sum(-(y-ypred)*x)
        c_gradient = sum(-(y-ypred))

        #print(f"Cost={sse}, slope={m_gradient} yintercept={c_gradient}")

        m_gradient = m_gradient - (learning_rate * m_gradient)
        c_gradient = c_gradient - (learning_rate * c_gradient)
        
#gradient_descent(X, y)



