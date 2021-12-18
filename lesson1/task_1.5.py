# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
for host in ['yandex.ru', 'youtube.com']:
    args = ['ping', host]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

# у меня windows, работает
