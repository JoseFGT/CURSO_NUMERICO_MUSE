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
Tf = 6
N = 5000
Dt = (Tf-To)/N
print("El salto de tiempo es: Dt =", Dt)



### ESQUEMA EULER ###

# Oscilador
U_o = array(zeros([N+1,3])) ; U_o[0,:] = array([To, xo_o , xdto_o])

for i in range(0,N):
   
    U_o[i+1,0] = To + Dt*(i+1)
    U_o[i+1,1:] = U_o[i,1:] + Dt*Fo(U_o[i,1:])


plt.axis("equal")
plt.plot( U_o[:, 0], U_o[:,1] )
plt.show()

 

#print("La solución del oscilador armónico por Euler es: ",U_o)


# Kepler
U_k = array(zeros([N+1,5])) ;  U_k[0,:] = array([To, xo, yo, xdto, ydto])
for i in range(0,N):

    U_k[i+1,0] = To + Dt*(i+1)
    U_k[i+1,1:] = U_k[i,1:] + Dt*Fk(U_k[i,1:])


plt.axis("equal")
plt.plot( U_k[:, 1], U_k[:,2] )
plt.show()


#print("La solución del problema de Kepler por Euler es: ",U_k)

### ESQUEMA EULER  INVERSO ###

# Oscilador
U_o = array(zeros([N+1,3])) ; U_o[0,:] = array([To, xo_o , xdto_o])

for i in range(0,N):
   
    U_o[i+1,0] = To + Dt*(i+1)
    U_o[i+1,1:] = newton(lambda X: X - U_o[i,1:] - Dt*Fo(X), U_o[i,1:]) 


plt.axis("equal")
plt.plot( U_o[:, 0], U_o[:,1] )
plt.show()

# Kepler
U_k = array(zeros([N+1,5])) ;  U_k[0,:] = array([To, xo, yo, xdto, ydto])

for i in range(0,N):
   
    U_k[i+1,0] = To + Dt*(i+1)
    U_k[i+1,1:] = newton(lambda X: X - U_k[i,1:] - Dt*Fk(X), U_k[i,1:]) 


plt.axis("equal")
plt.plot( U_k[:, 1], U_k[:,2] )
plt.show()

### ESQUEMA CRACK-NICKOLSON ###

# Oscilador
U_o = array(zeros([N+1,3])) ; U_o[0,:] = array([To, xo_o , xdto_o])

for i in range(0,N):
   
    U_o[i+1,0] = To + Dt*(i+1)
    U_o[i+1,1:] = newton(lambda X: X - U_o[i,1:] - (Dt/2)*(Fo(X)+Fo(U_o[i,1:])), U_o[i,1:]) 


plt.axis("equal")
plt.plot( U_o[:, 0], U_o[:,1] )
plt.show()

# Kepler
U_k = array(zeros([N+1,5])) ;  U_k[0,:] = array([To, xo, yo, xdto, ydto])

for i in range(0,N):
   
    U_k[i+1,0] = To + Dt*(i+1)
    U_k[i+1,1:] = newton(lambda X: X - U_k[i,1:] - (Dt/2)*(Fk(X)+Fk(U_k[i,1:])), U_k[i,1:]) 


plt.axis("equal")
plt.plot( U_k[:, 1], U_k[:,2] )
plt.show()


