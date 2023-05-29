import view, model

def menu():
    view.greeting()
    while True:
        view.menu()
        answer = int(input("Введите номер команды: "))
        if answer == 1:
            data = model.get_data()    
        elif answer == 2:
            firstname, lastname, phoneNum = input("Введите данные для добавления.\n Имя: "), input ("Фамилия: "), input("Телефон: ")
            result = model.add_contact(firstname, lastname, phoneNum)
            view.result(result)
        elif answer == 3:
            view.find()
            command = input("Введите команду: ")
            model.find_contact(command)
        #     view.show_contacts(result)
        elif answer == 4:
            old_name = input("Введите старое имя для поиска контакта: ")
            new_name = input("Введите новое имя: ")
            result = model.change_person(new_name, old_name)
        elif answer == 5:
            name = input("Введите имя контакта для удаления: ")
            result = model.delete_person(name)
        elif answer == 6:
            break
                     
        else:
            view.error()

if __name__ == '__main__':
    menu()