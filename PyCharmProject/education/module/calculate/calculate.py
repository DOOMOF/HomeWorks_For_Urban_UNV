import tkinter as tk
from tkinter import ttk

import FUNCTION as FUN


window = tk.Tk()

window.title('культеляпр')
window.geometry("350x350")
window.resizable(False,False)

#поле для 1 числа
number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=75, y=140)

#поле для 2 числа
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=75, y=190)

#поле для ответа
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=75, y=235)

def GetValueONE():
    num_1 = int(number1_entry.get())
    return num_1

def GetValueTWO():
    num_2 = int(number1_entry.get())
    return num_2

def set_values(value):
    answer_entry.delete(0, 'end')
    print("удалено")
    answer_entry.insert(0, value)
    print("dcnfdktyj")


#Кнопка '+'
button_add = ttk.Button(window, text="+", command=set_values(FUN.add(GetValueONE(), GetValueTWO())))
button_add.place(width=40, height=70, x=300, y=200)
#Кнопка '+'
#button_add = tk.Button(window, text="+", width=3, height=3, command=add)
#button_add.place(x=300, y=200)

#кнопка '-'
button_add = ttk.Button(window, text="-", command=set_values(FUN.sub(GetValueONE(), GetValueTWO())))
button_add.place(width=40, height=70, x=258, y=200)
#кнопка '-'
#button_sub = tk.Button(window, text="-", width=3, height=3, command=sub)
#button_sub.place(x=265, y=200)

#кнопка '/'
button_add = ttk.Button(window, text="/", command=set_values(FUN.div(GetValueONE(), GetValueTWO())))
button_add.place(width=40, height=70, x=300, y=128)
#кнопка '/'
#button_div = tk.Button(window, text= "/", width=3, height=3, command=div)
#button_div.place(x=265, y=140)

#кнопка '*'
button_add = ttk.Button(window, text="*", command=set_values(FUN.mul(GetValueONE(), GetValueTWO())))
button_add.place(width=40, height=70, x=258, y=128)
#кнопка '*'
#button_mul = tk.Button(window, text="*", width=3, height=3, command=mul)
#button_mul.place(x=300, y=140)

#текст для 1 поля
number1_label = tk.Label(window, text="Введите первое число:")
number1_label.place(x=75, y=120)

#текст для 2 поля
number2_label = tk.Label(window, text="Введите второе число:")
number2_label.place(x=75, y=170)

#текст для ответа
answer_label = tk.Label(window, text="Ответ:")
answer_label.place(x=75, y=215)

window.attributes("-toolwindow", True)
window.mainloop()
