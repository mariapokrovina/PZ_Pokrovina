#Даны целые положительные числа N и K. Найти сумму 1
# в степени K+2 в степени K+...+N в степени K.
N = (input("Введите целое положительное число(N): "))
K = (input("Введите целое положительное число(K): "))
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = (input("Введите целое положительное число(N): "))
while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print("Неправильно ввели!")
        K = (input("Введите целое положительное число(K): "))
print ("N = ", N)
print ("K = ", K)
if N >= 0 and K >= 0:
 sum = 0
 for i in range(1, N + 1):
     sum += i ** K
 print("Результат: ", sum)
else:
    print("Введите ПОЛОЖИТЕЛЬНОЕ число")
