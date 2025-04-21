#This is my first python program
print("I like Sushi")
print("It's great")

#strings
first_name = "Function"
food = "Sushi"
email = "DaBess@email.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your Email is {email}")

#integer
age = 34
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#float
price = 10.99
gpa = 3.69
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

#boolean
is_student = False
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")

#str(), int(), float(), bool()
name = "Big Man Blastoise"
age = 35
gpa = 3.69
is_student = True

print(type(name))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa) #resolves to 3 if 3.69

age = float(age)
print(age)

age = str(age)
print(age)

name = bool(name)
print(name) #resolves to true

#input

name = input("What is your name? ")
age = int(input("How old are you? "))

age = age + 1

print(f"Hello {name}!")
print(f"You are {age} years old")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area is: {area}cm²") #numlock on; Alt + 0178

item = input("What item would you like to buy?: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity}x {item}/s")
print(f"Your total is: ${total}")

