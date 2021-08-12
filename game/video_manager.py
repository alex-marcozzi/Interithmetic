import pyglet
import cv2
import os
import game.colors as colors

class VideoManager:
    def __init__(self, width, height):
        # colors.BLUE   = (19,41,75)
        # colors.ORANGE = (232,74,39)
        self.batch = pyglet.graphics.Batch()

        f = open("./assets/images/frame.jpg", "a")
        f.write("placeholder")
        f.close()
        
        pyglet.resource.path = ['./assets/images']
        pyglet.resource.reindex()

        self.width = width
        self.height = height
        self.blank_sprite = self.pathToSprite('background.jpg', self.width, self.height)
        self.frame = self.blank_sprite
        #self.border_sprite     = self.pathToSprite('border.png', self.width * 0.55, self.height * 0.55)
        self.background_rec = pyglet.shapes.Rectangle(0, 0, self.width, self.height, color = colors.BLUE[:3], batch = self.batch)
        self.border_rec = pyglet.shapes.Rectangle(self.width // 2, self.height // 2, self.width * 0.55, self.height * 0.55, color = colors.ORANGE[:3], batch = self.batch)
        self.border_rec.anchor_x = self.border_rec.width // 2
        self.border_rec.anchor_y = self.border_rec.height // 2
        # self.border_rec.x = self.width // 2
        # self.border_rec.y = self.height // 2
        #self.top_label = pyglet.text.Label(text = "Words go here", color = (232,74,39,255), font_name = 'Calibri', font_size = 48,
        #                    x = width // 2, y = height * 0.85, anchor_x = 'center')

        #self.classif = Classifier('./assets/converted_keras/model.h5')

        
        pyglet.resource.path = ['./assets/images']
        pyglet.resource.reindex()

        self.vid = cv2.VideoCapture(0)
        self.update(0)

    def update(self, dt):
        ret, self.f = self.vid.read()
        cv2.imwrite('./assets/images/frame.jpg', self.f)
        self.frame = self.blank_sprite
        self.frame = self.pathToSprite('frame.jpg', self.width // 2, self.height // 2)
        #print(self.classif.classify('./assets/images/frame.jpg'))

    def draw(self):
        self.background_rec.draw()
        self.border_rec.draw()
        #self.background_sprite.draw()
        #self.border_sprite.draw()
        #self.top_label.draw()
        self.frame.draw()

    def setBorderColor(self, color):
        self.border_rec.color = color[:3]

    def pathToSprite(self, path, width, height):
        image = pyglet.resource.image(path)
        image.width    = width
        image.height   = height
        image.anchor_x = image.width  // 2
        image.anchor_y = image.height // 2
        sprite = pyglet.sprite.Sprite(img = image, x = self.width // 2, y = self.height // 2)
        return sprite
    
    def cleanUp(self):
        self.vid.release()
        cv2.destroyAllWindows()
        if os.path.exists('./assets/images/frame.jpg'):
           os.remove('./assets/images/frame.jpg')