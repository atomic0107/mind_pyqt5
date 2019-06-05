"""
https://python.atelierkobato.com/sigmoid/
"""
import matplotlib.pyplot as plt
import numpy as np
import math


def logistic_func_t1(a,b,c,t):
    f = a / (1 + np.exp(-b * a * (t - c)))
    #f = (a*b)/(a+(b-a)*np.exp(-1*c*t))
    return f

"""
amin    : 描画開始位置
amax    : 描画終了位置
x       : xの標本数
x0      : 傾き最大のｘの位置
h       : 傾き
s       : s > 0
"""
def logistic_func_t2(amin,amax,x,x0,h,s):

    y1 = amin
    y2 = amax - amin
    y3 = (x/x0)**(-1*h)
    y4 = 1 + (y3**s)
    f = y1 + ( y2 / y4 )
    #f = (a*b)/(a+(b-a)*np.exp(-1*c*t))
    return f


def main():

    x = np.arange(0, 5, 1) #not 0 start
    amin = [-9, -3, 3, 9]
    amax = [-10,-5,0, 5, 10]
    #amax=[0]
    x0 = [2.5]#傾き最大のx座標
    #h = [-15,-10,-5,0, 5, 10, 15]#中心の傾き係数
    h=[15]
    s = 0.5# s > 0
    for damin in amin:
        for damax in amax:
            for dx0 in x0:
                for dh in h:
                    f=[]
                    for t in x:
                        y = logistic_func_t2(damin,damax,t,dx0,dh,s)
                        f.append(y)
                    #plt.scatter(x,f,marker="o",color='red')
                    plt.plot(x,f,color='red')
    plt.show()

if __name__ == "__main__":
    main()