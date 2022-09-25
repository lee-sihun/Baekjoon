import sys
input = sys.stdin.readline

def factorial(x):
    for i in range(x-1,1,-1):
        if x > 1:
            x *= i
    if x == 0:
        return 1
    else:
        return x

n = int(input())
n = list(str(factorial(n)))[::-1]
cnt = 0

for i in n:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)