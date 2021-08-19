import pyglet
from game.state_engine import StateEngine

# you have to make the font size scale with window size
game_window = pyglet.window.Window(800, 600)

state_engine = StateEngine(game_window.width, game_window.height)
#pyglet.clock.schedule_interval(engine.update, 0.05)

@game_window.event
def on_draw():
    game_window.clear()

    state_engine.draw()

# this is maybe not needed?
if __name__ == '__main__':
    pyglet.app.run()

state_engine.cleanUp()