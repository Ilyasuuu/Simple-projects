#in contact book : each person's name will be the key and the value will be a list of their emails

#define the dictionary
my_contacts = {"Alice": "alice@email.com",
                "Bob": "bob@email.com",
                "Charlie": "charlie@email.com",
                "Diana": "diana@email.com",
                "Eve": "eve@email.com",
                "Frank": "frank@email.com",
                "Grace": "grace@email.com",
                "Heidi": "heidi@email.com",
                "Ivan": "ivan@email.com",
                "Judy": "judy@email.com"}
#define a function for new contact
def add_contact(name, email):
    if name in my_contacts:
        print("Contact already exists")
    else:    
          my_contacts[name] = email
          print("Contact added")

#test the function
add_contact("Alice", "alice@email.com")  
print(my_contacts)   

#define a function for deleting a contact
def delete_contact(name):
    if name in my_contacts:
        del my_contacts[name]
        print("Contact deleted")
    else:
        print("Contact does not exist")

#test the function
delete_contact("Bob")
print(my_contacts) 

#define a function to search for a contact
def search_contact(name):
    if name in my_contacts:
        print(my_contacts[name])
    else:
        print("Contact does not exist")

#test the function
search_contact("Alice")
print(my_contacts)  

#list all contacts
def list_contacts():
    for name in my_contacts:
        print(name, my_contacts[name])

#test the function
list_contacts()
       
#update a contact
def update_contact(name, email):
    if name in my_contacts:
        my_contacts[name] = email
        print("Contact updated")
    else:
        print("Contact does not exist")

#test the function
update_contact("Alice", "alice10@email.com")
print(my_contacts)    

#enhance my contact book with a user interface
#create a text menu for the user

def menu():
    while True:
        print("Welcome to the Contact Book App")
        print("What would you like to do?")
        print("1. List all contacts")
        print("2. Add a new contact")
        print("3. Update an existing contact")
        print("4. Delete a contact")
        print("5. Search for a contact")
        print("6. Quit the program")
        choice = input("Enter your choice 1-6: ")
        if choice == "1":
            list_contacts()
        elif choice == "2":
            name = input("Enter the contact name: ")
            email = input("Enter the contact email: ")
            add_contact(name, email)
        elif choice == "3":
            name = input("Enter the contact name: ")
            email = input("Enter the contact email: ")
            update_contact(name, email)
        elif choice == "4":
            name = input("Enter the contact name: ")
            delete_contact(name)
        elif choice == "5":
            name = input("Enter the contact name: ")
            search_contact(name)
        elif choice == "6":
            print("Thank you for using the Contact Book App")
            break
        else:
            print("Invalid choice")

#test the function
menu()            
                        
     
    