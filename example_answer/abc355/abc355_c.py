from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict, deque
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7
VEC4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VEC9 = list(product([-1, 0, 1], [-1, 0, 1]))

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


def nCr(n: int, r: int):
    # desc: nCrを求める関数
    if n<r: return 0
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


def STR_INs(len_n: int, trans_func=None):
    return [STR_IN(trans_func) for _ in range(len_n)] if trans_func else [STR_IN().strip() for _ in range(len_n)]

def double_range(h, w):
    return product(range(h), range(w))

# main
n, m  = IN()
A = IN(list)

bingo = [[0 for _ in range(n)] for _ in range(n)]

# ビンゴの穴を順番に記入
cnt=1
for a in A:
    bingo[(a-1)//n][(a-1)%n]=cnt
    cnt+=1

ans = [] 
for _i in range(n):
    ma_x, ma_y = 0, 0
    flag_x, flag_y = True, True
    for _j in range(n):
        if bingo[_i][_j]==0: flag_x=False
        if bingo[_j][_i]==0: flag_y=False
        ma_x = max(ma_x, bingo[_i][_j])
        ma_y = max(ma_y, bingo[_j][_i])
        
    # ビンゴの場合，完成したターンを記録
    if flag_x: ans.append(ma_x)
    if flag_y: ans.append(ma_y)

ma_xy, ma_yx = 0, 0
flag_xy, flag_yx = True, True
for _i in range(n):
    if bingo[_i][_i]==0: flag_xy=False
    if bingo[_i][n-_i-1]==0: flag_yx=False
    ma_xy = max(ma_xy, bingo[_i][_i])
    ma_yx = max(ma_yx, bingo[_i][n-_i-1])

if flag_xy: ans.append(ma_xy)
if flag_yx: ans.append(ma_yx)
if len(ans)==0: print(-1)
else: print(min(ans))