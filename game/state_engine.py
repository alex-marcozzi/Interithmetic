# Title: state_engine.py
# Description: Contains the StateEngine class for Interithmetic.
# Author: Alexander Marcozzi
# Date: 08/21/2021

import pyglet
import game.colors as colors
import game.audio as audio
from pyglet.window import mouse
from enum import Enum
from game.engine import Engine

class State(Enum):
    """
    An enum class representing the states of the game.
    ...
    Attributes
    ----------
    MAIN : int
        the main menu
    DIFFICULTY_SELECT : int
        the level select menu
    CREDITS : int
        the credits screen
    PLAYING : int
        the game is being played
    PAUSED : int
        the game is paused
    """

    MAIN              = 1
    DIFFICULTY_SELECT = 2
    CREDITS           = 3
    PLAYING           = 4
    PAUSED            = 5

class StateEngine:
    """
    A class that handles the state of the game, including menu traversal.

    All "magic numbers" and formulas were acquired from manual testing.

    ...

    Attributes
    ----------
    batch : pyglet graphics batch object
        graphics batch used for drawing
    width : int
        the width of the display, in pixels
    height : int
        the height of the display, in pixels
    state : State
        the current state
    engine : Engine
        the gameplay engine
    background_rec : pyglet rectangle object
        rectangle used for the application's background
    x_label : pyglet label object
        label holding specific text, where x varries depending on the purpose
    music : pyglet player object
        plays the menu music
    
    Methods
    -------
    update(dt)
        Updates the game (dt is unused but necessary for pyglet scheduling)
    draw(screen)
        Draws the current state onto the screen
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
        self.batch = pyglet.graphics.Batch()
        self.width = width
        self.height = height
        self.state = State.MAIN
        self.engine = Engine(width, height)
        self.background_rec = pyglet.shapes.Rectangle(0, 0, self.width, self.height, color = colors.BLUE[:3], batch = self.batch)
        self.back_label = pyglet.text.Label(text = "< Back", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.045,
                                x = self.width * 0.15, y = self.height * 0.10, anchor_x = 'center')
        self.pause_label = pyglet.text.Label(text = "Pause", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.045,
                                x = self.width * 0.15, y = self.height * 0.10, anchor_x = 'center')

        self.createMainLabels()
        self.createDSLabels()
        self.createCreditsLabels()
        self.createPausedLabels()
        
        self.music = pyglet.media.Player()
        self.music.queue(audio.music[0])
        self.music.play()
        
    def createMainLabels(self):
        """
        Creates the labels needed to draw the main menu.
        """

        self.main_label = pyglet.text.Label(text = "Interithmetic", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.10,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.mo1_label = pyglet.text.Label(text = "Play", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.60, anchor_x = 'center')
        self.mo2_label = pyglet.text.Label(text = "Credits", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.40, anchor_x = 'center')
        self.mo3_label = pyglet.text.Label(text = "Exit", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.20, anchor_x = 'center')

    def createDSLabels(self):
        """
        Creates the labels needed to draw the difficulty select screen.
        """

        self.DS_label = pyglet.text.Label(text = "Difficulty Select", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.10,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.dso1_label = pyglet.text.Label(text = "Easy", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.60, anchor_x = 'center')
        self.dso2_label = pyglet.text.Label(text = "Normal", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.40, anchor_x = 'center')
        self.dso3_label = pyglet.text.Label(text = "Hard", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.20, anchor_x = 'center')
        
    def createCreditsLabels(self):
        """
        Creates the labels needed to draw the credits screen.
        """

        self.credits_label = pyglet.text.Label(text = "Credits", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.10,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.co1_label = pyglet.text.Label(text = "Created by Alexander Marcozzi", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.05,
                                x = self.width // 2, y = self.height * 0.60, anchor_x = 'center')
        self.co2_label = pyglet.text.Label(text = "E-Mail: alex.marcozzi1@gmail.com", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.045,
                                x = self.width // 2, y = self.height * 0.45, anchor_x = 'center')
        self.co3_label = pyglet.text.Label(text = "GitHub: github.com/alex-marcozzi", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.045,
                                x = self.width // 2, y = self.height * 0.35, anchor_x = 'center')
        self.co4_label = pyglet.text.Label(text = "Music: see README", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.045,
                                x = self.width // 2, y = self.height * 0.20, anchor_x = 'center')
        
    def createPausedLabels(self):
        """
        Creates the labels needed to draw the paused screen.
        """
        
        self.paused_label = pyglet.text.Label(text = "Paused", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.125,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.po1_label = pyglet.text.Label(text = "Resume", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.08,
                                x = self.width // 2, y = self.height * 0.50, anchor_x = 'center')
        self.po2_label = pyglet.text.Label(text = "Main Menu", color = colors.ORANGE, font_name = 'Calibri', font_size = self.width * 0.065,
                                x = self.width // 2, y = self.height * 0.30, anchor_x = 'center')
    
    def update(self, dt):
        """
        Updates the state engine.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """
        
        # nothing to be done unless the game is being played
        if self.state == State.PLAYING:
            self.engine.update(dt)

    def draw(self):
        """
        Draws the current state.
        """

        self.background_rec.draw()
        if self.state == State.MAIN:
            self.drawMainScreen()
        elif self.state == State.DIFFICULTY_SELECT:
            self.drawDSScreen()
        elif self.state == State.CREDITS:
            self.drawCreditsScreen()
        elif self.state == State.PLAYING:
            self.engine.draw()
            if self.engine.question_over == False and self.engine.game_over == False:
                self.pause_label.draw()
        elif self.state == State.PAUSED:
            self.drawPausedScreen()

    def drawMainScreen(self):
        """
        Draws the main menu screen.
        """

        self.main_label.draw()
        self.mo1_label.draw()
        self.mo2_label.draw()
        self.mo3_label.draw()
    
    def drawDSScreen(self):
        """
        Draws the difficulty select screen.
        """
        
        self.DS_label.draw()
        self.dso1_label.draw()
        self.dso2_label.draw()
        self.dso3_label.draw()
        self.back_label.draw()
    
    def drawCreditsScreen(self):
        """
        Draws the credits screen.
        """
        
        self.credits_label.draw()
        self.co1_label.draw()
        self.co2_label.draw()
        self.co3_label.draw()
        self.co4_label.draw()
        self.back_label.draw()

    def drawPausedScreen(self):
        """
        Draws the paused screen.
        """
        
        self.paused_label.draw()
        self.po1_label.draw()
        self.po2_label.draw()
        
    def handleClick(self, x, y, button, modifiers):
        """
        Handles click events.

        Parameters
        ----------
        x: int
            The x location of the click
        y: int
            The y location of the click
        button: int
            The button that was clicked
        modifiers:
            Unused but necessary for pyglet click handling
        """
        
        if button != mouse.LEFT:
            return

        if self.state == State.MAIN:
            self.handleClickMain(x, y)
        elif self.state == State.DIFFICULTY_SELECT:
            self.handleClickDS(x, y)
        elif self.state == State.CREDITS:
            self.handleClickCredits(x, y)
        elif self.state == State.PLAYING:
            self.handleClickPlaying(x, y)
        elif self.state == State.PAUSED:
            self.handleClickPaused(x, y)
            
    def handleClickMain(self, x, y):
        """
        Handles click events for the main menu.

        Parameters
        ----------
        x: int
            The x location of the click
        y: int
            The y location of the click
        """

        if self.labelIsClicked(self.mo1_label, x, y):
            self.state = State.DIFFICULTY_SELECT
        elif self.labelIsClicked(self.mo2_label, x, y):
            self.state = State.CREDITS
        elif self.labelIsClicked(self.mo3_label, x, y):
            pyglet.app.exit()

    def handleClickDS(self, x, y):
        """
        Handles click events for the difficulty select screen.

        Parameters
        ----------
        x: int
            The x location of the click
        y: int
            The y location of the click
        """
        
        if self.labelIsClicked(self.dso1_label, x, y):
            self.music.pause()
            self.engine.startGame(10, 20)
            self.state = State.PLAYING
        elif self.labelIsClicked(self.dso2_label, x, y):
            self.music.pause()
            self.engine.startGame(10, 10)
            self.state = State.PLAYING
        elif self.labelIsClicked(self.dso3_label, x, y):
            self.music.pause()
            self.engine.startGame(10, 5)
            self.state = State.PLAYING
        elif self.labelIsClicked(self.back_label, x, y):
            self.state = State.MAIN

    def handleClickCredits(self, x, y):
        """
        Handles click events for the credits screen.

        Parameters
        ----------
        x: int
            The x location of the click
        y: int
            The y location of the click
        """
        
        if self.labelIsClicked(self.back_label, x, y):
            self.state = State.MAIN
    
    def handleClickPlaying(self, x, y):
        """
        Handles click events for when the game is being played.

        Parameters
        ----------
        x: int
            The x location of the click
        y: int
            The y location of the click
        """
        
        if self.engine.game_over == True and self.labelIsClicked(self.engine.end_return_label, x, y):
            self.engine.pause()
            self.music.queue(audio.music[0])
            self.music.next_source()
            self.music.play()
            self.state = State.MAIN
        elif self.engine.question_over != True and self.labelIsClicked(self.pause_label, x, y):
            self.engine.pause()
            self.state = State.PAUSED
    
    def handleClickPaused(self, x, y):
        """
        Handles click events for the paused screen.

        Parameters
        ----------
        x: int
            The x location of the click
        y: int
            The y location of the click
        """
        
        if self.labelIsClicked(self.po1_label, x, y):
            self.engine.resume()
            self.state = State.PLAYING
        elif self.labelIsClicked(self.po2_label, x, y):
            self.music.queue(audio.music[0])
            self.music.next_source()
            self.music.play()
            self.state = State.MAIN
    
    def labelIsClicked(self, label, x, y):
        """
        Checks if the click at location (x,y) is on the given label.

        Parameters
        ----------
        label: pyglet label object
            The label to check
        x: int
            The x location of the click
        y: int
            The y location of the click

        Returns
        -------
        True if the label was clicked on, else False
        """
        
        # these calculations are because label's anchor point is is the middle
        start_x = label.x - label.content_width // 2
        end_x   = label.x + label.content_width // 2
        start_y = label.y - label.content_height // 2
        end_y   = label.y + label.content_height // 2
        return ((start_x < x and x < end_x) and (start_y < y and y < end_y))

    def cleanUp(self):
        """
        Cleans up various objects and files. Should be called before the program terminates.
        """
        
        self.engine.cleanUp()