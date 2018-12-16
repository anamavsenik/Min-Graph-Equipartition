import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(10)
nx.draw_networkx(G)
plt.show()


