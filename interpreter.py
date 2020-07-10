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

# Data structures shown throughout the animation:
global STACK
global ARR

# This is the main function, it calls everything it needs
# to in order to produce an animation similar to interpretor.mp4
class interp (Scene):
    STACK = VGroup()
    ARR = VGroup()
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
    self.wait(5)
    self.play(FadeOutAndShiftDown(defin))

# This will show the purple box of instructions
# in interpreter.mp4 in the lower left corner
def instruct_box (self): # Called second
    text = [TextMobject("VPC push 20", tex_to_color_map={"push 20": BLACK}),
            TextMobject("push 22", tex_to_color_map={"push 22": BLACK}),
            TextMobject("add", tex_to_color_map={"add": BLACK}),
            TextMobject("store", tex_to_color_map={"store": BLACK})]
    # This is what is "stored" in the Array
    
    ARR = Arrayo.Array().build(len(text), PURPLE, text)

    ARR.to_corner(DOWN + RIGHT)
    ARR.set_width(FRAME_WIDTH / 2) # this is a rando number

    self.add(ARR)
    self.play(ShowCreation(ARR))

    self.ARR = ARR

# This will show the orange stack on the bottom
# right corner of interpreter.mp4.
def make_stack(self): # Called third
    empty_text = [TextMobject(""), TextMobject(""), TextMobject("SP", tex_to_color_map={"SP": BLACK})]
    stacko = Stacko.Stack().build(len(empty_text), ORANGE, empty_text)
    title = TextMobject("STACK") # label on top of the stack

    STACK = VGroup(title, stacko)
    STACK.arrange(DOWN)
    STACK.to_corner(TOP + RIGHT)
    STACK.set_width(FRAME_WIDTH / 10) # this is a rando number

    self.add(STACK)
    self.play(ShowCreation(STACK))

    self.STACK = STACK

    
# code_box is the lefthand side of interpreter.mp4
# where there displas code for add, push, and store.
def code_box(self): # Called fourth
    # Make that top yellow label box:
    label_box = Rectangle(fill_color=YELLOW, fill_opacity=1)
    label_txt = TextMobject("CODE[VPC]", tex_to_color_map={"CODE[VPC]": BLACK})
    label_txt.bg = BackgroundRectangle(label_txt, fill_color=YELLOW, fill_opacity=1)
    label_group = VGroup(label_box, label_txt.bg, label_txt)

    # Make blue code stack
    text1a = TextMobject("add:{", tex_to_color_map={"add:{": BLACK})
    text1b = TextMobject("push(pop()+pop());", tex_to_color_map={"push(pop()+pop());": BLACK})
    text1c = TextMobject ("VPC++;}", tex_to_color_map={"VPC++;}": BLACK})
    text1 = VGroup(text1a, text1b, text1c)

    text2a = TextMobject("push:{", tex_to_color_map={"push:{": BLACK})
    text2b = TextMobject("push(CODE[VPC+1]);", tex_to_color_map={"push(CODE[VPC+1]);":BLACK})
    text2c = TextMobject("VPC+=2}", tex_to_color_map={"VPC+=2}": BLACK})
    text2 = VGroup(text2a, text2b, text2c)

    text3a = TextMobject("store:{", tex_to_color_map={"store:{": BLACK})
    text3b = TextMobject("Mem[CODE[VPC+1]]=pop();", tex_to_color_map={"Mem[CODE[VPC+1]]=pop();": BLACK})
    text3c = TextMobject("VPC+=2}", tex_to_color_map={"VPC+=2}": BLACK})
    text3 = VGroup(text3a, text3b, text3c)
    
    text1.arrange(DOWN) # These are VGroups so they can be displayed
    text2.arrange(DOWN) #   similarly to how code would normally look
    text3.arrange(DOWN)

    text1.set_width(3)
    text2.set_width(3)
    text3.set_width(3)

    text = [text1, text2, text3] # This is what will be printed in the boxes

    code_stack = Stacko.Stack().build(len(text), BLUE, text)

    group = VGroup(label_group, code_stack)
    group.arrange(DOWN)
    group.set_width(FRAME_WIDTH/8) # this is a rando number
    group.to_corner(UP + LEFT)

    self.add(group)
    self.play(ShowCreation(group))


# subtitle is maintaining different comments on what
# is happening on the screen. This becomes the "main" func
# for the rest of the program, since it multitaks exaplaining
# what's on the screen, and updates objects as it goes.
def subtitle (self): # Called fifth
    say = TextMobject("Here's an interpreter for the program " +
                       "x = 20 + 22. It only supports 3 " +
                       "instructions: push, add, and store" )
    say2 = TextMobject("Let's execute the program! The first instruction " +
                        "is 'push 20'. We jump to the instruction handler " +
                        "for 'push', push 20 on the stack, and advance the " +
                        "virtual program counter (VPC)")
    say3 = TextMobject("Then we execute the next instruction, 'push 22', " +
                        "which pushes the value 22 on the stack")
    say4 = TextMobject("Next is the 'add' instruction. It takes no " +
                        "arguments. It pops 2 values off the stack, adds " +
                        "them, and pushes the result")
    say5 = TextMobject("Finally, the instruction 'store x', pops the result " +
                       "off the stack and stores it in variable x.")

    # Make 'em fit
    say.scale(.5)
    say2.scale(.5)
    say3.scale(.5)
    say4.scale(.5)
    say5.scale(.5)
    
    main_group = main_boxo(self, "x: 99") # draws "main function" onto screen
    self.play(ShowCreation(main_group))
    
    # First round of subtitles
    self.play(Write(say))
    self.wait()
    self.play(FadeOut(say), FadeIn(say2))
    self.wait()

    # Change stack and arr
    update_stack(self, [TextMobject(""),
                        TextMobject("SP", tex_to_color_map={"SP": BLACK}),
                        TextMobject("20")])
    update_arr(self, [TextMobject("push 20", tex_to_color_map={"push 20": BLACK}),
        TextMobject("VPC push 22", tex_to_color_map={"push 22": BLACK}),
        TextMobject("add", tex_to_color_map={"add": BLACK}),
        TextMobject("store", tex_to_color_map={"store": BLACK})])
    self.wait(3)

    # next subtitles
    self.play(FadeOut(say2), FadeIn(say3))
    self.wait()

    # Change stack and arr
    update_stack(self, [TextMobject("SP", tex_to_color_map={"SP": BLACK}),
                        TextMobject("22"),
                        TextMobject("20")])

    update_arr(self, [TextMobject("push 20", tex_to_color_map={"push 20": BLACK}),
        TextMobject("push 22", tex_to_color_map={"push 22": BLACK}),
        TextMobject("VPC add", tex_to_color_map={"add": BLACK}),
        TextMobject("store", tex_to_color_map={"store": BLACK})])
    self.wait(3)
    
    # next subtitles
    self.play(FadeOut(say3), FadeIn(say4))
    self.wait()

    # Change stack 3 times
    # Pops 22
    update_stack(self, [TextMobject(""),
                        TextMobject("SP", tex_to_color_map={"SP": BLACK}),
                        TextMobject("20")])
    self.wait()
    
    # Pops 20
    update_stack(self, [TextMobject(""),
                        TextMobject(""),
                        TextMobject("SP", tex_to_color_map={"SP": BLACK})])
    self.wait()
    
    #Pushes 42
    update_stack(self, [TextMobject(""),
                        TextMobject("SP", tex_to_color_map={"SP": BLACK}),
                        TextMobject("42")])
    self.wait(3)

    # next subtitles
    self.play(FadeOut(say4), FadeIn(say5))
    self.wait()

    # change arr then stack then main_box's x
    update_arr(self, [TextMobject("push 20", tex_to_color_map={"push 20": BLACK}),
        TextMobject("push 22", tex_to_color_map={"push 22": BLACK}),
        TextMobject("VPC add", tex_to_color_map={"add": BLACK}),
        TextMobject("store", tex_to_color_map={"store": BLACK})])
    update_stack(self, [TextMobject(""), TextMobject(""),
                        TextMobject("SP", tex_to_color_map={"SP": BLACK})])
    self.wait()
    self.play(Transform(main_group, main_boxo(self, "x: 42")))
    self.wait(3)

# THESE ARE THE THINGS SUBTITLE CALLS:

# This makes the main function in the top right corner
# of the screen
def main_boxo(self, x):
    main_box = Square(side_length=2)
    label_txt1 = TextMobject("main()")
    label_txt2 = TextMobject("int x=99;")
    label_txt3 = TextMobject ("x=20+22; }")

    label_txt = VGroup(label_txt1, label_txt2, label_txt3)
    label_txt.arrange(DOWN)
    label_txt.set_width(FRAME_WIDTH/8)
    
    label_txt.bg = BackgroundRectangle(label_txt)

    x_label = TextMobject(x, tex_to_color_map={x: BLUE})
    
    mg = VGroup(main_box, label_txt.bg, label_txt)
    main_group = VGroup(mg, x_label)
    main_group.arrange(DOWN)
    main_group.to_corner(UP + RIGHT)

    return main_group # Returns so if you need it to fade out later you can

# This updates what's in the stack by taking a list of
# TextMobjects and transforming the old stack into a new one
def update_stack(self, text):
    new_stack = Stacko.Stack().build(len(text), ORANGE, text)
    title = TextMobject("STACK") # label

    new_stack = VGroup(title, new_stack)
    new_stack.arrange(DOWN)
    new_stack.to_corner(TOP + RIGHT)
    new_stack.set_width(FRAME_WIDTH / 10) # this is a rando number

    self.play(Transform(self.STACK, new_stack))

    self.STACK = new_stack # update STACK
   
# This updates what's in the array by taking a list of
# TextMobjexts and transforming the old array into a new one
def update_arr(self, text):
    new_arr = Arrayo.Array().build(len(text), PURPLE, text)

    new_arr.to_corner(DOWN + RIGHT)
    new_arr.set_width(FRAME_WIDTH / 2) # this is a rando number

    self.add(new_arr)
    self.play(Transform(self.ARR, new_arr))

    self.ARR = new_arr
    
