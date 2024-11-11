from matplotlib import pyplot as plt, patches
import numpy as np

#T1

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)

x = np.cos(angles_rad)
y = np.sin(angles_rad)

labels = [r'$30^\circ$', r'$45^\circ$', r'$60^\circ$', r'$90^\circ$', r'$120^\circ$',
          r'$150^\circ$', r'$180^\circ$', r'$270^\circ$']

plt.scatter(x, y, color='purple', marker='X')
for i in range(len(angles_rad)):
    plt.annotate(labels[i],
                 xy=(x[i], y[i]), xycoords='data',
                 xytext=(+10, +5), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()