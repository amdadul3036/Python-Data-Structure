# all_words_of_a_text.py

counts = dict()
line = input("Input the text lines here: ")
# print("Input the text lines here: ")
# line = input('')

words = line.split()
print('Words: ' , words)


print('Continuing...')
for word in words:
    counts[word] = counts.get(word,0) + 1
for word in words:
    print(word)
print("Counts: " , counts)