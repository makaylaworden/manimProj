# Author: Makayla Worden
# Summer 2020 Manim Proj

# This is the manim version of Interpreter.mp4 (see Git).
# Interpreter is a hardcoded animation of something similar
# to what the final version of this project will be used for.

# To run this code, make sure it is in the same folder as manim.py and
# call in cmd like so:
#   python manim.py interpreter.py interp

from manimlib.imports import *
from myVMobjects import Arrayo
from myVMobjects import Stacko

# This is the main function, it calls everything it needs
# to in order to produce an animation similar to interpretor.mp4
class interp (Scene):
    def construct(self):
        introduction(self)
        instruct_box(self)
        make_stack(self)
        code_box(self)
        subtitle(self)


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
    self.play(FadeOutAndShiftDown(defin))

# This will show the purple box of instructions
# in interpreter.mp4 in the lower left corner
def instruct_box (self): # Called second
    text = [TextMobject("VPC\npush 20", tex_to_color_map={"push 20": BLACK}),
            TextMobject("push 22", tex_to_color_map={"push 22": BLACK}),
            TextMobject("add", tex_to_color_map={"add": BLACK}),
            TextMobject("store", tex_to_color_map={"store": BLACK})]
    # This is what is "stored" in the Array
    
    meArr = Arrayo.Array().build(len(text), PURPLE, text)

    meArr.to_corner(DOWN + RIGHT)
    meArr.set_width(FRAME_WIDTH / 2) # this is a rando number

    self.add(meArr)
    self.play(ShowCreation(meArr))

# This will show the orange stack on the bottom
# right corner of interpreter.mp4.
def make_stack(self): # Called third
    empty_text = [TextMobject(""), TextMobject(""), TextMobject("SP", tex_to_color_map={"SP": BLACK})]
    stacko = Stacko.Stack().build(len(empty_text), ORANGE, empty_text)
    title = TextMobject("STACK") # label on top of the stack

    group = VGroup(title, stacko)
    group.arrange(DOWN)
    group.to_corner(TOP + RIGHT)
    group.set_width(FRAME_WIDTH / 8) # this is a rando number

    self.add(group)
    self.play(ShowCreation(group))

    
# code_box is the lefthand side of interpreter.mp4
# where there displas code for add, push, and store.
def code_box(self): # Called fourth
    # Make that top yellow label box:
    label_box = Rectangle(fill_color=YELLOW, fill_opacity=1)
    label_txt = TextMobject("CODE[VPC]", tex_to_color_map={"CODE[VPC]": BLACK})
    label_txt.bg = BackgroundRectangle(label_txt, fill_color=YELLOW, fill_opacity=1)
    label_group = VGroup(label_box, label_txt.bg, label_txt)

    # Make blue code stack
    text1 = TextMobject("add:{\n\tpush(pop()+pop());\n\tVPC++;}",
                        tex_to_color_map={"add:{\n\tpush(pop()+pop());\n\tVPC++;}": BLACK})
    text2 = TextMobject("push:{\n\tpush(CODE[VPC+1]);\n\tVPC+=2}",
                        tex_to_color_map={"push:{\n\tpush(CODE[VPC+1]);\n\tVPC+=2}": BLACK})
    text3 = TextMobject("store:{\n\tMem[CODE[VPC+1]]=pop();\n\tVPC+=2}",
                        tex_to_color_map={"store:{\n\tMem[CODE[VPC+1]]=pop();\n\tVPC+=2}": BLACK})
    text = [text1, text2, text3] # This is what will be displayed on the boxes
    code_stack = Stacko.Stack().build(len(text), BLUE, text)

    group = VGroup(label_group, code_stack)
    group.arrange(DOWN)
    group.set_width(FRAME_WIDTH/4) # this is a rando number
    group.to_corner(UP + LEFT)

    self.add(group)
    self.play(ShowCreation(group))

# subtitle is maintaining different comments on what
# is happening on the screen
def subtitle (self): # Called fifth
    say = TextMobject( "Here's an interpreter for the program " +
                       "x = 20 + 22. It only supports 3 " +
                       "instructions: push, add, and store" )
    say2 = TextMobject( "Let's execute the program! The first instruction " +
                        "is 'push 20'. We jump to the instruction handler " +
                        "for 'push', push 20 on the stack, and advance the " +
                        "virtual program counter (VPC)")

    main_box = Square(side_length=2)
    label_txt1 = TextMobject("main()")
    label_txt1.scale(.5)
    label_txt2 = TextMobject("     int x=99;")
    label_txt2.scale(.5)
    label_txt3 = TextMobject ("     x=20+22; }")
    label_txt3.scale(.5)
    # TODO learn Latex lol

    label_txt = VGroup(label_txt1, label_txt2, label_txt3)
    label_txt.arrange(DOWN)
    
    label_txt.bg = BackgroundRectangle(label_txt)
    main_group = VGroup(main_box, label_txt.bg, label_txt)
    main_group.to_corner(UP + RIGHT)
    
    say.scale(.5)
    say2.scale(.5)
    say.to_corner(TOP + RIGHT)
    self.play(Write(say))
    self.wait()
    self.play(FadeOut(say), FadeIn(say2), ShowCreation(main_group))
    
