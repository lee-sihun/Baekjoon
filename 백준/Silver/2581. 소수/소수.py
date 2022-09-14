def prime_number(x):
    if not x < 2:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


m = int(input())
n = int(input())
num_list = []

for i in range(m, n+1):
    if prime_number(i) == True:
        num_list.append(i)

if len(num_list) != 0:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)
