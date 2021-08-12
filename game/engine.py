import pyglet
import numpy as np
import game.audio as audio
from game.classifier import Classifier
from game.video_manager import VideoManager
from game.question_manager import QuestionManager

class Engine:
    def __init__(self, width, height):
        self.ORANGE        = (232,74,39,255)
        self.GREEN         = (0,255,0,255)
        self.RED           = (255,0,0,255)
        self.WHITE         = (255,255,255,255)
        self.NUM_SAMPLES   = 10
        self.QUESTION_TIME = 10
        self.REVEAL_TIME   = 2.5  # the time between the question ending and the answer being reveled
        self.DOWN_TIME     = 3  # the time between the answer being revealed and a new question starting

        self.width         = width
        self.height        = height
        self.rm            = VideoManager(width, height)
        self.classifier    = Classifier('./assets/converted_keras/model.h5')
        self.qm            = QuestionManager()
        self.frame_counter = 0
        self.sample_counts = [0 for i in range(6)]
        self.question_over = False
        self.time_left     = self.QUESTION_TIME

        
        self.top_label = pyglet.text.Label(text = "Words", color = self.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.85, anchor_x = 'center')
        self.q_label = pyglet.text.Label(text = self.qm.questionToString(False), color = self.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.10, anchor_x = 'center')
        self.response = 0
        self.response_label = pyglet.text.Label(text = str(self.response), color = self.ORANGE, font_name = 'Calibri', font_size = 64,
                           x = width * 0.10, y = height * 0.50, anchor_x = 'center')
        self.time_label = pyglet.text.Label(text = "Time: " + str(self.time_left), color = self.ORANGE, font_name = 'Calibri', font_size = 36,
                           x = width * 0.85, y = height * 0.85, anchor_x = 'center')

        self.music = pyglet.media.Player()
        self.music.queue(audio.music[0])

        self.newQuestion(0)

        # self.drums = pyglet.media.load('./assets/sfx/drumroll.mp3', streaming=False)
        # self.cheer = pyglet.media.load('./assets/sfx/cheer.mp3')
        # self.awwww = pyglet.media.load('./assets/sfx/awwww.mp3')

        pyglet.clock.schedule_once(self.endQuestion, self.QUESTION_TIME)
        pyglet.clock.schedule_interval(self.tickTimer, 1)
    
    def update(self, dt):
        self.frame_counter += 1
        self.rm.update(dt)
        if (self.question_over == False):
            self.sample_counts[self.classifier.classify('./assets/images/frame.jpg')] += 1
            if (self.frame_counter >= self.NUM_SAMPLES):
                self.response = np.argmax(self.sample_counts)
                self.response_label.text = str(self.response)
                self.sample_counts = [0 for i in range(6)]
                self.frame_counter = 0
        #print(self.response)
        # self.qm.update(response)

    def draw(self):
        self.rm.draw()
        self.top_label.draw()
        self.q_label.draw()
        self.response_label.draw()
        self.time_label.draw()

    def setUIColor(self, color):
        self.top_label.color      = color
        self.q_label.color        = color
        self.response_label.color = color
        self.time_label.color     = color
        self.rm.setBorderColor(color[:3])

    def endQuestion(self, dt):
        # pause music here, play sound effect
        self.setUIColor(self.WHITE)
        self.question_over = True
        self.time_left = 0
        self.time_label.text = "Time: " + str(self.time_left)
        self.music.pause()
        audio.drums.play()
        pyglet.clock.schedule_once(self.checkAnswer, self.REVEAL_TIME)

    def checkAnswer(self, dt):
        if self.response == self.qm.getAnswer():
            self.setUIColor(self.GREEN)
            audio.cheer.play()
        else:
            self.setUIColor(self.RED)
            audio.awwww.play()
        self.q_label.text = self.qm.questionToString(True)
        pyglet.clock.schedule_once(self.newQuestion, self.DOWN_TIME)
    
    def newQuestion(self, dt):
        self.qm.generateQuestion()
        self.q_label.text = self.qm.questionToString(False)
        self.setUIColor(self.ORANGE)
        self.question_over = False
        self.time_left = self.QUESTION_TIME
        self.music.queue(audio.randomSong())
        self.music.next_source()
        self.music.play()
        pyglet.clock.schedule_once(self.endQuestion, self.QUESTION_TIME)

    def tickTimer(self, dt):
        if self.time_left != 0:
            self.time_left -= 1
            self.time_label.text = "Time: " + str(self.time_left)

    def cleanUp(self):
        self.rm.cleanUp()