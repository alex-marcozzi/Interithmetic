import pyglet
import random

class QuestionManager:
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
        self.first_number  = random.randint(1, 100)
        self.second_number = random.randint(1, 2)  # CHANGE THIS BACK TO 5
        self.operation     = random.randint(self.ADDITION, self.MULTIPLICATION)

        # prevent negative answers
        if self.operation == self.SUBTRACTION and self.first_number <= 5:
            self.first_number += 5
        self.third_number  = self.calculateThird()
    
    def calculateThird(self):
        if self.operation == self.ADDITION:
            return self.first_number + self.second_number
        elif self.operation == self.SUBTRACTION:
            return self.first_number - self.second_number
        else:
            return self.first_number * self.second_number

    def opToString(self):
        if self.operation == self.ADDITION:
            return '+'
        elif self.operation == self.SUBTRACTION:
            return '-'
        else:
            return '*'
    
    def questionToString(self, showAnswer):
        q = str(self.first_number) + ' ' + self.opToString() + ' '
        if showAnswer:
            q += str(self.second_number) + ' '
        else:
            q += '? '
        q += '= ' + str(self.third_number)

        return q

    def getAnswer(self):
        return self.second_number