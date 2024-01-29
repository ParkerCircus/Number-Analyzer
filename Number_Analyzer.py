name = input("Please enter your name:")
while True:
    x = int(input("Please enter an integer between 1 and 100:"))
    if 1 <= x <= 100:
        if x % 2 != 0 and x < 60:
            print(x, "Odd and less than 60")
        elif x % 2 == 0 and 2 <= x <= 24:
            print("Even and less than 25")
        elif x % 2 == 0 and 26 <= x <= 60:
            print("Even and between 26 and 60 inclusive")
        elif x % 2 == 0 and x > 60:
            print(x, "Even and greater than 60")
        elif x % 2 != 0 and x > 60:
            print(x, "Odd and greater than 60")

        response = input(f"Would you like to enter another integer, {name}?")
        if response == "Yes":
            x = int(input("Please enter an integer between 1 and 100:"))
        elif response == "No":
            print("Thank you", name, ", have a great day!")
        else:
            print("What!?")
        break
