import matplotlib.pyplot as plt

from Algorithms.RecuriseSquare import *
from Drawing.Canvas import *

fig,ax = plt.subplots()


RecuriseSquare(ax,0,0,100)
SetView(ax,-10,100,-10,100)
ax.set_aspect("equal")

plt.show()
fig.savefig("OutPut/Square.png")