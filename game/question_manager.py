# Title: question_manager.py
# Description: Contains the QuestionManager class for Interithmetic.
# Author: Alexander Marcozzi
# Date: 11/19/2021

import pyglet
import random

class QuestionManager:
    """
    A class that manages the questions used in the game, including generation,
    answer checking, and other operations

    ...

    Attributes
    ----------
    ADDITION : int
        code for if the current question is addition-based
    SUBTRACTION : int
        code for if the current question is subtraction-based
    MULTIPLICATIONS : int
        code for if the current question is multiplication-based
    first_number : int
        the first number in the equation (range: 1 - 100)
    second_number : int
        the second number in the equation (range: 1 - 2), this is the number
        that the player needs to figure out to answer the question
    third_number : int
        the third number in the equation, on the right of the equal sign
    operation : int
        the operation that the current question is based on, addition,
        subtraction, or multiplication
    
    Methods
    -------
    generateQuestion()
        Generates a new question, randomly choosing numbers and an operation
    calculateThird(color)
        Using the first two numbers and the current operation, calculates what
        the third number in the equation must be
    opToString()
        Returns a string corresponding to the current question's operation, '+'
        for addition, '-' for subtraction, and '*' for multiplication
    questionToString()
        Creates a string formatted in a game-usable way based on the current
        question's numbers and operation and returns it
    getAnswer()
        Returns the second number, the number that the player must answer the
        question with
    """

    def __init__(self):
        self.ADDITION       = 0
        self.SUBTRACTION    = 1
        self.MULTIPLICATION = 2

        self.first_number  = 0
        self.second_number = 0
        self.third_number  = 0
        self.operation     = self.ADDITION
        self.generateQuestion()
    
    def generateQuestion(self):
        """
        Generates a new question, randomly choosing numbers and an operation.
        """

        self.first_number  = random.randint(1, 100)
        self.second_number = random.randint(1, 2)  # change if 3-5 implemented
        self.operation     = random.randint(self.ADDITION, self.MULTIPLICATION)

        # prevent negative answers
        if self.operation == self.SUBTRACTION and self.first_number <= 5:
            self.first_number += 5
        self.third_number  = self.calculateThird()
    
    def calculateThird(self):
        """
        Using the first two numbers and the current operation, calculates what
        the third number in the equation must be.
        """

        if self.operation == self.ADDITION:
            return self.first_number + self.second_number
        elif self.operation == self.SUBTRACTION:
            return self.first_number - self.second_number
        else:
            return self.first_number * self.second_number

    def opToString(self):
        """
        Returns a string corresponding to the current question's operation, '+'
        for addition, '-' for subtraction, and '*' for multiplication.
        """

        if self.operation == self.ADDITION:
            return '+'
        elif self.operation == self.SUBTRACTION:
            return '-'
        else:
            return '*'
    
    def questionToString(self, showAnswer):
        """
        Creates a string formatted in a game-usable way based on the current
        question's numbers and operation and returns it.
        """

        q = str(self.first_number) + ' ' + self.opToString() + ' '
        if showAnswer:
            q += str(self.second_number) + ' '
        else:
            q += '? '
        q += '= ' + str(self.third_number)

        return q

    def getAnswer(self):
        """
        Returns the second number, the number that the player must answer the
        question with.
        """

        return self.second_number