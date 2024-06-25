import random


def create_list():
    try:
        with open("dictionary.txt", encoding="utf-8") as file:
            lst = file.readlines()
    except FileNotFoundError:
        print("Файл не найден. Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")

    lst = [x.lower().strip().split() for x in lst]
    lst = [x[1] for x in lst if len(x[1]) > 5]

    return lst


def show_hangman(mstk, hm_list):
    """ Функция по отображению текущего состояния виселицы """

    if mstk == 1:
        hm_list[2] = '|     O    '
    elif mstk == 2:
        hm_list[3] = '|  ---+    '
    elif mstk == 3:
        hm_list[3] = '|  ---+--- '
    elif mstk == 4:
        hm_list[4] = '|     ^    '
    elif mstk == 5:
        hm_list[5] = '|    /     '
    elif mstk == 6:
        hm_list[5] = '|    / \   '

    print("\nТекущее состояние виселицы:")
    for x in hm_list:
        print(x)


def find_letter_in_word(random_word, player_word, letter, mstk, wl_list):
    """ Функция по поиску введенной буквы в слове """

    rand_word = list(random_word)
    play_word = list(player_word)
    if letter in rand_word:
        for i, x in enumerate(rand_word):
            if letter == x:
                play_word[i] = x
    else:
        mstk += 1
        wl_list.append(letter)
    word = ''
    for x in play_word:
        word += x

    return word, mstk, wl_list


def run_main_app():
    """ Основная функция приложения """

    wrong_letters_list = []
    words_list = create_list()
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    hangman_list = ['+-----+    ',
                    '|     |    ',
                    '|          ',
                    '|          ',
                    '|          ',
                    '|          ',
                    '|          ',
                    '+----------']
    random_word = random.choice(words_list)
    player_word = random_word[0] + ('_' * (len(random_word) - 2)) + random_word[-1]
    mstk = 0
    print(f'Текущее слово: {player_word}')

    while mstk < 6:
        letter = input('Введите ОДНУ букву: ').lower().strip()

        if letter not in alph or len(letter) != 1:
            print('Ошибка ввода. Пожалуйста введите ОДНУ букву русского алфавита')
        elif letter in wrong_letters_list:
            print("Данная буква уже была введена и отсутствует в слове. Пожалуйста введите другую букву")
        else:
            player_word, mstk, wrong_letters_list = find_letter_in_word(random_word, player_word, letter, mstk, wrong_letters_list)
            show_hangman(mstk, hangman_list)

            if mstk < 6:
                print(f'Текущее слово: {player_word}, кол-во ошибок: {mstk}, осталось попыток: {6 - mstk}')
            else:
                print(f'Кол-во ошибок: {mstk}')
                print('Поражение. Игра окончена\n')

            if random_word == player_word:
                print(f'Загаданное слово: {random_word}')
                print('Победа! Игра окончена\n')
                break

    #mstk = 0


if __name__ == '__main__':
    command = ""

    while command != '0':
        print("Нажмите 1, чтобы начать новую игру")
        print("Нажмите 0, чтобы выйти из приложения")
        command = input("Выберите номер команды из списка: ")

        while command not in ['0', '1']:
            print("Ошибка ввода. Пожалуйста введите значение равное 0 или 1")
            command = input("Выберите номер команды из списка: ")

        if command == '1':
            run_main_app()  # Запуск основной функции программы