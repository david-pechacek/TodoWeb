FILEPATH = "todos.txt"

def get_todos(file_name=FILEPATH):
    """ Gets the saved todo items from the given (or default) file """
    with open(file_name, "r") as file:
        temp_todos = file.readlines()
    return temp_todos

def save_todos(todos_to_save, file_name=FILEPATH):
    """ Saves todo items """
    with open(file_name, "w") as file:
        file.writelines(todos_to_save)

def add_todo(todos, new_todo):
    todos.append(new_todo+'\n')

# to only run code outside a function in an import when the import file itself is run
if __name__ == "__main__":
    print("hello from functions.py")