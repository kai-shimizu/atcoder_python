import sys
input = sys.stdin.readline

n = int(input())

ans = ["1"]
for i in range(2, n+1):
    ans.extend([str(i), *ans])

print(*ans)