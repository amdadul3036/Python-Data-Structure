dict1 = {
    1:"JavaScript",
    2:"ReactJS",
    3:"NodeJS",
    4:"Python",
    5:"MongoDB",
    5:"Django",
    "1st Learn": "C Programming",
    "Then go": "Where you want to go..."
}


# 1:"JavaScript" --- Here 1 is called key and "JavaScript" is called value

print(dict1)
# It will print the whole dictionary.


print(dict1[1])
# It will print "JavaScript"; So numbering of Dictionary starts from 1


dict1[3] ="ES6"
print(dict1)
# Thus we can change the value of dictionary . 


# We can add new element inside the dictionary 
dict1[6] = "Ruby"
print(dict1)


# We can delete the element of dictionary
del dict1[2]
print(dict1)

# OR

dict1.pop(1)
print(dict1)


# We can print only keys of the dictionary. 

print("Here is the keys: " , dict1.keys())


# We can print the values of the dictionary. 
print("Here is the values: " , dict1.values())




# We can get all key values in a list under tuple by using items function
print("Here is the dictionary Items: " , dict1.items())