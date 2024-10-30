from numpy import zeros, array
from scipy.optimize import newton
import matplotlib.pyplot as plt 

#### Físicas del problema

## Problema de kepler

def Fk(U):
    x = U[0] ; y = U[1] ; xdt =  U[2] ; ydt = U[3]
    F1 = xdt
    F2 = ydt
    F3 = -x/(x**2 + y**2)**(3/2)
    F4 = -y/(x**2 + y**2)**(3/2)
    return array([F1 , F2 , F3, F4 ])

## Oscilador Armónico

def Fo(U):
    x = U[0] ; xdt =  U[1]
    F1 = xdt
    F2 = -x

    return array([F1 , F2])

## Plots 
def PlotKepler(U_k, titulo = "título"):
    
    plt.figure()  # Crear una nueva figura
    plt.axis("equal")                  # Escala igual para ambos ejes
    plt.plot(U_k[:, 1], U_k[:,2])     # Gráfico de tus datos
    plt.title(titulo)     # Añadir título
    plt.xlabel("x")        # Título del eje X
    plt.ylabel("y")        # Título del eje Y
    plt.grid(True)                      # Mostrar la cuadrícula
    plt.show()  # Mostrar el gráfico

def PlotOscilador(U_o, titulo = "título"):
    
    plt.figure()  # Crear una nueva figura
    plt.axis("equal")                  # Escala igual para ambos ejes
    plt.plot(U_o[:, 0], U_o[:,1])     # Gráfico de tus datos
    plt.title(titulo)     # Añadir título
    plt.xlabel("time")        # Título del eje X
    plt.ylabel("x")        # Título del eje Y
    plt.grid(True)                      # Mostrar la cuadrícula
    plt.show()  # Mostrar el gráfico


### Condiciones Iniciales y Nº pasos ###

# Kepler
xo = 1
yo = 0
xdto = 0
ydto = 1

# Oscilador
xo_o = 0
xdto_o = 1


To = 0 
Tf = 50
N = 50000
Dt = (Tf-To)/N
print("El salto de tiempo es: Dt =", Dt)

Problema = int(input("¿Que problema quieres resolver?: [1] = Kepler  [2] = Oscilador Armónico "))

if Problema == 1:
    ### Kepler ###
 
    ### Euler
    U_k = array(zeros([N+1,5])) ;  U_k[0,:] = array([To, xo, yo, xdto, ydto])
    for i in range(0,N):

        U_k[i+1,0] = To + Dt*(i+1)
        U_k[i+1,1:] = U_k[i,1:] + Dt*Fk(U_k[i,1:])

    PlotKepler(U_k,"Solución por Euler")

    ### Euler Inverso
    U_k = array(zeros([N+1,5])) ;  U_k[0,:] = array([To, xo, yo, xdto, ydto])

    for i in range(0,N):
    
        U_k[i+1,0] = To + Dt*(i+1)
        U_k[i+1,1:] = newton(lambda X: X - U_k[i,1:] - Dt*Fk(X), U_k[i,1:]) 


    PlotKepler(U_k,"Solución por Euler inverso")

    ### Crank-Nicolson

    U_k = array(zeros([N+1,5])) ;  U_k[0,:] = array([To, xo, yo, xdto, ydto])

    for i in range(0,N):
    
        U_k[i+1,0] = To + Dt*(i+1)
        U_k[i+1,1:] = newton(lambda X: X - U_k[i,1:] - (Dt/2)*(Fk(X)+Fk(U_k[i,1:])), U_k[i,1:]) 


    PlotKepler(U_k,"Solución por Crank-Nicolson")   
else:

    ### Euler

    U_o = array(zeros([N+1,3])) ; U_o[0,:] = array([To, xo_o , xdto_o])

    for i in range(0,N):
    
        U_o[i+1,0] = To + Dt*(i+1)
        U_o[i+1,1:] = U_o[i,1:] + Dt*Fo(U_o[i,1:])

    PlotOscilador(U_o, titulo = "Solución por Euler")

    ### Euler inverso

    U_o = array(zeros([N+1,3])) ; U_o[0,:] = array([To, xo_o , xdto_o])

    for i in range(0,N):
    
        U_o[i+1,0] = To + Dt*(i+1)
        U_o[i+1,1:] = newton(lambda X: X - U_o[i,1:] - Dt*Fo(X), U_o[i,1:]) 


    PlotOscilador(U_o, titulo = "Solución por Euler Inverso")


    ### Crank-Nicolson

    U_o = array(zeros([N+1,3])) ; U_o[0,:] = array([To, xo_o , xdto_o])

    for i in range(0,N):
    
        U_o[i+1,0] = To + Dt*(i+1)
        U_o[i+1,1:] = newton(lambda X: X - U_o[i,1:] - (Dt/2)*(Fo(X)+Fo(U_o[i,1:])), U_o[i,1:]) 


    PlotOscilador(U_o, titulo = "Solución por Crank-Nicolson")



