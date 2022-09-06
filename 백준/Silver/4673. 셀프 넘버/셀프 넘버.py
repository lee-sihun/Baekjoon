def d(num):
    result = num
    while num > 0:
        result += num % 10
        num //= 10
    return result


# 셀프넘버 = 생성자가 없는 수
all_num = set(range(1, 10001))
not_self = set()

for i in range(1, 10001):
    num = d(i)
    if num <= 10000:
        not_self.add(num)

self_num = sorted(all_num - not_self)

for i in self_num:
    print(i)
