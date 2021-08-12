# module file for audio

import pyglet
import random

# sound effects
drums = pyglet.media.load('./assets/sfx/drumroll.mp3', streaming=False)
cheer = pyglet.media.load('./assets/sfx/cheer.mp3', streaming=False)
awwww = pyglet.media.load('./assets/sfx/awwww.mp3', streaming=False)

# music
music = [
    pyglet.media.load('./assets/music/jeopardy.mp3', streaming=False),  # Jeopardy song
    pyglet.media.load('./assets/music/rose.mp3', streaming=False),      # Rondo Brothers, Yellow Flower of Berkely
    pyglet.media.load('./assets/music/thinking.mp3', streaming=False),  # Kevin MacLeod, Thinking Music
    pyglet.media.load('./assets/music/nitro.mp3', streaming=False),     # Nitro Fun, Checkpoint
    pyglet.media.load('./assets/music/last7.mp3', streaming=False),     # oneohkay, Last 7 Letters
    pyglet.media.load('./assets/music/moon.mp3', streaming=False),      # Gecko&Tokage Parade, Moon
    pyglet.media.load('./assets/music/beat.mp3', streaming=False),      # Nujabes, Beat laments the world
    pyglet.media.load('./assets/music/prayer.mp3', streaming=False),    # Nujabes, Prayer
    pyglet.media.load('./assets/music/rush.mp3', streaming=False),      # The Seatbelts, Rush
    pyglet.media.load('./assets/music/dog.mp3', streaming=False),       # The Seatbelts, Bad Dog No Biscuits
]

# convenience functions
def randomSong():
    return music[random.randint(0,len(music)-1)]



# NOTES
# You still need to train the model with the full range of answers as well. I think you can probably
# start working on the menus, so maybe add a MenuEngine class or something, which will work a lot like in SSB2,
# with an enum class for knowing what the game state is (MAIN, CREDITS, DIFFICULTY_SELECT, PAUSED, PLAYING).
# Also, add another parameter to the Engine constructor, which is the number of seconds per questions. This can
# be used to implement difficutly settings, like 30 seconds for easy, 10 seconds for normal, and 5 for hard, or
# something like that. 