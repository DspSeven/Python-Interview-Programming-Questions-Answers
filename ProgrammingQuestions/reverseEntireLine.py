word = input().split()

reverseEntireWord = ""
new_word = []

for i in word:
    for j in i:
        reverseEntireWord = j.lower() + reverseEntireWord
    new_word.append(reverseEntireWord)
    reverseEntireWord=""
print(' '.join(new_word))
