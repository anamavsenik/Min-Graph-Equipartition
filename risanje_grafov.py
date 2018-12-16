import networkx as nx
import matplotlib.pyplot as plt

A=numpy.matrix([[0,0,1,0,1,0,0],[0,0,1,1,0,0,0],[1,1,0,0,0,1,0],[0,1,0,0,1,0,1],[1,0,0,1,0,1,1],[0,0,1,0,1,0,1],[0,0,0,1,1,1,0]])
G=nx.from_numpy_matrix(A)
nx.draw_networkx(G)
plt.show()

#predloga barvanja grafov na dve barvi:
G = nx.erdos_renyi_graph(20,0.1)
color_map = []
for node in G:
    if node <10:
        color_map.append('blue')
    else:
        color_map.append('green')
nx.draw(G,node_color = color_map,with_labels = True)
plt.show()

