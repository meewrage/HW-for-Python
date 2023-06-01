import controller, view
filename = "data_file.txt" 
myfile = open("data_file.txt", "a+") 
myfile.close() 

def get_data():  
    myfile = open('data_file.txt', 'r', encoding='utf-8')
    open(filename, "r+") 
    filecontents = myfile.read() 
    if len(filecontents) == 0:
        view.no_result() 
    else:
        view.result_of_data(filecontents)  
    myfile.close 
   

def add_contact(firstname, lastname, phoneNum):
    with open('data_file.txt', 'a', encoding='utf-8') as data_file:
        data_file.write(firstname + " " + lastname + " " + phoneNum)

def search(information_from_user: str):
    with open('data_file.txt', 'r', encoding='utf-8') as file:
        return[line.strip() for line in file if information_from_user in line]
    

def replace_data(old_name: list, new_name: list):
    with open('data_file.txt', 'r+', encoding='utf-8') as file:
        old_data, new_data = file.readlines(), list()
        old_lines, new_lines = list(), list()
        for line in old_data:
            if all(words in line for words in old_name):
                old_lines.append(line.strip())
                for i in range(len(old_name)):
                    line = line.replace(old_name[i], new_name[i])
                new_lines.append(line.strip())
            new_data.append(line)
        file.seek(0)
        file.truncate(0)
        file.writelines(new_data)
        return old_lines, new_lines
    
def delete_contact(info_for_delete: list):
    with open('data_file.txt', 'r+', encoding='utf-8') as file:
        old_data, new_data, deleted_line = file.readlines(), list(), list()
        for line in old_data:
            if all(words in line for words in info_for_delete):
                deleted_line.append(line.strip())
            else:
                new_data.append(line)
        file.seek(0)
        file.truncate(0)
        file.writelines(new_data)
        return deleted_line
        