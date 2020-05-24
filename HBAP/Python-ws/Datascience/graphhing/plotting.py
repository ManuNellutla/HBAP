import matplotlib.pyplot as plt
import numpy as np

fig, (ax1,ax2) = plt.subplots(2)
#fig.suptitle('Vertically stacked subplots')
fig.tight_layout()

def gendata():
    y = [np.random.randint(low=0, high=500) for i in range(100)]
    x = [i for i in range(100)]
    return x,y

def plotme(x, y):
    ax1.plot(x, y, '-ro')
    ax1.set_title("100 Random numnbers plot")
    ax1.set(xlabel="roll id", ylabel="Random Numbers")
    #ax1.ylabel("Random Numbers")
    #ax1.xlabel("roll id")



def plotty():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    ax2.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^', t, t ** 4, 'y+')
    ax2.set_title("T, T Squared, T cubed")


def main():

    x_axis, y_axis = gendata()
    plotme(x_axis, y_axis)
    plotty()

    plt.show()

if __name__ == '__main__':
    main()



