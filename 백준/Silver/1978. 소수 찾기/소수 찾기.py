n = int(input())
num = map(int, input().split())
cnt = 0


def prime_numver(x):
    if not x < 2: 
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


for i in num:
    if prime_numver(i) == True:
        cnt += 1

print(cnt)
