# 2. Имеется текстовый файл «Кинотеатр» , строка, которого содержит в
# себе информацию: название кинофильма, дата сеанса стоимость билета.
# Вывести на экран все фильмы, стоимость которых меньше 15 рублей.
# Вывести на экран все фильмы за определенную дату. Файл заполнить
# заранее(не программно), не менее 10 строк.
# Пример файла:
# Кунг-фу панда 12.07.2022 10 – 3 балла
import datetime


def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def date_func():
    running = True
    output = []
    while running:
        years = input("Введите год(1950-2023): ")
        if isint(years):
            if 1949 < int(years) < 2024:
                years = int(years)
                break
            else:
                print("Диапозон от 1950 до 2023")
        else:
            print("Введите целочисленный тип данных")
    while running:
        month = input("Введите месяц: ")
        if isint(month):
            if 0 < int(month) < 13:
                month = int(month)
                break
            else:
                print("Диапозон от 1 до 12")
        else:
            print("Введите целочисленный тип данных")
    while running:
        day = input("Введите день: ")
        if isint(day):
            if (month == 1 or month == 3 or month == 5) and 0 < int(day) < 32:
                day = int(day)
                output.append(day)
                output.append(month)
                output.append(years)
                return output
            elif (month == 7 or month == 8 or month == 10 or month == 12) and 0 < int(day) < 32:
                day = int(day)
                output.append(day)
                output.append(month)
                output.append(years)
                return output
            elif (month == 4 or month == 6 or month == 9 or month == 11) and 0 < int(day) < 31:
                day = int(day)
                output.append(day)
                output.append(month)
                output.append(years)
                return output
            elif (month == 2 and (years % 4 == 0 and (years % 100 != 0 or years % 400 == 0))) and 0 < int(day) < 30:
                day = int(day)
                output.append(day)
                output.append(month)
                output.append(years)
                return output
            elif month == 2 and years % 4 != 0 and 0 < int(day) < 29:
                day = int(day)
                output.append(day)
                output.append(month)
                output.append(years)
                return output
            else:
                print("Введите день в верном диапозоне")
                continue
        else:
            print("Введите целочисленный тип данных")


def price_cinema(f):
    with open(f, "r", encoding='utf-8') as file:
        print("Введите дату: ")
        b_day = date_func()
        day_b = b_day[0]
        month_b = b_day[1]
        years_b = b_day[2]
        beg_date = datetime.datetime(years_b, month_b, day_b)
        lines = file.readlines()
        print("\nНазвание фильмов, стоимость которых меньше 15 руб: ")
        for i in lines:
            test_str = i.split(",")
            if float(test_str[2]) < 15:
                print(f"Название фильма: \033[33m{test_str[0]}\033[0m")
        print("\nФильмы за определенную дату: ")
        for i in lines:
            test_str = i.split(",")
            date = test_str[1].split(".")
            day = int(date[0])
            month = int(date[1])
            years = int(date[2])
            file_date = datetime.datetime(years, month, day)
            if beg_date == file_date:
                print(f"Название фильма: \033[33m{test_str[0]}\033[0m\nЦена фильма: \033[33m{test_str[2]}\033[0m")


if __name__ == "__main__":
    name_f = r"D:\Users\ilako\PycharmProjects\laba_3\2 task\Кинотеатр.txt"
    price_cinema(name_f)
