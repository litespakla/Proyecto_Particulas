# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:00:07 2020

@author: Usuario

"""

absorcion = [0.13,0.25,0.54]
energia = 120

def changevalue(energia):
    absgrasa = 0
    abspiel = 0
    absgrasa = 0
    absmusculo = 0
    abshueso = 0
    if energia <= 60:
        abspiel = 3215.71787*energia**-2.73458938
        
    else:
        abspiel = 0.01250664*energia**0.15783241
        
        
    if energia <= 50:
        absgrasa = 2694.39091931*energia**-2.7519139
        
    else:
        absgrasa = 0.01112367*energia**0.17925315
        
    if energia <=80:
        absmusculo = 3773.19217*energia**-2.69091704
        
    else:
        absmusculo = 0.01231854*energia**0.16106276
        
    if energia <= 4:
        abshueso = 3460.14646*energia**-2.64177814
        
    else:
        abshueso = 10512.2889*energia**-2.74523673
        
    coeficientes = [abspiel,absgrasa,absmusculo,abshueso,1-abspiel,1-absgrasa,1-absmusculo,1-abshueso]
    
    print(coeficientes)  
        
        
valor = 30
changevalue(valor)
     
        
        
    
    
    
        
    
