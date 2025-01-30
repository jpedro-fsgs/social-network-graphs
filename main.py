import networkx as nx

def gerar_dados(G):
    number_of_nodes = G.number_of_nodes()

    degrees = nx.degree(G)
    average_degree = sum(dict(degrees).values()) / number_of_nodes

    average_clustering = nx.average_clustering(G)
    average_shortest_path_length = nx.average_shortest_path_length(G)\
          if number_of_nodes < 5000 else "O(n²), não vai rolar"

    return (
        f"Conectividade Média: {average_degree}\n" +
        f"Coeficiente de Agregação Médio: {average_clustering}\n" +
        f"Menor Caminho Médio: {average_shortest_path_length}\n"
        )


G_twitter = nx.read_edgelist("twitter_combined.txt", create_using=nx.Graph, nodetype=int)
G_facebook = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph, nodetype=int)

nx.write_graphml(G_twitter, "grafo_twitter.graphml")
nx.write_graphml(G_facebook, "grafo_facebook.graphml")

print("Twitter:\n\n" + gerar_dados(G_twitter))
print("Facebook:\n\n" + gerar_dados(G_facebook))

