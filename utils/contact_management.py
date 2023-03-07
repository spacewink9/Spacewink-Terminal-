import csv

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone})"
    
class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, email, phone):
        contact = Contact(name, email, phone)
        self.contacts.append(contact)
        print("Contact added successfully!")
    
    def remove_contact(self, email):
        for contact in self.contacts:
            if contact.email == email:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found.")
    
    def list_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
            return
        print("List of contacts:")
        for contact in self.contacts:
            print(contact)
    
    def save_contacts(self, filename):
        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['name', 'email', 'phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'name': contact.name, 'email': contact.email, 'phone': contact.phone})
        print(f"Contacts saved to {filename} successfully!")
    
    def load_contacts(self, filename):
        with open(filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.add_contact(row['name'], row['email'], row['phone'])
        print(f"Contacts loaded from {filename} successfully!")
