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
        price = float(price)
    except ValueError:
        print(f'Не верное значение "price" = {price}')
    try:
        discount = float(discount)
    except ValueError:
        print(f'Не верное значение "discount" = {discount}')
    try:
        max_discount = int(max_discount)
    except ValueError:
        print(f'Не верное значение "max_discount" = {max_discount}')
    try:
        if max_discount >= 100:
            print('Очень большая скидка')
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except TypeError:
        print('В значениях задали неверный тип данных.')
        print(f'Проверьте переданные значения: "price" = {price}, "discount" = {discount}, '
              f'"max_discount" = {max_discount}')


if __name__ == "__main__":
    print('step_1: ', discounted(100, 2))
    print('step_2: ', discounted(100, "3"))
    print('step_3: ', discounted("100", "4.5"))
    print('step_4: ', discounted("five", 5))
    print('step_5: ', discounted("сто", "десять"))
    print('step_6: ', discounted(100.0, 5, "10"))
    print('step_7: ', discounted(100.0, 5, 10.17))
