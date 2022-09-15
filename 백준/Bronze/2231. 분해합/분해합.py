n = int(input())
create = 0

for i in range(1, n+1):
    num = list(map(int,str(i)))
    num.append(i)
    create = sum(num)
    
    if create == n:
        print(i)
        break
    if i == n:
        print(0)
     




