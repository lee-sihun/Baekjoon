import sys 
input = sys.stdin.readline

n = int(input())
num = list(range(1,n+1))
index = 0

for i in range(len(num)-1):
    index += 1
    num.append(num[index])
    index += 1

print(num[index])