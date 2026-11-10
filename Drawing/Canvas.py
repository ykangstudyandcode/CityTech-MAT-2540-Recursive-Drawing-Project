def SetView(ax,a,b,c,d):
    """
    这是一个帮助控制xy轴大小的方法
    a是x轴的左边，b是x轴的右边
    c是y轴的底部，d是一个y轴的顶部
    """
    ax.set_xlim(a,b)
    ax.set_ylim(c,d)