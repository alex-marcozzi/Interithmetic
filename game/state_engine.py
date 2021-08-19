import pyglet
import game.colors as colors
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
        self.createTitleLabels()
        self.createDSLabels()
        self.createCreditsLabels()
        self.createPausedLabels()
        
    def createTitleLabels(self):
        self.title_label = pyglet.text.Label(text = "Interithmetic", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.85, anchor_x = 'center')
        self.to1_label = pyglet.text.Label(text = "Play", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.65, anchor_x = 'center')
        self.to2_label = pyglet.text.Label(text = "Credits", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.50, anchor_x = 'center')
        self.to3_label = pyglet.text.Label(text = "Exit", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.35, anchor_x = 'center')

    def createDSLabels(self):
        self.DS_label = pyglet.text.Label(text = "Difficulty Select", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.85, anchor_x = 'center')
        self.dso1_label = pyglet.text.Label(text = "Easy", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.65, anchor_x = 'center')
        self.dso2_label = pyglet.text.Label(text = "Normal", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.50, anchor_x = 'center')
        self.dso3_label = pyglet.text.Label(text = "Hard", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.35, anchor_x = 'center')
        
    def createCreditsLabels(self):
        self.credits_label = pyglet.text.Label(text = "Credits", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.85, anchor_x = 'center')
        self.co1_label = pyglet.text.Label(text = "Created by Alexander Marcozzi", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.65, anchor_x = 'center')
        self.co2_label = pyglet.text.Label(text = "E-Mail: alex.marcozzi1@gmail.com | github: github.com/alex-marcozzi", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.50, anchor_x = 'center')
        self.co3_label = pyglet.text.Label(text = "Music: see README", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.35, anchor_x = 'center')
        
    def createPausedLabels(self):
        self.paused_label = pyglet.text.Label(text = "Paused", color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                                x = self.width // 2, y = self.height * 0.85, anchor_x = 'center')
        self.po1_label = pyglet.text.Label(text = "Resume", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = self.width // 2, y = self.height * 0.50, anchor_x = 'center')
    
    def draw(self):
        self.background_rec.draw()
        if self.state == State.MAIN:
            self.drawTitleScreen()
        elif self.state == State.DIFFICULTY_SELECT:
            self.drawDSScreen()
        elif self.state == State.CREDITS:
            self.drawCreditsScreen()
        elif self.state == State.PLAYING:
            self.engine.draw()
        elif self.state == State.PAUSED:
            self.drawPausedScreen()

    def drawTitleScreen(self):
        self.title_label.draw()
        self.to1_label.draw()
        self.to2_label.draw()
        self.to3_label.draw()
    
    def drawDSScreen(self):
        self.DS_label.draw()
        self.dso1_label.draw()
        self.dso2_label.draw()
        self.dso3_label.draw()
    
    def drawCreditsScreen(self):
        self.credits_label.draw()
        self.co1_label.draw()
        self.co2_label.draw()
        self.co3_label.draw()

    def drawPausedScreen(self):
        self.paused_label.draw()
        self.po1_label.draw()

    def cleanUp(self):
        self.engine.cleanUp()