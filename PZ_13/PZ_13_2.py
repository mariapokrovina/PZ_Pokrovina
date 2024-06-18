#В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
#A = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]]

A = [[x*y for x in range(1, 4)] for y in range(1, 4)]
print(A)

n = len(A)

result_A = list(map(lambda i: list(map(lambda x, j: x * 2 if i != j else x, A [i], range(n))), range(n)))

print(result_A)