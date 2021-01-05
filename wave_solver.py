import numpy as np

# 定数
T = 10
X = 1
Y = 1
Z = 1
c = 1

# 刻み幅
dt = 0.01
dl = 0.1

# 解配列の大きさ
tn = int(T / dt)
xn = int(X / dl)
yn = int(Y / dl)
zn = int(Z / dl)

print(tn, xn, yn, zn)

# 解に使う配列と初期条件
P = np.zeros((tn, xn, yn, zn))
P[0][xn // 2][yn // 2][zn // 2] = 200

# 陽的差分法
alpha = c ** 2 * dt ** 2 / dl ** 2
for i in range(tn - 1):
    for j in range(1, xn - 1):
        for k in range(1, yn - 1):
            for l in range(1, zn - 1):
                a = P[i][j + 1][k][l] + P[i][j - 1][k][l]
                b = P[i][j][k + 1][l] + P[i][j][k - 1][l]
                c = P[i][j][k][l + 1] + P[i][j][k][l - 1]
                P[i + 1][j][k][l] = -P[i - 1][j][k][l] - alpha * (a + b + c) + (6 *alpha + 1) * P[i][j][k][l]

# 解の表示
print(P[tn - 1][xn // 2][yn // 2])