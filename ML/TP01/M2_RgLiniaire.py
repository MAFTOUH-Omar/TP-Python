import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n_observation = 100
X = np.linspace(0 , 10 , n_observation).reshape((n_observation , 1))
Y = X + np.random.randn(n_observation , 1)
plt.scatter(X , Y)
plt.show()

x1 = np.ones(n_observation)
x = np.c_[x1,X]
print(x)
def reggression_lineare_ols(X , y) :
    theta = np.linalg.inv(X.T@X)@X.T@Y
    return theta
theta = reggression_lineare_ols(x , Y)

predection = X.dot(theta)

plt.scatter(X[ : , 1] , Y)
plt.plot(X[ :  , 1] , predection , color = 'red')