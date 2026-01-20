contact_book = {}
while True:
    print("----- Contact Management System -----")
    print("1 Add New Contact")
    print("2 Show All Contacts")
    print("3 Find Contact")
    print("4 Remove Contact")
    print("5 Exit")
    user_choice = input("Select an option: ")
    if user_choice == "1":
        person_name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email_id = input("Enter email id: ")
        home_address = input("Enter address: ")
        contact_book[person_name] = {
            "phone": phone_number,
            "email": email_id,
            "address": home_address
        }
        print("Contact saved successfully")

    elif user_choice == "2":
        if not contact_book:
            print("No contacts available")
        else:
            for name in contact_book:
                print(name, "-", contact_book[name]["phone"])
    elif user_choice == "3":
        search_name = input("Enter name to search: ")

        if search_name in contact_book:
            data = contact_book[search_name]
            print("Phone:", data["phone"])
            print("Email:", data["email"])
            print("Address:", data["address"])
        else:
            print("Contact not found")
    elif user_choice == "4":
        delete_name = input("Enter name to delete: ")

        if delete_name in contact_book:
            del contact_book[delete_name]
            print("Contact removed")
        else:
            print("Contact does not exist")
    elif user_choice == "5":
        print("Exiting program")
        break
    else:
        print("Please enter a valid option")
