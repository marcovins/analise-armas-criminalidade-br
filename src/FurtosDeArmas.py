import pandas as pd

# Carregar o arquivo CSV
arquivo_base = pd.read_csv("../rsc/datasets/ocorrencias/OCORRENCIAS_2024.csv", encoding='ISO-8859-1', delimiter=';')

pd.set_option('display.max_columns', None)  # Exibir todas as colunas

# Filtrar as diferentes categorias de ocorrência
furtos = arquivo_base.loc[arquivo_base['TIPO_OCORRENCIA'].str.strip() == 'Furto de Arma de Fogo']
apreensao = arquivo_base.loc[arquivo_base['TIPO_OCORRENCIA'].str.strip() == 'Apreensão de Arma de Fogo']
recuperacao = arquivo_base.loc[arquivo_base['TIPO_OCORRENCIA'].str.strip() == 'Recuperação de Arma de Fogo']
extravio_perca = arquivo_base.loc[arquivo_base['TIPO_OCORRENCIA'].str.strip() == 'Extravio/Perda de Arma de Fogo']
roubo = arquivo_base.loc[arquivo_base['TIPO_OCORRENCIA'].str.strip() == 'Roubo de Arma de Fogo']

# Limpar e obter os municípios únicos
municipios = arquivo_base['MUNICIPIO'].str.strip().unique()

# Exibir os municípios únicos
for municipio in municipios:
    print(municipio)

df_municipios = pd.DataFrame(municipios, columns=['MUNICIPIO'])

df_municipios.to_csv("../datasets/ocorrencias/municipios.csv")

print(df_municipios)