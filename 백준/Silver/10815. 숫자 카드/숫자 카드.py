import sys
input = sys.stdin.readline


def binary_search(target, num, first, last):
    if first > last:
        return -1

    mid = (first + last) // 2
    if num[mid] == target:
        return 1
    elif num[mid] > target:
        last = mid - 1
    else:
        first = mid + 1

    return binary_search(target, num, first, last)


n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

n_num.sort()

for i in m_num:
    if binary_search(i,n_num,0,len(n_num)-1) == 1:
        print(1,end=' ')
    else:
        print(0,end=' ')
