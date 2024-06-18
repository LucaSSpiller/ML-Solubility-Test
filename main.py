# EXEMPLO PRÁTICO - Aprendizado Supervisionado

# COMO TREINAR A MAQUINA...
# COMO O ML FAZ COM QUE OS PCS APRENDAM COM OS DADOS, E COMO FAZER COM QUE ELES TOMEM A DECISÃO SEM PRECISAR SEREM PROGRAMADOS
# PARA CADA SITUAÇÃO ESPECÍFICA


# Identificar se um composto é ou não solúvel em água dependendo das características informadas

from sklearn.svm import LinearSVC

composto1 = [1, 1, 1]
composto2 = [0, 0, 0]
composto3 = [1, 0, 1]
composto4 = [0, 1, 0]
composto5 = [1, 1, 0]
composto6 = [0, 0, 1]

dados_treino = [composto1, composto2, composto3, composto4, composto5, composto6]
rotulos_treino = ['S', 'N', 'S', 'N', 'S', 'S']


# Agora vou fazer um 'fit' - pegar os dados do treino, com os rotulos de cada dado de treino - e então começar a aprender
modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)

teste1 = [1, 0, 0]
teste2 = [0, 1, 1]
teste3 = [1, 0, 1]

dados_teste = [teste1, teste2, teste3]

previsoes = modelo.predict(dados_teste)

mapeamento_previsoes = {'S': 'Solúvel', 'N': 'Não Solúvel'}

print("Previsões do modelo para os compostos testados: ", previsoes)
for i, previsao in enumerate(previsoes):
    print(f'O composto {i+1} pode ser considerado {mapeamento_previsoes[previsao]}')


# BLZ, ATÉ AQUI MOSTROU NA TELA O QUE FOI PEDIDO, MAS COMO SABER SE O QUE FOI MOSTRADO ESTÁ CORRETO???

# A ANÁLISE ESTÁ SENDO FEITA NO ARQUIVO 'solubility.py'

