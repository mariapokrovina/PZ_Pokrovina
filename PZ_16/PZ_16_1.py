#Создайте класс “Животное” с атрибутами “имя” и ”вид”.
# Напишите метод, который выводит информацию о животном в формате “Имя: имя, Вид: вид”.
class animal:
    def __init__(self, name, vid):
        self.name = name
        self.vid = vid

    def information(self):
        print("Имя:", self.name)
        print("Вид:", self.vid)

# Пример:
animal = animal("Мурка", "Кошка")
animal.information()
