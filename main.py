import networkx as nx
from faker import Faker

fake = Faker("pt_BR")
G = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph, nodetype=int)


for node in G.nodes:
    G.add_node(node, name=fake.name())


print(G.nodes.data())
nx.write_graphml(G, "grafo.graphml")
