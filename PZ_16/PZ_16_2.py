#Создайте класс “Фигура”, который содержит метод расчёта площади фигуры.
# Создайте классы “Квадрат” и “Прямоугольник”, которые наследуются от класса “Фигура”.
# Каждый класс должен иметь метод расчёта площади собственной фигуры.

#базовый класс для других фигур
class figure:
    def __init__(self, *args):
        pass

    def ploshad(self):
        pass

#Вычисляем площадь квадрата
class kvadrat(figure):
    def __init__(self, storona):
        self.storona = storona

    def ploshad(self):
        return self.storona ** 2

#Вычисляем площадь прямоугольика
class pramoygolnik(figure):
    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina

    def ploshad(self):
        return self.dlina * self.shirina

# Пример:
kvadrat1 = kvadrat(4)
print("Площадь квадрата:", kvadrat1.ploshad())

pramoygolnik1 = pramoygolnik(6, 4)
print("Площадь прямоугольника:", pramoygolnik1.ploshad())
