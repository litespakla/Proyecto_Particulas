# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:00:07 2020

@author: Usuario

"""


energia = 10
#Esta función cambia el valor de los coeficientes a partir de la nueva energía
def changevalue(energia):
    absgrasa = 0
    abspiel = 0
    absgrasa = 0
    absmusculo = 0
    abshueso = 0
    
    totgrasa = 0
    totpiel = 0
    totmusculo = 0
    tothueso = 0

#El valor se consigue con una función exponencial, sacada de un ajuste para los diferentes medios
#Para el caso de estos coeficientes, el ajuste funciona bien para el rango de energía que se esta trabajando
    absgrasa = 2694.39091931*energia**(-2.7519139)
    absmusculo = 3773.19217*energia**(-2.69091704)
    totmusculo = 3774.03737*energia**(-2.68821618)
    abspiel = 3215.71787*energia**(-2.73458938)    
    totpiel = 3580.323*energia**(-2.73456854)
    totgrasa = 2695.2778397*energia**(-2.74969947)
        

        
     #Para el caso de estos otros el ajuste no funciona bien para cierto rango de energías por lo que hay que 
  #poner una condición para usar los ajustes en el rango correcto
    if energia <= 4:
        abshueso = 3460.14646*energia**(-2.64177814)
        
    else:
        abshueso = 10512.2889*energia**(-2.74523673)
        
    
    if energia <= 4:
        tothueso = 3460.85224*energia**(-2.63591768)
        
    else:
        tothueso = 12044.1895*energia**(-2.77809405)
        
          #Una vez sacado los coeficientes se devuelve un vector que contiene el de absorción y el de comptón
    coeficientes = [abspiel,absgrasa,absmusculo,abshueso,totpiel-abspiel,totgrasa-absgrasa,totmusculo-absmusculo,tothueso-abshueso]
    
    print(coeficientes)  
    print(abspiel)
        
        
valor = 10
changevalue(valor)
     
        
        
    
    
    
        
    
