import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num.sort(reverse=True)
print(num[1])