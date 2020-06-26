# Author: Makayla Worden
# Summer 2020 Manim Proj

# Stacko is used to give a visual representation
# of how computer scientists typically view a stack.
# This program allows a user to display squares vertically
# on their screen.

# TODO: Get a pixel size setter

from manimlib.imports import *

# The main class of Stacko, call build to build
# a stack with your prefered color and size.
class Stack(VGroup):
    def __init__(self):
        VMobject.__init__(self)
    def build(self, size, color, text):
        stacko = VGroup() # to be returned
        for i in range (size): # Add size number of squares
            boxo = Rectangle(fill_color=color, fill_opacity=1)

            label = text[i]
            label.bg = BackgroundRectangle(label, width=(boxo.width/2),
                                           fill_color=color, fill_opacity=1)

            lil_stacko = VGroup(boxo, label.bg, label)
            
            stacko.add(lil_stacko)
            
        stacko.arrange(DOWN) # assemble vertically
        return stacko


