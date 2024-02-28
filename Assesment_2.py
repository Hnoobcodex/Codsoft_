class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        if not results:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for result in results:
                print(f"Name: {result.name}, Phone: {result.phone_number}")

    def update_contact(self, name):
        contact = next((c for c in self.contacts if c.name.lower() == name.lower()), None)
        if contact:
            print(f"Enter new details for {contact.name}:")
            contact.phone_number = input("Phone Number: ")
            contact.email = input("Email: ")
            contact.address = input("Address: ")
            print(f"Contact {contact.name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        contact = next((c for c in self.contacts if c.name.lower() == name.lower()), None)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact {contact.name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            contact_book.view_contact_list()

        elif choice == "3":
            keyword = input("Enter Name or Phone Number to search: ")
            contact_book.search_contact(keyword)

        elif choice == "4":
            name = input("Enter Name of contact to update: ")
            contact_book.update_contact(name)

        elif choice == "5":
            name = input("Enter Name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
