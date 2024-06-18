from sklearn.svm import LinearSVC

# Pega os dados retornados pelo modelo, recebe os dados originais, e verifica a acurácia dessa predição
from sklearn.metrics import accuracy_score 


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
rotulos_teste = ['S', 'S', 'S'] 
# Repostas que ele vai usar como base da predição
# Aqui estou definindo que os 3 compostos são solúveis, por isso de 100% de precisão no acerto...
# Se eu mudar um dos rótulos para 'N', ou seja, Não Solúvel, a taxa de acerto mudará


previsoes = modelo.predict(dados_teste)

mapeamento_previsoes = {'S': 'Solúvel', 'N': 'Não Solúvel'}

taxa_acerto = accuracy_score(rotulos_teste, previsoes)
print("Taxa de acerto: %.2f%%" % (taxa_acerto * 100))