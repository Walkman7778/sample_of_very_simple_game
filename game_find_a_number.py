import math, random
print('Добро пожаловать в числовую угадайку')
print("Введите предел максимального заганного числа")
c = int(input())
a = random.randint(1, c)
def numbers_of_tries(n):
    return math.ceil(math.log2(n))
def is_valid(n):
    if (1 <= int(n) <= c) and n.isdigit():
        return True
    else:
        return False
def ugadaika():
    s = 0
    while True:
        print(f"Введите целое число от 1 до {c}" )
        s += 1
        n = input()
        if is_valid(n):
            n = int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            n = input()
        if n < a:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            s += 1
        elif n > a:
            print('Ваше число больше загаданного, попробуйте еще разок')
            s += 1
        else:
            print(f'Вы угадали число за {s} попыток, поздравляем!')
            break
continue_ugadaika = True
while continue_ugadaika == True:
    print(ugadaika())
    print("Хотите съиграть еще: 'Y' - да 'N' - нет")
    condition = input()
    if condition == 'Y':
        pass
    else:
        continue_ugadaika = False
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
