def F(x,y,xd,yd):
    F1 = xd
    F2 = yd
    F3 = -x/(x**2 + x**2)**(3/2)
    F4 = -y/(x**2 + x**2)**(3/2)
    return F1 , F2 , F3, F4 


#Condiciones Iniciales

xn = 1 
yn = 0
xdn = 0
ydn = 1

print (xn, yn)

#Iteración 1

F1, F2, F3, F4 = F(xn,yn,xdn,ydn)

xn1 = xn + 0.1*F1
yn1 = yn + 0.1*F2
xdn1 = xdn + 0.1*F3
ydn1 = ydn + 0.1*F4

xn = xn1
yn = yn1
xdn = xdn1
ydn = ydn1

print (xn, yn)

#Iteración 2

F1, F2, F3, F4 = F(xn,yn,xdn,ydn)

xn1 = xn + 0.1*F1
yn1 = yn + 0.1*F2
xdn1 = xdn + 0.1*F3
ydn1 = ydn + 0.1*F4

xn = xn1
yn = yn1
xdn = xdn1
ydn = ydn1

print (xn, yn)

#Iteración 3

F1, F2, F3, F4 = F(xn,yn,xdn,ydn)

xn1 = xn + 0.1*F1
yn1 = yn + 0.1*F2
xdn1 = xdn + 0.1*F3
ydn1 = ydn + 0.1*F4

xn = xn1
yn = yn1
xdn = xdn1
ydn = ydn1

print (xn, yn)


#Iteración 4

F1, F2, F3, F4 = F(xn,yn,xdn,ydn)

xn1 = xn + 0.1*F1
yn1 = yn + 0.1*F2
xdn1 = xdn + 0.1*F3
ydn1 = ydn + 0.1*F4

xn = xn1
yn = yn1
xdn = xdn1
ydn = ydn1

print (xn, yn)

#Iteración 5

F1, F2, F3, F4 = F(xn,yn,xdn,ydn)

xn1 = xn + 0.1*F1
yn1 = yn + 0.1*F2
xdn1 = xdn + 0.1*F3
ydn1 = ydn + 0.1*F4

xn = xn1
yn = yn1
xdn = xdn1
ydn = ydn1

print (xn, yn)

