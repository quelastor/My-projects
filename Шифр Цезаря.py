print('Вас приветствует программма-ключ для Шифра Цезаря')       #Приветствие

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'                #Алфавиты
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def enscription():
    s = input(('\nНапишите текст который требуется зашифровать: '))
    k = int(input('Ваш сдвиг шага: '))
    nl = ''
    for i in s:
        if i in rus_lower_alphabet:
            nl += rus_lower_alphabet[(rus_lower_alphabet.find(i) + k) % 32]
        if i in rus_upper_alphabet:
            nl += rus_upper_alphabet[(rus_upper_alphabet.find(i) + k % 32)]
        if i in eng_lower_alphabet:
            nl += eng_lower_alphabet[(eng_lower_alphabet.find(i) + k % 26)]
        if i in eng_upper_alphabet:
            nl += eng_upper_alphabet[(eng_upper_alphabet.find(i) + k % 26)]
        if i.isalpha() == False:
            nl += i
    print('\nВаш зашифрованный текст:', nl)


def decryption():
    s = input(('\nНапишите текст который требуется Дешифровать: '))
    k = int(input('Ваш сдвиг шага: '))
    nl = ''
    for i in s:
        if i in rus_lower_alphabet:
            nl += rus_lower_alphabet[(rus_lower_alphabet.find(i) - k) % 32]
        if i in rus_upper_alphabet:
            nl += rus_upper_alphabet[(rus_upper_alphabet.find(i) - k % 32)]
        if i in eng_lower_alphabet:
            nl += eng_lower_alphabet[(eng_lower_alphabet.find(i) - k % 26)]
        if i in eng_upper_alphabet:
            nl += eng_upper_alphabet[(eng_upper_alphabet.find(i) - k % 26)]
        if i.isalpha() == False:
            nl += i
    print('\nВаш зашифрованный текст:', nl)


choise = input('Для шифрования напишите "Ш", для дешифрования напишите "Д": ').upper()
if choise == 'Д':
    decryption()
elif choise == 'Ш':
    enscription()