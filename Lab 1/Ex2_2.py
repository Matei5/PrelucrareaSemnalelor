import numpy
import matplotlib.pyplot as plt

def x(t):
    return numpy.cos(520*numpy.pi*t + numpy.pi/3)

def y(t):
    return numpy.mod(t, 0.2)

def z(t):
    return numpy.sign(x(t))

def w(x,y):
    arr = numpy.zeros((x,y))
    for i in range(x):
        for j in range(y):
            # arr[i][j] = numpy.mod(i,j+1)
            arr[i][j] = numpy.mod(i-64,j-63)
    return arr

fig, axs = plt.subplots(2)
fig.suptitle("Exercitiu 2")

#E
arr = numpy.array(numpy.random.rand(128,128))
axs[0].imshow(arr)

#F
arr = numpy.array(w(128,128))
axs[1].imshow(arr)

plt.show()
