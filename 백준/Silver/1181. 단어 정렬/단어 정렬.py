import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n):
    word_list.append(sys.stdin.readline().strip())

word_list = list(sorted(set(word_list)))
word_list.sort(key=len)
# print(word_list)
# for i in range(len(word_list)):
#     for j in range(len(word_list)):
#         if len(word_list[i]) < len(word_list[j]):
#             word_list[i], word_list[j] = word_list[j], word_list[i]

for i in word_list:
    print(i)
