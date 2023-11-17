"""
# Exemplo 1: Pizzas

import matplotlib.pyplot as plt

# Gráfico de pizza. Cada fatia da pizza corresponde a um sabor diferente.
nomes = 'Calabresa', 'Marguerita', 'Caipira', 'Peruana'
valores = [2, 2, 2, 2]
destaque = (0, 0, 0, 0)

plt.pie(valores, explode=destaque, labels=nomes, autopct='%1.2f%%', shadow=True, startangle=90)
plt.legend(nomes, title='Sabores', loc='right')
plt.axis("equal")  # Permite que a caixinha com as legendas se movimente no gráfico conforme o tamnho da figura.
plt.title("Pizzas")
plt.show()



# Exemplo 2: Bolão Mega da Virada

import matplotlib.pyplot as plt

# Gráfico de pizza. Cada fatia da pizza corresponde a um valor de aposta na mega sena.
nomes = 'Eduardo', 'Ana', 'Giovanni', 'Julia', 'Daniel', 'Bruna', 'Lucca'
valores = [100, 120, 90, 95, 80, 80, 200]
destaque = (0, 0, 0, 0, 0.1, 0.1, 0)

plt.pie(valores, explode=destaque, labels=nomes, autopct='%1.2f%%', shadow=False, startangle=90)
plt.legend(nomes, title='Apostadores', loc='best')
plt.axis("equal")  # Permite que a caixinha com as legendas se movimente no gráfico conforme o tamnho da figura.
plt.title("Aposta Mega da Virada")
plt.show()


# Exemplo 3: Python Avançado. Utilizando um dicionário para a criação de um gráfico.


import matplotlib.pyplot as plt

# Gráfico de pizza. Cada fatia da pizza corresponde a um valor de aposta na mega sena.

grupo = {'Eduardo':100, 'Ana':120, 'Giovanni':90, 'Julia':95, 'Daniel':80, 'Bruna':80, 'Lucca':200}

nomes = tuple(grupo.keys())
valores = list(grupo.values())

destaque = (0, 0, 0, 0, 0.1, 0.1, 0)

plt.pie(valores, explode=destaque, labels=nomes, autopct='%1.2f%%', shadow=False, startangle=90)
plt.legend(nomes, title='Apostadores', loc='best')
plt.axis("equal")  # Permite que a caixinha com as legendas se movimente no gráfico conforme o tamnho da figura.
plt.title("Aposta Mega da Virada")
plt.show()

"""

