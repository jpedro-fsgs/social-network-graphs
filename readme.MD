# Apresentação: Análise de Redes Sociais com Teoria de Grafos

## Slide 1: Introdução
- A análise de redes sociais é essencial para compreender a estrutura das conexões entre indivíduos.
- Utilizamos a teoria de grafos para modelar e estudar essas interações.
- Neste trabalho, analisamos redes sociais extraídas do Facebook e Twitter utilizando dados da plataforma SNAP Stanford.

## Slide 2: Objetivos
- Reproduzir e validar a implementação de análise de redes sociais.
- Examinar a estrutura das redes do Facebook e Twitter em termos de conectividade e densidade.

## Slide 3: Metodologia e Métodos
- Dados extraídos de: [SNAP Stanford](https://snap.stanford.edu/data/)
- Representação dos dados: Matriz de adjacência no formato:
  ```
  0 1
  0 2
  0 3
  0 4
  ...
  ```
- Ferramentas utilizadas:
  - NetworkX para manipulação e análise de grafos.
  - Formato GraphML para armazenamento dos grafos.
  - Gephi para representação gráfica dos grafos

## Slide 4: Execução
- Código implementado em Python com NetworkX:
```python
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

    density = nx.density(G)

    return (
        f"Número de nós: {number_of_nodes}\n"
        f"Número de arestas: {number_of_edges}\n"
        f"Conectividade Média: {average_degree}\n"
        f"Menor Caminho Médio: {average_shortest_path_length}\n"
        f"Densidade da Rede: {density}\n"
    )


G_twitter = nx.read_edgelist("twitter_combined.txt", create_using=nx.Graph, nodetype=int)
G_facebook = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph, nodetype=int)

nx.write_graphml(G_twitter, "grafo_twitter.graphml")
nx.write_graphml(G_facebook, "grafo_facebook.graphml")

print("Facebook:\n\n" + gerar_dados(G_facebook))
print("Twitter:\n\n" + gerar_dados(G_twitter))
```

## Slide 5: Resultados
**Facebook:**
- Número de nós: 4039
- Número de arestas: 88234
- Conectividade Média: 43.69
- Menor Caminho Médio: 3.69
- Densidade da Rede: 0.0108

**Twitter:**
- Número de nós: 81306
- Número de arestas: 1342310
- Conectividade Média: 33.01
- Menor Caminho Médio: O(n²), não vai rolar
- Densidade da Rede: 0.0004

## Slide 6: Discussão dos Resultados
- A amostra de rede do Facebook apresenta maior densidade e menor caminho médio, sugerindo maior interconectividade entre os usuários.
- A amostra de rede do Twitter, por ser significativamente maior, apresenta menor densidade e complexidade elevada para cálculo do menor caminho médio.
- Esses resultados estão alinhados com estudos de redes sociais, que sugerem que redes sociais fechadas (Facebook) tendem a ser mais densas do que redes abertas (Twitter).

## Slide 7: Representação Visual
- **Grafo do Facebook** ![Grafo do Facebook](graph_images/facebook_grafo.png)
- **Grafo do Twitter** ![Grafo do Twitter](graph_images/twitter_grafo.png)

## Slide 8: Conclusão
- O estudo demonstrou diferenças estruturais significativas entre as redes sociais analisadas.
- A metodologia utilizada pode ser aplicada a outras redes sociais para exploração de padrões e características estruturais.

## Slide 9: Referências
- Dados obtidos de: [SNAP Stanford](https://snap.stanford.edu/data/)
- Implementação baseada na documentação do NetworkX.
- Artigo relacionado: "Análise das Redes Sociais à Luz da Teoria de Grafos".
