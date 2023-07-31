from tkinter import *
from tkinter import messagebox

def newtask():
    task = my_entry.get()
    if task != "":
        l1.insert(END, task)
        # my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Enter some task")

def deleteTask():
    l1.delete(ANCHOR)

list = Tk()
list.title("TO DO List")
list.geometry("500x450+500+20")
list.config(bg="Purple")
list.resizable(width=False, height=True)

frame = Frame(list)
frame.pack(pady=25)

l1 = Listbox(frame, width=20, height=7, font=("Times", 18), bd=0, fg="teal", highlightthickness=0, selectbackground="#a7a6a8", activestyle="none")

l1.pack(side=LEFT, fill=BOTH)
task_list = ["Workout", "LearnSkills", "Practising", "Implements", "Updating"]

for item in task_list:
    l1.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

l1.config(yscrollcommand=sb.set)
sb.config(command=l1.yview)

my_entry = Entry(list, font=('Helvetica', 18))
my_entry.pack(pady=20)

button_frame = Frame(list)
button_frame.pack(pady=20)

addTask_btn = Button(button_frame, text='Add Task', font='Helvetica', bg='grey', padx=20, pady=10, command=newtask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame, text='Delete Task', font='times 14', bg='brown', padx=20, pady=10, command=deleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

list.mainloop()