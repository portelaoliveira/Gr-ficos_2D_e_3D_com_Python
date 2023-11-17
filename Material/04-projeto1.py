"""
Vamos criar um dicionário que contenha como chave o número do aluno e como valor tenha uma tupla com a nota das 6 provas
feitas ao longo do semestre.

Nosso projeto consistirá em:
    - Criar um gráfico de pizza com a porcentagem de alunos aprovados e reprovados
    - Criar um histograma com as médias finais dos alunos
    - Criar um gráfico de colunas mostrando as 3 maiores notas de cada um.

"""
# Nossos imports:
from numpy import*
import random
import matplotlib.pyplot as plt

# Nossos dados:

n_alunos = range(1, 26)

dados = {}

for posicao in n_alunos:
    chave = str(posicao)
    prova = 1
    notas = []
    while prova <= 6:
        nota = random.randrange(0, 11)
        notas.append(nota)
        prova += 1
    dados.update({chave: notas})

# Calculando a média dos alunos: A média será formada pelas 3 maiores notas obtidas por cada aluno.

def ordena_notas(listagem):  # Função para ordenar as notas em ordem decrescente.
    ordenadas = sorted(listagem, reverse=True)
    return ordenadas

def calcula_media(listagem):  # Função que calcula a média das 3 maiores notas obtidas.
    lista_ordenada = ordena_notas(listagem)
    pos = 0
    soma = 0
    while pos < 6:
        soma += lista_ordenada[pos]
        pos += 1
    return round(soma/6, 2)  # Função round() faz o arredondamento dos valores numéricos.


medias_alunos = {chave: calcula_media(valor) for chave, valor in dados.items()}

# Gráfico de colunas mostrando as 3 maiores notas de cada aluno.

def pega_nota(dicionario, posicao_nota):
    """Função que recebe um dicionário cujos valores são um iterável com as notas dos alunos
    e recebe a posição da nota desejada (Maior Nota, 2ª Maior nota, etc.)"""
    lista= []
    valores = dicionario.values()
    for i in valores:
        maior_nota = ordena_notas(i)[posicao_nota - 1]
        lista.append((maior_nota))
    return lista


x = arange(len(n_alunos))
largura = 0.3  # Largura das colunas

notas_1 = pega_nota(dados, 1)
notas_2 = pega_nota(dados, 2)
notas_3 = pega_nota(dados, 3)

grafico1 = plt.bar(x - 3*largura/2, notas_1, width=largura, label='1ª Maior Nota', align='edge')
grafico2 = plt.bar(x, notas_2, width=largura, label='2ª Maior Nota', align='center')
grafico3 = plt.bar(x + largura/2, notas_3, width=largura, label='3ª Maior Nota', align='edge')

plt.xlabel('Alunos')
plt.title('Maiores Notas por aluno')
plt.xticks(x, dados.keys())
plt.legend()

def legenda_automatica(grafico):
    for i in grafico:
        altura = i.get_height()
        plt.annotate(f'{altura}', xy=(i.get_x() + i.get_width()/2, altura),
                     xytext=(0, 2), textcoords='offset points', ha='center')


legenda_automatica(grafico1)
legenda_automatica(grafico2)
legenda_automatica(grafico3)
plt.show()

# Histograma com as médias finais.

plt.hist(medias_alunos.values(), bins=25, align='mid',
         histtype='barstacked', color='cyan', label='Médias Finais')
plt.legend()
plt.xlabel("Médias")
plt.ylabel("Número de Alunos")
plt.title("Médias Finais")
plt.show()

media0 = 0
media1 = 0
media2 = 0
media3 = 0
media4 = 0
media5 = 0
media6 = 0
media7 = 0
media8 = 0
media9 = 0
media10 = 10

for i in medias_alunos:
    valor = medias_alunos.get(i)
    if 0 <= valor < 1:
        media0 += 1
    if 1 <= valor < 2:
        media1 += 1
    if 2 <= valor < 3:
        media2 += 1
    if 3 <= valor < 4:
        media3 += 1
    if 4 <= valor < 5:
        media4 += 1
    if 5 <= valor < 6:
        media5 +=1
    if 6 <= valor < 7:
        media6 += 1
    if 7 <= valor < 8:
        media7 += 1
    if 8 <= valor < 9:
        media8 += 1
    if 9 <= valor < 10:
        media9 += 1
    if valor == 10:
        media10 += 1

reprovados = media0 + media1 + media2 + media3 + media4
aprovados = media5 + media6 + media7 + media8 + media9 + media10

# Gráfico de pizza (Aprovados/Reprovados)

plt.pie((aprovados, reprovados), explode=(0, 0.1), autopct='%1.2f%%',
        shadow=True, startangle=135)
plt.axis('equal')
plt.legend(("Aprovados", "Reprovados"), loc="right")
plt.title("Porcentagem Aprovados/Reprovados")
plt.show()



