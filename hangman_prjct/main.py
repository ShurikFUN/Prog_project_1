import random
import time
import intro_def

pictures = ["""






=================""",
            """
             |
             |
             |
             |
             |
            =================""",
            """
             ___________
             |
             |
             |
             |
             |
            =================""",
            """
             ___________
             |     |
             |
             |
             |
             |
            =================""",
            """
             ___________
             |     |
             |     0
             |
             |
             |
            =================""",
            """
             ___________
             |     |
             |     0
             |     |
             |
             |
            =================""",
            """
             ___________
             |     |
             |     0
             |     |\\
             |
             |
            =================""",
            """
             ___________
             |     |
             |     0
             |    /|\\
             |
             |
            =================""",
            """
             ___________
             |     |
             |     0
             |    /|\\
             |      \\
             |
            =================""",
            """
             ___________
             |     |
             |      0   "First time?"
             |    /|\\ 
             |    / \\
             |         З
            ================="""]

words = ["turkey", "snow", "carol", "reindeer", "present", "wreath",
         "holly", "sleigh", "stocking",
         "mistletoe", "fireplace", "candy cane", "santa"]

max_wrong = len(pictures)
random_word = random.choice(words) # выбор слова
goal_word = list("-" * len(random_word))
wrong_amount = -1
guessed_letters = set()


def choose_hint():
    """
    принятие выбранной подсказки
    """

    while True:
        choosed_hint = input("Choose 1 or 2: ")
        if choosed_hint in {"1", "2"}:
            return choosed_hint
        print("Wrong input, please enter 1 or 2.")

def hint1(random_word, guessed_letters):
    """
    функционал первой подсказки
    """

    for letter in random_word:
        if letter not in guessed_letters:
            print(f"Hint: Try the letter '{letter}'.")

def hint2(random_word, guessed_letters):
    """
    функционал второй подсказки
    """

    chance = 0.7
    print("-Friend: Yo, let me think")
    time.sleep(3)

    if random.random() <= chance:       #сравнение рандомного шанса с выбранным
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        not_in_word = [letter for letter in alphabet if letter not in random_word and letter not in guessed_letters]

        if not_in_word:
            incorrect_letter = random.choice(not_in_word)
            print(f"-Friend: Man, im not really sure, but i think you should try letter'{incorrect_letter}'.")
    else:
        for letter in random_word:
            if letter not in guessed_letters:
                print(f"-Friend: Man, im not really sure, but i think you should try letter '{letter}'.")

def hint_use(random_word, guessed_letters):
    """
    приминение подсказки в зависимости от выбора
    """

    hint = choose_hint()
    if hint == "1":
        hint1(random_word, guessed_letters)
    else:
        hint2(random_word, guessed_letters)

def display_picture():
    """
    отображение картинки
    """

    print(pictures[wrong_amount])

def check(random_word, goal_word):
    """
    проверка ответа
    """

    global wrong_amount

    guess = input("Enter letter: ").lower()

    if guess == "hint":     # если требует подсказку
        print("1) Get one letter"
        " 2) Ring your friend")
        hint_use(random_word, guessed_letters)
        return
    if guess in guessed_letters:
        print("You already guessed that letter!")
        return

    guessed_letters.add(guess)  # Добавляем букву в список угадываемых

    if guess in random_word:    #основная проверка
        for i, letter in enumerate(random_word):
            if letter == guess:
                goal_word[i] = guess
        display_picture()
        print("Correct")
    else:       #в случае неверного ответа
        wrong_amount += 1
        display_picture()
        print("Wrong")


def main():
    """
    основная функция, запускает другие
    """

    global wrong_amount
    print("".join(goal_word))       #отобразит засекреченное слово(-----)
    while wrong_amount < max_wrong and "-" in goal_word:
        check(random_word, goal_word)
        print("".join(goal_word))

    if "-" not in goal_word:
        print("You won!")
        return
    else:
        print(f"Game over! The word was: {random_word}")

intro_def.intro()
main()
