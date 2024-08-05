"""
Title: ship captain and crew
author: Marco Ou
date: April 3rd 2024
"""

from player import Player


class Game:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.winning_gold = 0
        self.minimum_round = 0
        self.current_round = 0

    def setup(self):
        """
        gets the winning conditions for the game
        """
        print(" ### --- Welcome to Ship Captain and Crew! --- ###")
        print("Please Enter the Winning Conditions:")
        print("")
        print("Gold required to Win (Note Gold is 2* dice value): ")
        self.winning_gold = int(input("> "))
        print("Minimum rounds Played: ")
        self.minimum_round = int(input("> "))
        print(
            f"Required Gold to Win: {self.winning_gold}, and the minimum amount of rounds played to Win: {self.minimum_round}")
        confirmation = input("Please Input (Y) to confirm these numbers: > ")
        if confirmation == "Y":
            pass
        else:
            return self.setup()

    def player1Turn(self):
        print("### --- Player 1's Turn --- ###")
        self.player1.rollDice()
        self.player1.holdDie()
        self.player1.displayRolledDie()
        self.player1.displayHeldDice()
        print(f"Rolls left for Player 1: {self.player1.rolls_left}")
        self.player1.getGold()
        self.player1.resetVar()
        self.player1.displayGold()

    def player2Turn(self):
        print("### --- Player 2's Turn --- ###")
        self.player2.rollDice()
        self.player2.holdDie()
        self.player2.displayRolledDie()
        self.player2.displayHeldDice()
        print(f"Rolls left for Player 2: {self.player2.rolls_left}")
        self.player2.getGold()
        self.player2.resetVar()
        self.player2.displayGold()

    def run(self):
        """
        The majority of the game will happen here
        """
        while True:
            self.current_round += 1
            print(f"================ ROUND {self.current_round} ================")
            print("")
            self.player1Turn()
            print("")
            self.player2Turn()
            print("")
            if self.current_round >= self.minimum_round:
                if self.player1.gold >= self.winning_gold:
                    if self.player1.gold == self.player2.gold:
                        print("It is a Tie!")
                        exit()
                    print(f"Player 1 Wins! with {self.player1.gold}")
                    exit()
                elif self.player2.gold >= self.winning_gold:
                    if self.player1.gold == self.player2.gold:
                        print("It is a Tie!")
                        exit()
                    print(f"Player 2 Wins! with {self.player2.gold}")
                    exit()


if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()
