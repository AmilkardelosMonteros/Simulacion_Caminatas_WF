import matplotlib.pyplot as plt
import numpy as np

A1 = np.loadtxt('Experimento1A_frecuencia_0.5_u1_1%102.0_u2_1%50.0.txt')
B1 = np.loadtxt('Experimento1B_frecuencia_0.5_u1_1%101.0_u2_1%50.0.txt')

A2 = np.loadtxt('Experimento2A_frecuencia_0.5_u1_1%102.0_u2_1%50.0.txt')
B2 = np.loadtxt('Experimento2B_frecuencia_0.5_u1_1%101.0_u2_1%50.0.txt')

walkA = np.loadtxt('Walk_A_frecuencia_0.5_u1_1%102.0_u2_1%50.0.txt')
walkB = np.loadtxt('Walk_B_frecuencia_0.5_u1_1%101.0_u2_1%50.0.txt')

def grafica(a,b,n):
    alfa = 0.03
    x_A,y_A,x_B,y_B = [],[],[],[]
    for i in range(len(a)):
        tem_A = a[i]
        x_A.append(tem_A[0])
        y_A.append(tem_A[1])
        tem_B = b[i]
        x_B.append(tem_B[0])
        y_B.append(tem_B[1])
    f, (ax1, ax2) = plt.subplots(2, 1, sharey=True)
    ax1.plot(x_A, y_A,'o',alpha = alfa)
    ax1.set_title('Experiemento' +str(n) +'A')
    plt.plot(x_B,y_B,'o',alpha = alfa)
    ax2.set_title('Experiemento'+str(n)+ 'B')
    plt.xlabel('$ s $', fontsize = 32)
    plt.ylabel('$\kappa$', fontsize = 32)    
    ax1.set_aspect(1)
    ax2.set_aspect(1)
    plt.show()
grafica(A1,B1,1)
grafica(walkA,walkB,3)
grafica(A2,B2,2)
