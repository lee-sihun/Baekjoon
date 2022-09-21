import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n = list(range(1, n+1))
cnt = k-1
result = []

for i in range(len(n)):
    # if cnt > len(n):
    #     cnt = cnt - len(n)
    # if cnt == len(n):
    #     cnt = 0
    while cnt >= len(n):
        cnt = cnt - len(n)
        if cnt == len(n):
            cnt = 0
            # print(result,cnt,len(n),n)
            break
        # print(result,cnt,len(n),n)


    result.append(n[cnt])
    del n[cnt]
    cnt += k-1
    # print(result,cnt,len(n),n)

print('<'+str(result)[1:-1]+'>')

# cnt 2 / 3
# 1 2 3 4 5 6 7

# cnt 4 / 3 6
# 1 2 4 5 6 7

# cnt 6 / 3 6
# 1 2 4 5 7
