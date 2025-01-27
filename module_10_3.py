import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range (0, 1000):
            time.sleep(0.01)
            deposit_sum = random.randint(50, 501)
            self.balance += deposit_sum
            print(f'Пополнение: {deposit_sum}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range (0, 1000):
            time.sleep(0.01)
            take_sum = random.randint(50, 501)
            print(f'Запрос на {take_sum}')
            if take_sum > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= take_sum
                print(f'Снятие: {take_sum}. Баланс: {self.balance}')


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')