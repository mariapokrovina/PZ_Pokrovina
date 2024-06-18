#Описать функцию TrianglePS(a, P, S), вычисляющую по стороне а
# равностороннего треугольника его периметр P = 3*a и
# площадь S = a2 √3/4 (а - входной, P и S - выходные параметры;
# все параметры являются вещественными). С помощью этой функции найти периметры
# и площади трех равносторонних треугольников с данными сторонами.
import math
def triangleps(a):
    p = 3 * a
    s = pow(a, 2) * math.sqrt(3) / 4
    return p, s
if __name__ == "__main__":
    for i in range(1, 4):
        a = (input("a:"))
        while type(a) != int:
            try:
                a = int(a)
            except ValueError:
                print("Неправильно ввели!")
                a = (input("a: "))
        p, s = triangleps(a)
        print("P:", p)
        print("S:", s)