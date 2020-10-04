# count_with_dictionary.py

names = ['Dhrubo' , 'Dhruboish' , 'Amdadul' , 'Oaliullah' , 'Shakib' , 'Jockey' , 'PK']

dict = {}
for name in names:
    key = len(name)
    if key not in dict:
        dict[key] = []
    dict[key].append(name)
        
print(dict)