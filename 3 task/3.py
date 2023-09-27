# 3. Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#  Физика: 30(л) 10(лаб)
#  Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
# 30}– 3 балла
import re


def information_func(f1):
    with open(f1, "r", encoding='utf-8') as file:
        my_dict = {}
        lines = file.readlines()
        for i in lines:
            sum = 0
            test_str = i.split()
            key = test_str[0][:len(test_str[0]) - 1]
            for j in range(1, len(test_str)):
                value = re.sub(r"[^0-9]", "", test_str[j])
                sum += int(value)
            my_dict[key] = sum
        return my_dict


if __name__ == "__main__":
    name_file = r"D:\Users\ilako\PycharmProjects\laba_3\3 task\Учебные предметы.txt"
    print(information_func(name_file))
