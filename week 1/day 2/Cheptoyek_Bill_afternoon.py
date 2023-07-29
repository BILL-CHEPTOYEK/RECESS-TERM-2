# Convert from integer to a float
integer_value = 42
float_value = float(integer_value)

print(float_value)

#float to complex
complex_value=complex(float_value)
print(complex_value)

#casting
#doesn't wrk with complex numbers
h=int(20)
print(h)
a=int(4)
print(a)
print(type(a))

#Dictionaries
#ordered, changeable but do not allow duplicates
myphone={
    "myName": "Bill",
    "phone": "Samsung S20",
    "model": "Samsung",
    "SerialNo": 7657855768
}
print(myphone)
print(len(myphone))
z=myphone["phone"]
print(z)
#input what you need to know
info=str(input("What do you need to know:"))
output=myphone[info]
print(output)

# dict 
# Exercise one: use the values method to return a list of all values in the 

student_scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}
scores_list = list(student_scores.values())
print(scores_list)

# Exercise two: Check if a key does exit in your dictionary
key="Bob"
if key in student_scores:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")

#Exercise three: Give an example on how to change dictionary items, How to update
#changing dictionary values(consider the dictionary student_scores)
student_scores["Alice"]=95
student_scores["Charlie"]=78
print(student_scores)
#updating the dictionary
# Define a sample dictionary

print("Original Dictionary:")
print(student_scores)

         # Update the dictionary with new key-value pairs
student_scores.update({"Bob": 95, "Frank": 87})

         # Print the updated dictionary
print("\nUpdated Dictionary:")
print(student_scores)

#Exercise four: Give an example how to add dictionary items, how to remove dictionary items.
#add an item to the dictionary
student_scores["Bill"]=99

# Remove an item from the dictionary
del student_scores["Bob"]
print(student_scores)


# Exercise five: Give an example on how you can loop through a dictionary and also how to nest dictionaries

# Loop through the dictionary using a for loop
print("Looping through the dictionary:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

#nesting dictionaries
student_records = {
    "Alice": {
        "Math": 85,
        "Science": 92,
        "English": 88
    },
    "Bob": {
        "Math": 90,
        "Science": 78,
        "English": 82
    },
    "Charlie": {
        "Math": 78,
        "Science": 85,
        "English": 90
    }
}
print(student_records["Alice"]["Math"]) 
print(student_records["Bob"]["Science"])
print(student_records["Charlie"]["English"])  


# use a condition to show how to use 
x = 5
y = 10
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")
