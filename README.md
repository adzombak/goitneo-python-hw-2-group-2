# goitneo-python-hw-2-group-2

## Task #1:
Commands:

- add [name] [phone]: Add a new contact.
- change [name] [phone]: Change the phone number of an existing contact.
- phone [name]: Retrieve the phone number of a specific contact.
- all: View all contacts in the contact list.
- hello: Receive a friendly greeting.
- exit or close: Terminate the contact assistant.


## Task #2:

**Structure:**
1) Field: A base class providing basic functionality for Name and Phone
2) Name: A subclass of Field containing a person's name.
3) Phone: A subclass of Field containing a person's phone number. The Phone class validates that the phone number consists of exactly 10 digits.
4) Record: This class represents a unique person's details that include Name and a list of Phone records. Provides methods for adding, removing, editing, and finding a Phone number.
5) AddressBook: Again, this class is a dictionary-like container specifically designed for subclassing, and it manages all the Record objects.