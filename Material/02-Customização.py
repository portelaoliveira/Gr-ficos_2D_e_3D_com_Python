"""
import matplotlib.pyplot as plt

Adicionaremos a linha:
plt.twinx() Esse comando já diz ao gráfico que usaremos o eixo x duas vezes para o plot de 2 gráficos diferentes.


# Exemplo 1:

import matplotlib.pyplot as plt
from numpy import*

# Criar nossos dados:

t = arange(0.01, 10, 0.01)
dados1 = exp(t)
dados2 = sin(2*pi*t)

# Como já feito anteriormente:

plt.plot(t, dados1, color='red', label='exp(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('exp(t)', color='red')
plt.tick_params(axis='y', labelcolor='red')  # Escrever os dados do eixo y em vermelho.
plt.legend()

plt.twinx()  # Linha essencial para esse tipo de modificação. Comoando que duplica o eixo x.

plt.plot(t, dados2, color='blue', label='sen(2$\pi$t)')
plt.ylabel('sen(2$\pi$t)', color='blue')
plt.tick_params(axis='y', labelcolor='blue')  # Escrever os dados do eixo y em azul.
plt.legend()

plt.title('Gráficos em função do tempo.')
plt.show()


# Exemplo 2: Alterando a escala do eixo y

import matplotlib.pyplot as plt
from numpy import*

# Criar nossos dados:

t = arange(0.01, 10, 0.01)
dados1 = exp(t)
dados2 = sin(2*pi*t)

# Como já feito anteriormente:

plt.plot(t, dados1, color='red', label='exp(t)')
plt.yscale('log')  # Altera a escala do eixo y (linear -> logaritmica)
plt.xlabel('Tempo (s)')
plt.ylabel('exp(t)', color='red')
plt.tick_params(axis='y', labelcolor='red')  # Escrever os dados do eixo y em vermelho. Função Nova!
plt.legend()

plt.twinx()  # Linha essencial para esse tipo de modificação. Comoando que duplica o eixo x.

plt.plot(t, dados2, color='blue', label='sen(2$\pi$t)')
plt.ylabel('sen(2$\pi$t)', color='blue')
plt.tick_params(axis='y', labelcolor='blue')  # Escrever os dados do eixo y em azul.
plt.legend()

plt.title('Gráficos em função do tempo.')
plt.show()
"""
