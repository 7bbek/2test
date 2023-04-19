# Creating an empty dictionary
phoneDirectory = {}

# Displaying the menu
print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n")
print("1. Add a record\n2. Search a record\n3. Change a record\n4. Delete a record\n5. Quit")

# Loop to continuously ask for user input until they choose to quit
while True:
    choice = input("\nEnter your choice: ")

    # Option 1: Add a record
    if choice == '1':
        name = input("\nEnter name: ")
        phone = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record added\n")

    # Option 2: Search a record
    elif choice == '2':
        name = input("\nEnter name to search: ")
        if name in phoneDirectory:
            print(name + ": " + phoneDirectory[name])
        else:
            print("Record not found\n")

    # Option 3: Change a record
    elif choice == '3':
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            phone = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = phone
            print("Record updated\n")
        else:
            print("Record not found\n")

    # Option 4: Delete a record
    elif choice == '4':
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted\n")
        else:
            print("Record not found\n")

    # Option 5: Quit the program
    elif choice == '5':
        break

    # Invalid input
    else:
        print("Invalid input. Please enter a valid option.\n")

