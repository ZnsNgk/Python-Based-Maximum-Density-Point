from maximum_density_point import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes

D = []    #生成一个100个元素，2维的数据集
for i in range(100):
    D.append([])
    for j in range(2):
        D[i].append(random.uniform(1, 100))
r = 10
most = most_point(D, r)
print(most)
X = []
Y = []
for i in range(len(D)):
    X.append(D[i][0])
    Y.append(D[i][1])
fig, ax = plt.subplots()
plt.scatter(X, Y, color='black')
if math.isnan(most):
    plt.legend()
    plt.show()
else:
    circle = mpathes.Circle(D[most], r, color='R', fc='None')
    plt.scatter(X[most], Y[most], color='R')
    ax.add_patch(circle)
    #plt.legend()
    plt.show()
    