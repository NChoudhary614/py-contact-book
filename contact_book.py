# contact_book.py
import os

# Constants
CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """Load all contacts from the text file"""
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:  # Skip empty lines
                        # Split each line into contact details
                        details = line.split(',')
                        if len(details) >= 4:  # Make sure we have all fields
                            contacts.append({
                                'name': details[0],
                                'phone': details[1],
                                'email': details[2],
                                'address': details[3] if len(details) > 3 else ""
                            })
        except Exception as e:
            print(f"Error loading contacts: {e}")
    return contacts

def save_contacts(contacts):
    """Save all contacts to the text file"""
    try:
        with open(CONTACTS_FILE, 'w') as file:
            for contact in contacts:
                # Escape commas in fields if any
                name = contact['name'].replace(',', ';')
                phone = contact['phone'].replace(',', ';')
                email = contact['email'].replace(',', ';')
                address = contact['address'].replace(',', ';')
                
                line = f"{name},{phone},{email},{address}\n"
                file.write(line)
        return True
    except Exception as e:
        print(f"Error saving contacts: {e}")
        return False

def add_contact():
    """Add a new contact"""
    print("\n" + "=" * 30)
    print("ADD NEW CONTACT")
    print("=" * 30)
    
    # Get contact details from user
    name = input("Enter name: ").strip()
    
    # Validate input
    if not name:
        print("Error: Name is required!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    # Load existing contacts
    contacts = load_contacts()
    
    # Add new contact
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    
    # Save updated contacts
    if save_contacts(contacts):
        print(f"\nContact '{name}' added successfully!")
    else:
        print("\nFailed to save contact!")

def view_contacts():
    """View all contacts"""
    print("\n" + "=" * 30)
    print("ALL CONTACTS")
    print("=" * 30)
    
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts found.")
        return
    
    print(f"Total contacts: {len(contacts)}\n")
    
    # Display each contact with numbering
    for i, contact in enumerate(contacts, 1):
        print(f"Contact #{i}")
        print(f"  Name:    {contact['name']}")
        print(f"  Phone:   {contact['phone']}")
        print(f"  Email:   {contact['email']}")
        print(f"  Address: {contact['address']}")
        print("-" * 30)

def search_contacts():
    """Search for contacts by name or phone"""
    print("\n" + "=" * 30)
    print("SEARCH CONTACTS")
    print("=" * 30)
    
    search_term = input("Enter name or phone number to search: ").strip().lower()
    
    if not search_term:
        print("Please enter a search term.")
        return
    
    contacts = load_contacts()
    found_contacts = []
    
    # Search through all contacts
    for contact in contacts:
        if (search_term in contact['name'].lower() or 
            search_term in contact['phone'].lower()):
            found_contacts.append(contact)
    
    # Display results
    if found_contacts:
        print(f"\nFound {len(found_contacts)} contact(s):\n")
        
        for i, contact in enumerate(found_contacts, 1):
            print(f"Contact #{i}")
            print(f"  Name:    {contact['name']}")
            print(f"  Phone:   {contact['phone']}")
            print(f"  Email:   {contact['email']}")
            print(f"  Address: {contact['address']}")
            print("-" * 30)
    else:
        print(f"\nNo contacts found with '{search_term}'")

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("       CONTACT BOOK APPLICATION")
    print("=" * 40)
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search contacts")
    print("4. Exit")
    print("=" * 40)

def main():
    """Main function to run the contact book application"""
    print("Welcome to the Command-Line Contact Book!")
    print("Your contacts are stored in 'contacts.txt' file.\n")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                add_contact()
            elif choice == '2':
                view_contacts()
            elif choice == '3':
                search_contacts()
            elif choice == '4':
                print("\nThank you for using Contact Book. Goodbye!")
                break
            else:
                print("\nInvalid choice! Please enter a number between 1 and 4.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Check if this script is being run directly
if __name__ == "__main__":
    main()