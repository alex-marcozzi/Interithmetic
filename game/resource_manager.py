import pyglet

class ResourceManager:
    def __init__(self, background_path, font_path, width, height):
        self.width = width
        self.height = height

        background_image = pyglet.resource.image(background_path)
        background_image.width = 800
        background_image.height = 600
        background_image.anchor_x = background_image.width  // 2
        background_image.anchor_y = background_image.height // 2
        self.background_sprite = pyglet.sprite.Sprite(img = background_image, x = width // 2, y = height // 2)

        pyglet.font.add_file('./assets/fonts/MomcakeBold-WyonA.ttf')
        font = pyglet.font.load('Momcake')
        self.top_label = pyglet.text.Label(text = "Interithmetic", color = (0,0,0,255), font_name = 'Calibri', font_size = 48,
                            x = width // 2, y = height * 0.9, anchor_x = 'center')

    def draw(self):
        self.background_sprite.draw()
        self.top_label.draw()