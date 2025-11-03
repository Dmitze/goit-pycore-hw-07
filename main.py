from models.address_book import AddressBook
from models.record import Record

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Invalid command format."
    return wrapper

def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args

@input_error
def add_contact(args, book):
    if len(args) < 2:
        return "Give me name and phone please."
    
    name = args[0]
    phone = args[1]
    
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    
    record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    if len(args) < 3:
        return "Give me name, old phone and new phone please."
    
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    
    record = book.find(name)
    if record is None:
        return "Contact not found."
    
    record.edit_phone(old_phone, new_phone)
    return "Phone number updated."

@input_error
def show_phone(args, book):
    if len(args) < 1:
        return "Enter contact name please."
    
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    
    phones = [phone.value for phone in record.phones]
    return f"{name}: {', '.join(phones)}"

@input_error
def show_all(book):
    if not book.data:
        return "No contacts saved."
    
    result = []
    for record in book.data.values():
        result.append(str(record))
    return "\n".join(result)

@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return "Give me name and birthday please."
    
    name = args[0]
    birthday = args[1]
    
    record = book.find(name)
    if record is None:
        return "Contact not found."
    
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    if len(args) < 1:
        return "Enter contact name please."
    
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    
    if record.birthday is None:
        return f"{name} doesn't have birthday set."
    
    return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"

@input_error
def show_birthdays(book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in next week."
    
    result = ["Upcoming birthdays:"]
    for item in upcoming:
        result.append(f"{item['name']}: {item['congratulation_date']}")
    return "\n".join(result)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()