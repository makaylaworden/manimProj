# Author: Makayla Worden
# Summer 2020 Manim Proj

# Stacko is used to give a visual representation
# of how computer scientists typically view a stack.
# This program allows a user to display squares vertically
# on their screen.

# TODO: Get a pixel size setter
# TODO: Be able to write directly on the stack, probs
#       use something like a list to keep track of stuff.

from manimlib.imports import *

# The main class of Stacko, call build to build
# a stack with your prefered color and size.
class Stack(VGroup):
    def __init__(self):
        VMobject.__init__(self)
    def build(self, size, color):
        stacko = VGroup() # to be returned
        for i in range (size): # Add size number of squares
            lil_stacko = Square()
            lil_stacko.set_fill(color, opacity=1)
            stacko.add(lil_stacko)
            
        stacko.arrange(DOWN) # assemble vertically
        return stacko
