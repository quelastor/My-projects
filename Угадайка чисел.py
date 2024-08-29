import random

n = 100

counter_of_attempts = 0
def is_valid(input_string):
    if input_string.isdigit():
        number = int(input_string)
        if 1 <= number <= n:
            return True
    return False


def cheking_the_number(num):
    global counter_of_attempts
    counter_of_attempts += 1
    if num < random_digit:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return False
    elif num > random_digit:
        print('Ваше число больше загаданного, попробуйте еще разок')
        return False
    elif num == random_digit:
        print('Вы угадали, поздравляем!')
        print(f'Количество ваших попыток: {counter_of_attempts}')

        return True


def restart_the_game():
    ans = input("Отличная игра! Сыграем еще раз? Да - д / Нет - н")
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input(
                'Вроде, взрослый человек, а на простой вопрос ответить не может...Сыграем еще раз? Да - д / Нет - н"')
        elif ans in ('n', 'н'):
            return False
        else:
            return True

def game():

    global n
    global random_digit
    random_digit = random.randint(1, n)
    while True:
        print("Введите число от 1 до", n)
        num = input()

        if is_valid(num) != True:
            print('А может быть все-таки введем целое число от 1 до', n, '?')
            continue
        else:
            num = int(num)
            if cheking_the_number(num):
                if restart_the_game():
                    game()
                else:
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break


def new_game():
    print("Добро пожаловать в числовую угадайку")
    print("╔═══━━━───────── • ───────────━━━═══╗")
    print("           Новая Игра - Н          ")
    print("          Настройки - Нс")
    print("         Выйти из Игры - В")
    print("╚═══━━━───────── • ───────────━━━═══╝")

    while True:
        s = input('Введите букву в соответсвии с действием')
        if s.lower() == 'Н'.lower() or s == 'Н':
            game()
            break
        elif s.lower() == "Нс".lower() or s == "Нс":
            settings()
            break
        elif s.lower() == "В".lower() or s == "В":
            print("Хорошего дня!")
            break
        else:
            print("Ты помоему перепутал...")
            continue


def settings():
    print("Введите диапазон угадывания числа:")
    global n

    b = input()
    while True:
        if b.isdigit:
            n = int(b)
            new_game()
            return
        else:
            print('А может быть все-таки введем целое число?')
            continue
new_game()



