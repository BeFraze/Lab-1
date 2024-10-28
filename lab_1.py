#Serov Nikita
import os
import time


RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'

if __name__ == '__main__':

    print(f"{'Вариант 10'}{END}")
    print(f"{'№1 Cтран: Швейцария'}{END}")

    for i in range(5):
        if not i % 4:
            print(f"{RED}{'  ' * 5}{END}")
        elif i % 2:
            print(f"{RED}{'  ' * 2}{WHITE}{'  ' * 1}{RED}{'  ' * 2}{END}")
        else:
            print(f"{RED}{'  ' * 1}{WHITE}{'  ' * 3}{RED}{'  ' * 1}{END}")
    print(f"{END}")


    print(f"{'№2 Узор: j'}{END}")

    for i in range(10):
        print(f"{'◯' * 10}{END}")
    print(f"{END}")


    print(f"{'№3 Функция: x/3'}{END}")

    for i in range(9, -1, -1):
        print(i, end=' ')
        for j in range(28):
            if j // 3 == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print(f"{END}")


    print(f"{'№4 Условие: Числа от -3 до 3 и остальные'}{END}")

    s = [float(x) for x in open('sequence.txt')]
    f = [x for x in s if -3 <= x <= 3]
    print(f"{(len(f) / len(s) * 100)}% {RED}{'  ' * (round(len(f) / len(s) * 100))}{END}")
    print(f"{(len(s) - len(f)) / len(s) * 100}% {YELLOW}{'  ' * (round((len(s) - len(f)) / len(s) * 100))}{END}")
    print(f"{END}")

    print(f"{'№5 Анимация'}{END}")

    while 1:
        for i in range(10):
            print(f"{END}")
            print(f"{BLUE}  ☁   ☁ ☁ {END}")
            print(f"{BLUE}{' ' * i}✈ {BLUE}{' ' * (9 - i)}{END}")
            print(f"{BLUE}☁    ☁  ☁ {END}")
            time.sleep(1)
            os.system("cls")