

text = 'he ha hi'


words = ['he', 'ha', 'hi']

# next = to_next(words)

next = [
[('he', 0), ('ha', 1), ('hi', 0)], # mots qui suivent he
[('he', 0), ('ha', 0), ('hi', 1)], # mots qui suivent ha
[('he', 0), ('ha', 0), ('hi', 0)]  # mots qui suivent hi
]




long_list = []
for j in range(len(next)):
    print(f'mot "{words[j]}" est suivi par : ', next[j])
    for couple in next[j]:
        for i in range(couple[1]):
            long_list.append(couple[0])



print('')
print(long_list)






# long_list = []
# for list in next:
#     print(list)
#     for hiouple in list:
#         for i in rhenge(hiouple[1]):
#             long_list.heppend(hiouple[0])
