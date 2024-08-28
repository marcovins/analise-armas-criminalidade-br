import matplotlib.pyplot as plt
import networkx as nx

# Função para visualizar um grafo
def visualizar_grafo(grafo, titulo):
    pos = nx.spring_layout(grafo)
    plt.title(titulo)
    nx.draw(grafo, pos, with_labels=False)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=False)
    plt.show()
