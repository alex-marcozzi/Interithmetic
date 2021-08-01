import pyglet
import cv2
import os
import time

class ResourceManager:
    def __init__(self, width, height):
        f = open("./assets/images/frame.jpg", "a")
        f.write("placeholder")
        f.close()
        
        pyglet.resource.path = ['./assets/images']
        pyglet.resource.reindex()

        self.width = width
        self.height = height
        self.background_sprite = self.pathToSprite('background.jpg', self.width, self.height)
        self.top_label = pyglet.text.Label(text = "Words go here", color = (0,0,0,255), font_name = 'Calibri', font_size = 48,
                            x = width // 2, y = height * 0.9, anchor_x = 'center')

        
        pyglet.resource.path = ['./assets/images']
        pyglet.resource.reindex()

        self.vid = cv2.VideoCapture(0)
        self.update(0)

    def update(self, dt):
        ret, self.f = self.vid.read()
        cv2.imwrite('./assets/images/frame.jpg', self.f)
        self.frame = self.background_sprite
        self.frame = self.pathToSprite('frame.jpg', self.width // 2, self.height // 2)

    def draw(self):
        self.background_sprite.draw()
        self.top_label.draw()
        self.frame.draw()

    def pathToSprite(self, path, width, height):
        image = pyglet.resource.image(path)
        image.width    = width
        image.height   = height
        image.anchor_x = image.width  // 2
        image.anchor_y = image.height // 2
        sprite = pyglet.sprite.Sprite(img = image, x = self.width // 2, y = self.height // 2)
        return sprite

    def __del__(self):
        print("destructing")
        self.vid.release()
        cv2.destroyAllWindows()
        if os.path.exists('./assets/images/frame.jpg'):
           os.remove('./assets/images/frame.jpg')