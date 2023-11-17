"""
#Exemplo 1:

import matplotlib.pyplot as plt


def funcao_terc_grau(x, a=1, b=1, c=1, d=1):
     Uma função que recebe cinco parametros de entrada, sendo que os quatro ultimos são opcionais com
    default igual a 1.
    y = a*x**3 + b*x**2 + c*x + d
    return y


lista_x = range(-5, 5)
lista_y = []

for i in lista_x:
    lista_y.append(funcao_terc_grau(i))

plt.plot(lista_x, lista_y, label='3º Grau', color='green')
plt.scatter(lista_x, lista_y, color='green', marker='*')
plt.legend()
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.title("Gráfico de f(x)")
plt.show()


#Exemplo 2: Gráficos Sobrepostos

import matplotlib.pyplot as plt


def funcao_terc_grau(x, a=1, b=1, c=1, d=1):
     Uma função que recebe cinco parametros de entrada, sendo que os quatro ultimos são opcionais com
    default igual a 1.
    y = a*x**3 + b*x**2 + c*x + d
    return y


def funcao_sec_grau(x, a=1, b=1, c=1):
    y = a*x**2 + b*x + c
    return y


lista_x = range(-10, 10)
lista_y_3 = []
lista_y_2 = []

for i in lista_x:
    lista_y_3.append(funcao_terc_grau(i))
    lista_y_2.append(funcao_sec_grau(i, b=-3))


plt.plot(lista_x, lista_y_3, label='3º Grau', color='green')
plt.plot(lista_x, lista_y_2, label='2º Grau', color='yellow')
#plt.scatter(lista_x, lista_y, color='green', marker='*')
plt.legend()
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.title("Gráfico de f(x)")
plt.show()

#Exemplo 3: Utilizando função Map

import matplotlib.pyplot as plt


def funcao_terc_grau(x, a=1, b=1, c=1, d=1):
    Uma função que recebe cinco parametros de entrada, sendo que os quatro ultimos são opcionais com
    default igual a 1.
    y = a*x**3 + b*x**2 + c*x + d
    return y


def funcao_sec_grau(x, a=1, b=1, c=1):
    y = a*x**2 + b*x + c
    return y


lista_x = range(-10, 10)

lista_map = list(map(funcao_sec_grau, lista_x))  # Utilizando a função map e transformando o resultado em uma lista.

plt.plot(lista_x, lista_map, label='2º Grau', color='red')
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.title("Função Segundo Grau")
plt.legend()
plt.show()

"""
