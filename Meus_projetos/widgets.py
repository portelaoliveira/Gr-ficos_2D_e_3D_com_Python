#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 12:28:05 2021

@author: portela
"""

from vpython import *

terra = sphere(texture=textures.earth)

def Botao(b):
    print("Fala Broww")

button(bind=Botao, text="Clique", color=color.white, background=color.black)

def Radio(r):
    print(r.text)
    
radio(bind=Radio, text="Azul")
radio(bind=Radio, text="Verde")
radio(bind=Radio, text="Amarelo")

def Check(c):
    if c.checked == True:
        terra.texture = textures.rock
    else:
        terra.texture = textures.earth
        
checkbox(bind=Check, text="Pedra")

def Sld(s):
    print(s.value)
    
slider(bind=Sld, min=0, max=100, step=1, vertical=True, value=50)

def Menu(m):
    print(m.selected, m.index)
    
menu(bind=Menu, choices=["Pizza", "Macarrão", "Carne"])

def Texto(t):
    print(t.text, t.number)

winput(bind=Texto, text="Entre com um dado", width=130)

while True:
    a = scene.waitfor("mousedown")
    if a.event == "mousedown":
        scene.delete()

        