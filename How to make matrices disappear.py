import numpy as np
import csv
import time



# How to make matrices disappear


def Test(L) :
    l = len(L)
    for i in range(0,l) :
        if np.all(L[i] == [[0,0],[0,0]]) :
            return (True)
            break

def MD(A,B) :
    K = [A,B]
    while Test(K) != True :
        l = len(K)
        M = []
        for i in range(0,l) :
            M.append(np.dot(K[i],A))
            M.append(np.dot(K[i],B))
        K = M
    print(True)

A = [[2,-2],[2,2]]
B = [[0,0],[0,1]]
MD(A,B)
