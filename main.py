from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f'checking {record.name.value}')
        print(f'checking {self.data[record.name.value]}')
    
    def find(self, record, name):
        print
        if record.name.value == name:
            return self.data[record.name.value]  

    def delete(self, record):
        pass

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(phone.number)
        

    def edit_phone(self, phone_old, phone_new): 
        index = self.phones.index(phone_old)
        self.phones[index] = phone_new
    

    def remove_phone(self, phone):
        self.phones.remove(phone)
    
    def find_phone(self, name, phone):
        pass
        #13task
    
    def __str__(self):
        return f"Name: {self.name.value}, Phones: {', '.join(str(phone) for phone in self.phones)}"


class Field:
    def __init__(self, value = None):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        if self.is_valid(new_value):
            self._value = new_value
        else:
            raise ValueError("Invalid field value")
    def is_valid(self, value):
        return bool(value.strip())

class Name(Field):

    def __init__(self, value):
        self.value = value
        #print(self.value)

    def is_valid(self, value):
        return value is not None and value.isalpha() and value.strip()
    
    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, number):
        self.number = number
        
    def is_valid(self, value):
        return value is not None and len(value) == 10
    
    def __str__(self):
        return self.number


#phone_book = {} #We use adr_book instance of AdressBook class instead

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid input. Please enter name and phone number."
        except IndexError:
            return "Error: You don't have any contacts yet."
    return inner

    
@input_error
def add_contact(adr_book, name, phone):
    name_u = Name(name)
    phone_u = Phone(phone)

    if name_u.is_valid(name) and phone_u.is_valid(phone):
        if name in adr_book.data:
            existing_record = adr_book.data[name]
            existing_record.add_phone(phone_u)
        else:
            record = Record(name_u)
            
            record.add_phone(phone_u)
            adr_book.add_record(record)
            print(adr_book.data)
            print(adr_book.data[name])
    
        return f"Contact {name} with phone {phone} has been added."
    raise ValueError

@input_error
def find_contact(adr_book, name):
    name_u = Name(name)
    if name not in adr_book.data:
        raise KeyError
    #existing_record = adr_book.data[name]
    record = Record(name_u)
    existing_record = adr_book.find(record, name)
    phone_numbers = ', '.join(str(phone) for phone in existing_record.phones)
    result = f"Phone numbers for {name}: {phone_numbers}"
    return result


@input_error
def change_contact(adr_book, name, phone_old, phone_new ):
    phone_u_new = Phone(phone_new)
    if name not in adr_book.data:
        raise KeyError
    existing_record = adr_book.data[name]
    if phone_u_new.is_valid(phone_new):
        for num in existing_record.phones:
            if str(num) == phone_old:
                existing_record.edit_phone(num, phone_u_new)
                return f"Phone number for {name} has been changed to {phone_new}."
    raise ValueError
        
@input_error
def delete_contact(adr_book, name, phone):
    if name not in adr_book.data:
        raise KeyError
    existing_record = adr_book.data[name]
    for num in existing_record.phones:
        if str(num) == phone:
            existing_record.remove_phone(num)
            return f"Phone number {phone} has been deleted from {name}."

@input_error
def show_contacts(adr_book):
    result = "Contacts:\n"
    for record in adr_book.data.values():
        result += str(record) + "\n"
        
    return result


    
def handle_requirement(req):
    split_command = ''
    for char in req:
        if char != ' ':
            split_command += char.lower()
        else:
            break
    return split_command

def split_req(req):
    return req.split()


def main():
    adr_book = AddressBook()
    print(adr_book)
    

    def hello_func():
        print("How can I help you? \n")

    def add_func():
        if len(do_requirement_parts) < 3:
            print("Error: Tap an existed name and new phone")
        else:
            print(add_contact(adr_book, do_requirement_parts[1], do_requirement_parts[2]))
    
    def change_func():
        if len(do_requirement_parts) < 4:
            print("Error: Tap an existed name and new phone")
        else:
            print(change_contact(adr_book, do_requirement_parts[1], do_requirement_parts[2], do_requirement_parts[3]))

    def delete_func():
        if len(do_requirement_parts) < 3:
            print("Error: Tap an existed name and new phone")
        else:
            print(delete_contact(adr_book, do_requirement_parts[1], do_requirement_parts[2]))

    def phone_func():
        if len(do_requirement_parts) < 2:
            print("Error: Tap an existed name")
        else:
            print(find_contact(adr_book, do_requirement_parts[1]))
    
    def show_all_func():
        print(show_contacts(adr_book))


    while True:
        do_requirement = input(f'Write your command: ')

        do_requirement_parts = split_req(do_requirement)

        split_command = handle_requirement(do_requirement)
        
        all_commands = {
            'hello': hello_func,
            'add': add_func,
            'change': change_func,
            'delete': delete_func,
            'phone': phone_func,
            'show all': show_all_func,
            'good bye': lambda: print("Good bye!"),
            'close': lambda: print("Good bye!"),
            'exit': lambda: print("Good bye!")

        }


        if do_requirement in all_commands:
            all_commands[do_requirement]()
            if do_requirement.lower() in ('good bye', 'close', 'exit'):
                break
        
        elif split_command in all_commands:
            all_commands[split_command]()


        else:
            print("Use command only: 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', or 'exit'")


if __name__ == '__main__':
    main()







    
        


