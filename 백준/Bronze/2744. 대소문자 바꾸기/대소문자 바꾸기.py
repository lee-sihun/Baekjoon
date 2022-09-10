from curses.ascii import islower, isupper


str = input()
result = ''

for i in str:
    if isupper(i) == True:
        result += i.lower()
        # print(i + "대문자")
    elif islower(i) == True:
        result += i.upper()
        # print(i + "소문자")

print(result)
