import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.address_book import AddressBook
from models.record import Record

def test_add_record():
    book = AddressBook()
    record = Record("John")
    record.add_phone("1234567890")
    book.add_record(record)
    assert "John" in book.data
    print("✓ test_add_record passed")

def test_find_record():
    book = AddressBook()
    record = Record("John")
    book.add_record(record)
    found = book.find("John")
    assert found is not None
    assert found.name.value == "John"
    print("✓ test_find_record passed")

def test_delete_record():
    book = AddressBook()
    record = Record("John")
    book.add_record(record)
    book.delete("John")
    assert "John" not in book.data
    print("✓ test_delete_record passed")

if __name__ == "__main__":
    test_add_record()
    test_find_record()
    test_delete_record()
    print("All address book tests passed!")