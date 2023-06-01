import controller, model

def greeting():
    print("Добро пожаловать в телефонный справочник!")


def menu():
    print("Доступные команды:\n1. Показать все контакты. \n2. Добавить новый контакт. \n3. Найти контакт. \n4. Изменить данные в контакте. \n5. Удалить контакт. \n6. Выход.")

def result(firstname, lastname, phoneNum):
    print(firstname, lastname, phoneNum)

def no_result():
    print("Нет доступных контактов. Для содания нажмите '2'.") 

def result_of_data(filecontents): 
    print(filecontents) 
       
def find():
    print("Искать по: \n1. ФИО \n2. Номеру телефона ")

def show_contacts(date: list):
    print(*date, sep='\n')

def submenu():
    print(
        '1 - Изменить Фамилию, Имя, Отчество, Телефон\n'
        '2 - Вывести список всех контактов\n'
        '3 - Вернуться в основное меню'
    )

def show_red_contacts(old: list, new: list):
    print("Контакты: ", *old, sep='\n')
    print("Заменены на: ",*new, sep='\n')
    

def error():
    print("Неверно введены данные. Попробуйте еще раз.")
   
        
def deleted_contact(deleted_contact):
    print(f'Успешное удаление контакта: {" ".join(deleted_contact)}')

def error_to_del_contact():
    print("Ошибка! контакта с такими данными не существует.")

def error_to_red():
    print(
        'Ошибка при попытке редактирования контакта.\n'
        'Пожалуйста введите правильные данные.\n'
        'Число элементов, подлежащих замене должно быть равно числу заменяемых'
    )       



