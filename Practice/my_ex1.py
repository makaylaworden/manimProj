# Author: Makayla Worden
# Summer 2020 Manim Proj

# This is my first attempt to make my own manim scene,
# it follows closely with what is done in example_scene.py (from git),
# along with Manim tutorial 1.1 (https://www.youtube.com/watch?v=yI2YJff9SgI)

# To run this code, make sure it is in the same folder as manim.py and
# follow the commands given above each method.


from manimlib.imports import *

# circle_to_square shows a simple transition from a
# circle to a square
# Running this in cmd:
#   python manim.py my_ex1.py circle_to_square -pl
class circle_to_square (Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        circle.flip(UP)
        circle.rotate(-3 * TAU / 8)
        circle.set_fill(BLUE, opacity=1)
        square.set_fill (BLUE, opacity=1)
        
        self.play(ShowCreation(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(square))

# tri_circ_square shows a transition from
# a triangle to a circle to a square
# Running in cmd:
#   python manim.py my_ex1.py tri_circ_square  -pl
class tri_circ_square(Scene):
    def construct(self):
        tri = Triangle()
        circle = Circle()
        square = Square()
        tri.set_fill(BLUE, opacity=1)
        circle.set_fill(YELLOW, opacity=1)
        square.set_fill(PINK, opacity=1)

        self.play(ShowCreation(tri))
        self.play(Transform(tri, circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(square))
        
