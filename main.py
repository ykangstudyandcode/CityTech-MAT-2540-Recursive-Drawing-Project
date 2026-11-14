import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from Algorithms.RecuriseAlog import *
from Drawing.Canvas import *

fig,ax = plt.subplots()


#RecuriseSquare(ax,0,0,100)

RecuriseTri(ax,0,1,60,1,30,60)


SetView(ax,-1,61,-1,61)
ax.set_aspect("equal")

plt.show()
fig.savefig("OutPut/Tri.png")