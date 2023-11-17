"""
-Fazendo o import:
import matplotlib.pyplot as plt
from numpy import*

- Criando o Gráfico:
plt.hist(varios parametros). O unico parametro obrigatorio é um iteravel.
Alguns outros parametros qua são uteis para uma boa formatação, são:
    -bins: É um parametro que tem como objetivo determinar a quantidade de colunas do nosso histograma. Recebe um numero inteiro
    -density: parametro booleano (True ou False). Se True, ao inves de colocar o numero de ocorrencias do evento,
coloca a densidade que ocorre.
    -color: altera a cor do histograma
    -label: recebe uma string. Coloca legenda no histograma
    -histtype: tem como default 'bar', mas se alterado para 'barstacked' é desenhado apenas o contorno do histograma.

plt.legend() -> aparecer as legendas do histograma
plt.title("Título") -> Titulo do gráfico
plt.show()

"""