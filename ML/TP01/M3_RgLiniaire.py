import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n_observation = 100
X = np.linspace(0 , 10 , n_observation).reshape((n_observation , 1))
Y = X + np.random.randn(n_observation , 1)
plt.scatter(X , Y)
plt.show()

theta = np.random.rand(2 , 1)
alpha = 1
nbrIteration = 100

def fonctionCout ( X , Y , theta) :
    n = len(Y)
    predection = X.dot(theta)
    cout = ( 1/2 * n ) * np.sum( np.square( predection - Y ) )
    return cout

def fonctionGradient ( X , Y , theta , alpha , nbrIteration ) :
    n = len(Y)
    coutHistorique = np.zeros(n , nbrIteration)
    for i in range(nbrIteration) :
        prediction = X.dot(theta)
        err = prediction - Y
        gradient = (1/n) * X.T.dot(err)
        theta = theta - alpha * gradient
        coutHistorique[i] = fonctionCout(X , Y , theta)
    return theta , coutHistorique

theta , coutHistorique = fonctionGradient( X , Y , theta , alpha , nbrIteration)
plt.plot(range(1 , nbrIteration + 1) , coutHistorique , color = 'red')
plt.show()