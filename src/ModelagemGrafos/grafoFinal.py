import networkx as nx
from src.visualizar import visualizar_grafo
def calcularPeso(pesoCrime: float, pesoOcorrencia: float, pesoPopulacao: float) -> float:
    pesoPopulacao = pesoPopulacao / 100000
    indiceCrimes = (pesoOcorrencia / pesoCrime) / pesoPopulacao
    return indiceCrimes

def somarOcorrencias(lista:list) -> float:
    total = 0.0
    for valor in lista:
        total+=valor[1]
    return total

# Leitura dos grafos
grafoCrimes = nx.read_gexf("../../rsc/datasets/grafo_crimes.gexf")
grafoOcorrencias = nx.read_gexf("../../rsc/datasets/grafo_ocorrencias.gexf")
grafoPopulacao = nx.read_gexf("../../rsc/datasets/grafo_populacao.gexf")

# Conversão dos nós do grafoCrimes para lista
crimes = list(grafoCrimes.nodes)
remocoes = ['Estupro', 'Furto de veículo', 'Homicídio doloso', 'Lesão corporal seguida de morte',
            'Roubo a instituição financeira', 'Roubo de carga', 'Roubo de veículo',
            'Roubo seguido de morte (latrocínio)', 'Tentativa de homicídio']
crimes = [crime for crime in crimes if crime not in remocoes]

# Inicialização correta do dicionário
dicionarioCrimes = {}

# Populando o dicionário com dados das arestas
for vertice in crimes:
    arestas = list(grafoCrimes.out_edges(vertice, data=True))
    if vertice not in dicionarioCrimes:
        dicionarioCrimes[vertice] = []
    for aresta in arestas:
        destino, dados = aresta[1], aresta[2]
        dicionarioCrimes[vertice].append((destino, dados['weight']))

# Conversão dos nós do grafoOcorrencias para lista
ocorrencias = list(grafoOcorrencias.nodes)
remocoes = ['Furto de Arma de Fogo', 'Extravio/Perda de Arma de Fogo',
            'Recuperação de Arma de Fogo', 'Apreensão de Arma de Fogo', 'Roubo de Arma de Fogo']
ocorrencias = [ocorrencia for ocorrencia in ocorrencias if ocorrencia not in remocoes]

# Dicionário para transformar siglas em nomes das UFs
ufs_brasil = {
    'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 'BA': 'Bahia',
    'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás',
    'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais',
    'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco', 'PI': 'Piauí',
    'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo',
    'SE': 'Sergipe', 'TO': 'Tocantins'
}

# Criando dicionário com dados das arestas
dicionarioOcorrencias = {}

# Preenchendo dict
for vertice in ocorrencias:
    arestas = list(grafoOcorrencias.out_edges(vertice, data=True))
    if vertice in ufs_brasil:
        nome_uf = ufs_brasil[vertice]
        if nome_uf not in dicionarioOcorrencias:
            dicionarioOcorrencias[nome_uf] = []
        for aresta in arestas:
            destino, dados = aresta[1], aresta[2]
            dicionarioOcorrencias[nome_uf].append((destino, dados['weight']))


# Conversão dos nós do grafoPopulacao para lista
populacao = sorted(list(grafoPopulacao.nodes))
del populacao[18]

dicionarioPopulacao = {}

for vertice in populacao:
    aresta = list(grafoPopulacao.out_edges(vertice, data=True))
    dicionarioPopulacao[vertice] = aresta[0][2]['weight']


# Inicialização do grafo final
grafoFinal = nx.DiGraph()
grafoFinal.add_node("Associação entre violência e a circulação ilícita de armas de fogo")
grafoFinal.add_nodes_from(ufs_brasil.values())

for vertice in ufs_brasil.values():
    origem = vertice
    quantidadeOcorrencias = somarOcorrencias(dicionarioOcorrencias[vertice])
    quantidadeCrimes = somarOcorrencias(dicionarioCrimes[vertice])
    populacao = dicionarioPopulacao[vertice]
    destino = "Associação entre violência e a circulação ilícita de armas de fogo"
    pesoAresta = calcularPeso(quantidadeCrimes, quantidadeOcorrencias, populacao)
    grafoFinal.add_edge(origem, destino, weight=pesoAresta)


#visualizar_grafo(grafoFinal, "Associação entre violência e a circulação ilícita de armas de fogo")


# Salvando o grafo no formato GEXF
#nx.write_gexf(grafoFinal, "../../rsc/datasets/grafo_final.gexf")
