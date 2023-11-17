"""
No Vpython, existem alguns tipos de widgets, sendo eles: button, radio, checkbox , slider, menu, winput.

    - button (botão 'simples'):
        button(bind='nome da função'   # Nesse parametro passamos o nome da função a ser chamada ao clicarmos
            text=str   # coloca um texto no botão
            color=color.(nome da função)  # Alteramos a cor do texto
            background=color.(nome da cor)  # altera a cor de fundo do botão
            disabled=True/False  # se True, o botão fica desativado
            delete()  # com essa função, deletamos o botão
            )

    - radio (botão redondo):
        radio(bind='nome da função'
            text=str             # Texto ao lado do botão
            disabled=True/False
            checked=True/False   # se True, o botão é selecionado. False é default.
            delete()
            )

    - checkbox (botão quadrado):
        checkbox(bind='nome da função'
            text=str             # Texto ao lado do botão
            disabled=True/False
            checked=True/False   # se True, o botão é selecionado. False é default.
            delete()
            )

    - slider (barra deslizante):
        slider(bind='nome da função',
            min=float   # Valor mínimo da barra
            max=float   # Valor máximo da barra
            step=float  # determina qual a variação minima de valor do slider. Possui como default 0.001*(max-min)
            vertical=True/False  # se True, o slider fica na vertical.
            lenght=float  # 'altura' do slider
            width=float   # 'largura do slider
            disabled=True/False
            delete()
            )

    - menu (menu com opções):
        menu(bind='nome da função'
            choices=lista  # Lista de strings que aparecem no menu
            selected() : lê a opção selecionada
            index() : lê o indice da opção selecionada
            disabled=True/False
            delete()
            )

    - winput (caixa em branco onde o usuário pode entrar com dados do teclado):
        winput(bind='nome da função'
            height=float  # determina a altura da caixa,
            width=float  # determina a largura da caixa
            text=str    # aparece um texto dentro da caixa.
            disabled=True/False
            delete()
            )

"""

