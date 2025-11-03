from .name import Name
from .phone import Phone
from .birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                found = True
                break
        if not found:
            raise ValueError("Old phone number not found")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = ', '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"