import time
import pyglet
import cv2
from game.resource_manager import ResourceManager

game_window = pyglet.window.Window(800, 600)

rm = ResourceManager(game_window.width, game_window.height)
pyglet.clock.schedule_interval(rm.update, 0.05)

@game_window.event
def on_draw():
    game_window.clear()

    rm.draw()


# this if maybe not needed?
if __name__ == '__main__':
    pyglet.app.run()

# vid = cv2.VideoCapture(0)

# while(True):
#     ret, frame = vid.read()

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# vid.release()

# cv2.destroyAllWindows()