import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Device1", "Device2"),
    ("Device1", "Device3"),
    ("Device2", "Device4"),
    ("Device3", "Device4"),
    ("Device4", "Device5")
])

plt.figure(figsize=(6,4))

nx.draw(
    G,
    with_labels=True,
    node_size=2000,
    font_size=10
)

plt.title("5-Node Network Topology")
plt.savefig("network_topology.png")
plt.show()

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())
