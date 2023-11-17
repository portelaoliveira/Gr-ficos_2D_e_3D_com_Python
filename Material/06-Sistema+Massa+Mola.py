
from vpython import*
import numpy as np

# Função com a Equação da Força Elástica:
def f(r):
    global k, m
    x = r[0]
    Vx = r[1]

    dx = Vx
    dVx = -k.value * x/m.value

    return np.array([dx, dVx], float)
#----------------------------------------------------------------------------------------------------------------------#
# Função com o cálculo numérico através do método de Runge-Kutta de 4ªOrdem:
def passo_rk4(r, h): # Calcula um passo no método de RK4
    k1 = h * f(r)
    k2 = h * f(r + 0.5 * k1)
    k3 = h * f(r + 0.5 * k2)
    k4 = h * f(r + k3)

    return (k1 + 2 * (k2 + k3) + k4)/6
#----------------------------------------------------------------------------------------------------------------------#

def Rodar():   # Função do botão Rodar/Pausar/Continuar
    global running
    running = not running
    if running:
        pausar.text = 'Pausar'
    else:
        pausar.text = 'Continuar'
#----------------------------------------------------------------------------------------------------------------------#
def Massa(c):  # Função que coloca legenda na caixa
    if c.checked:
        leg_caixa.visible = True
    else:
        leg_caixa.visible = False
#----------------------------------------------------------------------------------------------------------------------#
def Mola(c):  # Função que coloca legenda na mola
    if c.checked:
        leg_mola.visible = True
    else:
        leg_mola.visible = False
#----------------------------------------------------------------------------------------------------------------------#
def muda_original():  # Fução que altera a cor da caixa para a original
    global original, azul, vermelho, amarelo
    azul.checked = False
    vermelho.checked = False
    amarelo.checked = False
    caixa.color = vector(0.542, 0.949, 0.876)
#----------------------------------------------------------------------------------------------------------------------#
def muda_azul():  # Função que altera a cor da caixa para azul
    global original, azul, vermelho, amarelo
    vermelho.checked = False
    amarelo.checked = False
    original.checked = False
    caixa.color = color.blue
#----------------------------------------------------------------------------------------------------------------------#
def muda_vermelho():  # Função que altera a cor da caixa para vermelho
    global original, azul, vermelho, amarelo
    amarelo.checked = False
    original.checked = False
    azul.checked = False
    caixa.color = color.red
#----------------------------------------------------------------------------------------------------------------------#
def muda_amarelo():  # Função que altera a cor da caixa para amarelo
    global original, azul, vermelho, amarelo
    original.checked = False
    azul.checked = False
    vermelho.checked = False
    caixa.color = color.yellow
#----------------------------------------------------------------------------------------------------------------------#

# Customizar a Cena:
scene.background = vector(0.955, 0.949, 0.767)  # Cor de fundo da cena
scene.width = 1400  # Largura da Tela
running = False  # Variável para dizer se o programa está rodando ou parado.
scene.bind('click', Rodar)  # Comando para esperar o clique para iniciar o programa

# Criação dos Widgets:

pausar = button(text='Rodar', bind=Rodar)
scene.append_to_caption("\n Legendas:\n")  # Comando para colocar espaços na tela entre os widgets
check1 = checkbox(bind=Massa, text='Massa', checked=True)  # Checkbox 1: Para adicionar a legenda na caixa
check2 = checkbox(bind=Mola, text="Mola", checked=True)    # Checkbox 2: Para adicionar a legenda na mola

scene.append_to_caption("\n\n")
scene.append_to_caption("Mudança de Cores:\n")
original = radio(bind=muda_original, text="Original", checked=True)   # Checkbox redondo 1: muda a cor para a original
azul = radio(bind=muda_azul, text="Azul", checked=False)              # Checkbox redondo 2: muda a cor para azul
vermelho = radio(bind=muda_vermelho, text='Vermelho', checked=False)  # Checkbox redondo 3: muda a cor para vermelho
amarelo = radio(bind=muda_amarelo, text="Amarelo", checked=False)     # Checkbox redondo 4: muda a cor para amarelo

scene.append_to_caption("\n\n Opções:\n")

    # Slider 1: Alteração da constante elástica da mola (k)
scene.append_to_caption("  Constante Elástica:")
def const_elast(k):
    wts.text = f'{k.value}'
k = slider(min=1, max=100, value=10, bind=const_elast, step=1, lenght=100, width=10)
wts = wtext(text=f'{k.value}')

    # Slider 2: Alteração do numero de voltas da mola
scene.append_to_caption("\n  Número de voltas da mola:")
def num_voltas(voltas):
    wtm1.text = f'{voltas.value}'
n_voltas = slider(min=5, max=20, value=8, bind=num_voltas, step=1, lenght=100, width=10)
wtm1 = wtext(text=f'{n_voltas.value}')

    # Slider 3: Alteração da massa do bloco
scene.append_to_caption("\n  Massa do Bloco:")
def massa_bloco(massa):
    wtm2.text= f'{massa.value}'
m = slider(min=0.1, max=10, value=1, bind=massa_bloco, step=1, lenght=100, width=10)
wtm2 = wtext(text=f'{m.value}')
scene.append_to_caption("\n\n\n")



# Criando o Suporte:
parede = box(pos=vector(-4.8, 0, 0), size=vector(0.4, 4, 2.5), texture=textures.wood)  # Comando para criar a parede
mesa = box(pos=vector(0, -2, 0), size=vector(10, 0.4, 2.5), texture=textures.wood)  # Comando para criar a mesa





def main():
    global mola, caixa, leg_mola, leg_caixa

    mola = helix(pos=vector(-4.8, -1.3, 0), axis=vector(3.5, 0, 0), radius=0.4,
                 coils=8, color=color.orange)
    leg_mola = label(pos=vector(-2.5, -0.5, 0), text='Mola', color=color.black )
    liga = cylinder(pos=vector(-1.3, -1.3, 0), axis=vector(0, 0, 0.4), radius=0.02, color=color.orange)
    fio = cylinder(pos=vector(-1.3, -1.3, 0), axis=vector(0.2, 0, 0), radius=0.02, color=color.orange)

    caixa = box(pos=vector(-0.7, -1.3, 0), size=vector(1, 1, 1), color=vector(0.542, 0.949, 0.876))
    leg_caixa = label(pos=caixa.pos + vector(0, 1, 0), text='Massa', color=color.black )

    v0 = float(input("Digite o valor da velocidade inicial: "))
    ra = np.array([0, v0])
    r = ra

    h = 0.05  # Taxa de atualização

    while True:
        if running:
            rate(25)  # função que modifica a frequencia de atualização da animação
            dr = passo_rk4(r, h)
            r = r + dr

            mola.axis = vector(3.5 + dr[0], 0, 0)
            leg_mola.pos = vector(-2.5 + dr[0], -0.5, 0)
            liga.pos = vector(-1.3 + dr[0], -1.3, 0)
            fio.pos = vector(-1.3 + dr[0], -1.3, 0)
            caixa.pos = vector(-0.7 + dr[0], -1.3, 0)
            leg_caixa.pos = caixa.pos + vector(0, 1, 0)

            # Atualização dos atributos:
            mola.coils = n_voltas.value
            mola.thickness = k.value/500
            liga.radius = k.value/1000
            fio.radius = k.value/1000

main()
