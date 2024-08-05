# a_dice directory -> a_ice.py

"""
Title: Dice rolling program
Author: Marco Ou
Date: March 8th 2024
"""

from random import randint


class Die:
    """
    Create a die to roll for random numbers
    """

    # input (into the object)
    def __init__(self, max_sides=6):
        """
        constructor for the die object
        :param max_sides:
        """
        self.die_max = max_sides
        self.die_num = None
        self.is_even = None

    # processing
    def rollDie(self):
        """
        Update die with a new rolled number
        :return:
        """
        self.die_num = randint(1, self.die_max)

    def checkEven(self):
        """
        checks if the output is even
        :return: bool
        """
        if self.die_num % 2 == 0:
            self.is_even = True
        else:
            self.is_even = False

    # outputs

    def getEven(self):
        """
        returns whether the value is even
        :return: bool
        """
        return self.is_even

    def displayDie(self):
        """
        print the die value
        :return: None
        """
        print(self.die_num)

    def getDieValue(self):
        """
        returns the value of the die to the rest of the program
        :return: int
        """
        return self.die_num


if __name__ == "__main__":
    DIE_1 = Die()
    DIE_1.rollDie()
    DIE_1.checkEven()
    # print(DIE_1.die_num)
    DIE_1.displayDie()

    DIE_2 = Die(10)
    DIE_2.rollDie()
    print(DIE_1.getDieValue() + DIE_2.getDieValue())
