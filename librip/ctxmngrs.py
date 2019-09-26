import time
from contextlib import contextmanager


# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
class timer:
    def __init__(self):
        self.time = time.clock()

    def __enter__(self):
        self.time = time.clock()
        return self.time

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.clock() - self.time)


@contextmanager
def timer2():
    begin = time.clock()
    yield begin
    try:
        pass
    finally:
        print(time.clock() - begin)
