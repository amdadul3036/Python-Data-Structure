# number_of_same_length_character.py

names = ['Dhrubo' , 'Dhruboish' ,'Amdadul' , 'Poribrritto' , 'Dhrubo' , 'Shakib' , 'Arpa Roy' , 'Roy'  , 'Arun' , 'Amdadul' , 'Oaliullah' , 'Shakib' , 'Jockey' , 'PK']
count = dict()
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)


# OUTPUT
# {'Dhrubo': 2, 'Dhruboish': 1, 'Amdadul': 2, 'Poribrritto': 1, 'Shakib': 2, 'Arpa Roy': 1, 'Roy': 1, 'Arun': 1, 'Oaliullah': 1, 'Jockey': 1, 'PK': 1}
