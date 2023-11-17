"""
- Importando o módulo:
import matplotlib.pyplot as plt

- Criando o gráfico: pie = torta
plt.pie( vários parâmetros. ALguns obrigatórios, outros são necessários)
O unico parametro obrigatorio é um iteravel contendo os valores de cada uma das partes da pizza.

Pametros necessários:
    - labels: função que coloca uma legenda em cada uma das partes da pizza. Função recebe uma tupla.
    - autopct: Ao inserirmos o código '%1.2f%%'. Com este código será iniserido no gráfico o valor percentual equivalente
de cada fatia.
    - explode: função que permite destacar uma ou mais fatias da pizza. Recebe uma tupla com os valores.
    - shadow: função que coloca uma sombra no gráfico.
    - startangle: Angulo inicial que deseja começar a criar o gráfico. Tem como padrão 0 graus.

plt.legend(parametros adicionais):
É possivel adicionar um título nessa caixinha de legendas usando o comando title="título;
Possível ajustar a localização da caixinha com o comando loc="posição".
    best
    upper right
    upper left
    lower right
    lower left
    right
    center right
    lower center
    upper center
    center

plt.title("Título do gráfico"): mesmo comando do gráfico de dispersão

plt.show()

"""


