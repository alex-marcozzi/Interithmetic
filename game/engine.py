import pyglet
import numpy as np
import game.audio as audio
import game.colors as colors
from game.classifier import Classifier
from game.video_manager import VideoManager
from game.question_manager import QuestionManager
from game.label_manager import LabelManager

class Engine:
    def __init__(self, width, height):
        self.NUM_SAMPLES   = 10
        self.REVEAL_TIME   = 2.5  # the time between the question ending and the answer being reveled
        self.DOWN_TIME     = 3    # the time between the answer being revealed and a new question starting

        self.width           = width
        self.height          = height
        self.num_questions   = 0
        self.question_time   = 0
        self.question_number = 0
        self.num_correct     = 0
        self.frame_counter   = 0
        self.sample_counts   = [0 for i in range(6)]
        self.time_left       = self.question_time
        self.question_over   = False

        self.vm              = VideoManager(width, height)
        self.classifier      = Classifier('./assets/converted_keras/model.h5')
        self.qm              = QuestionManager()
        self.lm              = LabelManager(width, height, self.question_time, self.num_questions)

        # self.music = pyglet.media.Player()
        # self.music.queue(audio.music[0])

        # self.newQuestion(0)

        # pyglet.clock.schedule_interval(self.tickTimer, 1)
    
    def update(self, dt):
        self.frame_counter += 1
        self.vm.update(dt)
        if (self.question_over == False):
            self.sample_counts[self.classifier.classify('./assets/images/frame.jpg')] += 1
            if (self.frame_counter >= self.NUM_SAMPLES):
                self.response = np.argmax(self.sample_counts)
                self.lm.response_label.text = str(self.response)
                self.sample_counts = [0 for i in range(6)]
                self.frame_counter = 0

    def draw(self):
        self.vm.draw()
        self.lm.draw()
    
    def startGame(self, num_questions, question_time):
        self.num_questions   = num_questions
        self.question_time   = question_time
        self.question_number = 0
        self.num_correct     = 0
        self.frame_counter   = 0
        self.sample_counts   = [0 for i in range(6)]
        self.time_left       = self.question_time
        self.question_over   = False

        self.music = pyglet.media.Player()
        self.music.queue(audio.music[0])

        self.newQuestion(0)

        pyglet.clock.schedule_interval(self.tickTimer, 1)

    def setUIColor(self, color):
        self.lm.setLabelColors(color)
        self.vm.setBorderColor(color)

    def endQuestion(self, dt):
        self.setUIColor(colors.WHITE)
        self.question_over = True
        self.time_left = 0
        self.lm.time_label.text = "Time: " + str(self.time_left)
        self.music.pause()
        audio.drums.play()
        pyglet.clock.schedule_once(self.checkAnswer, self.REVEAL_TIME)

    def checkAnswer(self, dt):
        if self.response == self.qm.getAnswer():
            self.setUIColor(colors.GREEN)
            self.num_correct += 1
            self.lm.score_label.text = str(self.num_correct) + ' / ' + str(self.num_questions)
            audio.cheer.play()
        else:
            self.setUIColor(colors.RED)
            audio.awwww.play()
        self.lm.q_label.text = self.qm.questionToString(True)
        pyglet.clock.schedule_once(self.newQuestion, self.DOWN_TIME)
    
    def newQuestion(self, dt):
        self.question_number += 1
        self.qm.generateQuestion()
        self.lm.q_label.text = self.qm.questionToString(False)
        self.lm.top_label.text = "Question " + str(self.question_number)
        self.setUIColor(colors.ORANGE)
        self.question_over = False
        self.time_left = self.question_time
        self.music.queue(audio.randomSong())
        self.music.next_source()
        self.music.play()
        pyglet.clock.schedule_once(self.endQuestion, self.question_time)

    def tickTimer(self, dt):
        if self.time_left != 0:
            self.time_left -= 1
            self.lm.time_label.text = "Time: " + str(self.time_left)

    def cleanUp(self):
        self.vm.cleanUp()