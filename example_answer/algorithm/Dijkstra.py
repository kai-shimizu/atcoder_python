""" ダイクストラ法 """

from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict, deque
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline

Edges = [[[1, 4], [2, 3]],
         [[2, 1], [3, 1], [4, 5]],
         [[5, 2]],
         [[4, 3]],
         [[6, 2]],
         [[4, 1], [6, 4]], 
         []
        ]

# node(0~6)
node_n = 7

# 頂点へのコスト
dist = [inf]*node_n
dist[0] = 0
seen = [False]*node_n

stack = [0]
while len(stack)>0:
    ## 最小コストの頂点を選択
    sp = stack[0]
    for _s in stack:
        if seen[True]: continue
        if dist[sp]>dist[_s]:
            sp = _s
    
    seen[sp] = True
    stack.pop(stack.index(sp))

    for np, cost in Edges[sp]:
        if seen[np]: continue
        dist[np] = min(dist[np], dist[sp]+cost)
        stack.append(np)
    
print(dist)