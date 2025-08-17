# Task 5: Contact Book

# What?
# Add, view, search, delete contacts. 
contacts = {}
def add_contact():
    name = input("Enter name:")
    phone = input("Enter phone:")
    email = input("Enter email:")
    contacts[name] = {"phone": phone, "Email": email}
    print("contact added.")
def view_contacts():
    for name, info in contacts.items():
        print(f"{name} -> phone: {info['phone']}, Email: {info['Email']}")
def search_contact():
    name = input("Enter name to search:")
    if name in contacts:
        
        print(name, contacts[name])
    else:
        print("Not found.") 
def delete_contact():
    name = input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("Deleted.") 
    else:
        print("Not found.")                      
while True:
    print("\n-- contact book ---")
    print("1. Add contact\n2. view contacts\n3. search contact\n4. Delete contact\n5. Exit")
    choice = input("Enter choice:")
    if choice == "1":
          add_contact()
    elif choice == "2":
         view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break    
    else:
        print("Invalid choice.")


