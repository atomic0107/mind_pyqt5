"""
https://python.atelierkobato.com/sigmoid/
"""
from pandas import DataFrame
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate

import matplotlib.pyplot as plt
import numpy as np
import math


def logistic_func(a,b,c,t):
    f = a / (1 + np.exp(-b * a * (t - c)))
    #f = (a*b)/(a+(b-a)*np.exp(-1*c*t))
    return f

def main():
    #clf = LogisticRegression()


    print("matplotlib")
    x = np.arange(-15,15,1)
    #a = [-4,2, 4]
    a = [ -1]#yseppen ywidth
    b = [ 1]#傾き           constant
    #b = [-4,-2,2, 4]
    #c =  [-6,-4,-2, 0, 2, 4, 6]
    #c = [-4,-2,2, 4]
    c = [0]#xseppen  constant
    #c = [-4,0,4]#立ち上がり中心
    #for db in b:
    
    
    for da in a:
        for db in b:
            for dc in c:
                f = []
                for t in x:            
                    y=logistic_func(da,db,dc,t)
                    f.append([y,1])
                plt.scatter(x,f,marker="o",color='red')
        
    X = DataFrame(x)
    F = DataFrame(f)
    AX,PX,AF,PF = train_test_split(X, F, test_size = 0.2, random_state = 42) # 100%のデータを学習データに、20%を検証データにする
    #lr = LinearRegression()
    clf = LogisticRegression()
    #lr.fit(X,F)
    clf.fit(AX,AF)
    #PF = lr.predict(X)
    PF = clf.predict(AX)
    plt.plot(PX,PF,color='blue')
    plt.show()

if __name__ == "__main__":
    main()
