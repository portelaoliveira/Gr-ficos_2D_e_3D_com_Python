"""
- Mudança no nosso código:
plt.annotate(varios parametros)
    - uma str com o texto que deseja anotar no gráfico;
    - xy = (pos_x, pos_y): com esse comando, é possivel posicionar o local em que a str faz referencia.
    - xytext = (pos_x, pos_y): posição no gráfico onde a str é escrita.
    - arrowprops: recebe um dicionário tal que a chave desse dicionário é a cor da seta, e o valor é um valor numérico
q diz o quanto a seta será encurtada.

# plt.annotate('Valor Máximo', xy=(2, 1), xytext=(3, 1.5), arraowprops=dict(facecolor='black', shrink=0.05))


# Exemplo 1:
import matplotlib.pyplot as plt
from numpy import*

t = arange(0, 5.0, 0.01)
s = cos(2*pi*t)

plt.plot(t, s, label='cos(2$\pi$t)', color='orange')
plt.annotate('Valor Máximo', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1))
plt.legend()
plt.title('Função Cosseno')
plt.ylim(-2, 2)
plt.show()


# Exemplo 2:
import matplotlib.pyplot as plt
from numpy import*

t = arange(-5.0, 5.0, 0.01)
y = 2*t**2 + t*cos(t) + t  # Podemos colocar qualquer função para que seja calculado o ponto mínimo em um determinado intervalo.

y_minimo = min(y)
x_minimo = 0

# Laço para encontrar o valor de x_minimo.

for i in zip(t, y):  # list(zip object) -> [x, y]
    if i[1] == y_minimo:
        x_minimo = i[0]

plt.plot(t, y, label='2º Grau', color='orange')
plt.annotate('Ponto Mínimo',
             xy=(x_minimo, y_minimo), xytext=(x_minimo, y_minimo + 5),
             arrowprops=dict(facecolor='black', shrink=0.1))
plt.legend()
plt.title('Função 2º Grau')
plt.show()
"""

# Exemplo 2:
import matplotlib.pyplot as plt
from numpy import*

t = arange(-5.0, 5.0, 0.01)
y = 2*t**2 + t*cos(t) + t  # Podemos colocar qualquer função para que seja calculado o ponto mínimo em um determinado intervalo.

y_minimo = min(y)
x_minimo = 0

# Laço para encontrar o valor de x_minimo.

for i in zip(t, y):  # list(zip object) -> [x, y]
    if i[1] == y_minimo:
        x_minimo = i[0]

plt.plot(t, y, label='2º Grau', color='orange')
plt.annotate('Ponto Mínimo',
             xy=(x_minimo, y_minimo), xytext=(x_minimo, y_minimo + 5),
             arrowprops=dict(facecolor='black', shrink=0.1))
plt.legend()
plt.title('Função 2º Grau')
plt.show()


