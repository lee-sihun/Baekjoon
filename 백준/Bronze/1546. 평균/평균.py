n = int(input())
list = list(map(int, input().split()))
m = max(list)
num = 0

for i in list:
    num += i/m*100

print(num/n)
