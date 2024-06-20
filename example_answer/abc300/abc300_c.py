from bisect import bisect_left, bisect_right
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


def STR_INs(len_n: int, trans_func=lambda x: x):
    return [STR_IN(trans_func).strip() for _ in range(len_n)]

def double_range(h, w):
    return product(range(h), range(w))

# main
h, w = IN()
C = STR_INs(h)

ans = [0]*min(h, w)
# 1~h-1, 1~w-1を探索
for _y, _x in product(range(h-2), range(w-2)):
    base_y, base_x = _y+1, _x+1
    # "."の時，スキップ
    if C[base_y][base_x]==".": continue
    
    # ×の有無
    flag = True
    for dy, dx in product((-1, 1), (-1, 1)):
        if C[base_y+dy][base_x+dx]==".":
            flag = False
            break
    
    # ×のサイズ
    if flag:
        cnt = 0
        dy, dx = 1, 1
        this_y, this_x = base_y, base_x
        while (0<=this_y+dy<h and 0<=this_x+dx<w):
            this_y+=dy
            this_x+=dx
            if C[this_y][this_x]!="#": break
            cnt+=1
    
        ans[cnt-1]+=1

print(*ans)