def data():  
    with open('data_file.txt', 'r', encording='utf-8') as data_file:
        data = data_file().split('\n')
    return data

def add_contact(contact):
    with open('data_file.txt', 'a', encording='utf-8') as data_file:
        data_file.write(f'{contact}\n')
    return contact

def find_contact(data):
    command = input("Искать по: \n1. ФИО \n2. Номеру телефона") #view.py
    match command:
        case 1:
            find_name = input
