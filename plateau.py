# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:10:14 2018

@author: AMEILAC
"""

import piece as pc

limite_plateau_gauche = 0
limite_plateau_droite = 7
limite_plateau_haut = 0
limite_plateau_bas = 7

mouvement = "MVT"
manger = "ATT"

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
    
    def actionPiece(self, i, j):
        listeMouvements = []
        typePiece = self.cases[i][j].getType()
        couleurPiece = self.cases[i][j].getCouleur()
        if typePiece == pion:
            if positionDansDamier(i, j) and self.cases[i + 1][j].estVide():
                listeMouvements((i + 1, j))
            for x in [-1, 1]:
                if positionDansDamier(i, j + x):
                    if self.cases[i][j + x].estVide():
                        listeMouvements((i, j + x, mouvement))
                    elif not self.cases[i][j + x].estCouleur(couleurPiece):
                        listeMouvements((i, j + x, manger))
        elif typePiece == cavalier:
            for (x, y) in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1),(-1, -2), (-2, -1)]:
                if positionDansDamier(i + y, j + x):
                    if self.cases[i + y][j + x].estVide():
                        listeMouvements((i + y, j + x, mouvement))
                    elif not self.cases[i + y][j + x].estCouleur(couleurPiece):
                        listeMouvements((i + y, j + x, manger))
        elif typePiece == cavalier:
            for (x, y) in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1),(-1, -2), (-2, -1)]:
                if positionDansDamier(i + y, j + x):
                    if self.cases[i + y][j + x].estVide():
                        listeMouvements((i + y, j + x, mouvement))
                    elif not self.cases[i + y][j + x].estCouleur(couleurPiece):
                        listeMouvements((i + y, j + x, manger))
            
        elif typePiece == tour:
            # Axe descendant
            for y in range(i + 1, 8):
                if self.cases[y][j].estVide():
                    listeMouvements((y, j))
                elif self.cases[y][j].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, j))
                    break
            #Axe Montant
            for y in range(i - 1, 0, -1):
                if self.cases[y][j].estVide():
                    listeMouvements((y, j))
                elif self.cases[y][j].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, j))
                    break
            #Axe droite
            for x in range(j + 1, 8):
                if self.cases[i][x].estVide():
                    listeMouvements((i, x))
                elif self.cases[i][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((i, x))
                    break
            # Axe gauche
            for x in range(j - 1, 0, -1):
                if self.cases[i][x].estVide():
                    listeMouvements((i, x))
                elif self.cases[i][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((i, x))
                    break    
        elif typePiece == fou:
            #Axe Droite Descendant
            for dr in range(1, min(8 - x, 8 - y)):
                (x, y) = (x + dr, y + dr)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
            #Axe Gauche Montant
            for ul in range(1, min(x, y)):
                (x, y) = (x - ul, y - ul)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
            #Axe droite Montant
            for ur in range(1, min(8 - x, y)):
                (x, y) = (x + ur, y - ur)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
            # Axe gauche descendant
            for dl in range(1, min(x, 8 - y)):
                (x, y) = (x - dl, y + dl)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
        elif typePiece == reine:
            for y in range(i + 1, 8):
                if self.cases[y][j].estVide():
                    listeMouvements((y, j))
                elif self.cases[y][j].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, j))
                    break
            #Axe Montant
            for y in range(i - 1, 0, -1):
                if self.cases[y][j].estVide():
                    listeMouvements((y, j))
                elif self.cases[y][j].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, j))
                    break
            #Axe droite
            for x in range(j + 1, 8):
                if self.cases[i][x].estVide():
                    listeMouvements((i, x))
                elif self.cases[i][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((i, x))
                    break
            # Axe gauche
            for x in range(j - 1, 0, -1):
                if self.cases[i][x].estVide():
                    listeMouvements((i, x))
                elif self.cases[i][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((i, x))
                    break    
            #Axe Droite Descendant
            for dr in range(1, min(8 - x, 8 - y)):
                (x, y) = (x + dr, y + dr)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
            #Axe Gauche Montant
            for ul in range(1, min(x, y)):
                (x, y) = (x - ul, y - ul)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
            #Axe droite Montant
            for ur in range(1, min(8 - x, y)):
                (x, y) = (x + ur, y - ur)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break
            # Axe gauche descendant
            for dl in range(1, min(x, 8 - y)):
                (x, y) = (x - dl, y + dl)
                if self.cases[y][x].estVide():
                    listeMouvements((y, x))
                elif self.cases[y][x].getCouleur() != couleurPiece: # Ennemi 
                    listeMouvements((y, x))
                    break