import pandas as pd
import networkx as nx
from src.visualizar import visualizar_grafo

arquivo_base = pd.read_csv("../../rsc/datasets/crimes_por_estado/Crimes_brasil_uf.csv")

municipios = arquivo_base['Uf'].str.strip().unique()
crimes = arquivo_base['Tipo_crime'].str.strip().unique()
    
grafoCrimes = nx.DiGraph()
grafoCrimes.add_nodes_from(municipios)
grafoCrimes.add_nodes_from(crimes)

# Adicionando as arestas com os pesos
for _, row in arquivo_base.iterrows():
    uf = row['Uf'].strip()
    crime = row['Tipo_crime'].strip()
    quantidade = row['Ocorrencias']
    if quantidade:
        grafoCrimes.add_edge(uf, crime, weight=quantidade)

visualizar_grafo(grafoCrimes, "Grafo de Crimes")

# Salvando o grafo no formato GEXF
#nx.write_gexf(grafoCrimes, "../../rsc/datasets/grafo_crimes.gexf")
