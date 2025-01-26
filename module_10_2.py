import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        day_count = 0
        print(f'{self.name}, на нас напали!')
        while enemies:
            time.sleep(1)
            day_count += 1
            enemies -= self.power
            print(f'{self.name} сражается {day_count}й день, осталось {enemies} воинов')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')


