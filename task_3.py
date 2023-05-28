import csv
import os
import sys

# Определение функции для чтения CSV-файлов
def read_csv(file_name):
    with open(file_name, 'r', newline='', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        data = [rows for rows in reader]
        data.pop(0)
        return data

# Определение функции для фильтрации некорректных данных
def filter_data(data):
    f_data = []
    for rows in data:
        if int(rows[2]) < 13 and int(rows[3]) < 32 and int(rows[1]) in [2021, 2022, 2023]:
            f_data.append(rows)
    return f_data

# Определение функции для подсчета прибыли по месяцам
def count_profit(data, departments):
    result = []
    for year in range(2000, 2024):
        for month in range(1, 13):
            for dep in departments:
                if int(dep[1]) <= year and int(dep[2]) >= year:
                    profit = 0
                    for rows in data:
                        if int(rows[1]) == year and int(rows[2]) == month and rows[4] == dep[0]:
                            profit += int(rows[5])
                    result.append((year, month, dep[3], profit))
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_operations = sys.argv[1]
        file_departments = sys.argv[2]
    else:
        file_operations = "operations.csv"
        file_departments = "departments.csv"

    path = os.getcwd()  # текущая директория
    file_path_operations = os.path.join(path, file_operations)
    file_path_departments = os.path.join(path, file_departments)

# Чтение входных данных из файлов
    operations_data = read_csv(file_path_operations)
    departments_data = read_csv(file_path_departments)

# Фильтрация некорректных данных
    filtered_data = filter_data(operations_data)

# Подсчет прибыли по месяцам
    result_data = count_profit(filtered_data, departments_data)

# Вывод результатов на экран
    with open('income_out.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['year', 'month', 'department', 'income'])
        for row in result_data:
            writer.writerow(row)

    for row in result_data:
        print(f'Год: {row[0]}, Месяц: {row[1]}, Название Подразделения: {row[2]}, Суммарная Прибыль: {row[3]}')