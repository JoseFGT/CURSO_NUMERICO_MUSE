

from numpy import array, zeros, linspace, sin, pi 
import matplotlib.pyplot as plt 
import time

start = time.time()

print("Hello world")

t = linspace(0., 1., 100)
y = sin( 4*pi*t )

plt.plot(t,y)

end = time.time()

print(end - start)
plt.show()