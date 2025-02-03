from queue import Queue
import threading
import time
from random import randint
from threading import Thread

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __str__(self):
        return f'Стол номер {self.number}'

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        guest_delay = randint(3, 11)
        time.sleep(guest_delay)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        counter = 0
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table}')
                    table.guest = guest
                    counter += 1
                    break
                elif counter == 5:
                    print(f'{guest.name} в очереди')
                    self.queue.put(guest)
                    break

    def discuss_guests(self):
        while self.queue.empty() != True:
            for table in self.tables:
                 if not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'{table} свободен')
                    table.guest = None
                    #if self.queue.empty() != True:
                    guest = self.queue.get()
                    table.guest = guest
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за {table}')
                    guest.start()
                    if self.queue.empty() == True:
                        guest.join()
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'{table} свободен')
                    else:
                        break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
