"""
- Fazendo os imports:
import matplotlib.pyplot as plt
from numpy import*

- Crinado o gráfico:
plt.bar(vários parametros): 2 parametros obrigatórios e alguns necessários.
Como parametros obrigatórios:
    - O primeiro parametro obrigatório: um iterável com os valores no eixo x a partir de onde crescerão as colunas.
    - O segundo parametro obrigatório: com os tamanhos (as alturas) das colunas.
Paraâmetros adicionais: Necessários
    - width (largura): paraêmtro que altera a largura das nossas colunas. (recebe um valor numérico)
    - align (alinhamento): determina o alinhamento das colunas sobre o eixo x (recebe ums str: 'center', 'edge')
    - label: escreve uma legenda no gráfico (recebe uma string)

plt.ylabel(str): altera a legenda do eixo y


plt.xticks(varios parametros):  # Função Nova!
    - o primeiro parametro obrigatório: x (iterável) que determina onde os ticks aparecerão
    - o segundo parametro obrigatório: legenda (iterável) coloca as legendas (nomes) de cada ponto x.


plt.title(str): adiciona um título ao gráfico
plt.legends(parametros): coloca a legenda no gráfico
plt.show()





"""