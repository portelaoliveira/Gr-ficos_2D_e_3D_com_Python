"""
# Exemplo 3: Python avançado. Utilizando dicionário e função zip().

import matplotlib.pyplot as plt
from numpy import*

alunos = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]
notas_2 = [25, 32, 34, 20, 25]
notas_3 = [28, 30, 34, 27, 22]

dados_zip = zip(alunos, notas_1, notas_2, notas_3)
# A partir desse zip(), vamos criar um dicionário em que a chave seja o aluno e o valor seja a nota máxima obtida.

y = arange(len(alunos))
altura = 0.3

dados_dict = {dados[0]: max(dados[1], dados[2], dados[3]) for dados in dados_zip}

grafico1 = plt.barh(y, dados_dict.values(), height=altura, label="Maior Nota", align='center', color='red')

plt.xlabel("Notas")
plt.title("Pontuação por aluno")
plt.yticks(y, dados_dict.keys())
plt.legend()

def legenda_automatica(grafico):
    Adiciona a legenda ao lado da barra automaticamente
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
                     xytext=(7, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico1)
plt.show()
"""

# Exemplo 3: Python avançado. Utilizando dicionário e função zip().

import matplotlib.pyplot as plt
from numpy import*

alunos = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 34, 30, 35, 27]
notas_2 = [25, 32, 34, 20, 25]
notas_3 = [28, 30, 34, 27, 22]

dados_zip = zip(alunos, notas_1, notas_2, notas_3)
# A partir desse zip(), vamos criar um dicionário em que a chave seja o aluno e o valor seja a nota máxima obtida.

y = arange(len(alunos))
altura = 0.3

dados_dict = {dados[0]: max(dados[1], dados[2], dados[3]) for dados in dados_zip}

grafico1 = plt.barh(y, dados_dict.values(), height=altura, label="Maior Nota", align='center', color='red')

plt.xlabel("Notas")
plt.title("Pontuação por aluno")
plt.yticks(y, dados_dict.keys())
plt.legend()

def legenda_automatica(grafico):
    """Adiciona a legenda ao lado da barra automaticamente"""
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
                     xytext=(7, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico1)
plt.show()




