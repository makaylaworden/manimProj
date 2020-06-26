# Author: Makayla Worden
# Summer 2020 Manim Proj

# The job of Array is to show how the array data
# structure is commonly drawn in computer science.
# By importing this class into manim projects,
# a user can have squares dispayed horizontally next
# to each other.


# TODO: Have it also take in a pixel size and screen location

from manimlib.imports import *


# An array class that draws size number of horizontal
# boxes that visually represent an array
class Array(VGroup):
    def ___init__(self):
        VMobject.__init__(self)

    # build will assemble an Array to be drawn using
    # rectangles displayed horixontally in a VGroup.
    # size = how many elements in the Array
    # color = the color of the boxes
    # text = a list of size elemets that are what each element
    # in the Array should be labeled, these should be TextMobjects.
    def build(self, size, color, text):
        bloop = VGroup() # return me
        for i in range (size): # makes size number of squares
            boxo = Rectangle(fill_color=color, fill_opacity=1)
            
            label = text[i]
            label.bg = BackgroundRectangle(label, fill_color=color, fill_opacity=1)
            
            mini_bloop = VGroup(boxo, label.bg, label) # this will allow for text
                                                    # to be written on each box
            bloop.add(mini_bloop)

        bloop.arrange(RIGHT) # show horizontally bc Array
        return bloop
