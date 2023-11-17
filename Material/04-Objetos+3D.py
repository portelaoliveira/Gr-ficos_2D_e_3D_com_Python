"""
from vpython import*

seta = arrow(pos=vector(0, 0, 0), axis=vector(10, 4, 6), color=color.orange,
             opacity=0.1)

caixa = box(pos=vector(-3,0,0), color=color.magenta, emissive=True)

cone = cone(pos=vector(0,-10,0), axis=vector(10,4,6), radius=3, texture=textures.granite)

piramide = pyramid(pos=vector(2, 7, -1), axis=vector(0, -2, 1), shiness=1, texture=textures.rock)

cilindro = cylinder(pos=vector(0, 3, -2), axis=vector(7, 7, 0), radius=2.5,
                    color=vector(0.733, 0.169, 0.542), opacity=0.05)

from vpython import*

elipsoide = ellipsoid(pos=vector(0,0,0), size=vector(10,1,5), color=vector(0.875, 0.730, 0.980), shiness=0.5)

anel = ring(pos=vector(-2,-2,0), radius=3, thickness=0.5, texture=textures.earth)

helice = helix(pos=vector(0,0,0), axis=vector(-2,-2,0), radius=1, coils=10, color=color.white)

"""

