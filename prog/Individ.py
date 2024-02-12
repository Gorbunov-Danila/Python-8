#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # Пример кортежа целых чисел
    my_tuple = (1, 2, 4, 7, 8, 10, 12, 15, 16, 20)

    # Ищем индексы пар соседних чётных чисел
    indices = [i for i in range(1, len(my_tuple)-1) if my_tuple[i-1] % 2 == 0 and my_tuple[i] % 2 == 0]

    if indices:
        # Если есть такие пары, находим индекс последней пары и выводим элементы до него
        last_pair_index = indices[-1]
        elements_before_last_pair = my_tuple[:last_pair_index]
        print(f"Элементы, предшествующие последней паре соседних чётных чисел: {elements_before_last_pair}")
    else:
        print("В кортеже нет пар соседних чётных чисел.")

if __name__ == "__main__":
    main()