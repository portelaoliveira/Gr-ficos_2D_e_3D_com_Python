#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:21:38 2021

@author: portela

Objetos 3D

É possíve a gente criar os seguintes objetos
    - Seta (arrow) # arrow()
    - Cubo (box) # box()
    - Esfera (sphere) # sphere
    - Cone (cone) # cone
    - Cilindro (cylinder) # cylinder
    - elipsoíde (ellipsoid) # ellipsoid
    - Hélice (helix) # helix
    - Piramede (pyramid) # pyramid
    - Anel (ring) # ring()

from vpython import *
box(texture=textures.earth)
sphere(texture="https://i.imgur.com/IkGT0xU.jpeg")

"""

from vpython import *

seta = arrow(pos=vector(0, 0, 0), axis=vector(10, 4, 6), color=color.orange, opacity=0.2)
caixa = box(pos=vector(-3, 0, 0), color=color.magenta, emissive=True)
cone = cone(pos=vector(0, -10, 0), axis=vector(10, 4, 6), radius=3, texture=textures.granite)
piramide = pyramid(pos=vector(2, 7, -1), axis=vector(0, -2, 1), shiness=1, texture=textures.rock)