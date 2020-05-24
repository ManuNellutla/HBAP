
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig, (ax1,ax2) = plt.subplots(1, 2)

x = np.linspace(0, 10, 30)
y = np.sin(x)

ax1.plot(x, y, 'o', color='black');
for i, txt in enumerate(x):
    ax1.annotate(txt, (x[i], y[i]))


rng = np.random.RandomState(0)

for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    ax2.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
ax2.legend(numpoints=1)
ax2.set_xlim(0, 1.8)



plt.show()


plt.show()