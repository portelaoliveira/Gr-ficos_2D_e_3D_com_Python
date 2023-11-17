#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:59:09 2021

@author: portela

objeto_composto = compoud([lista de objetos])

cabo = cylinder(pos=vector(0, 0, 0), size=vector(1.3, 0.2, 0.2), color=color.orange)
cabeca = box(pos=vector(1.2, 0, 0), size=vector(0.2, 0.6, 0.2), color=color.blue)

martelo = compound([cabo, cabeca])
martelo.axis = vector(-3, 2, 4)

"""

from vpython import *

fio = cylinder(pos=vector(2, 2, 2), size=vector(1, 0.05, 0.05), color=color.white)
peso = sphere(pos=vector(3.25, 2, 2), radius=0.25, color=color.yellow)

pendolo = compound([fio, peso])