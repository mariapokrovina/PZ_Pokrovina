#Разработать программу с применением пакета tk, взяв в качестве условия
# одну любую задачу в ПЗ№2 (Известно, что X кг конфет стоит A. Определить, сколько стоит 1 кг и Y кг этих же конфет.)

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        x = float(entry_x.get())
        a = float(entry_a.get())
        y = float(entry_y.get())

        if x <= 0 or a <= 0 or y <= 0:
            raise ValueError("Значения должны быть больше 0")

        p = a / x
        label_p.config(text=f'Стоимость 1 кг: {p:.2f}')
        r = y * p
        label_r.config(text=f'Стоимость {y} кг: {r:.2f}')
    except ValueError as e:
        messagebox.showerror("Ошибка ввода", str(e))


# создание окна
window = tk.Tk()
window.geometry('300x300')
window.title("Расчет стоимости конфет")

# поля для ввода x, a, y
label_x = tk.Label(window, text="Введите количество конфет (в кг):")
label_x.pack()
entry_x = tk.Entry(window)
entry_x.pack()

label_a = tk.Label(window, text="Введите стоимость конфет (в руб):")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

label_y = tk.Label(window, text="Введите количество конфет (в кг):")
label_y.pack()
entry_y = tk.Entry(window)
entry_y.pack()

# кнопка для расчета
button_calculate = tk.Button(window, text="Рассчитать", command=calculate)
button_calculate.pack()

# метки для вывода результатов
label_p = tk.Label(window, text="")
label_p.pack()

label_r = tk.Label(window, text="")
label_r.pack()

window.mainloop()
