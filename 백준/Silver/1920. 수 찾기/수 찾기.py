import sys
input = sys.stdin.readline

n = int(input())
a_num = set(map(int,input().split()))
m = int(input())
m_num = list(map(int,input().split()))

for i in m_num:
    if i in a_num:
        print(1)
    else:
        print(0)  

