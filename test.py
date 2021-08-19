import pyglet
from game.engine import Engine

# you have to make the font size scale with window size
game_window = pyglet.window.Window(800, 600)

engine = Engine(game_window.width, game_window.height)
engine.startGame(10, 10)
pyglet.clock.schedule_interval(engine.update, 0.05)

@game_window.event
def on_draw():
    game_window.clear()

    engine.draw()

# this is maybe not needed?
if __name__ == '__main__':
    pyglet.app.run()

engine.cleanUp()