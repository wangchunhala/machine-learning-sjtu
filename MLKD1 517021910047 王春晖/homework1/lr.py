from numpy import  *
import pandas as pd
from sklearn.datasets import load_iris
def sigmoid(z):
    return 1/(1+exp(-z))
def solve(X_train,y_train,X_test,y_test,m):
    w = [1 for i in range(m)]
    b = 0
    l = 0.01
    for i in range(1000):
      dw=mat([0 for i in range(m)])
      db=0
      for (x,y) in zip(X_train,y_train):
          dw=dw+(sigmoid(float(mat(x)*mat(w).T+b))-y)*mat(x)
          db=db+(sigmoid(float(mat(x)*mat(w).T+b))-y)
      w=w-0.01*dw
      b=b-0.01*db

    correct = 0
    for (x, y) in zip(X_test, y_test):
            y1=sigmoid(float(mat(x) * mat(w).T + b))
            if(y1<=0.5): y1=0
            else:       y1=1
            if(y1==y): correct+=1
    return correct/len(y_test)

def lr():
    print("#######################This is the result og logistic regression####################")
    file = open('data', 'r')
    X = []
    y = []
    n=17
    m=8
    ntrain=int(17*0.8)
    for i in range(0,17):
        s = file.readline().split()
        a = [eval(x) for x in s]
        X.append(a[:m])
        y.append(a[-1])
    l, r= -1, -1
    d = [3, 3, 3, 4, 4]
    print("accurancy in watermelon as follow")
    a=0
    for i in range(5):
        l = r + 1
        r = l + d[i] - 1
        X_train, y_train = X[:l] + X[r + 1:], y[:l] + y[r + 1:]
        X_test, y_test = X[l:r + 1], y[l:r + 1]
        print("the "+str(i+1)+"time "+str(solve(X_train, y_train, X_test, y_test, 8)))
        a+=(solve(X_train, y_train, X_test, y_test, 8))
    print("average=",a/5 )





    iris = load_iris()
    docdoc = random.permutation(100)
    attributes = iris.data
    target = iris.target
    labels = iris.feature_names


    print("Iris 0 and 1 acurancy as follow")
    y_,y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index!=2]
    target = iris.target[y_index!=2]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    LX=attributes
    ly=target
    p,q=-1,-1
    a=0
    for b in range(5):
            p = q+1
            q = p + 20-1
            X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[docdoc[q + 1:]].tolist()
            X_test, y_test = LX[docdoc[p:q+ 1]].tolist(), ly[docdoc[p:q+ 1]].tolist()
            print("the " + str(b + 1) + "time " + str(solve(X_train, y_train, X_test, y_test, 4)))
            a += (solve(X_train, y_train, X_test, y_test, 4))
    print("average=", a / 5)

    p, q =-1,-1
    y_,y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index!=1]
    target = iris.target[y_index!=1]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    for my in range(100):
        if (target[my]==2):target[my]=1
    LX=attributes
    ly=target
    print("Iris 0 and 2 acurancy as follow")
    a=0
    for b in range(5):
            p = q+1
            q = p + 20-1
            X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[docdoc[q + 1:]].tolist()
            X_test, y_test = LX[docdoc[p:q+ 1]].tolist(), ly[docdoc[p:q+ 1]].tolist()
            print("the " + str(b + 1) + "time " + str(solve(X_train, y_train, X_test, y_test, 4)))
            a += (solve(X_train, y_train, X_test, y_test, 4))
    print("average=", a / 5)

    y_,y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index!=0]
    target = iris.target[y_index!=0]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    for my in range(100):
        if (target[my]==2):target[my]=0
    p,q=-1,-1
    LX=attributes
    ly=target
    print("Iris 1 and 2 acurancy as follow")
    a=0
    for b in range(5):
            p = q+1
            q = p + 20-1
            X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[docdoc[q + 1:]].tolist()
            X_test, y_test = LX[docdoc[p:q+ 1]].tolist(), ly[docdoc[p:q+ 1]].tolist()
            print("the " + str(b + 1) + "time " + str(solve(X_train, y_train, X_test, y_test, 4)))
            a += (solve(X_train, y_train, X_test, y_test, 4))
    print("average=", a / 5)






