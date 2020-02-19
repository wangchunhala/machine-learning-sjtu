from numpy import *
from math import sqrt, pi, exp, log
from sklearn.datasets import load_iris
def solve(X_train,y_train,X_test,y_test):
    nx=len(X_train)
    nt=len(X_test)
    correct =0
    for (X,Y) in zip(X_test,y_test):
        gailv=[]
        for(ey)in [0,1]:
            a=[x for (x,y)in zip(X_train,y_train) if y==ey]
            p = len(a) / nx
            for i in range(6):

                cnt=0
                for x in a:
                    if x[i]==X[i]:cnt+=1
                p*=(cnt)/(len(a))
            for i in range (6,8):
               sum=0
               for x in a:
                   sum=sum+x[i]
               aver=sum/len(a)
               div=0
               for x in a:
                   div = div + (x[i]-aver)**2
               p*=1/math.sqrt(2*math.pi)/div*math.exp(-(X[i]-aver)*(X[i]-aver)/2/div/div)
            gailv.append(p)
        if(gailv.index(max(gailv))==Y):
            correct+=1
    print(correct/nt)
    return correct,correct/nt

def solve1(X_train, y_train, X_test, y_test):
        nx = len(X_train)
        nt = len(X_test)
        correct = 0
        for (X, Y) in zip(X_test, y_test):
            gailv = []
            pmax=0
            pmaxy=0
            for (ey) in [0, 1, 2]:
                a = [x for (x, y) in zip(X_train, y_train) if y == ey]
                p = len(a) / nx
                for i in range(4):
                    sum = 0
                    for x in a:
                        sum = sum + x[i]
                    aver = sum / len(a)
                    div = 0
                    for x in a:
                        div = div + (x[i] - aver) ** 2
                        div=math.sqrt(div)
                    p *= 1 / math.sqrt(2 * math.pi) / div * math.exp(-(X[i] - aver) * (X[i] - aver) / 2 / div / div)
                gailv.append(p)

            if (gailv.index(max(gailv))== Y):
                correct += 1
        return correct, correct / nt
def Bayes():
        print("#######################This is the result og Bayes####################")
        k = 5
        n=17
        m=8
        l, r= -1, -1
        d = [3, 3, 3, 4, 4]
        file = open('data', 'r')
        X = []
        y = []
        for i in range(n):
            s = file.readline().split()
            a = [eval(x) for x in s]
            X.append(a[:m])
            y.append(a[-1])
        corrects = 0
        corrects_rate=0

        print("watermelon")
        for i in range(5):
                l = r + 1
                r = l + d[i] - 1
                X_train, y_train = X[:l]+X[r+1:], y[:l]+y[r+1:]
                X_test, y_test = X[l:r+1], y[l:r+1]
                corrects+=solve(X_train,y_train,X_test,y_test)[1]
        print("average",corrects/5)


        iris = load_iris()
        docdoc = random.permutation(150)
        attributes = iris.data
        target = iris.target
        labels = iris.feature_names

        y_,y_index = unique(iris.target, return_inverse=True_)
        attributes = iris.data
        target = iris.target
        LX=attributes
        ly=target
        p,q=-1,-1
        print("iris")
        corrects=0
        for b in range(5):
                    p = q+1
                    q = p + 30-1
                    X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q+ 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[docdoc[q + 1:]].tolist()
                    X_test, y_test = LX[docdoc[p:q+ 1]].tolist(), ly[docdoc[p:q+ 1]].tolist()
                    print("iris of naive bayes the ",b,"time ",solve1(X_train, y_train, X_test, y_test)[1] )
                    corrects+=solve1(X_train, y_train, X_test, y_test)[1]
        print("average", corrects / 5)








