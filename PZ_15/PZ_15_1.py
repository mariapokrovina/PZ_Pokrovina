#Приложение ПРОКАТ АВТОМОБИЛЕЙ  для некоторой организации.
# БД должна содержать таблицу Клиент со следующей структурой записи:
# ФИО клиента, марка авто, срок проката, сумма, предоплата (да/нет).
import sqlite3 as sq

# Подключение к БД
con = sq.connect('car_prokat.db')
cur = con.cursor()

# Создание таблицы client
cur.execute('''
    CREATE TABLE IF NOT EXISTS client (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        mark TEXT NOT NULL,
        sr INTEGER,
        summa INTEGER,
        pre TEXT
    )''')

# Ввод данных в БД
def client():
    try:
        name = input('Введите ФИО клиента: ')
        mark = input('Введите марку авто: ')
        sr = input('Введите срок проката (количество дней): ')
        summa = float(input('Введите сумму проката (руб): '))
        pre = input('Есть ли предоплата (да/нет): ')

        cur.execute('INSERT INTO client (name, mark, sr, summa, pre) VALUES (?, ?, ?, ?, ?)',
                       (name, mark, sr, summa, pre))

        con.commit()
        print('Данные успешно добавлены в БД')
    except sq.Error as e:
        print(f"Произошла ошибка ввода данных в БД: {e}")

# Добавление данных в БД
client()

# Поиск клиента по имени
def search_client(name):
    cur.execute("SELECT * FROM client WHERE name = ?", (name,))
    result = cur.fetchall()

    if result:
        print(f"Найден клиент: {result}")
    else:
        print("Клиент не найден.")

# Удаление клиента
def delete_client(name):
    cur.execute("DELETE FROM client WHERE name = ?", (name,))
    con.commit()
    print("Клиент успешно удален.")

# Редактирование данных клиента
def edit_client(name, mark, sr, summa, pre):
    cur.execute("UPDATE client SET mark = ?, sr = ?, summa = ?, pre = ? WHERE name = ?",
                (mark, sr, summa, pre, name))
    con.commit()
    print("Данные клиента успешно отредактированы.")


search_name = input("Введите имя клиента для поиска: ")
search_client(search_name)

# Удаление клиента
delete_name = input("Введите имя клиента для удаления: ")
delete_client(delete_name)

# Редактирование данных клиента
edit_name = input("Введите имя клиента для редактирования: ")
new_mark = input("Введите новую марку авто: ")
new_sr = input("Введите новый срок проката (количество дней): ")
new_summa = float(input("Введите новую сумму проката: "))
new_pre = input("Введите новую предоплату (да/нет): ")

edit_client(edit_name, new_mark, new_sr, new_summa, new_pre)

# Пропущенное определение функции view_clients()
def view_clients():
    cur.execute("SELECT * FROM client")
    clients = cur.fetchall()

    if clients:
        for client in clients:
            print(client)
view_clients()

# Закрытие БД
con.close()
