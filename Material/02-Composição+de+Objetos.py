"""
Para fazer a composição de objetos, fazemos o seguinte:

objeto_composto = compound([lista de objetos])  # Comando para fazer a composição.

Obs.:
    - Não é possivel colocar as texturas individualmente.
    - Objetos baseados em curvas (curve, helix) não podem ser compostos com outros objetos.

from vpython import*

cabo = cylinder(pos=vector(0, 0, 0), size=vector(1.4, 0.2, 0.2), color=color.orange)

cabeca = box(size=vector(0.2, 0.6, 0.2), pos=vector(1.5, 0, 0), color=color.blue)

martelo = compound([cabo, cabeca])
martelo.axis=vector(-3,-2,4)

fio = cylinder(pos=vector(2,2,2), size=vector(1, 0.05, 0.05), color=color.yellow)
peso = sphere(radius=0.25, color=color.yellow, pos=vector(3.25, 2, 2))

pendulo = compound([fio, peso])
"""
