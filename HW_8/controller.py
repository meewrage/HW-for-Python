import view, model

def menu():
    view.greeting()
    while True:
        view.menu()
        answer = int(input("Введите номер команды: "))
        if answer == 1:
            date = model.get_data()
            view.show_contacts(date)
        elif answer == 2:
            contact = input("Введите данные для добавления: ")
        elif answer == 2:
            contact = input("Введите данные для добавления: ")
            result = model.add_contact(contact)
            view.result(result)
        elif answer == 3:
            contact = input("Введите данные для поиска: ")
            result = model.find(contact)
            view.show_contacts(result)
        elif answer == 4:
            break
        else:
            view.error()

