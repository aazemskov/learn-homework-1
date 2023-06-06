"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""


def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError) as err:
        return f"Введены не корректные данные, повторите ввод. Ошибка: {err}"
    if max_discount >= 100:
        return f"Слишком большая максимальная скидка. Она не может быть больше или равна 100%!"
    if discount >= max_discount:
        return price
    return price - (price * discount / 100)


if __name__ == "__main__":
    print('step_1: ', discounted(100, 2))
    print('step_2: ', discounted(100, "3"))
    print('step_3: ', discounted("100", "4.5"))
    print('step_4: ', discounted("five", 5))
    print('step_5: ', discounted("сто", "десять"))
    print('step_6: ', discounted(100.0, 5, "10"))
    print('step_7: ', discounted(100.0, 5, 10.17))
