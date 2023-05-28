# Tasks_For_The_Interview
Test_Tasks_For_The_Interview

Этот скрипт предназначен для чтения CSV-файла с числами, а затем поиска максимальной длины последовательности положительных чисел в этом файле. Сначала он проверяет аргументы командной строки, чтобы удостовериться, что нужный файл указан. Затем он обрабатывает файл, используя CSV модуль, чтобы прочитать данные в список словарей. Словарь содержит информацию о каждом числе, включая его позицию в файле и его значение.

Следующим шагом является вызов функции, которая проходит по каждому элементу списка, ищет последовательность положительных чисел, сохраняет ее длину и сравнивает с максимальной длиной, которую он находил до этого. Наконец, он выводит максимальную длину на экран и записывает ее в новый CSV-файл "numbers_out.csv".

Общая концепция скрипта заключается в использовании функций, списков и циклов, чтобы найти и обработать данные в CSV-файле, а затем сохранить результаты в новый CSV-файл. Работа с файлами CSV осуществляется с помощью библиотеки csv.
