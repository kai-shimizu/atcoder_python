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


# main 二次元累積和
# (https://masayuki14.hatenablog.com/entry/2020/12/11/2%E6%AC%A1%E5%85%83%E7%B4%AF%E7%A9%8D%E5%92%8C%E3%82%92%E3%81%BE%E3%81%AA%E3%81%B6)
### 動的計画法の高速化 ###
## k<= l<= n の時は dp[k][l][n]と置く ##
""" main """
H, W, n, h, w = IN()
a = INs(H, list)
## 今回は各種類で累積させる
cum2 = [[[0]*n for _ in range(W+1)] for _ in range(H+1)]
for x in range(n):
    for _h in range(H):
        for _w in range(W):
            cum2[_h+1][_w+1][x] = cum2[_h+1][_w][x]+cum2[_h][_w+1][x]-cum2[_h][_w][x]
            if a[_h][_w]==x+1:
                cum2[_h+1][_w+1][x]+=1

# print("\n--- cum2 ---")
# for _h in range(H+1): print(*cum2[0][_h])

## 範囲h,wに存在する個数を求める
ans = [[] for _ in range((H-h+1))]
for _h in range(H-h+1):
    for _w in range(W-w+1):
        cnt = 0
        for x in range(n):
            cnt+=min(1, cum2[H][W][x]-cum2[_h+h][_w+w][x]+cum2[_h+h][_w][x]+cum2[_h][_w+w][x]-cum2[_h][_w][x])
        ans[_h].append(cnt)

for i in ans: print(*i)

""" 誤答（間に合わない） """
# cnt_all = Counter()
# for _h in range(H):
#     cnt_all += Counter(a[_h])

# for _h in range(H-h+1):
#     for _w in range(W-w+1):
#         mask = []
#         for dh, dw in product(range(h),range(w)):
#             mask.append(a[_h+dh][_w+dw])

#         ans = 0
#         cnt = cnt_all-Counter(mask)
#         for key in cnt.keys():
#             if cnt[key]!=0: ans+=1
#         print(ans, end=" ")
#     print()

""" 二次元累積和（サンプル）"""
# h, w = 4, 5
# a = [
#   [1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1]
# ]

# cum2 = [[0]*(w+1) for _ in range(h+1)]
# for _h in range(h): print(*cum2[_h])
# print("--------------")

# for _h in range(h):
#     for _w in range(w):
#         cum2[_h+1][_w+1] = a[_h][_w] + cum2[_h+1][_w] + cum2[_h][_w+1] - cum2[_h][_w]

# for _h in range(h+1): print(*cum2[_h])


