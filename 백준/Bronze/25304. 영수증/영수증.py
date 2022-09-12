x = int(input())
n = int(input())
num = 0

for i in range(n):
    a,b = map(int, input().split())
    num += a*b

if x == num:
    print("Yes")
else:
    print("No")