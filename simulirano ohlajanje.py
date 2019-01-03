import random
import math

def simulirano_ohlajanje(G,t): #temperaturo običajno nastavimo na visoko vrednost
    n = len(G)
    for a in range(0, n): #spremenimo diagonalo, da ima same 0
        if G[a][a] == 1:
            G[a][a] = 0
    d1 = int(n / 2)
    X = list(range(0, d1)) #vektorja indeksov vozlišč
    Y = list(range(d1, n))
    A = list(range(0, d1)) #vektorja indeksov vozlišč
    B = list(range(d1, n))
    k = 1
    (najboljsi_seznam_stevila_sosedov, najboljse_stevilo_povezav) = seznam_stevila_sosedov(G,X,Y)
    #tisti, ki je pri prejsnjem koraku najboljsi glede na vse prejsnje
    while (t>0):
        (trenutni_seznam_stevila_sosedov, trenutno_stevilo_povezav) = (najboljsi_seznam_stevila_sosedov, najboljse_stevilo_povezav)
        mesto = random.randrange(len(A))
        a = A[mesto]
        mesto2 = random.randrange(len(B))
        b = B[mesto2]
        #prvi indeks ti vedno pove s kolikimi je povezan v svoji množici, drugi  pa s kolikimi v drugi množici
        trenutno_stevilo_povezav += trenutni_seznam_stevila_sosedov[a][0] + trenutni_seznam_stevila_sosedov[b][0]
        trenutno_stevilo_povezav -= trenutni_seznam_stevila_sosedov[a][1] + trenutni_seznam_stevila_sosedov[b][1]
        if G[a][b] == 1:
            trenutno_stevilo_povezav += 2
        print(trenutno_stevilo_povezav,trenutni_seznam_stevila_sosedov,a,b)
        Q = najboljse_stevilo_povezav-trenutno_stevilo_povezav #naša kvaliteta
        if (trenutno_stevilo_povezav < najboljse_stevilo_povezav) or (random.uniform(0, 1) < math.exp(Q/t)):
            najboljse_stevilo_povezav = trenutno_stevilo_povezav
            #pogledamo, kako se spremenijo sosedi
            for i in A:
                if G[i][a] == 1:
                    trenutni_seznam_stevila_sosedov[i][0] -= 1
                    trenutni_seznam_stevila_sosedov[i][1] += 1
                if G[i][b] ==1:
                    trenutni_seznam_stevila_sosedov[i][0] += 1
                    trenutni_seznam_stevila_sosedov[i][1] -= 1
            for j in B:
                if G[j][b] == 1:
                    trenutni_seznam_stevila_sosedov[j][0] -= 1
                    trenutni_seznam_stevila_sosedov[j][1] += 1
                if G[j][a] ==1:
                    trenutni_seznam_stevila_sosedov[j][0] += 1
                    trenutni_seznam_stevila_sosedov[j][1] -= 1
            #pri vozliščih, ki sta se zamnjali, notranje povezave postanejo zunanje in obratno
            obrat = trenutni_seznam_stevila_sosedov[a][0]
            trenutni_seznam_stevila_sosedov[a][0] = trenutni_seznam_stevila_sosedov[a][1]
            trenutni_seznam_stevila_sosedov[a][1] = obrat
            obrat2 = trenutni_seznam_stevila_sosedov[b][0]
            trenutni_seznam_stevila_sosedov[b][0] = trenutni_seznam_stevila_sosedov[b][1]
            trenutni_seznam_stevila_sosedov[b][1] = obrat2
            najboljsi_seznam_stevila_sosedov = trenutni_seznam_stevila_sosedov
            vmesni= A[mesto] #zamenjamo ju še v vektorju A in B
            A[mesto] = B[mesto2]
            B[mesto2] = vmesni
        k += 1
        t -= 0.1
    return A, B, trenutno_stevilo_povezav

def seznam_stevila_sosedov(G,C,D):    #izracuna zacetno stevilo sosedov za vsako vozlisce in stevilo povezav med mnozicama vozlisc
    n = len(G)
    #prva stevilka pove stevilo, s kolikimi je povezan v svoji mnozici, druga pa s kolikimi je povezan v drugi množici:
    seznam_stevila_sosedov = [[0, 0]] * n
    stevilo_povezav = 0
    for nahajanje, i in enumerate(C, 0):
        Ix = 0
        Ox = 0
        for m in C:
            if G[i][m] == 1:
                Ix += 1
        for j in D:
            if G[i][j] == 1:
                Ox += 1
        seznam_stevila_sosedov[nahajanje] = [Ix, Ox]
        stevilo_povezav += Ox
    for nahajanje2, j in enumerate(D,0):
        Iy = 0
        Oy = 0
        for l in C:
            if G[j][l] == 1:
                Oy += 1
        for o in D:
            if G[j][o] == 1:
                Iy += 1
        seznam_stevila_sosedov[nahajanje2 + len(C)] = [Iy, Oy]
    return seznam_stevila_sosedov, stevilo_povezav

#primeri simuliranega ohlajanja in delovanje pri različnih temperaturah
# MATRIKE
A = [[0,0,0,1,1,1,1,0,0,1,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0],[1,1,1,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,1],[1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,0]]
B = [[0,1,0,0,0,0,1],[1,0,0,0,1,0,1],[0,0,0,0,1,0,1],[0,0,0,0,1,1,0],[0,1,1,1,0,1,0],[0,0,0,1,1,0,0],[1,1,1,0,0,0,0]]
B1 = [[0,0,1,1,1,0,0],[0,0,0,0,0,1,0],[1,0,0,1,0,1,0],[1,0,1,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,0,0,0,1],[0,0,0,1,1,1,0]]
C = [[0,1,0,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,0,1,0,0]]
C1 = [[0,0,1,1,0,0],[0,0,0,1,0,1],[1,0,0,0,1,0],[1,1,0,0,0,1],[0,0,1,0,0,1],[0,1,0,1,1,0]]
D = [[0,1,1,0,1,1],[1,0,0,1,1,0],[1,0,0,1,0,1],[0,1,1,0,1,0],[1,1,0,1,0,1],[1,0,1,0,1,0]]
D1 = [[0,0,1,1,1,1],[0,0,1,0,1,1],[1,1,0,1,1,1],[1,0,1,0,0,1],[1,1,1,0,0,0],[1,1,1,1,0,0]]
E = [[0,1,1,0,1,1,1],[1,0,1,1,1,0,1],[1,1,0,1,1,1,0],[0,1,1,0,1,1,1],[1,1,1,1,0,1,0],[1,0,1,1,1,0,1],[1,1,0,1,0,1,0]]
E1 = [[0,1,1,1,1,1,0],[1,0,0,1,1,1,0],[1,0,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,0,1,1],[1,1,1,1,1,0,0],[0,0,1,1,1,0,0]]
# J,A,B,B1,C,C1: redki grafi; G,D,D1,E,E1: gosti grafi
#generiranje naključnih matrik poljubnih velikosti:

import numpy as np

def nakljucna_matrika(velikost): #funkcija ki vrne simetrične matrike
    A = np.random.randint(2, size=(velikost,velikost))
    m= np.tril(A) + np.tril(A,-1).T
    return np.array(m).tolist()

#funkcija, ki iz matrike A nariše graf v dveh barvah

import networkx as nx
import matplotlib.pyplot as plt

def pobarvaj_graf(A,X,Y):
    M=numpy.matrix(A)
    G=nx.from_numpy_matrix(M)
    color_map = []
    for node in G:
        if node in X:
            color_map.append('blue')
        else:
            color_map.append('green')
    nx.draw(G,node_color = color_map,with_labels = True)
    plt.show()
