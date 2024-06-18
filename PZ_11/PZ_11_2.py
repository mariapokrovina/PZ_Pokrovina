# пунктцацию первых четырёх строках. Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы верхнего регистра на нижний.
# Чтение содержимого файла text18-23.txt и подсчет знаков и пунктуации в первых четырех строках


with open('text18-23.txt', 'r', encoding='utf-16') as file:
 lines = file.readlines()
 for line in lines:
  print(line.strip())

 total_chars = 0
 total_punctuation = 0
 for line in lines[:4]:
  total_chars += len(line)
  total_punctuation += sum([1 for char in line if char in '.?!,:;'])

 print(f"Количество знаков в первых четырех строках: {total_chars}")
 print(f"Количество пунктуации в первых четырех строках: {total_punctuation}")

lines_lower = [line.lower() for line in lines]

with open('new_poem.txt', 'w', encoding='utf-16') as new_file:
 for line in lines_lower:
  new_file.write(line)

print("Текст в стихотворной форме сохранен в файл new_poem_.txt")