name = input("Enter your name: ")
month = input("Enter your birth month: ")

this_month = "january"

print("Hey, " + name + "!")
print("Your name is " + str(len(name)) + " characters long.")

if month.lower() == this_month:
    print("Happy Birthday month!")