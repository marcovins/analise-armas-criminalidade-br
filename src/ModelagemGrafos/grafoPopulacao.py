import pandas as pd
import networkx as nx
from src.visualizar import visualizar_grafo

arquivo_base = pd.read_excel("../../rsc/datasets/populacao/POP2022_Brasil_e_UFs.xltx")

grafoCrimes = nx.DiGraph()
grafoCrimes.add_node('Populacao')
grafoCrimes.add_nodes_from(arquivo_base['UNIDADES DA FEDERAÇÃO'])


# Adicionando as arestas com os pesos
for _, row in arquivo_base.iterrows():
    origem = row['UNIDADES DA FEDERAÇÃO'].strip()
    destino = 'Populacao'
    quantidade = row['POPULAÇÃO']
    if quantidade:
        grafoCrimes.add_edge(origem, destino, weight=quantidade)

#visualizar_grafo(grafoCrimes, "Grafo de Crimes")

# Salvando o grafo no formato GEXF
#nx.write_gexf(grafoCrimes, "../../rsc/datasets/grafo_populacao.gexf")