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
        data_file.write(firstname + " " + lastname + " " + phoneNum)

def search(information_from_user: str):
    with open('data_file.txt', 'r', encoding='utf-8') as file:
        return[line.strip() for line in file if information_from_user in line]
    

