import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    # print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Its my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# on_change izsauc funkciju 'add_todo', kad lietotājs ievada tekstu
st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


# region Kods, kas palīdz saprast, kas notiek
print('End')

# st.session_state ir īpašs datu tips streamlit vidē
st.session_state
# endregion
