# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:10:14 2018

@author: AMEILAC
"""

import piece as pc
import copy

limite_plateau_gauche = 0
limite_plateau_droite = 7
limite_plateau_haut = 0
limite_plateau_bas = 7

action_deplacer = "MVT"
action_manger = "ATT"

def estDansDamier(i, j):
    return not(i < limite_plateau_gauche 
               or i > limite_plateau_droite 
               or j < limite_plateau_haut 
               or j > limite_plateau_bas)
      
class Plateau:
    
    def __init__(self):
        self.cases = [[pc.Piece(pc.tour, pc.noir), pc.Piece(pc.cavalier, pc.noir), pc.Piece(pc.fou, pc.noir), pc.Piece(pc.roi, pc.noir), pc.Piece(pc.reine, pc.noir), pc.Piece(pc.fou, pc.noir), pc.Piece(pc.cavalier, pc.noir), pc.Piece(pc.tour, pc.noir)],
                      [pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir), pc.Piece(pc.pion, pc.noir)],
                      [pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide)],
                      [pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide)],
                      [pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide)],
                      [pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide), pc.Piece(pc.vide, pc.vide)],
                      [pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc), pc.Piece(pc.pion, pc.blanc)],
                      [pc.Piece(pc.tour, pc.blanc), pc.Piece(pc.cavalier, pc.blanc), pc.Piece(pc.fou, pc.blanc), pc.Piece(pc.roi, pc.blanc), pc.Piece(pc.reine, pc.blanc), pc.Piece(pc.fou, pc.blanc), pc.Piece(pc.cavalier, pc.blanc), pc.Piece(pc.tour, pc.blanc)]]

    def __str__(self):
        string = ""
        for i in range(8):
            for j in range(8):
                string += str(self.cases[i][j]) + "\t"
            string += "\n"
        return string
    
    def at(self, i, j):
        return self.cases[i][j] 
    
    def move(self, action):
        """
        Les actions sont au format (case de la piece, case ou la bouger, action a réaliser)
            par exemple : ((0, 1), (2, 0, 'MVT'))
        """
        (y_beg, x_beg) = action[0]
        (y_end, x_end, act) = action[1]
        self.cases[y_end][x_end] = self.cases[y_beg][x_beg]
        self.cases[y_beg][x_beg] = pc.Piece(pc.vide, pc.vide)
    
    def listePieceAllie(self, couleur):
        L = []
        for i in range(8):
            for j in range(8):
                if self.cases[i][j].estCouleur(couleur):
                    L.append((i, j, self.cases[i][j]))
        return L
    
    def listePieceEnnemi(self, couleur):
        if couleur == pc.blanc:
            return self.listePieceAllie(pc.noir)
        elif couleur == pc.noir:
            return self.listePieceAllie(pc.blanc)
    
    
