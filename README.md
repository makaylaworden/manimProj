# manimProj
Based off Manim, this project creates it's own animations that will be applicable to computer science concepts.

Install Manim: https://github.com/3b1b/manim

As of 6/5/2020:
my_ex1.py is the my first attempt at making my own manim scenes. To run, put my_ex1.py in the same folder as manim.

There are 2 methods so far in my_ex1.py, both of which working with the transformation of different shapes. circle_to_square
transforms a circle into a square, and tri_circ_sqaure shows a trianlge turn into a circle and then a square. To show these, use
the following cmd commands.
For circle_to_square: python manim.py my_ex1.py circle_to_square -pl
For tri_circ_square: python manim.py my_ex1.py tri_circ_square  -pl


As of 6/12/2020:
my_ex2.py is the second go at making manim scenes. To run, put my_ex2.py in the same folder as manim.

There are 2 methods in my_ex2.py, both are working with different text transitions and making the animations look smoother. To run these on the Command Prompt, do as follows:
For text: python manim.py my_ex2.py text
For text_and_shapes: python manim.py my_ex2.py text_and_shapes

As of 6/20/2020:
Drive Link: https://drive.google.com/file/d/1u6PR_fCk3LBi9I-zzzOSF5a_Mzjy8lzC/view?usp=sharing
This is the link to interpreter.mp4, which is what interpreter.py is mimicing. Early progress on this shows the first few
slides of the mp4. There are some visuals of the "instruction box" and "stack" (the purple and orange boxes in the mp4).

To run in cmd: python manim.py interpreter.py interp

As of 6/26/2020:
Arrayo and Stacko objects have been created. These are used to display either horizontal or vertical boxes in a VGroup. Both classes have parameters of color, size, and text so the user can customize the way they look. More progress in finishing interpreter has been made, although it needs some work.

Christian:
I had to set
   setenv PYTHONPATH .
for python to pick up submodules.
