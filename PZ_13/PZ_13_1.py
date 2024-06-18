#В матрице найти максимальный положительный элемент, кратный 4.
A = [[x*y for x in range(1, 5)] for y in range(1, 5)]
print(A)

preobraz_matrix = [element for row in A for element in row]

result = max(filter(lambda x: x > 0 and x % 4 == 0, preobraz_matrix))

print("Максимальный положительный элемент кратный 4:", result)

