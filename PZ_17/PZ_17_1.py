#В соответствии с номером варианта (был взят 21 вариант) перейти по ссылки на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу.


import tkinter as tk
from tkinter import ttk


# Создание главного окна
root = tk.Tk()
root.title("Обработка формы")
root.geometry('730x630')
label = tk.Label(text="Форма регистрации пользователя", font='Arial 14')
label.pack()

#  Создание рамки
frame = tk.LabelFrame(root, padx=20, pady=20)
frame.pack(padx=20, pady=20)


def clear_entry():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set(None)
    hobbies_var.set(0)
    country_var.set("Ваша страна")
    city_var.set("Ваш город")
    about_text.delete("1.0", tk.END)
    comments_entry.delete(0, tk.END)

def submit_data():
    name = name_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    selected_hobbies = [
        hobby for i, hobby in enumerate(hobbies_list) if hobbies_var.get() and (1 << i)
    ]
    country = country_var.get()
    city = city_var.get()
    about = about_text.get("1.0", tk.END).strip()
    comments = comments_text.get("1.0", tk.END).strip()

    print("Ваше имя:", name)
    print("Пароль:", password)
    print("Возраст:", age)
    print("Пол:", gender)
    print("Ваши увлечения:", ", ".join(selected_hobbies))
    print("Ваша страна:", country)
    print("Ваш город:", city)
    print("Кратко о себе", about)
    print("Комментарий:", comments)

#  Создание внутри рамки
# Имя
name_label = tk.Label(frame, text="Ваше имя:", font='Arial 10')
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Пароль
password_label = tk.Label(frame, text="Пароль:", font='Arial 10')
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Возраст
age_label = tk.Label(frame, text="Возраст:", font='Arial 10')
age_label.grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Entry(frame)
age_entry.grid(row=2, column=1, padx=5, pady=5)

# Пол
gender_label = tk.Label(frame, text="Пол:", font='Arial 10')
gender_label.grid(row=3, column=0, padx=5, pady=5)
gender_var = tk.StringVar(value="Мужской")
male_radio = tk.Radiobutton(
    frame, text="Мужской", variable=gender_var, value="Мужской", font='Arial 10'
)
male_radio.grid(row=3, column=1, sticky="w")
female_radio = tk.Radiobutton(
    frame, text="Женский", variable=gender_var, value="Женский", font='Arial 10'
)
female_radio.grid(row=3, column=2, sticky="w")

# Увлечения
hobbies_label = tk.Label(frame, text="Ваши увлечения:", font='Arial 10')
hobbies_label.grid(row=4, column=0, padx=5, pady=5)
hobbies_list = ["Музыка", "Видео", "Рисование"]
hobbies_var = tk.IntVar()
for i, hobby in enumerate(hobbies_list):
    hobby_check = tk.Checkbutton(
        frame, text=hobby, variable=hobbies_var, onvalue=(1 << i), offvalue=0
    )
    hobby_check.grid(row=4, column=i + 1, sticky="w")

# Страна
country_label = tk.Label(frame, text="Ваша страна:", font='Arial 10')
country_label.grid(row=5, column=0, padx=5, pady=5)
country_var = tk.StringVar()
country_options = ["Россия", "Казахстан", "Белоруссия"]
country_dropdown = ttk.Combobox(
    frame, textvariable=country_var, values=country_options
)
country_dropdown.grid(row=5, column=1, padx=5, pady=5)

# Город
city_label = tk.Label(frame, text="Город:", font='Arial 10')
city_label.grid(row=6, column=0, padx=5, pady=5)
city_var = tk.StringVar()
city_options = ["Москва", "Санкт-Петербург", "Ростов-на-Дону", "Минкс"]
city_dropdown = ttk.Combobox(frame, textvariable=city_var, values=city_options)
city_dropdown.grid(row=6, column=1, padx=5, pady=5)

# О себе
about_label = tk.Label(frame, text="Кратко о себе:", font='Arial 10')
about_label.grid(row=7, column=0, padx=5, pady=5)
about_text = tk.Text(frame, height=3, width=30)
about_text.grid(row=7, column=0, columnspan=9, padx=5, pady=5)

# Решите пример

comments_label = tk.Label(frame, text="Решите пример, запишите результат в поле ниже:", font='Arial 10')
comments_label.grid(row=8, column=0, padx=5, pady=5)
comments_text = tk.Text(frame, height=3, width=30)
comments_text.grid(row=9, column=0, columnspan=9, padx=5, pady=5)

# Кнопки
clear_button = tk.Button(frame, text="Отменить ввод", command=clear_entry, font='Arial 10')
clear_button.grid(row=10, column=0, padx=5, pady=10)
submit_button = tk.Button(frame, text="Данные подтверждаю", command=submit_data, font='Arial 10')
submit_button.grid(row=10, column=1, padx=5, pady=10)


root.mainloop()
