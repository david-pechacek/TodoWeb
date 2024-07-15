import streamlit as st
import functions as functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    functions.add_todo(todos, todo)
    functions.save_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")

st.write("This app to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print("Removing", todo)
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a new todo:", placeholder="Enter a todo", on_change=add_todo, key="new_todo")

# Every load of page, it runs the entire script, top to bottom