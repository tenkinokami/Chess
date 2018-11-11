# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:14:04 2018

@author: AMEILAC
"""

import plateau as pl   
import copy

a = pl.Plateau()
b = copy.deepcopy(a)

b.move(((1, 3), (2, 3, "MVT")))
print("a :")
print(a)

print("b :")
print(b)