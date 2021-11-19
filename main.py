# Global Variables
hidden_word = []
used_words = []
num_of_tries = 0
MAX_TRIES = 6


def display_welcome_screen():
    print("""
    _     _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/""")
    print("\nDeveloped by Amittt2003\n")


def get_secret_word():
    while True:
        try:
            file_path = input("Enter file path: ")
            with open(file_path, 'r') as words_file:
                words_list = words_file.readline().split()
                break
        except:
            print("File does not exist")

    while True:
        try:
            index = int(input("Enter index: "))
            return words_list[index - 1]
        except ValueError:
            print("Invalid input! Index must be an integer")
        except IndexError:
            print("Invalid input! Index is out of range")


def is_valid_letter(user_guess):
    if len(user_guess) != 1:
        return False
    else:
        if not user_guess.isalpha():
            return False
        else:
            return True


def get_user_guess():
    user_guess = input("Guess a letter: ")

    while not is_valid_letter(user_guess):
        print("X")
        user_guess = input("Guess a letter: ")

    return user_guess.lower()


def initialize_hidden_word(secret_word_length):
    global hidden_word

    for _ in range(secret_word_length):
        hidden_word.append("_")


def display_hidden_word():
    print(' '.join(str(x) for x in hidden_word))


def update_hidden_word(user_guess, secret_word):
    global hidden_word
    hidden_word[secret_word.index(user_guess)] = user_guess


def display_used_words():
    global used_words

    used_words = sorted(used_words)
    print(' -> '.join(str(x) for x in used_words))


def get_hangman():
    if num_of_tries == 1:
        return "x-------x\n|\n|\n|\n|\n|"
    elif num_of_tries == 2:
        return """
        x-------x
        |       |
        |       0
        |
        |
        |
        """
    elif num_of_tries == 3:
        return """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """
    elif num_of_tries == 4:
        return """
         x-------x
         |       |
         |       0
         |      /|\ 
         |
         |
        """
    elif num_of_tries == 5:
        return """
         x-------x
         |       |
         |       0
         |      /|\ 
         |      /
         |
        """
    elif num_of_tries == 6:
        return """
         x-------x
         |       |
         |       0
         |      /|\ 
         |      / \ 
         |
        """


def handle_user_guess(user_guess, secret_word):
    global used_words

    if user_guess in secret_word and user_guess not in used_words:
        update_hidden_word(user_guess, secret_word)
        display_hidden_word()
        used_words.append(user_guess)
    elif user_guess in used_words:
        print("X")
        display_used_words()
    else:
        global num_of_tries
        num_of_tries += 1
        print(":(\n")
        print(get_hangman())
        display_hidden_word()
        used_words.append(user_guess)


def is_game_over(secret_word):
    if num_of_tries == MAX_TRIES:
        print("LOSE!")
        print("The secret word is: {}".format(secret_word))
        return True
    elif "".join(hidden_word) == secret_word:
        print("WIN!")
        return True
    else:
        return False


def display_start_screen(secret_word_length):
    print("Let’s start!\n")
    print("x-------x")
    initialize_hidden_word(secret_word_length)
    display_hidden_word()
    print("")


def game():
    display_welcome_screen()
    secret_word = get_secret_word()
    display_start_screen(len(secret_word))

    while not is_game_over(secret_word):
        user_guess = get_user_guess()
        handle_user_guess(user_guess, secret_word)


def main():
    game()


if __name__ == '__main__':
    main()
