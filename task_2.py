from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone=""):
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone")
        super().__init__(phone)

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            print("No such phone number found")

    def edit_phone(self, old_phone, new_phone):
        try:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        except ValueError:
            print("Can't edit non existent phone number")

    def find_phone(self, phone):
        if phone in self.phones:
            return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone for phone in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        return next((record for record in self.data.values() if record.name.value == name), None)

    def delete(self, name):
        del self.data[name]
