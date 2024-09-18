import tkinter as tk 
import csv 
tasks= []

def add_task():
    new_task = entry_task.get()
    tasks.append(new_task)
    task_list.insert(tk.END,new_task)
    entry_task.delete(0,tk.END)
    
def delete_task():
   selected_index = task_list.curselection()
   if selected_index:
       index = selected_index[0]
       deleted_task =task_list.get(index)
       tasks.remove(deleted_task)
       task_list.delete(index)
           
def save_task():
    with open('tareas.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        for tarea in tasks:
            writer.writerow([tarea])
    
    
window = tk.Tk()
window.title("Tasks List")

# Caja mostrar título de la Lista
lable_title = tk.Label(window,text= "Tasks List")
lable_title.pack()

# Caja de texto para ingresar nuevas tareas
entry_task = tk.Entry(window)
entry_task.pack()

# Botón para agregar tareas
button_add = tk.Button(window,text = "Add Task",command = add_task)
button_add.pack()

# Botón para ver las tareas
task_list = tk.Listbox(window)
task_list.pack()

# Botón para borrar las tareas

errase_button = tk.Button(window, text="Delete Task", command= delete_task)
errase_button.pack()

# Botón guardar Tareas CSV

button_save = tk.Button(window,text = "Save Task",command = save_task)
button_save.pack()

window.mainloop()
