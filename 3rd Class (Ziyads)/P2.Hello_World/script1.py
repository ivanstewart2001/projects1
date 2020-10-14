#Ask user for name

name = input("What is your name?: ")

#Ask user for age

age = input("What is your age?: ")

#Ask user for city

city = input("What city fo you live in: ") 

#Ask user what they enjoy

enjoy = input("What do you enjoy doing?: ")

#Create output text

output = "Hello {}. You are {} years old. You live in {} and you enjoy {}. Nice to meet you!".format(name, age, city, enjoy)

#Print output to screen

print(output)