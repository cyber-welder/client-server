from subprocess import Popen, CREATE_NEW_CONSOLE
import time

process_list = []
user_lists = ['Client1', 'Client2', 'Client3']
while True:
    user_command = input("Запустить несколько клиентов (s) / Закрыть всех клиентов (x) / Выйти (q) ")

    if user_command == 'q':
        break
    elif user_command == 's':
        process_list.append(Popen(f'python lesson7/server.py',
                                  creationflags=CREATE_NEW_CONSOLE))
        time.sleep(2)
        for user in user_lists[:8]:
            process_list.append(Popen(f'python -i lesson7/client.py -a localhost -p 7777 -u {user}',
                                      creationflags=CREATE_NEW_CONSOLE))
            # process_list[-1].communicate('pause')

        print(' Запущено 3 клиента и сервер')
    elif user_command == 'x':
        for p in process_list:
            p.kill()
        process_list.clear()
