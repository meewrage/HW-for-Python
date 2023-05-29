import controller, model

def greeting():
    print("Добро пожаловать в телефонный справочник!")


def menu():
    print("Доступные команды:\n1. Показать все контакты. \n2. Добавить новый контакт. \n3. Найти контакт. \n4. Изменить данные в контакте. \n5. Удалить контакт. \n6. Выход.")

def result(firstname, lastname, phoneNum):
    print(firstname, lastname, phoneNum)

def result_of_data():
    print( "Такого номера нет в писке.") 

def no_result(filecontents): 
    print(filecontents) 
       
def find():
    print("Искать по: \n1. ФИО \n2. Номеру телефона ")

# def show_contacts(myfile[values]):
#     print(myfile[values])
    







def error():
    print("Неверно введены данные. Попробуйте еще раз.")
    menu()
        
        



if __name__ == '__main__':
    show_contacts()