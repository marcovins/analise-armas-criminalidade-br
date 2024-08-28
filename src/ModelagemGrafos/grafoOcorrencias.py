import pandas as pd
import networkx as nx
from src.visualizar import visualizar_grafo


arquivo_base = pd.read_csv("../../rsc/datasets/ocorrencias/OCORRENCIAS_ate_2023.csv", encoding='ISO-8859-1', delimiter=',')

# Removendo linhas onde 'TIPO_OCORRENCIA' é um dos valores indesejados
lista_remocoes = ['Apostilada no Exercito', 'Campanha do Desarmamento', 'Remetida ao Exército para destruição', 'Sub Judice', 'Arrecadação', 'Alteração da Arma de Porte']
arquivo_base = arquivo_base[~arquivo_base['TIPO_OCORRENCIA'].str.strip().isin(lista_remocoes)]

# Removendo linhas onde 'ANO_OCORRENCIA' é inferior a 2015 ou superior a 2022
anos_validos = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
arquivo_base = arquivo_base[arquivo_base['ANO_OCORRENCIA'].isin(anos_validos)]

# Filtrar até janeiro de 2022
filtro = (arquivo_base['ANO_OCORRENCIA'] < 2022) | ((arquivo_base['ANO_OCORRENCIA'] == 2022) & (arquivo_base['MES_OCORRENCIA'] <= 1))
arquivo_base = arquivo_base[filtro]

# Filtrar desde dezembro de 2015
filtro = (arquivo_base['ANO_OCORRENCIA'] > 2015) | ((arquivo_base['ANO_OCORRENCIA'] == 2015) & (arquivo_base['MES_OCORRENCIA'] == 12))
arquivo_base = arquivo_base[filtro]

# Agrupar os dados por MUNICIPIO e TIPO_OCORRENCIA e contar as ocorrências
ocorrencias_agrupadas = arquivo_base.groupby(['UF', 'TIPO_OCORRENCIA']).size().reset_index(name='quantidade')

# Criando o grafo
grafo = nx.DiGraph()

# Adicionando as unidades federativas e tipos de ocorrência como nós no grafo
uf = arquivo_base['UF'].str.strip().unique()
crimes = arquivo_base['TIPO_OCORRENCIA'].str.strip().unique()

grafo.add_nodes_from(uf)
grafo.add_nodes_from(crimes)

# Adicionando as arestas com os pesos
for _, row in ocorrencias_agrupadas.iterrows():
    municipio = row['UF'].strip()
    crime = row['TIPO_OCORRENCIA'].strip()
    quantidade = row['quantidade']
    if quantidade:
        grafo.add_edge(municipio, crime, weight=quantidade)

# Visualizar o grafo
visualizar_grafo(grafo, "Grafo de Ocorrências por Município")

# Salvando o grafo no formato GEXF
#nx.write_gexf(grafo, "../../rsc/datasets/grafo_ocorrencias.gexf")

