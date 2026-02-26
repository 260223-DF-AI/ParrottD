# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

import datetime

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """

    contact = {"name": name, "phone": phone, "email": email, "category": category, "created_at": datetime.now()}
    contacts.append(contact)
    return contact
    # TODO: Create a contact dictionary with all fields
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    # TODO: Return the new contact
    pass


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    # TODO: Print table headers
    # TODO: Loop through contacts and print each row
    # TODO: Print footer

    print()
    print("="*45)
    print(f"                CONTACT BOOK ({len(contacts)} contacts)")
    print("="*45)
    print("#  | Name            | Phone         | Category")
    print("---|-----------------|---------------|----------")
    for index,contact in enumerate(contacts):
        print(f"{index+1}  | {contact["name"]} |  {contact["phone"]}  | {contact["category"]}    ")
    pass


def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details

    print("--- Contact Details ---")
    print(f"Name:     {contact["name"]}")
    print(f"Phone:    {contact["phone"]}")
    print(f"Email:    {contact["email"]}")
    print(f"Category: {contact["category"]}")
    print(f"Added:    {contact["created_at"]}")
    pass


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()

    matchedContacts = []
    for contact in contacts:
        if  query.lower() in contact["name"].lower():
            matchedContacts.append(contact)
    return matchedContacts
    pass


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    matchedContacts = []
    for contact in contacts:

        if category == contact["category"]:
            matchedContacts.append(contact)
    return matchedContacts
    pass


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone

    for contact in contacts:
        if phone in contact["phone"]:
            return contact
    return None
    pass


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """

    filteredContact = find_by_phone(contacts, phone)
    if filteredContact == None:
        print("No Contact with that phone number")
        return False
    else:
        for contact in contacts:
            if filteredContact["phone"] == contact["phone"]:
                contact[field] = new_value
                display_contact_details(contact)
    return True
    # TODO: Find contact by phone
    # TODO: Update the specified field
    # TODO: Return success/failure
    pass


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    filteredContact = find_by_phone(contacts, phone)
    if filteredContact == False:
        return False
    else:
        for contact in contacts:
            if filteredContact["phone"] == contact["phone"]:
                contacts.remove(contact)
                return True
    pass


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    # TODO: Count total contacts
    # TODO: Count contacts by category
    # TODO: Find most recently added contact
    print("--- Contact Book Statistics ---")
    print(f"Total Contacts: {len(contacts)}")
    print("By Category")
    print(f" - Friends: {len(filter_by_category(contacts, "friend"))}")
    print(f" - Family: {len(filter_by_category(contacts, "family"))}")
    print(f" - Work: {len(filter_by_category(contacts, "work"))}")
    print(f" - Other: {len(filter_by_category(contacts,"other"))}")
    lastContact = contacts[-1] 
    print(f"Most Recent: {lastContact["name"]} (added {lastContact["created_at"]})")
    pass


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    while True:
            display_menu()
            number = int(input("Enter a command"))
            if number == 1:
                #View all contacts
                display_all_contacts(contacts)
            elif number == 2:
                #add new contact
                print("Enter New Contact")
                name = input("Enter Name")
                phone = input("Enter Phone Number")
                email = input("Enter Email")
                relationship = input("Enter Relationship")
                category = relationship.lower()
                add_contact(contacts, name, phone, email, category)
                print("CONTACT ADDED")
            elif number == 3:
                #search contacts
                searchName = input("Enter Name of Contact")
                searchedContacts = search_by_name(contacts, searchName)
                print("Searched Contacts")
                display_all_contacts(searchedContacts)
            elif number == 4:
                #update contact
                phoneNumber = input("Give phone number of contact you wish to update")
                field = input("The field to update (name, phone, email, or category")
                update = input("What is the updated value")
                update_contact(contacts, phoneNumber, field, update)
            elif number == 5:
                #delete contact
                deleteNumber = input("Give phone number of contact you wish to delete")
                if delete_contact(contacts, deleteNumber) == True:
                    print("Contact Deleted")
                else:
                    print("Contact Not Found")
            elif number == 6:
                #view statistics
                display_statistics(contacts)
            elif number == 0:
                #exit
                break
            else:
                print("Invalid input, try again")

    pass


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    # TODO: Add at least 5 sample contacts
    # add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Bob Smith", "555-987-6543", "bob@work.com", "work")
    add_contact(contacts, "Carol White", "555-456-7890", "carol@family.net", "family")

    # TODO: Test your functions
    # display_all_contacts(contacts)



    # etc.
    
    # STRETCH: Uncomment to run interactive menu
main()
