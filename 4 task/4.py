# 4. Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста. – 1 балл (задача на
# оценку 10)
import json


def json_dict(f, f_dict):
    with open(f, "w") as file:
        json.dump(f_dict, file)
        return json.dumps(f_dict)


def profit_func(f):
    with open(f, "r", encoding='utf-8') as file:
        profit = []
        name_firm = []
        average_dict = {}
        average_profit = count = 0
        lines = file.readlines()
        end_list = []
        for i in lines:
            test_str = i.split()
            test_profit = int(test_str[2]) - int(test_str[3])
            profit.append(test_profit)
            name_firm.append(test_str[0])
        firm_dict = dict(zip(name_firm, profit))
        for i in profit:
            if i > 0:
                average_profit += i
                count += 1
        average_profit = float(average_profit / count)
        average_dict["average_profit"] = average_profit
        end_list.append(firm_dict)
        end_list.append(average_dict)
        return end_list


if __name__ == "__main__":
    name_f_python = r"D:\Users\ilako\PycharmProjects\laba_3\4 task\Данные о фирме.txt"
    name_f_json = r"D:\Users\ilako\PycharmProjects\laba_3\4 task\My_file.json"
    python_dict = profit_func(name_f_python)
    print(json_dict(name_f_json, python_dict))
