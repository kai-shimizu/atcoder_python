""" セグメント木の実装 """

from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict, deque
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline

# セグメント木（1-indexed）
class SegTree:
    def __init__(self, array, func, init_val=0):
        self.array = array
        self.func = func
        self.init_val = init_val
        self.data_n = len(array)
        self.leaves_num = 1<<(self.data_n-1).bit_length()
        self.data = [self.init_val for _ in range(2*self.leaves_num)]
        # 葉の構築
        for i in range(self.data_n):
            self.data[self.leaves_num+i] = self.array[i]
        # 木の構築(親iの子は2i,2i+1)
        for i in range(self.leaves_num-1, 0,-1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])
    def update(self, idx, val):
        # 葉に置換
        idx += self.leaves_num
        self.data[idx] = val
        while k>1:
            k//=2
            # 親kの子は2k,2k+1
            self.data[k] = self.func(self.data[2*k], self.data[2*k+1])
    
    def get(self, l, r):
        """_summary_
        Args:
            l : 開区間(l,-]
            r : 閉区間(-,r]
        """
        ans = self.init_val
        
        # 葉に置換
        l += self.leaves_num
        r += self.leaves_num
        
        while l<r:
            if l&1:
                ans = self.func(ans, self.data[l])
                l += 1
            if r&1:
                ans = self.func(ans, self.data[r-1])
            l //= 2
            r //= 2
        return ans

# main
player = [29, 18, 31, 19, 13, 12, 17, 27]
st = SegTree(player, max)
print(st.data)
print(st.get(1, 3))