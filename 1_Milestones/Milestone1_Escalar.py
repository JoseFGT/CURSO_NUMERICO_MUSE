from numpy import zeros, array
from scipy.optimize import newton
import matplotlib.pyplot as plt 

#### Físicas del problema

## Problema de kepler

def Fk(x,y,xd,yd):
    F1 = xd
    F2 = yd
    F3 = -x/(x**2 + y**2)**(3/2)
    F4 = -y/(x**2 + y**2)**(3/2)
    return F1 , F2 , F3, F4 

## Oscilador Armónico

def Fo(x,xd):
    F1 = xd
    F2 = -x
    return F1 , F2

### Condiciones Iniciales y Nº pasos ###

# Kepler
xo = 1
yo = 0
xdo = 0
ydo = 1

# Oscilador
xo_o = 0
xdo_o = 1


To = 0 
Tf = 7
N = 70
Dt = (Tf-To)/N
print("El salto de tiempo es: Dt =", Dt)



### ESQUEMA EULER ###

# Oscilador
xn = xo_o ; xdn = xdo_o ; U_o = array(zeros([N+1,2])) ; U_o[0,:] = array([To, xn])

for i in range(0,N):
    F1, F2 = Fo(xn,xdn)

   
    xn1 = xn + Dt*F1
    xdn1 = xdn + Dt*F2

    xn = xn1
    xdn = xdn1
    Ti1 = To + Dt*(i+1)
    U_o[i+1,:] = array([Ti1, xn])


plt.axis("equal")
plt.plot( U_o[:, 0], U_o[:,1] )
plt.show()

 

#print("La solución del oscilador armónico por Euler es: ",U_o)


# Kepler
xn = xo ; yn = yo ; xdn = xdo ; ydn = ydo ; U_k = array(zeros([N+1,3])) ;  U_k[0,:] = array([To, xn, yn])
for i in range(0,N):
    F1, F2, F3, F4 = Fk(xn,yn,xdn,ydn)

    
    xn1 = xn + Dt*F1
    yn1 = yn + Dt*F2
    xdn1 = xdn + Dt*F3
    ydn1 = ydn + Dt*F4

    xn = xn1
    yn = yn1
    xdn = xdn1
    ydn = ydn1
    Ti1 = To + Dt*(i+1)
    U_k[i+1,:] = array([Ti1, xn, yn])

plt.axis("equal")
plt.plot( U_k[:, 1], U_k[:,2] )
plt.show()


#print("La solución del problema de Kepler por Euler es: ",U_k)

