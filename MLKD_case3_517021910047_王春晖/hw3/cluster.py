import numpy as np

n, m = 17, 8
file = open('data1', 'r')
data = []
label = []
for i in range(n):
    s = file.readline().split()
    a = [eval(x) for x in s]
    data.append(a[:m])
    label.append(a[-1])
data = np.array(data)
def eur(ci,cj,data):
    eursum1=0
    a=len(ci)
    b=len(cj)
    for c in ci:
        eursum1+=np.sum(np.sqrt(np.sum((data[c]-data[cj])**2, 1)))

    eursum1 = eursum1 / a / b

    return eursum1
def ncut(ci,cj,W,D):
    cut = 0
    for c in ci:
        cut += np.sum(W[c][cj])
    volci=np.sum(D[ci])
    volcj=np.sum(D[cj])
    ncut=cut/volci+cut/volcj
    return ncut
def knn(data, K, sigma):
    n = data.shape[0]
    indices = np.zeros((n, K))
    distance = np.zeros((n, K))
    for i in range(n):
        dist = np.sum((data[i] - data) ** 2, 1)
        ind = np.argsort(dist)
        indices[i] = ind[1:K+1]
        distance[i] = dist[ind[1:K+1]]
    indices=indices.astype(np.int32)
    W = np.zeros((n, n))
    for i in range(n):
        W[i, indices[i]] = np.exp(-distance[i] / (2 * sigma**2))
    W = (W + W.T) / 2
    D = np.sum(W,1)
    return W, D


def merge(data, juli, labelright, K=3, sigma=2):
    W, D = knn(data, K, sigma)
    n = data.shape[0]
    label = np.arange(n)
    for i in range(n - 2):
        c = list(set(label))
        m = len(c)
        choices = []
        for x in range(m):
            for y in range(x + 1, m):
                if juli == 'eur':
                    p = eur(np.where(label == c[x])[0], np.where(label == c[y])[0], data)
                if juli == 'ncut':
                    p = ncut(np.where(label == c[x])[0], np.where(label == c[y])[0], W, D)
                choices.append([p, c[x], c[y]])
        choices.sort()
        x, y = choices[0][1:]
        #smallest distance
        label[label == y] = x
        print(i,'th',label)

    c = list(set(label))
    l0=[]
    l1=[]
    for i in range(n):
        if(label[i]==c[0]):l0.append(i)
        if (label[i] == c[1]): l1.append(i)
    print('class1 index',l0)
    print('class2 index',l1)






print ('ncut')
merge(data, 'ncut',label)
print ('eur')
merge(data, 'eur',label)
