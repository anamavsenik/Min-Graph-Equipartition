import networkx as nx
import matplotlib.pyplot as plt
import numpy

def pobarvaj_graf(A,X,Y):  #iz matrike A nariše graf v dveh barvah
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

