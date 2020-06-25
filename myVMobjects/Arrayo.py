# Author: Makayla Worden
# Summer 2020 Manim Proj

# The job of Array is to show how the array data
# structure is commonly drawn in computer science.
# By importing this class into manim projects,
# a user can have squares dispayed horizontally next
# to each other.


# TODO: Have it also take in a pixel size and screen location
# TODO: Allowing labeling on boxes, probably use an actual
#   array to keep track of stuff but idrk rn

from manimlib.imports import *


# An array class that draws size number of horizontal
# boxes that visually represent an array
class Array(VGroup):
    def ___init__(self):
        VMobject.__init__(self)

    def build(self, size, color):
        bloop = VGroup() # return me
        for i in range (size): # add size number of squares
            boxo = Rectangle()
            boxo.set_fill(color, opacity=1)
            bloop.add(boxo)

        bloop.arrange(RIGHT) # show horizontally
        return bloop
