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