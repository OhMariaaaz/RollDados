import os
os.system('clear')

calc = []
value = ""

while value != "V":
    print('|', ' ', ' ', ' ', ' ', ' ', '|')
    print('|', 1, '|', 2, '|', 3, '|', '+')
    print('|', 4, '|', 5, '|', 6, '|', '-')
    print('|', 7, '|', 8, '|', 9, '|', '*')
    print('|', 'V', '|', 0, '|', 'X', '|', '/')
    value = input()

    if (value == "1" or value == "2" or value == "3" or
            value == "4" or value == "5" or value == "6" or
            value == "7" or value == "8" or value == "9" or value == "0"):
        calc.append(float(value))
