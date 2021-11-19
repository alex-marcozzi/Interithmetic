# Title: video_manager.py
# Description: Contains the VideoManager class for Interithmetic.
# Author: Alexander Marcozzi
# Date: 11/19/2021

import pyglet
import cv2
import os
import game.colors as colors

class VideoManager:
    """
    A class that manages the video feed from the webcam

    ...

    Attributes
    ----------
    width : int
        the width of the display, in pixels
    height : int
        the height of the display, in pixels
    blank_sprite : pyglet sprite object
        default sprite used for resetting the frame
    frame : pyglet sprite object
        the current frame from the webcam
    background_rec : pyglet rectangle object
        the rectangle for the background of the game
    border_rec : pyglet rectangle object
        the ractangle for the border that goes around the player's webcam feed
    vid : OpenCV video capture object
    
    Methods
    -------
    update()
        Updates the frame
    draw()
        Draws the background, frame border, and frame
    setBorderColor(color)
        Sets the color of the frame border
    pathToSprite(path, width, height)
        Given a path to an image, loads it into a pyglet sprite object
    cleanUp()
        Releases the video feed, destroys all OpenCV windows, and deletes the
        temporary frame.jpg file
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        width: int
            The width of the display, in pixels
        height: int
            The height of the display, in pixels
        """

        self.batch = pyglet.graphics.Batch()

        # create the temporary frame file that will be written to and then
        # accessed later for image classification
        f = open("./assets/images/frame.jpg", "a")
        f.write("placeholder")
        f.close()
        
        pyglet.resource.path = ['./assets/images']
        pyglet.resource.reindex()

        self.width = width
        self.height = height
        self.blank_sprite = self.pathToSprite('background.jpg', 
                                              self.width, 
                                              self.height)
        self.frame = self.blank_sprite
        self.background_rec = pyglet.shapes.Rectangle(0, 
                                                      0, 
                                                      self.width, 
                                                      self.height, 
                                                      color = colors.BLUE[:3], 
                                                      batch = self.batch)

        self.border_rec = pyglet.shapes.Rectangle(self.width // 2, 
                                                  self.height // 2, 
                                                  self.height * 0.55 * 1.33, 
                                                  self.height * 0.55, 
                                                  color = colors.ORANGE[:3], 
                                                  batch = self.batch)

        self.border_rec.anchor_x = self.border_rec.width // 2
        self.border_rec.anchor_y = self.border_rec.height // 2

        self.vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.update(0)

    def update(self, dt):
        """
        Updates the frame.

        Parameters
        ----------
        dt : int
            Unused but necessary for pyglet scheduling
        """

        ret, f = self.vid.read()
        cv2.imwrite('./assets/images/frame.jpg', f)
        self.frame = self.blank_sprite
        self.frame = self.pathToSprite('frame.jpg', 
                                       (self.height // 2) * 1.33, 
                                       self.height // 2)

    def draw(self):
        """
        Draws the background, frame border, and frame.
        """

        self.background_rec.draw()
        self.border_rec.draw()
        self.frame.draw()

    def setBorderColor(self, color):
        """
        Sets the color of the frame border.

        Parameters
        ----------
        color: tuple(4)
            the color to set the border to, in RGBA format (0-255 for each)
        """

        self.border_rec.color = color[:3]

    def pathToSprite(self, path, width, height):
        """
        Given a path to an image, loads it into a pyglet sprite object.

        Parameters
        ----------
        path: string
            the path to the image file
        width: int
            the width of the sprite being created, in pixels
        height: int
            the height of the sprite being created, in pixels
        """

        image = pyglet.resource.image(path)
        image.width    = width
        image.height   = height
        image.anchor_x = image.width  // 2
        image.anchor_y = image.height // 2
        sprite = pyglet.sprite.Sprite(img = image, 
                                      x = self.width // 2, 
                                      y = self.height // 2)

        return sprite
    
    def cleanUp(self):
        """
        Releases the video feed, destroys all OpenCV windows, and deletes the
        temporary frame.jpg file
        """

        self.vid.release()
        cv2.destroyAllWindows()
        if os.path.exists('./assets/images/frame.jpg'):
           os.remove('./assets/images/frame.jpg')