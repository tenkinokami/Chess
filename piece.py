# -*- coding: utf-8 -*-

pion = "pion"
tour = "tour"
fou = "fou"
cavalier = "cavalier"
roi = "roi"
reine = "reine"

noir = "noir"
blanc = "blanc"

vide = ""

class Piece:
    
    def __init__(self, typePiece, couleurPiece):
        """
        Initialisation d'une pièce :
            -> type : (pion, tour, fou, cavalier, roi, reine)
            -> couleur : (noir, blanc)
        """
        self.type = typePiece
        self.couleur = couleurPiece    
        
    def __str__(self):
        if self.type != vide:
            return "({}, {})".format(self.type, self.couleur)
        else:
            return "@"
        
    def getType(self):
        return self.type
    
    def getCouleur(self):
        return self.type
    
    def estMangee(self):
        self.type = vide
        self.couleur = vide
        
    def estCouleur(self, couleur):
        return couleur == couleur
    
    def estVide(self):
        return self.type == vide
    
    def nonVide(self):
        return not self.estVide()
    
    def estEnnemi(self, OtherPiece):
        return self.nonVide() and OtherPiece.nonVide() and self.getCouleur() != OtherPiece.getCouleur()


def sontEnnemis(Piece1, Piece2):
    return Piece1.estEnnemi(Piece2)