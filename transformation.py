#Importando as bibliotecas para análise

import pandas as pd

#Importando os arquivos
base_dados = pd.read_csv("compilation.csv", sep = ";")

#Retirando o espaço vazio antes e depois do nome da coluna "Custo Material"
base_dados.rename(columns={' Custo Material ': 'Custo Material'}, inplace = True) 

# Criar uma nova coluna chamada "sinal" para indicar se o valor é positivo ou negativo (Custo Material)
base_dados['sinal'] = base_dados['Custo Material'].str.contains("-").astype(int)

# Remova o sinal de negativo dos valores na coluna "Custo Material"
base_dados['Custo Material'] = base_dados['Custo Material'].str.replace("-", "")
# Trocando a virgulo por ponto
base_dados['Custo Material'] = base_dados['Custo Material'].str.replace(",", ".")

# Converta a coluna "Custo Material" para o tipo float ou int, dependendo do seu conteúdo
base_dados['Custo Material'] = pd.to_numeric(base_dados['Custo Material'], errors='coerce')

# Multiplique a coluna "Custo Material" pelo sinal para obter os valores corretos
base_dados['Custo Material'] = base_dados['Custo Material'] * (-1) ** base_dados['sinal']

# Remover a coluna auxiliar "Sinal" da base de dados
base_dados.drop(columns = ["sinal"], inplace = True)

# Converter a coluna "Posting date" para o tipo data
base_dados["Posting date"] = pd.to_datetime(base_dados["Posting date"])	

# Exportar a base de dados editada para o formato csv
base_dados.to_csv("compilation_att.csv")
