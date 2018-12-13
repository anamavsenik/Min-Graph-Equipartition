# libraries
import as plt
import networkx as nx
import pandas as pd

# Build a dataframe with 4 connections
df = pd.DataFrame({'from': ['A', 'B', 'C', 'A'], 'to': ['D', 'A', 'E', 'C']})
df

# Build your graph
G = nx.from_pandas_dataframe(df, 'from', 'to')

# Plot it
nx.draw(G, with_labels=True)
plt.show()
