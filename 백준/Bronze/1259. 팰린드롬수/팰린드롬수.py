while True:
    num = int(input())
    if num == 0:
        break

    num = list(str(num)) 
    if num == num[::-1]:
        print('yes')
    else:
        print('no')