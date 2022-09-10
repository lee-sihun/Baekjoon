num = list(map(int, input().split()))
cnt = 0
for i in num:
    cnt += i * i

print(cnt%10)
