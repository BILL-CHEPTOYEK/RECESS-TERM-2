#Exercise 1(lists)
print("Exercise 1")

#1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["John", "Mary", "David", "Sarah", "Michael"]
print(names[1])

#2. Write a python program to change the value of the first item to a new value
names = ["John", "Mary", "David", "Sarah", "Michael"]
names[0] = "Bill"
print(names)

#3. Write a python program to add a sixth item to the list
names = ["John", "Mary", "David", "Sarah", "Michael"]
names.append("Emily")
print(names)

#4. Write a python program to add “Bathel” as the 3rd item in your list
names = ["John", "Mary", "David", "Sarah", "Michael"]
names.insert(2, "Bathel")
print(names)

#5. Write a python program to remove the 4th item from the list
names = ["John", "Mary", "Bathel", "David", "Sarah", "Michael"]
names.pop(3)
print(names)

#6. Use negative indexing to print the last item in your list
names = ["John", "Mary", "Bathel", "Sarah", "Michael"]
print(names[-1])

#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
items = [1, 2, 3, 4, 5, 6, 7]
print(items[2:5])

#8. Write a list of countries and make a copy of it.
countries = ["Uganda","USA", "Canada", "UK", "Australia"]
# Using copy() method
countries_copy1 = countries.copy()
# Using slicing
countries_copy2 = countries[:]
print(countries_copy1)
print(countries_copy2)

#9. Write a python program to loop through the list of countries
countries = ["USA", "Canada", "UK", "Australia"]
for country in countries:
    print(country)

#10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["Dog","Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
# Ascending order
animals.sort()
print(animals)
# Descending order
animals.sort(reverse=True)
print(animals)

#11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
animals = ["Dog","Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print(animals_with_a)

#12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["Bill"]
second_names = ["Cheptoyek"]
full_names = first_names + second_names
print(full_names)

# Exercise2 (Tuples)
print("EXERCISE 2")
#1. Consider the tuple below;
#x = (“samsung”, “iphone”, “tecno”, “redmi”) Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[0]
print(favorite_brand)

#2. Use negative indexing to print the 2nd last item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(second_last_item)

#3. Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")
updated_tuple = list(x)
updated_tuple[1] = "itel"
x = tuple(updated_tuple)
print(x)

#4. Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
updated_tuple = list(x)
updated_tuple.append("Huawei")
x = tuple(updated_tuple)
print(x)

#5. Write a python program to loop through the tuple above.
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:
    print(item)

#6. Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
updated_tuple = x[1:]
print(updated_tuple)

#7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(cities)

#8. Write a python program to unpack your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print(brand1)
print(brand2)
print(brand3)
print(brand4)

#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara")
print(cities[1:4])

#10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Mary", "David")
second_names = ("Doe", "Smith", "Johnson")
full_names = first_names + second_names
print(full_names)

#11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print(multiplied_colors)

#12. Return the number of times 8 appears in this tuple
#thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = tuple.count(8)
print(count_8)

# Exercise3 (Sets)
print("EXERCISE 3")
#1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print(beverages)

#2. Use the correct method to add 2 more items to the beverages set.
beverages.add("water")
beverages.add("soda")
print(beverages)

#3. Given the set below;
#mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
#Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# 4. Write a python program to remove “kettle” from the set above.

mySet.remove("kettle")
print(mySet)

#5. Write a python program to loop through the set above.

for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35}
first_names = {"John", "Mary", "David"}
joined_set = ages.union(first_names)
print(joined_set)


# Exercise4 (Strings)
print("EXERCISE 4")
# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
num = 10
text = "Hello"
concatenated = str(num) + text
print(concatenated)

# 2. Consider the example below;
# txt = “ Hello, Uganda! ”
# Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
output = txt.strip()
print(output)

# 3. Write a python program to convert the value of ‘txt’ to uppercase.
txt = "Hello, Uganda!"
uppercase = txt.upper()
print(uppercase)

# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = "Hello, Uganda!"
replaced = txt.replace('U', 'V')
print(replaced)

# 5. Using the code below, write a python program to return a range of characters in the 2nd, rd and 4th position.
#y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)

# 6. The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!”
#Write a python program to correct it.
x = "All \"Data Scientists\" are cool!"
print(x)

# Exercise5 (Dictionaries)
print("EXERCISE 5")
"""
 1. With reference to the dictionary below, write a python program to print the value of the
shoe size.
Add this dictionary to your .py file
Shoes = {
“brand” : “Nick”,
“color” : “black”,
“size” : 40
}
"""
Shoes = {"brand": "Nick", "color": "black", "size": 40}
print(Shoes["size"])


# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)

#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary 
Shoes["type"] = "sneakers"
print(Shoes)

#4. Write a python program to return a list of all the keys in the dictionary above.
keys_list = list(Shoes.keys())
print(keys_list)
#5. Write a python program to return a list of all the values in the dictionary above.
values_list = list(Shoes.values())
print(values_list)
#6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")
#7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, value)
#8. Write a python program to remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)
#9. Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)
#10. Write a dictionary of your choice and make a copy of it.
my_dict = {"key": "value1", "key2": "value2"}
my_dict_copy = my_dict.copy()
print(my_dict_copy)

#11. Write a python program to show nested dictionaries
nested_dict = {
    "person1": {
        "name": "John",
        "age": 25,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "country": "USA"
        }
    },
    "person2": {
        "name": "Jane",
        "age": 30,
        "address": {
            "street": "456 Elm St",
            "city": "London",
            "country": "UK"
        }
    }
}

# Accessing nested dictionary values
print(nested_dict["person1"]["name"])  # Output: John
print(nested_dict["person2"]["address"]["city"])  # Output: London

# Modifying nested dictionary values
nested_dict["person1"]["age"] = 26
nested_dict["person2"]["address"]["country"] = "United Kingdom"

# Adding new key-value pair to a nested dictionary
nested_dict["person1"]["occupation"] = "Engineer"

# Printing the nested dictionary
print(nested_dict)



                               
nest={
    "person": {
        "Bill" : { "title" : "Software engineer", "age" : "90"},
        "Mike"  : { "title" : "Agric officer", "age" : "20"} 
    }
}
print(nest["person"]["Bill"])
