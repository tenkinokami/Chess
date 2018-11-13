# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:10:32 2018

@author: AMEILAC
"""
import piece as pc
import jeu
import copy

a = jeu.Jeu()
print("a ..... :")
print(a)
L = a.actionsDisponibles(pc.blanc)
b = copy.deepcopy(a)
b.move(L[0])
print("a ..... :")
print(a)
print("b ..... :")
print(b)