from bisect import bisect_left, bisect_right
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7
VEC4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VEC9 = product([-1, 0, 1], [-1, 0, 1])

# 自作関数
def lcm(a, b):
    # desc: 最小公倍数を求める関数
    return a*b // gcd(a, b)

def prime_numbers(max_n):
    # 素数数列を返す
    def is_prime(n):
        # 素数判定
        for p in ps:
            if n % p == 0:
                return False
            if p ** 2 >= n:
                break
        return True
    ps = []
    for n in range(2, max_n+1):
        if is_prime(n):
            ps.append(n)

    return ps

def divisor(n: int):
    # 約数を返す
    ans = []
    for i in range(1, ceil(sqrt(n))+1):
        if n % i == 0:
            ans.append(i)
            ans.append(n//i)
    return ans

def cum(array: list, key=lambda x: x):
    # 累積和
    cum_sum = [key(array[0])]
    for i in range(len(array)-1):
        cum_sum.append(cum_sum[-1]+key(array[i+1]))
    return cum_sum


def combination(n: int, r: int):
    # desc: nCrを求める関数
    return factorial(n) // factorial(r) // factorial(n - r)

def rle(s):
    # ランレングス圧縮
    bef = s[0]
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if s[i] == bef:
            cnt += 1
        else:
            arr.append([bef, cnt])
            bef = s[i]
            cnt = 1
    arr.append([bef, cnt])
    return arr

def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list:
        return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN(trans_func=lambda x: x):
    input_ = input().strip().split()
    return trans_func(input_[0]) if len(input_) == 1 else input_


def INs(len_n: int, trans_func=lambda x: x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main
n, m = IN()
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = IN()
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

WHITE = 0
BLACK = 1
EMPTY = -1
color_graph = [EMPTY]*n

ans = n*(n-1)//2-m
for i in range(n):
    if color_graph[i]!=EMPTY: continue
    BLACK_NUM = 0
    WHITE_NUM = 1
    color_graph[i] = WHITE
    q = Queue()
    q.put((graph[i], WHITE))
    while not q.empty():
        ps, this_color = q.get()
        this_color = WHITE if this_color==BLACK else BLACK
        for p in ps:
            if color_graph[p]==EMPTY:
                if this_color==BLACK: BLACK_NUM+=1
                else: WHITE_NUM+=1
                color_graph[p] = this_color
                q.put((graph[p], this_color))
            elif color_graph[p]!=this_color:
                print(0)
                exit()
    ans -= (BLACK_NUM*(BLACK_NUM-1)//2 + WHITE_NUM*(WHITE_NUM-1)//2)
print(ans)

"""
## 二部グラフの判定(二色で塗分けることができる無向グラフ)
## 連結グラフが与えられたと仮定する

n, m = IN()
graph = [[] for _ in range(n)]

## 隣接行列を求める
for _ in range(m):
    u, v = IN()
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

WHITE = 0
BLACK = 1
EMPTY = -1
color_graph = [EMPTY]*n

## 最初の頂点0を白とする
color_graph[0] = WHITE
q = Queue()
q.put((graph[0], WHITE))

## 二部グラフの判定
while not q.empty():
    ## 現在の頂点から連結している頂点(ps)と色(this_color)を取得
    ps, this_color = q.get()
    ## 色の反転
    this_color = WHITE if this_color==BLACK else BLACK
    
    ## 連結している頂点の色を確認
    for p in ps:
        ## 色がなければ、現在とは逆色を代入
        if color_graph[p]==EMPTY:
            color_graph[p] = this_color
            q.put((graph[p], this_color))
        
        ## 現在の色と同じ色の場合、二部グラフではない
        elif color_graph[p]!=this_color:
            print("二部グラフではない")
            exit()

print("二部グラフである")

"""