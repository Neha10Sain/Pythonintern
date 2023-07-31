import tkinter as tk
from tkinter import *

cal = tk.Tk()
def press(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
expression = ""
# clear content of text box
def clear():
    global expression
    expression = ""
    input_text.set(" ")
input_text = StringVar()

# driver code
cal.geometry('290x250')
cal.maxsize(width=250, height=180)
cal.minsize(width=250, height=180)
cal.title("Python Calculator")
cal.configure(bg="purple")

# create label to display final result
result_label = tk.Label(cal, text="")
result_label.grid(row=6, column=1, columnspan=3)

expression_field = Entry(cal, textvariable=input_text)
expression_field.grid(columnspan=4, ipadx=70)

# create button and place at a particular location in calculator gui
button1 = Button(cal, text='1', fg='white', bg='purple', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)
button2 = Button(cal, text='2', fg='white', bg='purple', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
button3 = Button(cal, text='3', fg='white', bg='purple', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
button4 = Button(cal, text='4', fg='white', bg='purple', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
button5 = Button(cal, text='5', fg='white', bg='purple', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
button6 = Button(cal, text='6', fg='white', bg='purple', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
button7 = Button(cal, text='7', fg='white', bg='purple', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
button8 = Button(cal, text='8', fg='white', bg='purple', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(cal, text='9', fg='white', bg='purple', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
button0 = Button(cal, text='0', fg='white', bg='purple', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

add = Button(cal, text=' + ', fg='white', bg='purple', command=lambda: press(" + "), height=1, width=7)
add.grid(row=2, column=3)
sub = Button(cal, text=' - ', fg='white', bg='purple', command=lambda: press(" - "), height=1, width=7)
sub.grid(row=3, column=3)
mul = Button(cal, text=' * ', fg='white', bg='purple', command=lambda: press(" * "), height=1, width=7)
mul.grid(row=4, column=3)
divide = Button(cal, text=' / ', fg='white', bg='purple', command=lambda: press(" / "), height=1, width=7)
divide.grid(row=5, column=3)
equal = Button(cal, text=' = ', fg='white', bg='purple', command=lambda: bt_equal(), height=1, width=7)
equal.grid(row=5, column=2)
clear_text = Button(cal, text='clear', fg='white', bg='purple', command=lambda: clear(), height=1, width=7)
clear_text.grid(row=5, column=1)
decimal = Button(cal, text=' . ', fg='white', bg='purple', command=lambda: press(" . "), height=1, width=7)
decimal.grid(row=6, column=0)


# start the GUI
cal.mainloop()