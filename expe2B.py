import numpy as np
import matplotlib.pyplot as plt

#u1 = 0.01 #Incremento en K (y)
a1 = 1
b1 = 101.0
u1 = a1/b1#0.00980392156862745 #por que hicimos mas pequeño  el dominio

a2 = 1
b2 = 50.0
u2 = a2/b2#Incremento en S (x)
rep = 5000

frec_inicial = 0.5
x_init = 0
y_init = (1-u1)/2.0

def probafixWF(a,y): #para k = 0, (es un WF normal) a es la seleccion y y la frecuencia inicial
    p = (1-np.exp(- 2*a*y))/(1 - np.exp(-2*a))
    return p

#a es tu s, k es kappa y y es la frec inicial (1/2 para ti)
def probafixM1(a, k, y):
    if 2*a < k:
        S = 1 - (1 - k)**(1 - 2*a/k)
        p = (1/S)* (1-(1 - k*(1-y))**(1 - 2*a/k))
    elif 2*a == k:
        S = np.log(1.0/(1.0-k))
        p = (1/S)*np.log(1.0/(1.0-k*(1-y)))
    else:
        S = (1 - k)**(1 - 2*a/k)  - 1
        p = (1/S)* ((1 - k*(1-y))**(1 - 2*a/k)-1)
    return 1-p

def probabilidades(s,k):
    s_barra =  u2/(1+s)
    s_barra_neg  = -u2/(1+s)
    p_mas_mas  = probafixWF(s_barra,frec_inicial)
    p_menos_mas = p_mas_mas 
    p_menos_menos = probafixWF(s_barra_neg,frec_inicial)
    p_mas_menos =  p_menos_menos
    Sum  = p_mas_mas+p_mas_menos+p_menos_menos+p_menos_mas
    p_mas_mas =  p_mas_mas/Sum
    p_menos_mas =  p_menos_mas/Sum
    p_mas_menos =  p_mas_menos/Sum
    p_menos_menos =  p_menos_menos/Sum
    return [p_mas_mas,p_mas_menos,p_menos_mas,p_menos_menos]

def caminata():
    x = x_init
    y = y_init
    while True:
        if abs(x) >= 1 or y > 1-u1 or y < 0:
            break
        else:
            P = probabilidades(x,y)
            salto = np.random.choice([0,1,2,3],p = P)
            if salto == 0:
                y = y + u1
                x = x + u2
            if salto == 1:
                y = y + u1
                x = x - u2
            if salto == 2:
                y = y - u1
                x = x + u2
            if salto == 3:
                y = y - u1
                x = x - u2
    np.savetxt(archivo,np.matrix([float(x),float(y)]))

nombre = 'Experimento2B_'+'frecuencia_'+str(frec_inicial)+'_u1_'+str(a1)+'%'+str(b1)+'_u2_'+str(a2)+'%'+ str(b2)+'.txt'
archivo = open(nombre,'w')
for i in range(rep):
    caminata()
archivo.close()
