from tkinter import *

# the funcation of Calculator
# I want to display the right reslve when user put the button0

# setting a GUI
a = Tk()
a.title('Calculator')
a.geometry('420x340')
a.resizable(width=False, height=False)
# I don't want user to resize the calculator


# It is a funcation for enter a number button and display it.
# Setting a expression a empty string, whenver user click the button, expression become that number
# 0 = 0+1
def click_button(item):
    global expression
    expression = expression + str(item)
    display_input.set(expression)

# It is a funcation for clear all number and  display nothing on it.
# Setting a expression a empty string.


def delete_button():
    global expression
    expression = ""
    display_input.set("")

# It is a funcation for equal all number and  display  on it.


def equal_button():
    global expression
    result = str(eval(expression))
    display_input.set(result)
    expression = ""


expression = ""
display_input = StringVar()

'''
To able to display the right value, need to use Variable Classes
x = StringVar() # Holds a string; default value ""
x = IntVar() # Holds an integer; default value 0
x = DoubleVar() # Holds a float; default value 0.0
x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True
'''
# setting a frame for the display input
frame = Frame(a)
frame.pack(side=TOP)

# setting a display field into the frame
display = Entry(frame, width=70, font=(
    'Times New Roman', 18, 'italic'), textvariable=display_input)
display.grid(row=0, column=0)
display.pack(ipady=30)

# setting a frame for button  0 to 9 and *,-,+,/
butframe = Frame(a, bd=0, width=312, height=272.5)
butframe.pack()


# row1
button0 = Button(butframe, text='0', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(0))
button0.grid(row=1, column=0, padx=1, pady=1)
button1 = Button(butframe, text='1', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(1))
button1.grid(row=1, column=1, padx=1, pady=1)
button2 = Button(butframe, text='2', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(2))
button2.grid(row=1, column=2, padx=1, pady=1)
button_delete = Button(butframe, text='DEL', fg='#f1f1f4',
                       bg='#22222b', height=3, width=10, font=(10), command=lambda: delete_button())
button_delete.grid(row=1, column=3, padx=1, pady=1)

# row2

button3 = Button(butframe, text='3', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(3))
button3.grid(row=2, column=0, padx=1, pady=1)

button4 = Button(butframe, text='4', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(4))
button4.grid(row=2, column=1, padx=1, pady=1)

button5 = Button(butframe, text='5', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(5))
button5.grid(row=2, column=2, padx=1, pady=1)
button_divide = Button(butframe, text='/', fg='#f1f1f4',
                       bg='gray', height=3, width=10, font=(10), command=lambda: click_button('/'))
button_divide.grid(row=2, column=3, padx=1, pady=1)

# row3
button6 = Button(butframe, text='6', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(6))
button6.grid(row=3, column=0, padx=1, pady=1)

button7 = Button(butframe, text='7', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(7))
button7.grid(row=3, column=1, padx=1, pady=1)

button8 = Button(butframe, text='8', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(8))
button8.grid(row=3, column=2, padx=1, pady=1)
button_multiply = Button(butframe, text='*', fg='#f1f1f4',
                         bg='gray', height=3, width=10, font=(10), command=lambda: click_button('*'))
button_multiply.grid(row=3, column=3, padx=1, pady=1)

# row4
button_point = Button(butframe, text='.', fg='#f1f1f4',
                      bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button('.'))
button_point.grid(row=4, column=0, padx=1, pady=1)
button9 = Button(butframe, text='9', fg='#f1f1f4',
                 bg='#22222b', height=3, width=10, font=(10), command=lambda: click_button(9))
button9.grid(row=4, column=1, padx=1, pady=1)
button_equal = Button(butframe, text='=', fg='#f1f1f4',
                      bg='#22222b', height=3, width=10, font=(10), command=lambda: equal_button())
button_equal.grid(row=4, column=2, padx=1, pady=1)
button_plus = Button(butframe, text='+', fg='#f1f1f4',
                     bg='gray', height=3, width=10, font=(10), command=lambda: click_button('+'))
button_plus.grid(row=4, column=3, padx=1, pady=1)


a.mainloop()
