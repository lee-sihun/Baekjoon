import sys
input = sys.stdin.readline

n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
count = 0
result = 0
# print(time_list)
for time in time_list:
    count = time + count
    result += count 

print(result)
# 1 2 3 3 4

# 1 = 1
# 2 1 + 2 = 3
# 3 1 + 2 + 3 = 6
# 4 1 + 2 + 3 + 3 = 9
# 5 1 + 2 + 3 + 3 + 4 = = 13