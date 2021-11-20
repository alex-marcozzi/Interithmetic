# Title: audio.py
# Description: Module file for audio used in Interithmetic.
# Author: Alexander Marcozzi
# Date: 11/19/2021

import pyglet
import random

# sound effects
drums = pyglet.media.load('./assets/sfx/drumroll.mp3', streaming=False)
cheer = pyglet.media.load('./assets/sfx/cheer.mp3', streaming=False)
awwww = pyglet.media.load('./assets/sfx/awwww.mp3', streaming=False)

# music
music = [
    pyglet.media.load('./assets/music/garden.mp3', streaming=False),    # www.youtube.com/watch?v=SnFqblwmIoA
    pyglet.media.load('./assets/music/jeopardy.mp3', streaming=False),  # Jeopardy song
    pyglet.media.load('./assets/music/rose.mp3', streaming=False),      # Rondo Brothers, Yellow Flower of Berkeley
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
    """
    Randomly selects a song and returns it.
    """

    return music[random.randint(1,len(music)-1)]