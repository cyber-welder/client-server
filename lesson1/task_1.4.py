# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).
for test in ['разработка', 'администрирование', 'protocol', 'standard']:
    print('Строка:', test)
    test = test.encode('utf-8')
    print('\t', test)
    test = test.decode('utf-8')
    print('\t', test)
