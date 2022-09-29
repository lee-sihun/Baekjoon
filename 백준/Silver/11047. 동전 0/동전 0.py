import sys
input = sys.stdin.readline

n, k = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
count = 0

for coin in a:
    if k == 0: #n이 0이라면 종료 
        break
    
    if k == coin: #n이 coin 이라면 
        count += 1
        break
    elif k % coin == 0: #n을 coin으로 나눈 나머지 값이 0이라면 
        count += k // coin
        break
    else:
        count += k // coin
        k %= coin

print(count)
