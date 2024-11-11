import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)

C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X, C, label='Kosini', color='purple')
plt.plot(X, S, label='Sini', color='orange')

plt.xlabel('X values (radians)')
plt.ylabel('Arvot')
plt.title('Sini- ja kosinikäyrät (-3π to 3π)')

plt.show()