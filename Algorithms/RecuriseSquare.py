from Drawing.Draw import *

def RecuriseSquare(ax,x,y,size):
    """
    这是一个递归函数，用于不停的call DrawSquare方法画图
    每次新的边长会是原图的四分之一
    每次图像尺寸会小一半
    """
    if size <= 10:
        return
    DrawSquare(ax,x,y,size)
    new_size = size / 2
    new_x = x + size / 4
    new_y = y + size / 4

    RecuriseSquare(ax,new_x,new_y,new_size)