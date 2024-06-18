#Дана строка, состоящая из русских слов, разделенных пробелами
# (одним или несколькими). Найти длину самого длинного слова..
import sys
def main():
    s = input('Введите строку: ')
    res = float('-inf')
    k = float('-inf')
    s = ' ' + s
    s += ' '
    i = 0
    while i < len(s):
        if s[i] != ' ':
            k = 1
            while s[i+1] != ' ':
                k += 1
                i += 1
        res = max(res, k)
        i += 1
    print(res)

if __name__ == "__main__":
    main()