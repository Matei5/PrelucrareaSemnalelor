import numpy
import matplotlib.pyplot as plt

def x(t):
    return numpy.cos(520*numpy.pi*t + numpy.pi/3)

def y(t):
    return numpy.cos(280*numpy.pi*t - numpy.pi/3)

def z(t):
    return numpy.cos(120*numpy.pi*t + numpy.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle("Exercitiu 1")

# t = numpy.linspace(0, 0.03, 59) 
t = numpy.linspace(0, 0.03, 6)

axs[0].stem(t, x(t))
axs[0].set_title("x(t)")
axs[1].stem(t, y(t))
axs[1].set_title("y(t)")
axs[2].stem(t, z(t))
axs[2].set_title("z(t)")

plt.tight_layout()
plt.show()

# for ax in axs.flat:
# ax.set_xlim([xmin, xmax])

# plt.stem(x,y)
# numpy.pi
# numpy.cos(), numpy.sin()
# numpy.floor, numpy.mod, numpy.sign
# numpy.random.rand(d0,d1,...,dn)
# numpy.ones(shape), numpy.zeros(shape)
# numpy.linspace(start, end, no_samples)
# numpy.round(numpy.number)