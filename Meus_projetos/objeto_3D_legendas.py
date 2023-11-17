#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:58:02 2021

@author: portela

legenda = label(pos=vector(x, y, z), text="legenda")

"""

from vpython import *

terra = sphere(texture=textures.earth, radius=10)
legenda = label(pos=terra.pos, text="Terra", xoffset=12, yoffset=12, box=True, border=1, color=color.blue, background=color.white,
                line=True, linecolor=color.cyan, linewidth=0.5)
