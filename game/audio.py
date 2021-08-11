# module file for audio

import pyglet
import random

# sound effects
drums = pyglet.media.load('./assets/sfx/drumroll.mp3', streaming=False)
cheer = pyglet.media.load('./assets/sfx/cheer.mp3', streaming=False)
awwww = pyglet.media.load('./assets/sfx/awwww.mp3', streaming=False)

# music
music = [
    pyglet.media.load('./assets/music/jeopardy.mp3', streaming=False),
    pyglet.media.load('./assets/music/rose.mp3', streaming=False)
]

# convenience functions
def randomSong():
    return music[random.randint(0,1)]