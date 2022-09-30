import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
result = 0

for i in range(n):
    num = b.pop(b.index(max(b)))
    result += a[i] * num

print(result)