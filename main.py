import networkx as nx

G = nx.read_edgelist("twitter_combined.txt", create_using=nx.Graph, nodetype=int)
G = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph, nodetype=int)

nx.write_graphml(G, "grafo_twitter.graphml")
nx.write_graphml(G, "grafo_facebook.graphml")
