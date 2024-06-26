# Projeto de Machine Learning: Identificação de Solubilidade em Água
## Descrição

Este projeto de machine learning identifica se um composto é solúvel ou não em água com base nas características informadas. Foi utilizado um modelo de classificação, especificamente um `LinearSVC` da biblioteca `scikit-learn`, para realizar essa tarefa.
## Estrutura do Projeto
### Dados de Treinamento

Os dados de treinamento consistem em vetores que representam diferentes compostos químicos, com características binárias simplificadas. Cada composto é rotulado como 'S' (Solúvel) ou 'N' (Não Solúvel).

```python
composto1 = [1, 1, 1]
composto2 = [0, 0, 0]
composto3 = [1, 0, 1]
composto4 = [0, 1, 0]
composto5 = [1, 1, 0]
composto6 = [0, 0, 1]

dados_treino = [composto1, composto2, composto3, composto4, composto5, composto6]
rotulos_treino = ['S', 'N', 'S', 'N', 'S', 'S']
```

### Treinamento do Modelo

O modelo `LinearSVC` é treinado utilizando os dados de treinamento acima.

```python
from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)
```
### Dados de Teste

Os dados de teste são novos compostos cujas solubilidades devem ser previstas pelo modelo.
```python
teste1 = [1, 0, 0]
teste2 = [0, 1, 1]
teste3 = [1, 0, 1]

dados_teste = [teste1, teste2, teste3]
```
### Previsões

O modelo faz previsões sobre os dados de teste e as mapeia para uma descrição mais amigável.

```python
previsoes = modelo.predict(dados_teste)
mapeamento_previsoes = {'S': 'Solúvel', 'N': 'Não Solúvel'}

print("Previsões do modelo para os compostos testados: ", previsoes)
for i, previsao in enumerate(previsoes):
    print(f'O composto {i+1} pode ser considerado {mapeamento_previsoes[previsao]}')
```

## Análise de Resultados

As previsões do modelo são impressas para verificação. Para garantir a acurácia das previsões, é importante comparar os resultados com dados reais ou validar o modelo utilizando métodos estatísticos e métricas de performance.
## Arquivo de Implementação

A implementação completa deste projeto está no arquivo solubility.py.
## Exemplo de Uso

Para executar o projeto, basta rodar primeiro o arquivo `main.py` e depois o arquivo `solubility.py` e observar as previsões geradas pelo modelo.
