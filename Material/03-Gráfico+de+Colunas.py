"""
#Exemplo 1: Gráfico com uma coluna

import matplotlib.pyplot as plt
from numpy import*

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]

x = arange(len(legenda)) # Localização das legendas no eixo x
largura = 0.3  # Determina a largura das colunas

plt.bar(x, notas_1, width=largura, label='Notas P1', color='green', align='edge')
plt.ylabel('Pontos')
plt.title('Pontuação por aluno')
plt.xticks(x, legenda)
plt.legend()
plt.show()


#Exemplo 2: Gráfico com duas colunas

import matplotlib.pyplot as plt
from numpy import*

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]
notas_2 = [25, 32, 34, 20, 25]

x = arange(len(legenda)) # Localização das legendas no eixo x
largura = 0.3  # Determina a largura das colunas

plt.bar(x - largura/2, notas_1, width=largura, label='Notas P1', color='green')
plt.bar(x + largura/2, notas_2, width=largura, label='Notas P2', color='blue')
plt.ylabel('Pontos')
plt.title('Pontuação por aluno')
plt.xticks(x, legenda)
plt.legend()
plt.show()


#Exemplo 3: Gráfico com duas colunas e anotações.

import matplotlib.pyplot as plt
from numpy import*

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]
notas_2 = [25, 32, 34, 20, 25]

x = arange(len(legenda)) # Localização das legendas no eixo x
largura = 0.3  # Determina a largura das colunas

grafico1 = plt.bar(x - largura/2, notas_1, width=largura, label='Notas P1', color='green')
grafico2 = plt.bar(x + largura/2, notas_2, width=largura, label='Notas P2', color='blue')
plt.ylabel('Pontos')
plt.title('Pontuação por aluno')
plt.xticks(x, legenda)
plt.legend()


def legenda_automatica(grafico):
    Adiciona a legenda acima da coluna do gráfico de acordo com a altura desta
    for i in grafico:
        altura = i.get_height()
        plt.annotate(f'{altura}', xy=(i.get_x() + i.get_width()/2, altura),
                     xytext=(0, 2), textcoords='offset points', ha='center')


legenda_automatica(grafico1)
legenda_automatica(grafico2)

plt.show()
"""

