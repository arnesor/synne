import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)  # 100 jevnt fordelte punkter mellom 0 og 2pi
y = np.sin(x)

plt.plot(x, y, label="f(x) = sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graf for f(x) = sin(x)")
plt.legend()
plt.grid(True)
plt.show()
