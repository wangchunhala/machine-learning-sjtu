import csv
from sklearn import svm
from numpy import  *
from sklearn.datasets import load_iris

import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn", lineno=193)

def linearKernel(X, Y,Z1,Z2):
            clf = svm.SVC(kernel='linear')
            clf.fit(X, Y)

            ey = clf.predict(Z1)
            i=0
            correct=0
            for sy in ey:
               if(sy==Z2[i]):
                correct=correct+1;
               i=i+1
            return correct / len(Z2)

def gassianKernel(X, Y,Z1,Z2):
             clf = svm.SVC(kernel='rbf')
             clf.fit(X, Y)
             ey = clf.predict(Z1)
             i = 0
             correct = 0
             for sy in ey:
                 if (sy == Z2[i]):
                     correct = correct + 1;
                 i = i + 1
             return correct / len(Z2)
def polyKernel(X, Y,Z1,Z2):
             clf = svm.SVC(kernel='poly')
             clf.fit(X, Y)

             ey = clf.predict(Z1)
             i = 0
             correct = 0
             for sy in ey:
                 if (sy == Z2[i]):
                     correct = correct + 1;
                 i = i + 1
             return correct / len(Z2)

def sigmoidKernel(X, Y,Z1,Z2):
             clf = svm.SVC(kernel='sigmoid')
             clf.fit(X, Y)
             ey = clf.predict(Z1)
             i = 0
             correct = 0
             for sy in ey:
                 if (sy == Z2[i]):
                     correct = correct + 1;
                 i = i + 1
             return correct / len(Z2)
def svmwch():
    print("#######################This is the result og SVM####################")
    file = open('data', 'r')
    X = []
    y = []
    n=17
    nlist=8
    ntrain=int(17*0.8)
    for i in range(n):
        s = file.readline().split()
        a = [eval(x) for x in s]

        X.append(a[:nlist] )
        y.append(a[-1])
    X_train=X[:ntrain]
    y_train = y[:ntrain]
    X_test=X[ntrain:]
    y_test=y[ntrain:]
    X_train=mat(X_train)
    y_train=(y_train)
    X_test=mat(X_test)
    y_test=(y_test)
    print("watermelon")
    print("linearKernel",linearKernel(X_train, y_train,X_test,y_test))
    print("gassianKernel",gassianKernel(X_train, y_train,X_test,y_test))
    print("polyKernel",polyKernel(X_train, y_train,X_test,y_test))
    print("sigmoidKernel", sigmoidKernel(X_train, y_train,X_test,y_test))

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
    e=0
    r=0
    t=0
    u=0
    for b in range(5):
        p = q + 1
        q = p + 20 - 1
        X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[docdoc[q + 1:]].tolist()
        X_test, y_test = LX[docdoc[p:q + 1]].tolist(), ly[docdoc[p:q + 1]].tolist()
        X_train = mat(X_train)
        X_test = mat(X_test)
        y_train=(y_train)
        y_test=(y_test)

        print("the " + str(b + 1) + "time linearKernel" + str(linearKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time gassianKernel" + str(gassianKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time polyKernel" + str(polyKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time sigmoidKernel" + str(sigmoidKernel(X_train, y_train, X_test, y_test)))
        e+=linearKernel(X_train, y_train, X_test, y_test)
        r+=gassianKernel(X_train, y_train, X_test, y_test)
        t+=polyKernel(X_train, y_train, X_test, y_test)
        u+=sigmoidKernel(X_train, y_train, X_test, y_test)
    print("average of linearKernel",e/5)
    print("average of gassianKernel", r / 5)
    print("average of polyKernel", t / 5)
    print("average of sigmoidKernel", u / 5)
    p, q = -1, -1
    y_, y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index != 1]
    target = iris.target[y_index != 1]  # 获取类别数据，这里注意的是已经经过了处理，target里0、1、2分别代表三种类别
    for my in range(100):
        if (target[my] == 2): target[my] = 1
    LX = attributes
    ly = target
    print("Iris 0 and 2 acurancy as follow")
    e=0
    r=0
    t=0
    u=0
    for b in range(5):
        print("the " + str(b + 1) + " time")
        p = q + 1
        q = p + 20 - 1
        X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[docdoc[q + 1:]].tolist()
        X_test, y_test = LX[docdoc[p:q + 1]].tolist(), ly[docdoc[p:q + 1]].tolist()
        print("the " + str(b + 1) + "time linearKernel" + str(linearKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time gassianKernel" + str(gassianKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time polyKernel" + str(polyKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time sigmoidKernel" + str(sigmoidKernel(X_train, y_train, X_test, y_test)))
        e += linearKernel(X_train, y_train, X_test, y_test)
        r += gassianKernel(X_train, y_train, X_test, y_test)
        t += polyKernel(X_train, y_train, X_test, y_test)
        u += sigmoidKernel(X_train, y_train, X_test, y_test)
    print("average of linearKernel",e/5)
    print("average of gassianKernel", r / 5)
    print("average of polyKernel", t / 5)
    print("average of sigmoidKernel", u / 5)

    y_, y_index = unique(iris.target, return_inverse=True_)
    attributes = iris.data[y_index != 0]
    target = iris.target[y_index != 0]
    for my in range(100):
        if (target[my] == 2): target[my] = 0
    p, q = -1, -1
    LX = attributes
    ly = target
    print("Iris 1 and 2 acurancy as follow")
    e=0
    r=0
    t=0
    u=0
    for b in range(5):
        print("the "+str(b+1)+" time")
        p = q + 1
        q = p + 20 - 1
        X_train, y_train = LX[docdoc[:p]].tolist() + LX[docdoc[q + 1:]].tolist(), ly[docdoc[:p]].tolist() + ly[
            docdoc[q + 1:]].tolist()
        X_test, y_test = LX[docdoc[p:q + 1]].tolist(), ly[docdoc[p:q + 1]].tolist()
        print("the " + str(b + 1) + "time linearKernel" + str(linearKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time gassianKernel" + str(gassianKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time polyKernel" + str(polyKernel(X_train, y_train, X_test, y_test)))
        print("the " + str(b + 1) + "time sigmoidKernel" + str(sigmoidKernel(X_train, y_train, X_test, y_test)))
        e += linearKernel(X_train, y_train, X_test, y_test)
        r += gassianKernel(X_train, y_train, X_test, y_test)
        t += polyKernel(X_train, y_train, X_test, y_test)
        u += sigmoidKernel(X_train, y_train, X_test, y_test)
    print("average of linearKernel",e/5)
    print("average of gassianKernel", r / 5)
    print("average of polyKernel", t / 5)
    print("average of sigmoidKernel", u / 5)





