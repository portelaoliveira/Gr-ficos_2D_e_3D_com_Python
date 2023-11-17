"""from vpython import*

terra = sphere(texture=textures.earth)

def Botao(b):
    print('Olá! Bem vindo ao Curso da Geek University.')

button(bind=Botao, text='Clique!',color=color.white, background=color.black)

def Radio(r):
    print(r.text)
radio(bind=Radio, text='Azul')
radio(bind=Radio, text='Amarelo')
radio(bind=Radio, text='Vermelho')

def Check(c):
    if c.checked == True:
        terra.texture=textures.granite
    else:
        terra.texture=textures.earth

checkbox(bind=Check, text="Granito")

def Sld(s):
    print(s.value)

slider(bind=Sld, min=0, max=100, step=1, vertical=True, value=50)

def Menu(m):
    print(m.selected, m.index)

menu(bind=Menu, choices=["Macarrão", 'Pizza', 'Yakissoba', 'Sushi'])

def Texto(t):
    print(t.text, t.number)

winput(bind=Texto, text='Entre com um dado', width=130)


while True:
    a = scene.waitfor('mousedown')
    if a.event == 'mousedown':
        scene.delete()

"""
