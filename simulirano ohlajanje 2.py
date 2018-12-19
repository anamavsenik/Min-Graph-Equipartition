def pomozna(G,X,Y):
    n = len(G)
    k=0
    for i in X:
        for j in Y:
            while k < 3000 or t < 0:
                if S > 0 or random.uniform(0, 1) < math.exp(S/t):
                    x = X.index(i)
                    y = Y.index(j)
                    X[x] = j
                    Y[y] = i
                    return X, Y, False
                t = (500/log(k))
        k+=1
    return X,Y,True

def simulirano_ohlajanje(G): #G je matrika sosednosti
    n = len(G)
    for a in range(0,n):
        if G[a][a] ==1:
            G[a][a]=0
    d1=int(n/2)
    koncaj=False
    X=list(range(0,d1))
    Y=list(range(d1,n))
    while koncaj==False:
        [X,Y,koncaj]= pomozna(G,X,Y)
    return X,Y

