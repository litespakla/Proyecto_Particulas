# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:47:22 2020

@author: Sebastián Montero Alpízar
Proyecto Partículas
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import time 
from mpl_toolkits.mplot3d import Axes3D
start_time = time.time()

 


def rand_tau(n=1):
    r = [-np.log(1- random.uniform(0.0,1.0)) for i in range(n)]
    return r

def step(n,c):
    lista_step = []
    for i in rand_tau(n):
        lista_step.append(i*c)
    return lista_step


def rand_phi(n=1):
    r = [2 * np.pi *random.uniform(0.0,1.0) for i in range(n)]
    return  r

def rand_mu(n=1):
    r = [np.arccos(-1 + 2*random.uniform(0.0,1.0)) for i in range(n)]
    return r

"""
Aquí estoy poniendo una medida arbitraria del brazo


"""


class photon(object):
    def __init__(self, x=None, y=None, z=None, phi=None,mu = None):
        x = random.uniform(0.0,6) if x is None else x
        y = np.sqrt(1 - random.uniform(0.0,1.0)) if y is None else y
        z = random.uniform(0.0,10) if z is None else z
        n_x,n_y,n_z =0,0,0
        self.pos = [x, y, z]
        self.ang = [phi,mu]
        self.phi = phi
        self.mu = mu
        self.mov = [n_x,n_y,n_z]
        
    def scattering(self,s):
        phi = 2 * np.pi *random.uniform(0.0,1.0)
        mu = np.arccos(-1 + 2*random.uniform(0.0,1.0))
        n_x = s*np.cos(mu)*np.cos(phi)
        n_y = s*np.sin(phi)*np.cos(mu)
        n_z = s*np.sin(mu)
        movimiento =[n_x,n_y,n_z]
        
        nueva_posicion = []
        for i in range(len(movimiento)):
            nueva_posicion.append(movimiento[i] + self.pos[i])
        self.pos = nueva_posicion
        self.mov = [n_x,n_y,n_z]
        self.ang = [phi,mu]
        
        
        
    
