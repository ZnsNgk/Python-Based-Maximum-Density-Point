import math
import random

def get_point_distance(x, y): #计算N维空间中两点的距离
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i])**2
    d = math.sqrt(d)
    return d

def get_distance_list(N):   #通过计算任意两点间距离获得距离矩阵
    m = len(N)  #获取数据集中元素个数
    Dis = []
    for i in range(m):
        Dis.append([])
        for j in range(m):
            x1 = N[i]
            x2 = N[j]
            dis = get_point_distance(x1, x2)
            Dis[i].append(dis)  #将距离信息保存到距离矩阵内
    return Dis

def most_point(D, r):   #获取D中半径为r的最大密度点
    n = len(D)  #获取数据集中元素个数
    Distance = get_distance_list(D)
    f = 0
    num = []   #定义数量向量，其元素值为该点在r半径内的点的数量
    for i in range(n):
        flag = 0
        for j in range(n):
            if Distance[i][j] < r:
                flag += 1
        num.append(flag - 1)    #减一为了剔除自身（点到自身的距离为0）
    for i in range(n):  #判断该区域内有无点
        if num[i] != 0:
            f += 1
    if f == 0:
        return float('nan') #若该范围内没有点则返回NaN
    most = num.index(max(num))  #获取最大值所在的下标
    return most

if __name__ == '__main__':  #主函数，用于测试
    D = []    #生成一个100个元素，2维的数据集
    dim = 0
    num = 0
    r = 0
    num = input("请输入元素个数:")
    dim = input("请输入维度:")
    r = input("请输入半径r:")
    num = int(num)
    dim = int(dim)
    r = int(r)
    for i in range(num):
        D.append([])
        for j in range(dim):
            D[i].append(random.uniform(1, 100))
    most = most_point(D, r)
    print(most)
