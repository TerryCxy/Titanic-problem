import numpy as np
from builtins import object
from builtins import range
import math
from past.builtins import xrange


class Logistics_model(object):
    def __init__(self):
        pass

    def sigmoid(self, inX):
        inX=np.array(inX,dtype=np.float32)
        hx=1.0/(1.0 + np.exp(-inX))
        return hx

    def train_grad_up(self, X, y, iters=300, a=0.01):
        n = X.shape[1]
        X=np.mat(X)
        theta=np.ones((n,1))
        for iter in range(iters):
            error=y-self.sigmoid(X.dot(theth))
            theta = theta + a * (X.transpose()).dot(error)
        return theta

    def predict(self,X_test,theta):
        pred=self.sigmoid(X_test.dot(theta))
        pred[pred>=0.5]=1
        pred[pred<0.5]=0
        return pred