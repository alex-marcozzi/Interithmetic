import pyglet
# from game.resource_manager import ResourceManager
from game.engine import Engine

game_window = pyglet.window.Window(800, 600)

# rm = ResourceManager(game_window.width, game_window.height)
# pyglet.clock.schedule_interval(rm.update, 0.05)
engine = Engine(game_window.width, game_window.height, 10)
pyglet.clock.schedule_interval(engine.update, 0.05)

@game_window.event
def on_draw():
    game_window.clear()

    engine.draw()

# this if maybe not needed?
if __name__ == '__main__':
    pyglet.app.run()

engine.cleanUp()