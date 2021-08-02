from game.classifier import Classifier
from game.resource_manager import ResourceManager

class Engine:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.rm     = ResourceManager(width, height)
        self.classifier = Classifier('./assets/converted_keras/model.h5')
        # self.qm = QuestionManager()
    
    def update(self, dt):
        self.rm.update(dt)
        response = self.classifier.classify('./assets/images/frame.jpg')
        print(response)
        # self.qm.update(response)

    def draw(self):
        self.rm.draw()
        # self.qm.draw()
        
    def cleanUp(self):
        self.rm.cleanUp()