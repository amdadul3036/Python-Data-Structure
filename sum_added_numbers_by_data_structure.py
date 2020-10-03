# sum_added_numbers_by_data_structure.py

total = 0
count = 0
allNumInList = list()

while True:
    num = input("Enter your number: ")
    if num == 'done':
        break
    floatNum = float(num)
    allNumInList.append(floatNum)

sumofYourNumbers = sum(allNumInList)
average = sumofYourNumbers / len(allNumInList)
print(average)
