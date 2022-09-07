def d(num):
    num_list = [int(a) for a in str(num)]
    return num_list

# 한수 : 한자리, 두자릿 수 전부 포함
# 구하는 방법 : 첫째자리 - 둘째자리 = 둘째자리 - 셋째자리


n = int(input(''))
han = 0

for i in range(1, n+1):
    if i < 100:
        han += 1
    else:
        num = d(i)
        if num[0] - num[1] == num[1] - num[2]:
            han += 1
print(han)
