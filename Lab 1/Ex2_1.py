import numpy
import matplotlib.pyplot as plt

def x(t):
    return numpy.cos(520*numpy.pi*t + numpy.pi/3)

def y(t):
    return numpy.mod(t, 0.2)

def z(t):
    return numpy.sign(x(t))

def w(x,y):
    arr = numpy.ones((x,y))
    for i in range(x):
        for j in range(y):
            arr[i][j] = numpy.mod(i-64,j-63)
    return arr

fig, axs = plt.subplots(4)
fig.suptitle("Exercitiu 2")

# A
t = numpy.linspace(0, 4, 1600)
axs[0].stem(t, x(t))
axs[0].set_title("A")

#B
t = numpy.linspace(0, 3, 2400)
axs[1].plot(t, x(t))
axs[1].set_title("B")

#C
t = numpy.linspace(0, 1, 240)
axs[2].plot(t, y(t))
axs[2].set_title("C mod")

#D
t = numpy.linspace(0, 0.1, 30)
axs[3].plot(t, z(t))
axs[3].set_title("D sign")

plt.show()
