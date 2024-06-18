#Дана строка, изображающая целое положительное число. Вывести сумму цифр этого числа.
import random
import string
N = random.randrange(1,11)
s = ''.join(random.choice(string.digits) for x in range(N))
print("Число:",s)
L = list(s)
print("Вывод:",L)
L_int = list(map(int,L))
print("Сумма:",sum(L_int))