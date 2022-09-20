import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
tst = 0
# !합이 M을 넘지 않는 카드 3장을 찾아라!

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] > m:
                continue
            else:
                tst = max(tst,num[i] + num[j] + num[k])

print(tst)
# 완전탐색문제 