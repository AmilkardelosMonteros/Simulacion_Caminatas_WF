import numpy as np
import matplotlib.pyplot as plt
u1 = 1/50.0#Incremento en K (y)
u2 = 2/50.0 #Incremento en S (x)

archivo = open('Unifome.txt','w')

def caminata():
    x = 0
    y = 0.5
    while abs(x) < 1 and y < 1 and y > 0:
        P = [0.25,0.25,0.25,0.25]
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
    np.savetxt(archivo,np.matrix([x,y]))


for i in range(5000):
    caminata()

archivo.close()
