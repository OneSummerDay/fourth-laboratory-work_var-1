import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return x * np.sin(5 * x)


x_values = np.linspace(-2, 5, 500)

y_values = y_function(x_values)

plt.plot(x_values, y_values, label=r'$Y(x) = x \cdot \sin(5x)$')
plt.title('Графік функції Y(x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.legend()

#plt.savefig('graph.png')

plt.show()
