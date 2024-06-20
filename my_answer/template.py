from bisect import bisect, bisect_left, bisect_right
from itertools import count
from math import ceil, factorial, floor, gcd
from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7

# 定数
MOD = 10**9+7

# 自作関数


def lcm(a, b):
    # desc: 最小公倍数を求める関数
    return a*b // gcd(a, b)


# 素数数列を返す
def prime_numbers(max_n):
    ps = []

    def is_prime(n):
        for p in ps:
            if n % p == 0:
                return False
            if p ** 2 >= n:
                break
        return True

    for n in range(2, max_n+1):
        if is_prime(n):
            ps.append(n)

    return ps


def cum(array: list):
    cum_sum = [array[0]]
    for i in range(len(array)-1):
        cum_sum.append(cum_sum[-1]+array[i+1])
    return cum_sum


def combination(n: int, r: int):
    # desc: nCrを求める関数
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list:
        return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN():
    input_ = input().strip().split()
    return input_[0] if len(input_) == 1 else input_


def INs(len_n: int, trans_func=lambda x: x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main