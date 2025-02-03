import threading
import multiprocessing
import time

def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')
    for line in file:
        line = file.readline(-1)
        all_data.append(line)
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

#start_program = time.time()

#read_info('file 1.txt')
#read_info('file 2.txt')
#read_info('file 3.txt')
#read_info('file 4.txt')

#end_program = time.time()
#t = end_program - start_program
#print(t,'sec')

if __name__ == '__main__':
    start_program = time.time()
    with multiprocessing.Pool(4) as p:
         p.map(read_info, filenames)
    end_program = time.time()
    t = end_program - start_program
    print(t,'sec')