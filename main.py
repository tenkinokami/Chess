# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:10:32 2018

@author: AMEILAC
"""
import piece as pc
import plateau as pt
import jeu
import copy

a = jeu.Jeu()
#print("a ..... :")
#print(a)
L = a.actionsDisponibles(pc.blanc)
for action in L:
    b = copy.deepcopy(a)
    b.move(action)
    M = b.actionsDisponibles(pc.noir)
    for action2 in M:
        c = copy.deepcopy(b)
        c.move(action2)
        (score_blanc, score_noir) = jeu.score1(c)
        print(score_blanc, score_noir)