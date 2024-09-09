contacts = {}

def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[phone] = {
        'name': name,
        'email': email,
        'address': address
    }
    print(f"Contact for {name} added successfully!\n")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for phone, details in contacts.items():
            print(f"Name: {details['name']}, Phone: {phone}")
    else:
        print("\nNo contacts available.\n")
    print()

def search_contact():
    search = input("Enter name or phone number to search: ").strip().title()
    found = False
    for phone, details in contacts.items():
        if search in details['name'] or search == phone:
            print(f"\nFound Contact: Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}\n")
            found = True
            break
    if not found:
        print("\nContact not found.\n")

def update_contact():
    phone = input("Enter the phone number of the contact to update: ").strip()
    if phone in contacts:
        print(f"\nUpdating contact for {contacts[phone]['name']}...\n")
        contacts[phone]['name'] = input("Enter new name: ").strip().title()
        contacts[phone]['email'] = input("Enter new email: ").strip()
        contacts[phone]['address'] = input("Enter new address: ").strip()
        print("Contact updated successfully!\n")
    else:
        print("\nContact not found.\n")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ").strip()
    if phone in contacts:
        print(f"\nDeleting contact for {contacts[phone]['name']}...\n")
        del contacts[phone]
        print("Contact deleted successfully!\n")
    else:
        print("\nContact not found.\n")

def user_interface():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.\n")

user_interface()
