# Author: Makayla Worden
# Summer 2020 Manim Proj

# This is the manim version of Interpreter.mp4 (see Git).
# Interpreter is a hardcoded animation of something similar
# to what the final version of this project will be used for.

# To run this code, make sure it is in the same folder as manim.py and
# call in cmd like so:
#   python manim.py interpreter.py interp

from manimlib.imports import *

# This is the main function, it calls everything it needs
# to in order to produce an animation similar to interpretor.mp4
class interp (Scene):
    def construct(self):
        introduction(self)
        instruct_box(self)
        make_stack(self)


# introduction displays the first 2 slides of
# interpreter.mp4. This is the first part to play.
def introduction(self): # Called first
    intro = TextMobject ("How does an interpreter work?")
    defin = TextMobject (
        "An interpreter consists of an array of bytecodes, " +
        "an evaluation stack, an interpreter loop, and one " +
        "instruction handler for each instruction")
    
    g = VGroup (intro, defin)
    g.set_width (FRAME_WIDTH - 2 * LARGE_BUFF) # This keeps them in the window
    
    self.play(Write (intro))
    self.wait()
    self.play(ShowCreation(defin), Transform (intro, defin))
    self.wait()
    self.play(FadeOut(defin))

# This will show the purple box of instructions
# in interpreter.mp4 in the lower left corner
def instruct_box (self): # Called second
    push20 = Rectangle()
    push20.set_fill(PURPLE, opacity = 1)
    push22 = Rectangle()
    push22.set_fill(PURPLE, opacity = 1)
    add = Rectangle()
    add.set_fill(PURPLE, opacity = 1)
    store = Rectangle()
    store.set_fill(PURPLE, opacity = 1)

    group = VGroup(push20, push22, add, store)
    group.arrange(RIGHT)
    group.to_corner(DOWN + RIGHT)
    group.set_width(FRAME_WIDTH / 2)

    self.add(group)
    self.play(ShowCreation(group))
    self.wait()

# This will show the orange stack on the bottom
# right corner of interpreter.mp4.
def make_stack(self): # Called third
    title = TextMobject("Stack")
    box1 = Rectangle()
    box2 = Rectangle()
    box3 = Rectangle()
    box1.set_fill(ORANGE, opacity = 1)
    box2.set_fill(ORANGE, opacity = 1)
    box3.set_fill(ORANGE, opacity = 1)

    group = VGroup(title, box1, box2, box3)
    group.arrange(DOWN) # you may end up changing this to UP, not sure
    group.to_corner(TOP + RIGHT)
    group.set_width(FRAME_WIDTH / 5)

    self.add(group)
    self.play(ShowCreation(group))
    self.wait()
    
# instructions is the lefthand side of interpreter.mp4
# where there displas code for add, push, and store.
#def instructions(self):
    # TODO: ME!
    # GET BOXES (MAYBE GRID?)
    #BOZES IN HGROUP!!!!!!!!!!!!!!!
    # GET COLORS
    # GET TEXT ON BOXES
    # GET ARROWs
