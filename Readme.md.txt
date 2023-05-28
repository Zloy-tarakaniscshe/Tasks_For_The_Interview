Этот скрипт предназначен для чтения CSV-файла с числами, а затем поиска максимальной длины последовательности положительных чисел в этом файле. Сначала он проверяет аргументы командной строки, чтобы удостовериться, что нужный файл указан. Затем он обрабатывает файл, используя CSV модуль, чтобы прочитать данные в список словарей. Словарь содержит информацию о каждом числе, включая его позицию в файле и его значение.

Следующим шагом является вызов функции, которая проходит по каждому элементу списка, ищет последовательность положительных чисел, сохраняет ее длину и сравнивает с максимальной длиной, которую он находил до этого. Наконец, он выводит максимальную длину на экран и записывает ее в новый CSV-файл "numbers_out.csv".

Общая концепция скрипта заключается в использовании функций, списков и циклов, чтобы найти и обработать данные в CSV-файле, а затем сохранить результаты в новый CSV-файл. Работа с файлами CSV осуществляется с помощью библиотеки csv.


Исполняемый Код:

import os
import sys
import csv

def max_sequence_length(*numbers):
    max_len_res = 0
    cur_len = 0
    for num in numbers:
        if int(num['value']) > 0:
            cur_len += 1
            if cur_len > max_len_res:
                max_len_res = cur_len
        else:
            cur_len = 0
    return max_len_res


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "numbers.csv"

    path = os.getcwd()  # текущая директория
    file_path = os.path.join(path, file_name)

    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        numbers = [row for row in reader]

    max_len = max_sequence_length(*numbers)
    print("Max sequence length:", max_len)
    my_list = ["Max sequence length", max_len]

    with open('numbers_out.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE, quotechar='')
        for data in my_list:
            writer.writerow([data])