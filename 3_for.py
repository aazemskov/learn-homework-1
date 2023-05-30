"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
mobile_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main(work_list):
    items_sold_phones_all = 0
    items_sold_len = 0

    for mobile in mobile_list:
        items_sold_phones = sum(mobile['items_sold'])
        phones_avg = items_sold_phones / len(mobile['items_sold'])
        items_sold_phones_all += items_sold_phones
        items_sold_len += len(mobile['items_sold'])
        product_name = mobile['product']

        print(f'Количество проданных {product_name}: {items_sold_phones}')
        print(f'Среднее количество проданных {product_name}: {round(phones_avg, 2)} \n')

    print(f'Общее количество всех проданных телефонов: {items_sold_phones_all}')
    print(f'Среднее количество всех проданных телефонов: {round(items_sold_phones_all / items_sold_len, 2)}')


if __name__ == "__main__":
    main(mobile_list)
