name = input("what is your name?")
age = input("How old are you?")
try:
    age = int(age)
    birth_year = 2024 - age
    print(name, ", you were born in", birth_year, ".", sep="")
    number = input("give me a number to divide the age")
    number = int(number)
    print(age/number)

except ValueError:
    print("Invalid age. Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("No exceptions were raised.")
finally:
    print("thank you for playing")