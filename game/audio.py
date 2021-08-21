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
# Make it so that the game actually ends when you finish the final question. Maybe have a end screen like
# SSB2. Also, add music to the main menu (if you can find the music BORE.D uses, that would be great).
# Don't forget to train the model with the other three numbers (3, 4, and 5).
# If you really want to, you can make the question generation in question_manger more complex, with more numbers
# so that you have to do more calculations to actually get the answer. Maybe not necessary though.