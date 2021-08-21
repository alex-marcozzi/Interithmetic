import pyglet
import game.colors as colors
from pyglet.window import mouse
from enum import Enum
from game.engine import Engine

class State(Enum):
    MAIN              = 1
    DIFFICULTY_SELECT = 2
    CREDITS           = 3
    PLAYING           = 4
    PAUSED            = 5

class StateEngine:
    def __init__(self, width, height):
        self.batch = pyglet.graphics.Batch()
        self.width = width
        self.height = height
        self.state = State.MAIN
        self.engine = Engine(width, height)
        self.background_rec = pyglet.shapes.Rectangle(0, 0, self.width, self.height, color = colors.BLUE[:3], batch = self.batch)
        self.back_label = pyglet.text.Label(text = "< Back", color = colors.ORANGE, font_name = 'Calibri', font_size = 36,
                                x = self.width * 0.15, y = self.height * 0.10, anchor_x = 'center')
        self.pause_label = pyglet.text.Label(text = "Pause", color = colors.ORANGE, font_name = 'Calibri', font_size = 36,
                                x = self.width * 0.15, y = self.height * 0.10, anchor_x = 'center')
        self.createMainLabels()
        self.createDSLabels()
        self.createCreditsLabels()
        self.createPausedLabels()
        
    def createMainLabels(self):
        self.main_label = pyglet.text.Label(text = "Interithmetic", color = colors.ORANGE, font_name = 'Calibri', font_size = 80,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.mo1_label = pyglet.text.Label(text = "Play", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.60, anchor_x = 'center')
        self.mo2_label = pyglet.text.Label(text = "Credits", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.40, anchor_x = 'center')
        self.mo3_label = pyglet.text.Label(text = "Exit", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.20, anchor_x = 'center')

    def createDSLabels(self):
        self.DS_label = pyglet.text.Label(text = "Difficulty Select", color = colors.ORANGE, font_name = 'Calibri', font_size = 80,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.dso1_label = pyglet.text.Label(text = "Easy", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.60, anchor_x = 'center')
        self.dso2_label = pyglet.text.Label(text = "Normal", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.40, anchor_x = 'center')
        self.dso3_label = pyglet.text.Label(text = "Hard", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.20, anchor_x = 'center')
        
    def createCreditsLabels(self):
        self.credits_label = pyglet.text.Label(text = "Credits", color = colors.ORANGE, font_name = 'Calibri', font_size = 80,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.co1_label = pyglet.text.Label(text = "Created by Alexander Marcozzi", color = colors.ORANGE, font_name = 'Calibri', font_size = 42,
                                x = self.width // 2, y = self.height * 0.60, anchor_x = 'center')
        self.co2_label = pyglet.text.Label(text = "E-Mail: alex.marcozzi1@gmail.com", color = colors.ORANGE, font_name = 'Calibri', font_size = 36,
                                x = self.width // 2, y = self.height * 0.45, anchor_x = 'center')
        self.co3_label = pyglet.text.Label(text = "GitHub: github.com/alex-marcozzi", color = colors.ORANGE, font_name = 'Calibri', font_size = 36,
                                x = self.width // 2, y = self.height * 0.35, anchor_x = 'center')
        self.co4_label = pyglet.text.Label(text = "Music: see README", color = colors.ORANGE, font_name = 'Calibri', font_size = 36,
                                x = self.width // 2, y = self.height * 0.20, anchor_x = 'center')
        
    def createPausedLabels(self):
        self.paused_label = pyglet.text.Label(text = "Paused", color = colors.ORANGE, font_name = 'Calibri', font_size = 100,
                                x = self.width // 2, y = self.height * 0.80, anchor_x = 'center')
        self.po1_label = pyglet.text.Label(text = "Resume", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.50, anchor_x = 'center')
        self.po2_label = pyglet.text.Label(text = "Main Menu", color = colors.ORANGE, font_name = 'Calibri', font_size = 52,
                                x = self.width // 2, y = self.height * 0.30, anchor_x = 'center')
    
    def draw(self):
        self.background_rec.draw()
        if self.state == State.MAIN:
            self.drawMainScreen()
        elif self.state == State.DIFFICULTY_SELECT:
            self.drawDSScreen()
        elif self.state == State.CREDITS:
            self.drawCreditsScreen()
        elif self.state == State.PLAYING:
            self.engine.draw()
            if self.engine.question_over == False:
                self.pause_label.draw()
        elif self.state == State.PAUSED:
            self.drawPausedScreen()

    def drawMainScreen(self):
        self.main_label.draw()
        self.mo1_label.draw()
        self.mo2_label.draw()
        self.mo3_label.draw()
    
    def drawDSScreen(self):
        self.DS_label.draw()
        self.dso1_label.draw()
        self.dso2_label.draw()
        self.dso3_label.draw()
        self.back_label.draw()
    
    def drawCreditsScreen(self):
        self.credits_label.draw()
        self.co1_label.draw()
        self.co2_label.draw()
        self.co3_label.draw()
        self.co4_label.draw()
        self.back_label.draw()

    def drawPausedScreen(self):
        self.paused_label.draw()
        self.po1_label.draw()
        self.po2_label.draw()

    def update(self, dt):
        if self.state == State.PLAYING:
            self.engine.update(dt)
        
    def handleClick(self, x, y, button, modifiers):
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
        if self.labelIsClicked(self.mo1_label, x, y):
            self.state = State.DIFFICULTY_SELECT
        elif self.labelIsClicked(self.mo2_label, x, y):
            self.state = State.CREDITS
        elif self.labelIsClicked(self.mo3_label, x, y):
            pyglet.app.exit()

    def handleClickDS(self, x, y):
        if self.labelIsClicked(self.dso1_label, x, y):
            self.engine.startGame(10, 20)
            self.state = State.PLAYING
        elif self.labelIsClicked(self.dso2_label, x, y):
            self.engine.startGame(10, 10)
            self.state = State.PLAYING
        elif self.labelIsClicked(self.dso3_label, x, y):
            self.engine.startGame(10, 5)
            self.state = State.PLAYING
        elif self.labelIsClicked(self.back_label, x, y):
            self.state = State.MAIN

    def handleClickCredits(self, x, y):
        if self.labelIsClicked(self.back_label, x, y):
            self.state = State.MAIN
    
    def handleClickPlaying(self, x, y):
        if self.engine.question_over == True:
            return
        if self.labelIsClicked(self.pause_label, x, y):
            self.engine.pause()
            self.state = State.PAUSED
    
    def handleClickPaused(self, x, y):
        if self.labelIsClicked(self.po1_label, x, y):
            self.engine.resume()
            self.state = State.PLAYING
        elif self.labelIsClicked(self.po2_label, x, y):
            self.state = State.MAIN
    
    def labelIsClicked(self, label, x, y):
        # these calculations are because label's anchor point is is the middle
        start_x = label.x - label.content_width // 2
        end_x   = label.x + label.content_width // 2
        start_y = label.y - label.content_height // 2
        end_y   = label.y + label.content_height // 2
        return ((start_x < x and x < end_x) and (start_y < y and y < end_y))

    def cleanUp(self):
        self.engine.cleanUp()