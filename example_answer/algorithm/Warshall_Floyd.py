""" ワーシャルフロイド法の実装 """
"""
ワーシャルフロイド法は中間点mを通るかどうかを動的計画法で全探索する．
Point：s→m→l→gという経路が最短であるとする．
この時，s→m→lまたはm→l→gのいずれかが先に見つかるため，
s→m→(l)→gやs→(m)→l→gのいずれかで必ず最短経路が見つかる．
"""
from math import inf
import sys
input = sys.stdin.readline

point_n = 3
edge_n = 3
p2p = [[1, 2, 1], [1, 3, 1], [2, 3, 3]]
# 隣接行列表現
ad_mat = [[inf]*point_n for _ in range(point_n)]
## 自己ループを0とする
for i in range(point_n): ad_mat[i][i]=0
## 既知の値を入力
for p1, p2, dist in p2p:
    ad_mat[p1-1][p2-1] = dist
    ad_mat[p2-1][p1-1] = dist

# ワーシャルフロイド法
for m in range(point_n): # 中継点
    for s in range(point_n): # 始点
        for g in range(point_n): # 終点
            ad_mat[s][g] = min(ad_mat[s][g], ad_mat[s][m]+ad_mat[m][g])

print(ad_mat)