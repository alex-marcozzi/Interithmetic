import pyglet
import numpy as np
from game.classifier import Classifier
from game.resource_manager import ResourceManager
from game.question_manager import QuestionManager

class Engine:
    def __init__(self, width, height):
        self.ORANGE        = (232,74,39,255)
        self.NUM_SAMPLES   = 10
        self.QUESTION_TIME = 10
        self.DOWN_TIME     = 3

        self.width         = width
        self.height        = height
        self.rm            = ResourceManager(width, height)
        self.classifier    = Classifier('./assets/converted_keras/model.h5')
        self.qm            = QuestionManager()
        self.counter       = 0
        self.sample_counts = [0 for i in range(6)]
        
        self.top_label = pyglet.text.Label(text = "Words go here", color = self.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.85, anchor_x = 'center')
        self.q_label = pyglet.text.Label(text = self.qm.questionToString(False), color = self.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.10, anchor_x = 'center')
        self.response = 0
        self.response_label = pyglet.text.Label(text = str(self.response), color = self.ORANGE, font_name = 'Calibri', font_size = 64,
                           x = width * 0.10, y = height * 0.50, anchor_x = 'center')
        pyglet.clock.schedule_once(self.checkAnswer, self.QUESTION_TIME)
    
    def update(self, dt):
        self.counter += 1
        self.rm.update(dt)
        self.sample_counts[self.classifier.classify('./assets/images/frame.jpg')] += 1
        if (self.counter >= self.NUM_SAMPLES):
            self.response = np.argmax(self.sample_counts)
            self.response_label = pyglet.text.Label(text = str(self.response), color = self.ORANGE, font_name = 'Calibri', font_size = 64,
                            x = self.width * 0.10, y = self.height * 0.50, anchor_x = 'center')
            self.sample_counts = [0 for i in range(6)]
            self.counter = 0
        #print(self.response)
        # self.qm.update(response)

    def draw(self):
        self.rm.draw()
        self.top_label.draw()
        self.q_label.draw()
        self.response_label.draw()

    def checkAnswer(self, dt):
        if self.response == self.qm.getAnswer():
            print("You got it right!")
        else:
            print("You got it wrong! You really thought the answer was " + str(self.response) + "?!?!")
        self.q_label = pyglet.text.Label(text = self.qm.questionToString(True), color = self.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = self.width // 2, y = self.height * 0.10, anchor_x = 'center')
        pyglet.clock.schedule_once(self.newQuestion, 3)
    
    def newQuestion(self, dt):
        self.qm.generateQuestion()
        self.q_label = pyglet.text.Label(text = self.qm.questionToString(False), color = self.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = self.width // 2, y = self.height * 0.10, anchor_x = 'center')
        pyglet.clock.schedule_once(self.checkAnswer, self.QUESTION_TIME)


    def cleanUp(self):
        self.rm.cleanUp()