import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    str = list(input())
    cnt = 0

    for j in str:
        if j == "(":
            cnt += 1
        elif j == ")":
            cnt -= 1
        if cnt < 0:
            print('NO')
            break

    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print('YES')
