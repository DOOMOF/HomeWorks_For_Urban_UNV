from time import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    stat_time = time()
    for filename in filenames:
        read_info(filename)
    end_time = time()
    print(f'линейный вызов:{end_time - stat_time:.2f} секунд')

    stat_time = time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time()
    print(f'многопроцессный вызов: {end_time - stat_time:.2f} секунд ')


