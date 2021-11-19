# Title: label_manager.py
# Description: Contains the LabelManager class for Interithmetic.
# Author: Alexander Marcozzi
# Date: 11/19/2021

import pyglet
import game.colors as colors

class LabelManager:
    """
    A class that manages (most of) the labels used by the game, allowing the
    engine to easily update the text and color of the UI.

    ...

    Attributes
    ----------
    width : int
        the width of the display, in pixels
    height : int
        the height of the display, in pixels
    top_label : pyglet label object
        the label for the current question at the top of the screen
    q_label : pyglet label object
        the label for the question the player must answer
    response_label : pyglet label object
        the label for the player's current response
    time_label : pyglet label object
        the label for the current time
    score_label : pyglet label object
        the label for the player's current score
    
    Methods
    -------
    draw()
        Draws all labels
    setLabelColors(color)
        Sets the color of each label to the one specified
    """

    def __init__(self, width, height, time, num_questions):
        """
        Parameters
        ----------
        width: int
            The width of the display, in pixels
        height: int
            The height of the display, in pixels
        time: int
            The number of seconds for the time label
        num_questions: int
            The number of questions in the current game
        """

        self.width  = width
        self.height = height

        self.top_label = pyglet.text.Label(text = "Question 1", 
                                          color = colors.ORANGE, 
                                          font_name = 'Calibri', 
                                          font_size = self.width * 0.06, 
                                          x = width // 2, 
                                          y = height * 0.85, 
                                          anchor_x = 'center')

        self.q_label = pyglet.text.Label(text = '________', 
                                         color = colors.ORANGE, 
                                         font_name = 'Calibri', 
                                         font_size = self.width * 0.06, 
                                         x = width // 2, 
                                         y = height * 0.10, 
                                         anchor_x = 'center')

        self.response_label = pyglet.text.Label(text = str(0), 
                                                color = colors.ORANGE, 
                                                font_name = 'Calibri', 
                                                font_size = self.width * 0.08,
                                                x = width * 0.10, 
                                                y = height * 0.50, 
                                                anchor_x = 'center')

        self.time_label = pyglet.text.Label(text = "Time: " + str(time), 
                                            color = colors.ORANGE, 
                                            font_name = 'Calibri', 
                                            font_size = self.width * 0.045,
                                            x = width * 0.85, 
                                            y = height * 0.85, 
                                            anchor_x = 'center')

        self.score_label = pyglet.text.Label(text = "0 / " + str(num_questions), 
                                             color = colors.ORANGE, 
                                             font_name = 'Calibri', 
                                             font_size = self.width * 0.045,
                                             x = width * 0.15, 
                                             y = height * 0.85, 
                                             anchor_x = 'center')
    
    def draw(self):
        """
        Draws the labels.
        """

        self.top_label.draw()
        self.q_label.draw()
        self.response_label.draw()
        self.time_label.draw()
        self.score_label.draw()

    def setLabelColors(self, color):
        """
        Sets the color of each label to the one specified.

        Parameters
        ----------
        color : tuple(4)
            the color to set the labels to, in RGBA format (0-255 for each)
        """
        
        self.top_label.color      = color
        self.q_label.color        = color
        self.response_label.color = color
        self.time_label.color     = color
        self.score_label.color    = color