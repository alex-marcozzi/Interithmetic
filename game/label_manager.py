import pyglet
import game.colors as colors

class LabelManager:
    def __init__(self, width, height, time):
        self.width         = width
        self.height        = height

        self.top_label = pyglet.text.Label(text = "Words", color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                                x = width // 2, y = height * 0.85, anchor_x = 'center')
        self.q_label = pyglet.text.Label(text = '________', color = colors.ORANGE, font_name = 'Calibri', font_size = 48,
                           x = width // 2, y = height * 0.10, anchor_x = 'center')
        self.response_label = pyglet.text.Label(text = str(0), color = colors.ORANGE, font_name = 'Calibri', font_size = 64,
                           x = width * 0.10, y = height * 0.50, anchor_x = 'center')
        self.time_label = pyglet.text.Label(text = "Time: " + str(time), color = colors.ORANGE, font_name = 'Calibri', font_size = 36,
                           x = width * 0.85, y = height * 0.85, anchor_x = 'center')
    
    def draw(self):
        self.top_label.draw()
        self.q_label.draw()
        self.response_label.draw()
        self.time_label.draw()

    def setLabelColors(self, color):
        self.top_label.color      = color
        self.q_label.color        = color
        self.response_label.color = color
        self.time_label.color     = color