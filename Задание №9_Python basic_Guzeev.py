import threading  # модуль для работы с потоками
import time       # модуль для задержки (паузы)
from threading import Thread


def print_reverse():  # функция, которая будет выполняться в отдельном потоке
    name = threading.current_thread().name #узнаем имя текущего потока
    for i in range(10, -1, -1): # цикл от 10 до 0 с шагом -1
        print(f"{name}: {i}") # выводим текущее число
        time.sleep(1) # останавливаем выполнение на 1 секунду


# Создаём первый поток
thread_first = threading.Thread(target=print_reverse, name = "Первый поток")
thread_first.start()
thread_first.join()
print("Первый поток завершил работу")

# Запуск второго потока
thread_second = threading.Thread(target=print_reverse, name = "Второй поток")
thread_second.start()
thread_second.join()
print("Второй поток завершил работу")