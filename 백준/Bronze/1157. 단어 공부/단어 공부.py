text = list(input('').lower())
# lst = [0 for i in range(len(text))]
dic = {}
for i in range(len(text)):
    dic.setdefault(text[i], 0)

for j in text:
    if j in dic:
        # dic.update(j=1)
        dic[j] += 1

# lst = list(sorted(dic.items(), reverse=True))
# print(lst[0])

list_keys = list(dic.keys())
list_values = list(dic.values())
key = ''
num = 0

for k in range(0, len(list_values)):
    if num < list_values[k]:
        num = list_values[k]
        key = list_keys[k]
    elif num == list_values[k]:
        key = '?'

print(key.upper())
