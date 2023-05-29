import controller, view
filename = "data_file.txt" 
myfile = open("data_file.txt", "a+") 
myfile.close() 

def get_data():  
    myfile = open('data_file.txt', 'r', encoding='utf-8')
    open(filename, "r+") 
    filecontents = myfile.read() 
    if len(filecontents) == 0:
         view.result_of_data() 
    else:
        view.no_result(filecontents)  
    myfile.close 
   

def add_contact(firstname, lastname, phoneNum):
    with open('data_file.txt', 'a', encoding='utf-8') as data_file:
        data_file.write("[" + firstname + " " + lastname + ", " + phoneNum + "]\n")

    return firstname, lastname, phoneNum

def find_contact(command):
    myfile = open('data_file.txt', 'r', encoding='utf-8')
    open(filename, "r+")
    if command == "1":
            find_name = input('Введите имя: ')
            for values in myfile:
                 if myfile[values] == find_name:
                      
                    print(myfile[values])
    elif command == "2":
          find_name = input('Введите номер телефона, начиная с 8: ')
          for values in myfile:
                 if myfile[values] == find_name:
                      
                    print(myfile[values])
    myfile.close
    
def delete_person(name):
    # """Удаляет данные"""
    persons = get_data()
    with open("data.txt", "a", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    # """Изменяет данные"""
    persons = get_data()
    with open("data.txt", "a", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")


# def records(file_name: str):
#     with open(file_name, 'r+', encoding='utf-8') as data:
#         record_id = 0
#         for line in data:
#             if line != '':
#                 record_id = line.split(';', 1)[0]
#         print('Введите фамилию, имя, отчество, номер телефона через пробел')
#         line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
#         confirm = proof('добавление записи')
#         if confirm == 'y':
#             data.write(line)