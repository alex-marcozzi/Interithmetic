# Title: app.py
# Description: Main driver file for Interithmetic.
# Author: Alexander Marcozzi
# Date: 11/19/2021

from os import stat
import pyglet
from pyglet.window import mouse
from game.state_engine import StateEngine

#game_window = pyglet.window.Window(1000, 750)
game_window = pyglet.window.Window(fullscreen=True)

state_engine = StateEngine(game_window.width, game_window.height)
pyglet.clock.schedule_interval(state_engine.update, 0.05)

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    state_engine.handleClick(x, y, button, modifiers)

@game_window.event
def on_draw():
    game_window.clear()

    state_engine.draw()

if __name__ == '__main__':
    pyglet.app.run()

game_window.close()
state_engine.cleanUp()