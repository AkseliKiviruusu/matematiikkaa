import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)

C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X, C, label='Kosini', color='purple')
plt.plot(X, S, label='Sini', color='orange')

xticks = [-3 * np.pi, -2 * np.pi, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 2 * np.pi, 3 * np.pi]
xlabels = [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$2\pi$', r'$3\pi$']
plt.xticks(xticks, xlabels)

yticks = [-1, -0.5, 0, 0.5, 1]
ylabels = [r'$-1$', r'$-\frac{1}{2}$', r'$0$', r'$\frac{1}{2}$', r'$1$']
plt.yticks(yticks, ylabels)

plt.xlabel('X values (radians)')
plt.ylabel('Arvot')
plt.title('Sini- ja kosinikäyrät (-3π to 3π)')

plt.show()