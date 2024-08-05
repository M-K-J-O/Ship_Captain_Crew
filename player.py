# player.py in a_dice folder

"""
Title: Player Program
Author: Marco Ou
Date: March 12th 2024
"""
from a_dice import Die


class Player:
    """
    The player for the game Ship Captain Crew
    """

    def __init__(self):
        """
        Attributes for the player
        :return:
        """
        self.gold = 0
        self.dice = []
        for i in range(5):
            self.dice.append(Die())
        self.dice_held = []
        self.rolls_left = 3
        self.ship = False
        self.captain = False
        self.can_get_gold = False

    # Methods --> Behaviours

    def resetVar(self):
        """
        Resets variables after turn is over
        """
        self.dice = []
        for i in range(5):
            self.dice.append(Die())
        self.dice_held = []
        self.rolls_left = 3
        self.ship = False
        self.captain = False
        self.can_get_gold = False

    def getGold(self):
        """
        Gets gold for the player if can_get_gold = True
        Also re-rolls dice
        """
        if self.can_get_gold:
            GOLD = self.dice[0].getDieValue() + self.dice[1].getDieValue()
            print(f"Possible Gold to Gain {GOLD * 2}")
        if self.rolls_left > 0:
            print("Re-roll Dice? (Y/N) ")
            reroll = input("> ")
            if reroll == "Y":
                self.rollDice()
                self.holdDie()
                self.displayRolledDie()
                self.displayHeldDice()
                self.getGold()
            if reroll == "N" or self.rolls_left == 0:
                if self.can_get_gold:
                    self.addToGold()
                self.rolls_left = 0
            else:
                return self.getGold()
        elif not self.can_get_gold:
            print("Gold gained: 0")

    def holdDie(self):
        """
        Holds Dice Values if they = 6, then 5, then 4
        """
        cube = 0
        while cube <= len(self.dice) - 1:
            if 6 == self.dice[cube].getDieValue() or self.ship:
                if not self.ship:
                    self.dice_held.append(self.dice.pop(cube))
                    cube = 0
                self.ship = True
                if 5 == self.dice[cube].getDieValue() or self.captain:
                    if not self.captain:
                        self.dice_held.append(self.dice.pop(cube))
                        cube = 0
                    self.captain = True
                    if 4 == self.dice[cube].getDieValue() or self.can_get_gold:
                        if not self.can_get_gold:
                            self.dice_held.append(self.dice.pop(cube))
                            cube = 0
                        self.can_get_gold = True
            cube += 1

    def rollDice(self):
        """
        rolls dice
        """
        if self.rolls_left > 0:
            for i in range(len(self.dice)):
                self.dice[i].rollDie()
            self.rolls_left -= 1

    def addToGold(self):
        """
        adds gold
        :param NEW_GOLD: int
        :return: None
        """
        self.gold += self.dice[0].getDieValue() + self.dice[1].getDieValue()

    def displayRolledDie(self):
        print("Dice Rolled: ")
        for cube in self.dice:
            cube.displayDie()

    def displayGold(self):
        print(f" Current Gold: {self.gold}")

    def displayHeldDice(self):
        """
        displays Dice Held in hand (6, 5, 4)
        :return: None
        """
        dice_in_held = ""
        for cube in self.dice_held:
            dice_in_held += str(cube.getDieValue())
            dice_in_held += ", "
        print(f"Held Dice: {dice_in_held}")
        if len(self.dice_held) > 0:
            pass


if __name__ == "__main__":
    MARCO = Player()
    MARCO.rollDice()
    MARCO.holdDie()
    MARCO.displayRolledDie()
    MARCO.displayHeldDice()
    print(f"Rolls left for MARCO {MARCO.rolls_left}")
    MARCO.getGold()
