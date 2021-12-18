# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
import locale

def_coding = locale.getpreferredencoding()

print('Кодировка по умолчанию: ', def_coding)

with open("test_file.txt", 'w') as f:
    f.writelines(['сетевое программирование', '\n', 'сокет', '\n', 'декоратор'])

try:
    with open("test_file.txt", 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
    print('Файл открыт с кодировкой: utf-8')
except UnicodeDecodeError:
    with open("test_file.txt", 'r', encoding=def_coding) as f:
        for line in f:
            print(line)
    print('Файл открыт с кодировкой по умолчанию:', def_coding)

# у меня windows, открывает в cp1251
