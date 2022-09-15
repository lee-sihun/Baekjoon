n = int(input())
num_list = []

for i in range(n):
    x, y = map(int, input().split())
    num = x, y
    num_list.append(num)

for i in num_list:
    k = 1
    for j in num_list:
        if i[0] < j[0] and i[1] < j[1]:
            k += 1
    print(k, end=' ')
