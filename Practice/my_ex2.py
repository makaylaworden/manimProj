# Author: Makayla Worden
# Summer 2020 Manim Proj


# Second go at making my own manim scenes,
# this time working with getting text to appear and
# utilizing different transition ideas.

# To run this code, make sure it is in the same folder as manim.py and
# follow the commands given above each method.

from manimlib.imports import *


# text shows 2 different texts on the screen
# that have a few different colors.
# Running this in cmd:
#   python manim.py my_ex2.py text
class text (Scene):
    def construct(self):
        text = TextMobject(
            "Here's some text",
            tex_to_color_map={"text": YELLOW}
            )
        textA = TextMobject (
            "Here's some other text",
            tex_to_color_map={"some": PINK}
            )
        g = VGroup(text, textA)
        g.arrange(DOWN)
        g.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(text))
        self.play(Write(textA))
        self.wait()
        
# text_and_shapes combines text and a circle
# by first showing a transition from one text
# to another, and then transforming into a circle.
# Running this in cmd:
#   python manim.py my_ex2.py text_and_shapes
class text_and_shapes(Scene):
    def construct(self):
        hello = TextMobject (
            "Hello, world!",
            text_to_color_map={"Hello":BLUE}
            )
    
        self.play(FadeInFrom(hello, UP))
        self.wait()
        
        turn_circle = TextMobject (
            "Watch me turn into a circle",
            text_to_color_map={"Watch me turn into a circle":RED}
            )

        self.play(Write(turn_circle), Transform (hello, turn_circle))
        self.wait()
        self.play(FadeOut(turn_circle))
        
        circle = Circle()

        self.play(ShowCreation(circle))
    
        
