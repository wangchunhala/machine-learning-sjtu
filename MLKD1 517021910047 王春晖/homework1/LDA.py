import pandas as pd
from numpy import *
import csv
from sklearn.datasets import load_iris

def solve(X_train, y_train, X_test, y_test,m):
    x1=mat([0 for i in range(m)])
    xm1=[]
    x0 = mat([0 for i in range(m)])
    xm0=[]
    n0=0
    n1=0
    for x,y in zip(X_train,y_train):
        if (y==1):
            x1=x1+x
            xm1.append(x)
            n1+=1
        else:
            x0=x0+x
            xm0.append(x)
            n0+=1
    xm1=mat(xm1)
    xm0 = mat(xm0)
    x1=x1/n1
    x0=x0/n0
    sigma1=cov(xm1.T)
    sigma0=cov(xm0.T)
    sw1=sigma0+sigma1
    w=mat(mat(sw1).I*((x0-x1).T))

    w0=x0*w
    w1=x1*w
    y_predict=X_test*w
    syl=[]
    i=0
    correct=0
    for sy in y_predict:
        if (abs(sy-w0)<abs(sy-w1)) : sy=0;
        else:         sy=1
        if(sy==y_test[i]):
            correct=correct+1;
        i=i+1
    return correct/len(y_test)




def LDA():
    print("#######################This is the result og LDA####################")
    print("watermelon")
    file = open('data', 'r')
    X = []
    y = []
    n=17
    m=8
    ntrain=int(17*0.8)
    ap=[]
    for i in range(0,17):
        s = file.readline().split()
        a = [eval(x) for x in s]
        X.append(a[:8])
        y.append(a[-1])
    X_train=X[:ntrain]
    y_train = y[:ntrain]
    X_test=X[ntrain:]
    y_test=y[ntrain:]
    print(solve(X_train, y_train, X_test, y_test,8))
    iris = load_iris()
    docdoc = random.permutation(100)
    attributes = iris.data
    target = iris.target
    labels = iris.feature_names

    print("Iris 0 and 1 acurancy as follow")
    y_, y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index != 2]
    target = iris.target[y_index != 2]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    LX = attributes
    ly = target
    p, q = -1, -1
    a=0
    for b in range(5):
        p = q + 1
        q = p + 20 - 1
        X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q+ 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[
            docdoc[q + 1:]].tolist()
        X_test, y_test = LX[docdoc[p:q + 1]].tolist(), ly[docdoc[p:q + 1]].tolist()
        print("the " + str(b + 1) + "time " + str(solve(X_train, y_train, X_test, y_test, 4)))
        a+=solve(X_train, y_train, X_test, y_test, 4)
    print("average=", a / 5)

    p, q = -1, -1
    y_, y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index != 1]
    target = iris.target[y_index != 1]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    for my in range(100):
        if (target[my] == 2): target[my] = 1
    LX = attributes
    ly = target
    print("Iris 0 and 2 acurancy as follow")
    a=0
    for b in range(5):
        p = q + 1
        q = p + 20 - 1
        X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q+ 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[
            docdoc[q + 1:]].tolist()
        X_test, y_test = LX[docdoc[p:q + 1]].tolist(), ly[docdoc[p:q + 1]].tolist()
        print("the " + str(b + 1) + "time " + str(solve(X_train, y_train, X_test, y_test, 4)))
        a += solve(X_train, y_train, X_test, y_test, 4)
    print("average=", a / 5)
    y_, y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index != 0]
    target = iris.target[y_index != 0]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    for my in range(100):
        if (target[my] == 2): target[my] = 0
    p, q = -1, -1
    LX = attributes
    ly = target
    print("Iris 1 and 2 acurancy as follow")
    a=0
    for b in range(5):
        p = q + 1
        q = p + 20 - 1
        X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[
            docdoc[q + 1:]].tolist()
        X_test, y_test = LX[docdoc[p:q + 1]].tolist(), ly[docdoc[p:q + 1]].tolist()
        print("the " + str(b + 1) + "time " + str(solve(X_train, y_train, X_test, y_test, 4)))
        a += solve(X_train, y_train, X_test, y_test, 4)
    print("average=", a / 5)







