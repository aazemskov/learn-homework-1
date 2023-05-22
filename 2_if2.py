"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main(first_str, second_str):
    if type(first_str) is not str or type(second_str) is not str:
        return 0
    elif first_str == second_str:
        return 1
    elif first_str != second_str and len(first_str) > len(second_str) and second_str != 'learn':
        return 2
    elif first_str != second_str and second_str == 'learn':
        return 3


if __name__ == "__main__":
    print(main('first_sting', 'second_string'))
