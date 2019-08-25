import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

""" NOT my own code! Copied from 
    https://github.com/timbmg/easy21-rl/blob/master/utils.py
    """

def plot(Q, actions):

    pRange = list(range(1,22))
    dRange = list(range(1,11))
    vStar = list()
    for p in pRange:
        for d in dRange:
            vStar.append( [d,p, np.max([Q[d,p, a] for a in actions])] )

    df = pd.DataFrame(vStar, columns=['player', 'dealer', 'value'])

    # And transform the old column name in something numeric
    # df['player']=pd.Categorical(df['player'])
    # df['player']=df['player'].cat.codes

    # Make the plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(df['dealer'], df['player'], df['value'], cmap=plt.cm.viridis, linewidth=0.2)
    plt.show()

    # to Add a color bar which maps values to colors.
    surf=ax.plot_trisurf(df['dealer'], df['player'], df['value'], cmap=plt.cm.viridis, linewidth=0.2)
    fig.colorbar( surf, shrink=0.5, aspect=5)
    plt.show()

    # Rotate it
    ax.view_init(30, 45)
    plt.show()

    # Other palette
    ax.plot_trisurf(df['dealer'], df['player'], df['value'], cmap=plt.cm.jet, linewidth=0.01)
    plt.show()