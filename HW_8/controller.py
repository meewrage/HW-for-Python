import view, model

def menu():
    view.greeting()
    while True:
        view.menu()
        answer = int(input("Введите номер команды: "))
        if answer == 1:
            data = model.get_data()    
        elif answer == 2:
            firstname, lastname, phoneNum = input("Введите данные для добавления.\n Имя: ").capitalize(), input ("Фамилия: ").capitalize(), input("Телефон: ").capitalize()
            model.add_contact(firstname, lastname, phoneNum)
            view.result(firstname, lastname, phoneNum)
        elif answer == 3:
            info = input("Введите данные контакта для поиска: ")
            result = model.search(info)
            view.show_contacts(result)
        elif answer == 4:
            while True:
                view.submenu()
                user_response = input("Введите команду: ")
                if user_response == "1":
                    old_name = input("Введите данные, которые хотите заменить(в формате Ф И О номер телефона): ").split()
                    new_name = input("Введите новые данные для замены: ").split()
                    if len(old_name) == len(new_name):
                        old_data, new_data = model.replace_data(old_name, new_name)
                        view.show_red_contacts(old_data, new_data)
                    else:
                        view.error_to_red()
                elif user_response == "2":
                    date = model.get_data()
                    view.show_contacts(date)
                elif user_response == "3":
                    break
                else:
                    view.error()   
        elif answer == 5:
            info_for_delete = input("Введите данные контакта через пробел для удаления: ").split()
            deleted_cont = model.delete_contact(info_for_delete)
            if len(deleted_cont) != 0:
                view.deleted_contact(deleted_cont)
            else:
                view.error_to_del_contact()
        elif answer == 6:
            break
                     
        else:
            view.error()

if __name__ == '__main__':
    menu()