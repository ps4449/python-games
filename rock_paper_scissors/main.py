import random


def choose(ch):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    options = [rock, paper, scissors]
    return options[ch]


def decision(player, comp):
    if player == 0 and comp == 2:
        print("You win!")
    elif comp == 0 and player == 2:
        print("You lose.")
    elif comp > player:
        print("You lose.")
    elif player > comp:
        print("You win!")
    elif comp == player:
        print("Draw!")


if __name__ == '__main__':
    play_again = 1
    while play_again == 1:
        while True:
            ch_player = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
            if -1 < ch_player < 3:
                break
            else:
                print("Choose the correct option.")

        ch_computer = random.randint(0, 2)
        print("You chose:")
        print(choose(ch_player))
        print("The computer chose:")
        print(choose(ch_computer))
        decision(ch_player, ch_computer)

        play_again = int(input("Press 1 to play again, anything else to exit.\n"))
