import pyglet
from game.classifier import Classifier
from game.resource_manager import ResourceManager
from game.question_manager import QuestionManager

class Engine:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.rm     = ResourceManager(width, height)
        self.classifier = Classifier('./assets/converted_keras/model.h5')
        self.qm = QuestionManager()
        
        self.top_label = pyglet.text.Label(text = "Words go here", color = (232,74,39,255), font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.85, anchor_x = 'center')
        self.q_label = pyglet.text.Label(text = self.qm.questionToString(False), color = (232,74,39,255), font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.10, anchor_x = 'center')
        self.response = ' '
        pyglet.clock.schedule_interval(self.checkAnswer, 10)
    
    def update(self, dt):
        self.rm.update(dt)
        self.response = self.classifier.classify('./assets/images/frame.jpg')
        #print(self.response)
        # self.qm.update(response)

    def draw(self):
        self.rm.draw()
        self.top_label.draw()
        self.q_label.draw()
        #self.qm.draw()

    def checkAnswer(self, dt):
        if self.response == self.qm.getAnswer():
            print("You got it right!")
        else:
            print("You got it wrong! You really thought the answer was " + str(self.response) + "!?!?!?!")
        self.qm.GenerateQuestion()
        self.q_label = pyglet.text.Label(text = self.qm.questionToString(False), color = (232,74,39,255), font_name = 'Calibri', font_size = 48,
                           x = self.width // 2, y = self.height * 0.10, anchor_x = 'center')

    def cleanUp(self):
        self.rm.cleanUp()