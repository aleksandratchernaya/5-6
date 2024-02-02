drinks = ["vodka", "tequila", "rum", "akvavit", "rakia", "arak", "slivovitz"]
try:
    name= input("What is your name?")
    age = input("How old are you?")
    age = int(age)

except ValueError:
    print("Invalid age. Please enter a number.")

else:
    if age>120:
        print("You are too old. You can not play the awesome drinking game.")
    elif age<18:
        print("you are a minot. You can not play the awesome drinking game")
    else:
        print("You are an adult. You can play the awesome drinking game.")
        print("Have some", random.choice(drinks), "and enjoy the game.")