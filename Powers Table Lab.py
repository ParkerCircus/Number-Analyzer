while True:
    x = int(input("Enter an integer:"))
    y = range(1,x+1)
    operation = ["Number", "Squared", "Cubed"]
    dash = ["="*6, "="*7, "="*5]
    print(operation)
    print(dash)
    for num in y:
        print("   ", num, "        ", num*num, "        ", num*num*num)
    response = input("Would you like to continue?")
    if response != "Yes":
     print("Thank you!")
     break