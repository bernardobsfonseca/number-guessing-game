from random import randint


def show_title():
    print('''
$$\   $$\                         $$\                                  $$$$$$\                                          $$\                     
$$$\  $$ |                        $$ |                                $$  __$$\                                         \__|                    
$$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ $$\ $$$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$ |$$  __$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |
$$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$ |$$ |  $$ |$$ |  $$ |
$$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |
\__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \______/  \______/  \_______|\_______/ \_______/ \__|\__|  \__| \____$$ |
                                                                                                                                      $$\   $$ |
                                                                                                                                      \$$$$$$  |
                                                                                                                                       \______/
    ''')


def set_number_attempts(difficulty):
    return 10 if difficulty == 'e' else 5


def show_attempts(number):
    print(f'You have {number} attempts remaining to guess the number')


def is_the_answer(resp_num, guess):
    if guess > resp_num:
        print('Too high')
        print('Guess again')
        return False
    elif guess < resp_num:
        print('Too low')
        print('Guess again')
        return False
    else:
        print('This is the answer! Congratulations!')
        return True


def number_guessing_game():
    show_title()

    resp_number = randint(1, 100)

    print('I am thinking of a number between 1 and 100')
    difficulty = input('Choose a difficult: easy(e) or hard(h): ')

    number_attempts = set_number_attempts(difficulty)

    while number_attempts > 0:
        show_attempts(number_attempts)
        guess = int(input('Make a guess: '))

        if is_the_answer(resp_number, guess):
            break

        number_attempts -= 1

        if number_attempts == 0:
            print(f'No more attempts. The number is {resp_number}')
            break


number_guessing_game()
