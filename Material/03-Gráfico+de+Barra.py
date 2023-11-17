"""
# Exemplo 1: Gráfico com 2 barras

import matplotlib.pyplot as plt
from numpy import*

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]
notas_2 = [25, 32, 34, 20 ,25]

y = arange(len(legenda))
altura = 0.3  # Altura das barras

grafico1 = plt.barh(y - altura/2, notas_1, height=altura, label='Notas P1', color='yellow')
grafico2 = plt.barh(y + altura/2, notas_2, height=altura, label='Notas P2', color='cyan')

plt.xlabel('Pontos')
plt.title("Pontuação por aluno")
plt.yticks(y, legenda)
plt.legend()

def legenda_automatica(grafico):
    Adiciona a legenda ao lado da barra automaticamente
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
                     xytext=(7, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico1)
legenda_automatica(grafico2)

plt.show()


"""
# Vamos aos exemplos:

# Exemplo 2: Gráfico com 3 barras

import matplotlib.pyplot as plt
from numpy import*

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]
notas_2 = [25, 32, 34, 20, 25]
notas_3 = [28, 30, 34, 27, 22]

y = arange(len(legenda))
altura = 0.3  # Altura das barras

grafico1 = plt.barh(y - 3*altura/2, notas_1, height=altura, label='Notas P1', color='yellow', align='edge')
grafico2 = plt.barh(y, notas_2, height=altura, label='Notas P2', color='cyan', align='center')
grafico3 = plt.barh(y + altura/2, notas_3, height=altura, label='Notas P3', color='lime', align='edge')

plt.xlabel('Pontos')
plt.title("Pontuação por aluno")
plt.yticks(y, legenda)
plt.legend()

def legenda_automatica(grafico):
    """Adiciona a legenda ao lado da barra automaticamente"""
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
                     xytext=(7, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico1)
legenda_automatica(grafico2)
legenda_automatica(grafico3)

plt.show()


