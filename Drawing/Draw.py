from matplotlib.patches import *

def DrawSquare(ax,x,y,size):
    """
    这是一个用来封装绘图的方法，当使用方法的时候会传入图的x轴和y轴
    并且还会传入图的尺寸
    """
    square=Rectangle((x,y),size,size,fill=False)
    ax.add_patch(square)

def DrawTri(ax,A,B,C):
    triangle = Polygon([A,B,C],closed=True,fill=False)
    ax.add_patch(triangle)
