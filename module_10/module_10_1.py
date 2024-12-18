from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count +1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start_1 = time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end_1 = time()
time_res_1 = time_end_1 - time_start_1
print(f'Время работы функции{time_res_1}')

time_start_2 = time()

the_first = Thread(target=write_words, args=(10, "example5.txt"))
the_second = Thread(target=write_words, args=(30, "example6.txt"))
the_third = Thread(target=write_words, args=(200, "example7.txt"))
the_fourth = Thread(target=write_words, args=(100, "example8.txt"))

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()

time_end_2 = time()
time_res_2 = time_end_2 - time_start_2
print(f'Вреия работы потоков{time_res_2}')

