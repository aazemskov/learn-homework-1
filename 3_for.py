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
    phones_sum_all = 0
    items_sold_len = 0
    for mobile in mobile_list:
        phones_sum = 0
        items_sold_phones = mobile['items_sold']
        items_sold_len += len(mobile['items_sold'])
        phones_name = mobile['product']
        for phone in items_sold_phones:
            phones_sum += phone
        phones_avg = phones_sum / len(items_sold_phones)
        phones_sum_all += phones_sum
        print('Количество проданных ' + phones_name + ':', phones_sum)
        print('Среднее количество проданных ' + phones_name + ':', round(phones_avg, 2), '\n')

    print('Общее количество всех проданных телефонов:', phones_sum_all)
    print('Среднее количество всех проданных телефонов:', round(phones_sum_all / items_sold_len, 2))


if __name__ == "__main__":
    main(mobile_list)
