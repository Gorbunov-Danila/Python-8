#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    # Проверить количество элементов кортежа.
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)
    
    # Найти искомую сумму.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)

    # Найти искомую сумму.
    s = sum(a for a in A if abs(a) < 5)
    print(s)