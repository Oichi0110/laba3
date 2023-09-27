# 1. Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# все строки, в которых нет слов, совпадающих с первым словом. Определить
# количество согласных букв в первой строке файла F2. – 3 балла
def first_word_func(arr_lines):
    first_string = arr_lines[0]
    i = 0
    while i < len(first_string):
        if i == 0 and first_string[i] == " ":
            first_string = first_string[1:]
            continue
        break
    first_string = first_string.split()
    first_word = str(first_string[0])
    return first_word


def f1_wrt(f1):
    with open(f1, "w+", encoding='utf-8') as file:
        running = True
        while running:
            string = input("Введите строку: ")
            if string == "":
                return "Завершение ввода"
            file.write(string + "\n")


def f1_copy_in_f2(f1, f2):
    with open(f1, "r", encoding='utf-8') as fileF1:
        with open(f2, "w+", encoding='utf-8') as fileF2:
            lines = fileF1.readlines()
            first_word = first_word_func(lines)
            for i in lines:
                if first_word in i:
                    continue
                fileF2.write(i)
            return "Запись окончена"


def count_func(f2):
    count = 0
    with open(f2, "r", encoding='utf-8') as file:
        line = file.readline()
        constant = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz'
        line = line.lower()
        for i in line:
            if i in constant:
                count += 1
    return count


def main():
    f1 = r"D:\Users\ilako\PycharmProjects\laba_3\1 task\F1.txt"
    f2 = r"D:\Users\ilako\PycharmProjects\laba_3\1 task\F2.txt"
    print("Построчная запись в файл:")
    print(f1_wrt(f1))
    print("\nКопирование строк из файла F1 в файл F2:")
    print(f1_copy_in_f2(f1, f2))
    print("\nПодсчет согласных 1-ой строки в файле F2\nЧисло согласных символов в строке: {}".format(count_func(f2)))


if __name__ == "__main__":
    main()
