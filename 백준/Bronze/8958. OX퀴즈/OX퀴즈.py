n = int(input())
for i in range(n):
    str = input()
    str_list = list(str)
    score = 0
    num = 0

    for i in str_list:
        if i == 'O':
            score += num + 1
            num += 1
        else:
            num = 0
    print(score)
