import random
# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):

    def __init__(self):
        self.my_move = ''
        self.their_move = ''

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.their_move

    def move(self):
        x = random.choice(moves)
        if self.their_move == '':
            return x
        else:
            return self.their_move


class CyclePlayer(Player):

    def __init__(self):
        self.my_move = ''
        self.their_move = ''

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.my_move

    def move(self):
        x = random.choice(moves)
        if self.my_move == '':
            return x
        else:

            for i in range(len(moves)):
                if moves[i] == self.my_move:
                    try:
                        return moves[i+1]
                    except IndexError:
                        return moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            x = input("What's your move? rock, paper, scissors: ")
            if(x == 'rock' or x == 'paper' or x == 'scissors'):
                return x


def beats(one, two):

    if(
            one == 'rock' and two == 'scissors' or
            one == 'scissors' and two == 'paper' or
            one == 'paper' and two == 'rock'
            ):
        return "** PLAYER ONE WINS **\n"
    elif(one == two):
        return "** IT'S A TIE **\n"
    else:
        return "** PLAYER TWO WINS **\n"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1s = 0
        self.p2s = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer One threw: {move1}  Player Two threw: {move2}\n")
        print(beats(move1, move2))

        if(beats(move1, move2) == "** PLAYER ONE WINS **\n"):
            self.p1s += 1

        if(beats(move1, move2) == "** PLAYER TWO WINS **\n"):
            self.p2s += 1

        print(f"Score: Player One {self.p1s}, Player Two: {self.p2s}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!\n")
        if self.p1s > self.p2s:
            print("** Player one won the game **\n")
        elif self.p2s > self.p1s:
            print("** Player two won the game **\n")
        else:
            print("Game is a tie")


if __name__ == '__main__':
    while True:
        choose = input("""Who do you want to play against\n
        type 'random' or 'reflect' or 'cycle': """)
        if choose == 'cycle':
            game = Game(HumanPlayer(), CyclePlayer())
            break
        elif choose == 'random':
            game = Game(HumanPlayer(), RandomPlayer())
            break
        elif choose == 'reflect':
            game = Game(HumanPlayer(), ReflectPlayer())
            break
    game.play_game()
