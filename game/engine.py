# Title: engine.py
# Description: Contains the Engine class for Interithmetic.
# Author: Alexander Marcozzi
# Date: 08/25/2021

import pyglet
import numpy as np
import time
import game.audio as audio
import game.colors as colors
from game.classifier import Classifier
from game.video_manager import VideoManager
from game.question_manager import QuestionManager
from game.label_manager import LabelManager

class Engine:
    """
    A class that handles moment-to-moment gameplay.

    All "magic numbers" and formulas were acquired from manual testing.

    ...

    Attributes
    ----------
    NUM_SAMPLES : int
        the number of sample images taken from the webcam before making a 
        classification
    REVEAL_TIME : double
        the time between the question ending and the answer being revealed
    DOWN_TIME : int
        the time between the answer being revealed and a new question starting
    width : int
        the width of the display, in pixels
    height : int
        the height of the display, in pixels
    num_questions : int
        the number of questions in the current game
    question_time : int
        the time available to answer each question
    question_number : int
        the question that the player is currently on
    num_correct : int
        the number of questions that the player has gotten correct so far
    frame_counter : int
        the number of frames that the engine has sampled for classification this
        cycle
    sample_counts : list(int)
        the number of times each classification has been seen this cycle
    time_left : int
        the amount of time remaining in the current question
    question_over : bool
        if the question has ended or not (the player ran out of time)
    game_over : bool
        if the game is over or not (the player has answered all questions)
    vm : VideoManager object
        handles the webcam video feed
    classifier : Classifier object
        classifies images
    qm : QuestionManager object
        generates and handles game questions
    lm : LabelManager object
        handels various labels used in the game
    end_label : pyglet label object
        holds the player's score for use printing in the end screen
    end_return_label : pyglet label object
        holds a prompt for the player to return to main menu in the end screen
    music : pyglet player object
        plays music
    
    Methods
    -------
    update(dt)
        Updates the game (dt is unused but necessary for pyglet scheduling)
    draw()
        Draws the game
    startGame(num_questions, question_time)
        Starts a new game with the specified time and number of questions
    pause()
        Pauses the game
    resume()
        Resumes the game
    cleanUp()
        Cleans up various objects and files
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        width: int
            The width of the display, in pixels
        height: int
            The height of the display, in pixels
        """

        self.NUM_SAMPLES   = 10
        self.REVEAL_TIME   = 2.5
        self.DOWN_TIME     = 3

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
        self.game_over       = False

        self.vm              = VideoManager(width, height)
        self.classifier      = Classifier('./assets/converted_keras/model.h5')
        self.qm              = QuestionManager()
        self.lm              = LabelManager(width, 
                                            height, 
                                            self.question_time, 
                                            self.num_questions)

        self.end_label = pyglet.text.Label(text = "Score: 0 / 10", 
                                           color = colors.ORANGE, 
                                           font_name = 'Calibri', 
                                           font_size = self.width * 0.10,
                                           x = width // 2, 
                                           y = height * 0.60, 
                                           anchor_x = 'center')

        self.end_return_label = pyglet.text.Label(text = "Main Menu", 
                                                  color = colors.ORANGE, 
                                                  font_name = 'Calibri', 
                                                  font_size = self.width * 0.06,
                                                  x = width // 2, 
                                                  y = height * 0.40, 
                                                  anchor_x = 'center')
    
    def update(self, dt):
        """
        Updates the game.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """

        if self.game_over:
            return

        # if the player has answered all of the questions, the game is over
        if self.question_number > self.num_questions:
            self.end_label.text = ("Score: " + str(self.num_correct) + " / " 
                                    + str(self.num_questions))
            self.game_over = True
            return

        self.frame_counter += 1
        self.vm.update(dt)
        if (self.time_left != 0):
            self.sample_counts[self.classifier.classify(
                './assets/images/frame.jpg')] += 1

            # once enough frames have been sampled, classify the response
            if (self.frame_counter >= self.NUM_SAMPLES):
                self.response = np.argmax(self.sample_counts)
                self.lm.response_label.text = str(self.response)
                self.sample_counts = [0 for i in range(6)]
                self.frame_counter = 0
        elif (self.question_over == False):
            self.endQuestion(0)

    def draw(self):
        """
        Draws the game.
        """

        if self.game_over:
            self.drawEndScreen()
        else:
            self.vm.draw()
            self.lm.draw()
    
    def drawEndScreen(self):
        """
        Draws the end screen.
        """

        self.end_label.draw()
        self.end_return_label.draw()
    
    def startGame(self, num_questions, question_time):
        """
        Starts a new game with the specified time and number of questions.

        Parameters
        ----------
        num_questions : int
            the number of questions in the new game
        question_time : int
            the time for each question in the new game
        """

        self.num_questions   = num_questions
        self.question_time   = question_time
        self.question_number = 0
        self.num_correct     = 0
        self.frame_counter   = 0
        self.sample_counts   = [0 for i in range(6)]
        self.time_left       = self.question_time
        self.question_over   = False
        self.game_over       = False

        self.lm.score_label.text = (str(self.num_correct) + ' / ' 
                                    + str(self.num_questions))

        self.music = pyglet.media.Player()
        self.music.queue(audio.music[1])

        self.newQuestion(0)

        # click the timer down every second
        pyglet.clock.schedule_once(self.tickTimer, 1)

    def setUIColor(self, color):
        """
        Sets the color of the game UI to what is specified.

        Parameters
        ----------
        color : list(int)
            RGBA color format, where values range from 0 to 255
        """

        self.lm.setLabelColors(color)
        self.vm.setBorderColor(color)

    def endQuestion(self, dt):
        """
        Ends the current question, setting the UI to white and pausing the 
        music. Schedules to check the answer.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """

        self.setUIColor(colors.WHITE)
        self.question_over = True
        self.time_left = 0
        self.lm.time_label.text = "Time: " + str(self.time_left)
        self.music.pause()
        audio.drums.play()
        pyglet.clock.schedule_once(self.checkAnswer, self.REVEAL_TIME)

    def checkAnswer(self, dt):
        """
        Checks if the player's answer is correct and responds accordingly.
        Schedules the next question.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """

        if self.response == self.qm.getAnswer():
            self.setUIColor(colors.GREEN)
            self.num_correct += 1
            self.lm.score_label.text = (str(self.num_correct) + ' / ' 
                                        + str(self.num_questions))
            audio.cheer.play()
        else:
            self.setUIColor(colors.RED)
            audio.awwww.play()
        self.lm.q_label.text = self.qm.questionToString(True)
        pyglet.clock.schedule_once(self.newQuestion, self.DOWN_TIME)
    
    def newQuestion(self, dt):
        """
        Generates a new question, resets the UI, and plays a new song.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """

        self.question_number += 1
        self.qm.generateQuestion()
        self.lm.q_label.text = self.qm.questionToString(False)
        self.setUIColor(colors.ORANGE)
        self.question_over = False
        self.time_left = self.question_time
        self.lm.top_label.text = "Question " + str(self.question_number)
        self.lm.time_label.text = "Time: " + str(self.time_left)
        self.music.queue(audio.randomSong())
        self.music.next_source()
        self.music.play()

        # no scheduling is done in this function to allow for easy pausing of
        # the game, deciding when the question is over is handled in update

    def tickTimer(self, dt):
        """
        Ticks the game timer down by one and updates the label.
        Schedules itself to run again one second later, simulating a timer.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """
        if self.time_left != 0:
            self.time_left -= 1
            self.lm.time_label.text = "Time: " + str(self.time_left)
        pyglet.clock.schedule_once(self.tickTimer, 1)
        
    def pause(self):
        """
        Pauses the game.
        """

        self.music.pause()
        pyglet.clock.unschedule(self.tickTimer)
    
    def resume(self):
        """
        Resumes the game.
        """

        self.music.play()
        pyglet.clock.schedule_once(self.tickTimer, 1)

    def cleanUp(self):
        """
        Cleans up various objects and files. Should be called before the 
        program terminates.
        """

        self.vm.cleanUp()