from os import stat
import pyglet
from pyglet.window import mouse
from game.state_engine import StateEngine

# you have to make the font size scale with window size
game_window = pyglet.window.Window(800, 600)

state_engine = StateEngine(game_window.width, game_window.height)
#pyglet.clock.schedule_interval(engine.update, 0.05)

# maybe add this for menu option highlighting as a stretch goal
# @game_window.event
# def on_mouse_motion(x, y, dx, dy):
#     state_engine.handleMove(x, y, dx, dy)

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    state_engine.handleClick(x, y, button, modifiers)

@game_window.event
def on_draw():
    game_window.clear()

    state_engine.draw()

# this is maybe not needed?
if __name__ == '__main__':
    pyglet.app.run()

game_window.close()
state_engine.cleanUp()