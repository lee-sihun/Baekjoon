lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()

for i in lst:
    str = str.replace(i, '*')

print(len(str))
