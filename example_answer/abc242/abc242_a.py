import sys
input = sys.stdin.readline

a, b, c, x = map(int, input().split())

if x <= a:
    print(1)
elif a+1 <= x <= b:
    n = b-a
    print(c/n)
else:
    print(0)
