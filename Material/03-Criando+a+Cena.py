"""
- Criando nossa cena:

cena = canvas()  # Com esse comando, a cena é criada.
Algumas alterações nos parametros de entrada:
    - width (largura): Altera a largura da cena
    - height (altura): Altera a altura da cena
    - align (alinhamento): Altera o alinhamento da cena. Podemos colocar 'left', 'right', None (default)
    - background: Possui como default a cor preta, mas podemos alterar a cor de acordo com a necessidade.
    - delete: Apaga todos os elementos da cena.
    - capture(nome_do_arquivo): com este comando, será feito o download de um print da cena.
    - camera.follow(nome_do_objeto): com este comando, o centro da cena é automaticamente mudado para o objeto.
    - camera.pos(x, y, z): Altera o centro da camera para a posição desejada.

from vpython import*

cena = canvas(width=1000, height=1000, align='right', background=color.cyan)
box()

Vamos agora ver algumas interações que podemos fazer com o mouse e com o teclado:
    - scene.pause(): Aparece um ícone aguardando ser clicado para pausar a cena. Podemos inclusive escrever uma
mensagem neste ícone, basta adicionar uma str entre parenteses.
    - scene.waitfor(): utilizando essa função, a cena aguarda o comando de dentro dos parenteses.
        scene.waitfor('click')  # Aguarda o clique do mouse
        scene.waitfor('mousedown')
        scene.waitfor('mouseup')
        scene.waitfor('mousemove')
        scene.waitfor('keydown')  # aguarda ser pressionado o botão da seta para baixo do teclado
        scene.waitfor('keyup')
        scene.waitfor('click keydown') # Agurada ou um clique ou algum botão do teclado ser pressionado.

from vpython import*

box()
while True:
    a = scene.waitfor('keydown')
    if a.event == 'keydown':  # Para acessar o comando do waitfor, usamos a função .event.
        scene.delete()
        cena = canvas(width=1000, height=1000, align='right', background=color.cyan)
        sphere()
"""
