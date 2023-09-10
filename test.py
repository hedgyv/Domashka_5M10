from collections import UserDict

class AddressBook(UserDict):
    def has_in_values(self, value):
        print(self.data.keys())
        print(self.data.values())
        print(self.data)
        print(value in self.data.values())

phone_book = AddressBook()
phone_book['a'] = 1
phone_book.has_in_values(1)
print(phone_book.data)
print(phone_book['a'])

existnumber = phone_book.data['a']
print(type(existnumber))


# #___________________________________________________________
# class AddressBook(UserDict):
#     def add_record(self, record):
#         pass
# class Record:
#     def __init__(self, name):
#         self.name = name
# class Name:
#     pass

# name = 'Anya'

# the_name = Name(name)
# new_record = Record(the_name)




# def main():
#     phone_book = AddressBook()
#     phone_book.add_record(new_record)

# if __name__ == '__main__':
#     main()


# class AddressBook(UserDict): 
#     def add_record(self, record): 
#         self.data[record.name.value] = record   атрибут name тянется из класса Record? - class Record: 
#     def __init__(self, name):
# а value я так понял тащит с параметра class Name(Field): 
#     def is_valid(self, value): который передается в конструкторе the_name = Name(name)



# class AdressBook(UserDict):
#     def add_record(self, record):
#         self.data[record.name.value] = record
#         print(self.data[record.name.value])


# record = Record(name_u)
# adr_book.add_record(record)

# Output

# Name: Anya