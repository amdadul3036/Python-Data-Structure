lucky_numbers = [3,543,4,1,359,7,34,77,38,97]
friends = ["Dhrubo" , "Amdadul" , "Dhruboish" , "Kaosar" , "Tasnim" , "Dhruboish"]


print(lucky_numbers)
print(friends)


# Find the maximum value using max()
print(max(lucky_numbers))


# Find the minimum value using min()
print(min(lucky_numbers))


# Find sum of the numbers using sum() 
print(sum(lucky_numbers))

# Sort the values from min to max using sorted()
print(sorted(lucky_numbers))
# But actual list will not change
print("Prove that sorted function cannot change actual lucky number list: ", lucky_numbers)

# If we want to change the actual list then we should use sort function
lucky_numbers.sort()
# By default it will sort from min to max 
print("Actual lucky numbers sorting: " , lucky_numbers)


# If we want to sort max to min...
lucky_numbers.sort(reverse=True)
print("reverse = True : " , lucky_numbers)


# Make Multidimensional Array from 2 function. 
multi = [friends , lucky_numbers]
print(multi)



# Adding lucky_numbers after all elements of friends 
friends.extend(lucky_numbers)
print(friends)



# append() will add element at last of the list ; but it will add only 1 element
friends.append("Momin")
print(friends)



# You can insert in any index number position by using .insert function 
friends.insert(2,"Chagol Beda")
# That is I want to add "Chagol Beda" in index 2 
print(friends)


# We can append and extend more than one element but ....
# Append will add them as a tuple. And extend will add them as normal list elements
friends.append(("a","b","c",1))
print("Appending multiple element in a list:" , friends)

friends.extend(("a","b","c",1))
print("Appending multiple element in a list:" , friends)


# Remove element by useing function .remove(str)
friends.remove("Momin")
print(friends)
# remove() takes exactly one argument



# Remove only last element of the list using .pop() function 
friends.pop()
print(friends)



# Know how many times an element have in a list 
print(friends.count("Dhruboish"))

# .reverse() will reverse the list 
friends.reverse()
print(friends)


# We can copy a list in another list using .copy function
new_friends = friends.copy()
print(new_friends)



# We can clear all elements from a list using .clear()
friends.clear()
print(friends)
# It will give an empty list 




