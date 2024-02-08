while True:
    students = [{"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}]

    def get_new_student():
        new_name = input("Enter the student's name: ")
        new_hometown = input("Enter the student's hometown: ")
        new_favorite_food = input("Enter the student's favorite food: ")
        new_student = {"name": new_name,
                       "hometown": new_hometown,
                       "favorite_food": new_favorite_food}
        return new_student

    def list_names(students):
        count = 0
        for key in students:
            count +=1
            print(f"{count}. {key['name']}")
    options = input("Would you like to 'add', 'view', or 'quit' the student options? ")

    if options == "add":
        get_new_student()
    elif options == "view":
        list_names(students)
        select = int(input("What student would you like to select: "))
        print(f"You selected {students[select-1]['name']}.")
        select2 = input("Would you like to see their hometown or favorite food? ")
        if select2 == "hometown":
            print(f"{students[select-1]['name']}'s hometown is {students[select-1]['hometown']}.")
        elif select2 == "favorite food":
            print(f"{students[select-1]['name']}'s favorite food is {students[select-1]['favorite_food']}.")
    elif options == "quit":
        print("Thank you!")
        break
    else:
        options = input("Invalid response. Please enter 'add', 'view', or 'quit'.")
