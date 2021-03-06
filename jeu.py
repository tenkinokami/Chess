# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:05:10 2018

@author: AMEILAC
"""
import piece as pc
import plateau as pt
import copy

class Jeu:

    def __init__(self):
        self.plateau = pt.Plateau()
    
    def at(self, i, j):
        return self.plateau.at(i, j)
    
    def __str__(self):
        return str(self.plateau)
    
    def actionPion(self, i, j):
        L = []
        if self.at(i, j).getCouleur() == pc.blanc:
            direction = -1
        else:
            direction = 1
        if pt.estDansDamier(i + direction, j) and self.at(i + direction,j).estVide():
            L.append((i + direction, j, pt.action_deplacer))
        for (y, x) in [(i + direction, j + 1), (i + direction, j - 1)]:
            if pt.estDansDamier(y, x) and pc.sontEnnemis(self.at(i, j), self.at(y, x)):
                L.append((y, x, pt.action_manger))
        return L
    
    def actionCavalier(self, i, j):
        L = []
        case = self.at(i,j)
        for signe_mov_y in [-1, 1]:
            for signe_mov_x in [-1, 1]:
                for mov_x in [1, 2]:
                    mov_y = 3 - mov_x
                    (y, x) = (i + signe_mov_y * mov_y, j + signe_mov_x * mov_x)
                    if pt.estDansDamier(y, x):
                        other = self.at(y, x)
                        if other.estVide():
                            L.append((y, x, pt.action_deplacer))
                        elif pc.sontEnnemis(case, other):
                            L.append((y, x, pt.action_manger))
        return L
    
    def casesAccessiblesLigne_Haut(self, i, j):
        L = []
        case = self.at(i, j)
        for y in range(i + 1, 8):
            other = self.at(y, j)
            if other.estVide():
                L.append((y, j, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((y, j, pt.action_manger))
                break
            else:
                break
        return L
          
    def casesAccessiblesLigne_Bas(self, i, j):
        L = []
        case = self.at(i, j)
        for y in reversed(range(i)):
            other = self.at(y, j)
            if other.estVide():
                L.append((y, j, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((y, j, pt.action_manger))
                break
            else:
                break
        return L
    
    def casesAccessiblesLigne_Droite(self, i, j):
        L = []
        case = self.at(i, j)
        for x in range(j + 1, 8):
            other = self.at(i, x)
            if other.estVide():
                L.append((i, x, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((i, x, pt.action_manger))
                break
            else:
                break
        return L        
        
    def casesAccessiblesLigne_Gauche(self, i, j):
        L = []
        case = self.at(i, j)
        for x in reversed(range(i)):
            other = self.at(i, x)
            if other.estVide():
                L.append((i, x, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((i, x, pt.action_manger))
                break
            else:
                break
        return L
    
    def casesAccessiblesDiagonale_BasDroite(self, i, j):
        L = []
        case = self.at(i, j)
        for dr in range(1, min(8 - i, 8 - j)):
            (y, x) = (i + dr, j + dr)
            other = self.at(y, x)
            if other.estVide():
                L.append((y, x, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((y, x, pt.action_manger))
                break
            else:
                break
        return L

    def casesAccessiblesDiagonale_HautDroite(self, i, j):
        L = []
        case = self.at(i, j)
        for ur in range(1, min(i, 8 - j)):
            (y, x) = (i - ur, j + ur)
            other = self.at(y, x)
            if other.estVide():
                L.append((y, x, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((y, x, pt.action_manger))
                break
            else:
                break
        return L
    
    def casesAccessiblesDiagonale_BasGauche(self, i, j):
        L = []
        case = self.at(i, j)
        for dl in range(1, min(8 - i, j)):
            (y, x) = (i + dl, j - dl)
            other = self.at(y, x)
            if other.estVide():
                L.append((y, x, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((y, x, pt.action_manger))
                break
            else:
                break
        return L
    
    def casesAccessiblesDiagonale_HautGauche(self, i, j):
        L = []
        case = self.at(i, j)
        for ul in range(1, min(i, j)):
            (y, x) = (i - ul, j - ul)
            other = self.at(y, x)
            if other.estVide():
                L.append((y, x, pt.action_deplacer))
            elif pc.sontEnnemis(case, other): # Ennemi 
                L.append((y, x, pt.action_manger))
                break
            else:
                break
        return L

    def actionTour(self, i, j):
        L = self.casesAccessiblesLigne_Gauche(i, j)
        L.extend(self.casesAccessiblesLigne_Bas(i, j))
        L.extend(self.casesAccessiblesLigne_Haut(i, j))
        L.extend(self.casesAccessiblesLigne_Droite(i, j))
        return L
    
    def actionFou(self, i, j):
        L = self.casesAccessiblesDiagonale_BasDroite(i, j)
        L.extend(self.casesAccessiblesDiagonale_BasGauche(i, j))
        L.extend(self.casesAccessiblesDiagonale_HautDroite(i, j))
        L.extend(self.casesAccessiblesDiagonale_HautGauche(i, j))
        return L   
    
    def actionReine(self, i, j):
        L = self.casesAccessiblesDiagonale_BasDroite(i, j)
        L.extend(self.casesAccessiblesDiagonale_BasGauche(i, j))
        L.extend(self.casesAccessiblesDiagonale_HautDroite(i, j))
        L.extend(self.casesAccessiblesDiagonale_HautGauche(i, j))
        L.extend(self.casesAccessiblesLigne_Gauche(i, j))
        L.extend(self.casesAccessiblesLigne_Bas(i, j))
        L.extend(self.casesAccessiblesLigne_Haut(i, j))
        L.extend(self.casesAccessiblesLigne_Droite(i, j))
        return L  
    
    def listePieceEnnemi(self, couleur):
        L = self.plateau.listePieceEnnemi(couleur)
        return L 
    
    def listePieceAllie(self, couleur):
        L = self.plateau.listePieceAllie(couleur)
        return L
    
    def actionRoi(self, i, j):
        M = []
        case_couleur = self.at(i, j).getCouleur()
        for (pos_i, pos_j, piece) in self.listePieceEnnemi(case_couleur):
            case_type = piece.getType()
            if case_type == pc.pion:
                M.extend(self.actionPion(pos_i, pos_j))
            elif case_type == pc.cavalier:
                M.extend(self.actionCavalier(pos_i, pos_j))
            elif case_type == pc.fou:
                M.extend(self.actionFou(pos_i, pos_j))
            elif case_type == pc.reine:
                M.extend(self.actionReine(pos_i, pos_j))
            elif case_type == pc.tour:
                M.extend(self.actionTour(pos_i, pos_j))
            elif case_type == pc.noir:
                for y in range(pos_i - 1, pos_i + 2):
                    for x in range(pos_j - 1, pos_j + 2):
                        if (y, x) != (pos_i, pos_j):
                            M.append((pos_i, pos_j, action_deplacer)) ## action fausse
        M = [(el[0], el[1]) for el in M] ## On se fiche des actions
        L = []
        for y in range(i - 1, i + 2):
            for x in range(j - 1, j + 2):
                if (y, x) != (i, j):
                    if pt.estDansDamier(y, x) and (i, j) not in M: ## Dans le damier et case qui ne met pas le roi en echec
                        other = self.at(i, j)
                        if other.estVide():
                            L.append((y, x, pt.action_deplacer))
                        elif pc.sontEnnemis(self.at(i, j), other): # Ennemi 
                            L.append((y, x, pt.action_manger))
        return L
            
    def actionPiece(self, i, j):
        case_type = self.at(i, j).getType()
        if case_type == pc.pion:
            return self.actionPion(i, j)
        elif case_type == pc.cavalier:
            return self.actionCavalier(i, j)
        elif case_type == pc.fou:
            return self.actionFou(i, j)
        elif case_type == pc.reine:
            return self.actionReine(i, j)
        elif case_type == pc.tour:
            return self.actionTour(i, j) 
        elif case_type == pc.roi:
            return self.actionRoi(i, j)
        
    def actionsDisponibles(self, couleur):
        Actions = []
        for (i, j, piece) in self.plateau.listePieceAllie(couleur):
            L = self.actionPiece(i, j)
            for l in L:
                Actions.append(((i, j), l))
        return Actions
    
    def move(self, action):
        self.plateau.move(action)
        return 
     
def score1(plateau):
    score_blanc = len(plateau.listePieceAllie(pc.blanc))
    score_noir = len(plateau.listePieceAllie(pc.noir))
    return (score_blanc, score_noir)

def score2(plateau):
    score_blanc = 0
    score_noir = 0
    def f(case_type):
        if case_type == pc.pion:
            return 1
        elif case_type == pc.cavalier:
            return 2
        elif case_type == pc.fou:
            return 3
        elif case_type == pc.reine:
            return 5
        elif case_type == pc.tour:
            return 3
        elif case_type == pc.roi:
            return 0
        
    for (i, j, piece) in plateau.listePieceAllie(pc.blanc):
        score_blanc += f(piece.getType())

    for (i, j, piece) in plateau.listePieceAllie(pc.noir):
        score_noir += f(piece.getType())

    return (score_blanc, score_noir)
