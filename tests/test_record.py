import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.record import Record

def test_add_phone():
    record = Record("John")
    record.add_phone("1234567890")
    assert len(record.phones) == 1
    assert record.phones[0].value == "1234567890"
    print("✓ test_add_phone passed")

def test_remove_phone():
    record = Record("John")
    record.add_phone("1234567890")
    record.remove_phone("1234567890")
    assert len(record.phones) == 0
    print("✓ test_remove_phone passed")

def test_edit_phone():
    record = Record("John")
    record.add_phone("1234567890")
    record.edit_phone("1234567890", "0987654321")
    assert record.phones[0].value == "0987654321"
    print("✓ test_edit_phone passed")

def test_add_birthday():
    record = Record("John")
    record.add_birthday("15.12.1990")
    assert record.birthday is not None
    assert record.birthday.value.strftime("%d.%m.%Y") == "15.12.1990"
    print("✓ test_add_birthday passed")

if __name__ == "__main__":
    test_add_phone()
    test_remove_phone()
    test_edit_phone()
    test_add_birthday()
    print("All record tests passed!")