filename = "data_file.txt" 
myfile = open(filename, "a+") 
myfile.close 

def data():  
    with open('data_file.txt', 'r', encording='utf-8') as data_file:
        data = data_file().split('\n')
    return data

def add_contact(contact):
    with open('data_file.txt', 'a', encording='utf-8') as data_file:
        data_file.write("[" + firstname + " " + lastname + ", " + phoneNum + "]\n")

    return contact

def find_contact(data):
    command = input("Искать по: \n1. ФИО \n2. Номеру телефона \n Введите команду: ") #view.py
    if command == "1":
            find_name = input('Введите ФИО: ')
            for values in data:
                 if data[values] == find_name:
                      print(data[values])
    elif command == "2":
          find_name = input('Введите номер телефона, начиная с 8: ')
          for values in data:
                 if data[values] == find_name:
                      print(data[values])

