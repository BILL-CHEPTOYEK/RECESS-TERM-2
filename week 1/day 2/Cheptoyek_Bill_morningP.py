#for loop
set1={"rice", "matooke", "irish"}
for set in set1:
    print(set)

#while loop
minutes = 10
while minutes > 0:
    print(f"Time remaining: {minutes} minutes")
    minutes -= 1
print("Time's up!")

#break and continue statements
#break
x=0
while x<10:
    x+=1
    if x==5:
        break
    print(x)

#continue 
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)

print("Loop ended.")


# used to handle exceptions and perform error handling.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No exceptions were raised.")
finally:
    print("This is the finally block. It always executes.")

#Dict
emotions= {
    1:"normal",
    2: "unwell",
    3: "i don't know"       
}

# write a program to ask students to ask students about there mental health

mental_strength = {
    1: "You are unwell and may require immediate support.",
    2: "You are facing significant challenges and may need assistance.",
    3: "You are struggling and should consider seeking help.",
    4: "You are experiencing difficulties and should prioritize self-care.",
    5: "You are holding up reasonably well.",
    6: "You are doing fine and managing your mental well-being.",
    7: "You are in good shape mentally.",
    8: "You are strong and resilient.",
    9: "You are very resilient and have excellent mental strength.",
    10: "You are exceptionally strong mentally. Keep it up!"
}

# Set the number of students to rate
num_students = 5
# Initialize an empty dictionary to store the mental health ratings
student_ratings = {}

# Iterate over the range of students and ask for their mental health rating
for i in range(num_students):
    print(f"Rating for Student #{i+1}")
    rating = int(input("Rate your mental health on a scale of 1 to 10: "))
    student_ratings[f"Student #{i+1}"] = rating

# Print the mental health information based on the ratings
print("\nMental Health Information:")
for student, rating in student_ratings.items():
    if rating in mental_strength:
        info = mental_strength[rating]
        print(f"{student}: {info}")
    else:
        print(f"{student}: Invalid rating entered.")
