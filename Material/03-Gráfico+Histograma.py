"""
# Exemplo 1:

import matplotlib.pyplot as plt
from numpy import*

N = 10000000  # Número de dados gerados
n_colunas = 50  # Numero de colunas do histograma

x = random.randn(N)

plt.hist(x, bins=n_colunas, density=True, histtype='bar', color='purple', label='Histograma X')
plt.legend()
plt.ylabel("Número de Ocorrencias")
plt.title("Histograma")
plt.show()



# Exemplo 2: Mais de um histograma na mesma figura


import matplotlib.pyplot as plt
from numpy import*

N = 10000000  # Número de dados gerados
n_colunas = 50  # Numero de colunas do histograma

x = random.randn(N)

plt.hist(x, bins=n_colunas, density=False, histtype='bar', color='purple', label='Histograma X')

N2 = 5000000
y = 10 + random.randn(N2)
plt.hist(y, bins=n_colunas, density=False, histtype='bar', color='orange', label='Histograma Y')


plt.legend()
plt.ylabel("Número de Ocorrencias")
plt.title("Histograma")
plt.show()



# Exemplo 3: Histogramas Aninhados


import matplotlib.pyplot as plt
from numpy import*

N = 10000000  # Número de dados gerados
n_colunas = 25  # Numero de colunas do histograma

x = random.randn(N, 4)

cores = ['orange', 'blue', 'green', 'yellow']

plt.hist(x, bins=n_colunas, density=True, histtype='bar', color=cores, label=cores)
plt.legend()
plt.ylabel("Número de Ocorrencias")
plt.title("Histograma")
plt.show()
"""



