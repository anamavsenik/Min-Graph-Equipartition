def pomozna(G,X,Y):
    n = len(G)
    for i in X:
        for j in Y:
            Ix = 0
            Ox = 0
            Iy = 0
            Oy = 0
            for k in X:
                if G[i][k] == 1:
                    Ix += 1
                if G[j][k] == 1:
                    Oy += 1
            for l in Y:
                if G[j][l] == 1:
                    Iy += 1
                if G[i][l] == 1:
                    Ox += 1
            S = Ox - Ix + Oy - Iy - 2 * G[i][j]
            if S > 0:
                x = X.index(i)
                y = Y.index(j)
                X[x] = j
                Y[y] = i
                return X, Y, False
    return X,Y,True

def pozresna_metoda(G): #G je matrika sosednosti
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

#preizkusi na matriki
J=[[0,0,0,1,1,1,1,0,0,1,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0],[1,1,1,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,1],[1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,0]]
G= [[0, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1], [1, 1, 1, 0, 1, 0]]
