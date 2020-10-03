# sum_added_numbers.py

total = 0
count = 0

while True:
    num = input("Enter your number: ")
    if num == 'done':
        break
    floatNum = float(num)
    total += floatNum
    count+=1
    
average = total/count
print(average)