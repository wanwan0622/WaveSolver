import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# 定数
T = 0.003
X = 1
Y = 1
Z = 1
C = 1

# 刻み幅
dt = 0.0001
dl = 0.1

# 解配列の大きさ
tn = int(T / dt)
xn = int(X / dl)
yn = int(Y / dl)
zn = int(Z / dl)

print(tn, xn, yn, zn)

# 解に使う配列と初期条件
P = np.zeros((tn, xn, yn, zn))
P[0][xn // 2][yn // 2][zn // 2] = 0.5

# 陽的差分法(中心差分近似)
alpha = C ** 2 * dt ** 2 / dl ** 2
print(alpha)
for i in range(tn - 1):
    for j in range(1, xn - 1):
        for k in range(1, yn - 1):
            for l in range(1, zn - 1):
                a = P[i][j + 1][k][l] + P[i][j - 1][k][l]
                b = P[i][j][k + 1][l] + P[i][j][k - 1][l]
                c = P[i][j][k][l + 1] + P[i][j][k][l - 1]
                P[i + 1][j][k][l] = -P[i - 1][j][k][l] - alpha * (a + b + c) + (6 * alpha + 1) * P[i][j][k][l]

# 解の表示
print(P[tn - 1][xn // 2][yn // 2])

x = [i % yn % zn * dl for i in range(xn * yn  * zn)]
y = [i // zn % xn * dl for i in range(xn * yn  * zn)]
z = [i // xn // yn * dl for i in range(xn * yn  * zn)]
fig = plt.figure()
ax = Axes3D(fig)
"""
color = [P[tn - 1][i][j][k] for i in range(xn) for j in range(yn) for k in range(zn)]
p = ax.scatter(x, y, z, c=color, cmap='hot')
fig.colorbar(p)
plt.show()
"""
ims = []  #ここに1ステップごとのグラフを格納
for t in range(tn):
    color = [P[t][i][j][k] for i in range(xn) for j in range(yn) for k in range(zn)]
    p = ax.scatter(x, y, z, c=color, cmap='hot')
    ims.append([p])

ani = animation.ArtistAnimation(fig, ims, interval=10)  #ArtistAnimationでアニメーションを作成する。
ani.save('animate.gif', writer='imagemagick')  #gifで保存