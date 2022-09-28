import numpy as np
import pandas as pd

num_map = [(1000, 'M'), (900, 'CV'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
           (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def num2roman(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman = roman + r
                num = num - 1
    return roman

again = 'y'

while again == 'y':
    integer = input("Введите арабское число: ")
    integer = int(integer)
    print(num2roman(integer))
    again = input("Хотите проверить другое арабское число <y/n>")