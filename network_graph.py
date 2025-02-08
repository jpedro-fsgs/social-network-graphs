import networkx as nx

def gerar_dados(G):
    number_of_nodes = G.number_of_nodes()
    number_of_edges = G.number_of_edges()

    degrees = nx.degree(G)
    average_degree = sum(dict(degrees).values()) / number_of_nodes

    average_shortest_path_length = (
        nx.average_shortest_path_length(G)
        if number_of_nodes < 5000
        else "O(n²), não vai rolar"
    )

    return (
        f"Número de nós: {number_of_nodes}\n"
        f"Número de arestas: {number_of_edges}\n"
        f"Conectividade Média: {average_degree}\n"
        f"Menor Caminho Médio: {average_shortest_path_length}\n"
    )


G_facebook = nx.read_edgelist("source_data/facebook_combined.txt", create_using=nx.Graph, nodetype=int)
G_twitter = nx.read_edgelist("source_data/twitter_combined.txt", create_using=nx.Graph, nodetype=int)

nx.write_graphml(G_facebook, "grafo_facebook.graphml")
nx.write_graphml(G_twitter, "grafo_twitter.graphml")

print("Facebook:\n\n" + gerar_dados(G_facebook))
print("Twitter:\n\n" + gerar_dados(G_twitter))