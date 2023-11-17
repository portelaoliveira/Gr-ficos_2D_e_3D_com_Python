"""
Para adicionar uma legenda, utilizamos a função label().

legenda = label(pos=vector(x,y,z)   # Posição a qual a legenda faz referencia
                                    # (importante para acompanhar o objeto 3D em movimento) pos=obj.pos
            text='seu text'         # Recebe uma str com o texto da legenda
            xoffset=float           # deslocamento no eixo x que a legenda sofrerá
            yoffset=float           # deslocamento no eixo y que a legenda sofrerá
            height=float            # determina a altura do texto
        Podemos ainda desenhar uma caixa em volta da legenda:
            box=True                # desenha a caixa em volta do texto
            border=float            # determina a distancia entre o texto e a borda da caixa
            color=color.(nome da cor)  # altera a cor do texto
            background=color.(nome da cor) # altera a de fundo da caixa

        Podemos ainda colocar uma linha ligando o objeto e a legenda
            line=True               # Desenhar uma linha ligando o objeto e a caixinha
            linecolor=color.(nome da cor)  # Muda a cor da linha
            linewidth=float         # Muda a espessura da linha
            )

from vpython import*

terra = sphere(texture=textures.earth, radius=10)
legenda = label(pos=terra.pos, text='Terra', xoffset=12, yoffset=12, height=50,
                box=True, border=1, color=color.blue, background=color.white,
                line=True, linecolor=color.cyan, linewidht=0.5)
"""


