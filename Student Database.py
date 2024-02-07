list1 = ["Andy", "Beth", "Will", "Hope"]
list2 = ["Houston", "Chicago", "Boston", "Austin"]
list3 = ["Chili", "Pizza", "Lasagna", "Steak"]
ID = int(input("What student would you like to learn more about (enter a number from 1-4): "))
while True:
    while True:
        if 1 <= ID <= len(list1):
            print(list1[ID-1])
            break
        else:
            ID = int(input("Please enter a valid number: "))

    next = input("Which category would you like to display next: 'hometown' or 'favorite food'? ")
    while True:
        if next == "hometown":
            print(f"{list1[ID-1]}'s hometown is {list2[ID-1]}")
            break
        elif next == "favorite food":
            print(f"{list1[ID-1]}'s favorite food is {list3[ID-1]}")
            break
        else:
            next = input("Please enter 'hometown' or 'favorite food' ")

    answer = input("Would you like to learn about another student? (yes or no) ")

    if answer == "yes":
        ID = int(input("What student would you like to learn more about (enter a number from 1-4): "))
    else:
        print("Thank you!")
        break

