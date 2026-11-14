import numpy as np

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

def RecuriseTri(ax,x1,y1,x2,y2,x3,y3):
    #将参数转换成向量
    A=np.array([x1,y1])
    B=np.array([x2,y2])
    C=np.array([x3,y3])
    #计算三角形的面积
    S = CalTriSuc(A,B,C)
    DrawTri(ax,A,B,C)
    #如果三角形面积小于或者等于5，就停止了
    if(S <= 5 ):
        return
    t=0.1
    """
    这是一个矩阵运算
    [x2-x1][y2-y1],得出x1和x2相距多远，然后乘以向量t
    得出从x1到x1走10%距离是多远
    加上原来的向量x1，是让这个矩阵从x1出发到x2偏移10%
    """
    new_A=A+t*(B-A)
    new_B=B+t*(C-B)
    new_C=C+t*(A-C)
    RecuriseTri(ax,new_A[0],new_A[1],new_B[0],new_B[1],new_C[0],new_C[1])

def CalTriSuc(A, B, C):
    """
    公式来源
    zh.wikihow.com/计算三角形面积
    使用计算三角形的半周长
    再使用海伦三角公式计算出三角形的面积
    并且将面积返回
    """
    a=np.linalg.norm(B-C)
    b=np.linalg.norm(A-C)
    c=np.linalg.norm(A-B)
    s=(a+b+c)/2
    S=np.sqrt(s*(s-a)*(s-b)*(s-c))
    return S