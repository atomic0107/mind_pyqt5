import matplotlib.pyplot as plt
import numpy as np
import math


def logistic_func(a,b,c,t):
    f = 1/(1+np.exp(-1*b*(c-t)))
    return f

def main():
    
    print("matplotlib")
    x = np.arange(-6,6,0.1)
    a = [-4,-2, 0, 2, 4]
    #a = [ 1, 1, 1, 1, 1, 1, 1]
    #a = [0,2,4,6]
    #b = [-4,-2, 0, 2, 4]
    b = [ -1, 1, 1, 1, 1, 1, 1]
    #c=  [-6,-4,-2, 0, 2, 4, 6]
    c = [ 1, 1, 1, 1, 1]

    #for db in b:
    
    for da in a:
        for db in b:
            for dc in c:
                f = []
                for t in x:
                    y=logistic_func(da,db,dc,t)
                    f.append(y)
                plt.plot(x,f)
    plt.show()

if __name__ == "__main__":
    main()
