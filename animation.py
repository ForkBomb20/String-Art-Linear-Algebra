from math import cos, sin
from random import random

from manim import *


def get_pixel_grid(arr, label=False, small=False):
    grid = VGroup()
    square = Square(side_length=0.25)
    # square.set_fill(WHITE, opacity=0)
    square.set_stroke("0xffffff", width=0.5)
    for r in range(len(arr)):
        try:
            for c in range(len(arr[0])):
                grid.add(square.copy().set_fill("0x"+("0x{:02x}".format(int(arr[r][c]*255))[-2:]*3),opacity=1).shift(c*np.array([0.25,0,0]), r*np.array([0,-0.25,0])))
                if label:
                    if arr[r][c] <= 0.5:
                        col = "0xffffff"
                    else:
                        # col = "0x"+("0x{:02x}".format(int(255 - arr[r][c]*255))[-2:]*3)
                        col = "0x000000"
                    if small:
                        grid.add(Text(str(arr[r][c]),
                        color=ManimColor(col),font_size=0.25*32).shift(c*np.array([0.25,0,0]), r*np.array([0,-0.25,0])))
                    else:
                        grid.add(Text(str(arr[r][c]),
                                      color=ManimColor(col), font_size=0.25 * 48).shift(c * np.array([0.25, 0, 0]),
                                                                                        r * np.array([0, -0.25, 0])))
        except:
            grid.add(square.copy().set_fill("0x" + ("0x{:02x}".format(int(arr[r] * 255))[-2:] * 3), opacity=1).shift(
                r * np.array([0.25, 0, 0]), 0))
            if label:
                if arr[r] <= 0.5:
                    col = "0xffffff"
                else:
                    # col = "0x"+("0x{:02x}".format(int(255 - arr[r][c]*255))[-2:]*3)
                    col = "0x000000"
                if not all([val % 1 == 0 for val in arr]):
                    grid.add(Text(str(arr[r]),
                                  color=ManimColor(col), font_size=0.25 * 32).shift(r * np.array([0.25, 0, 0]),0))
                else:
                    grid.add(Text(str(arr[r]),
                                  color=ManimColor(col), font_size=0.25 * 48).shift(r * np.array([0.25, 0, 0]), 0))
    return grid



vert = [[0, 0, 1, 0.8, 1, 0, 0],
[0, 1, 1, 0.8, 1, 1, 0],
[1, 1, 1, 0.8, 1, 1, 1],
[1, 1, 1, 0.8, 1, 1, 1],
[1, 1, 1, 0.8, 1, 1, 1],
[0, 1, 1, 0.8, 1, 1, 0],
[0, 0, 1, 0.8, 1, 0, 0]]

horz = [[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
[1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0]]

tlbr = [[0, 0, 1, 1, 1, 0, 0],
[0, 0.8, 1, 1, 1, 1, 0],
[1, 1, 0.8, 1, 1, 1, 1],
[1, 1, 1, 0.8, 1, 1, 1],
[1, 1, 1, 1, 0.8, 1, 1],
[0, 1, 1, 1, 1, 0.8, 0],
[0, 0, 1, 1, 1, 0, 0]]

bltr = [[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 0.8, 0],
[1, 1, 1, 1, 0.8, 1, 1],
[1, 1, 1, 0.8, 1, 1, 1],
[1, 1, 0.8, 1, 1, 1, 1],
[0, 0.8, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0]]

cross = [[0, 0, 1, 0.8, 1, 0, 0],
[0, 1, 1, 0.8, 1, 1, 0],
[1, 1, 1, 0.8, 1, 1, 1],
[0.8, 0.8, 0.8, 0.64, 0.8, 0.8, 0.8],
[1, 1, 1, 0.8, 1, 1, 1],
[0, 1, 1, 0.8, 1, 1, 0],
[0, 0, 1, 0.8, 1, 0, 0]]

diags = [[0, 0, 1, 1, 1, 0, 0],
[0, 0.8, 1, 1, 1, 0.8, 0],
[1, 1, 0.8, 1, 0.8, 1, 1],
[1, 1, 1, 0.64, 1, 1, 1],
[1, 1, 0.8, 1, 0.8, 1, 1],
[0, 0.8, 1, 1, 1, 0.8, 0],
[0, 0, 1, 1, 1, 0, 0]]


class Full(Scene):
    def construct(self):
        Title.construct(self)
        self.clear()
        Objectives.construct(self)
        self.clear()
        PreviewProblem.construct(self)
        self.clear()
        IntroduceGrayscale.construct(self)
        self.clear()
        IntroduceStrings.construct(self)
        self.clear()
        ClearLabels.construct(self)
        self.clear()
        IntroduceLinear.construct(self)
        self.clear()
        explainSolve.construct(self)
        self.clear()
        Recap.construct(self)
        self.clear()
        CodeDemo.construct(self)
        self.clear()

class Title(Scene):
    def construct(self):
        pixels = get_pixel_grid(np.array([[0,0,1,1,1,0,0],
                                         [0,1,1,1,1,1,0],
                                         [1,1,0,1,0,1,1],
                                         [1,1,1,1,1,1,1],
                                         [1,0,1,1,1,0,1],
                                         [0,1,0,0,0,1,0],
                                         [0,0,1,1,1,0,0]]))
        pixels.scale(2)
        pixels.move_to((0,0,0))
        title = Text("String Art & Linear Algebra").move_to((0,3,0))
        ul = Underline(title)
        self.play(Create(title), Create(ul))
        self.play(Create(pixels, run_time=2))
        self.wait(2)

class Objectives(Scene):
    def construct(self):
        title = Text("Objectives").move_to((0, 3, 0))
        ul = Underline(title)
        self.add(title, ul)


        blist = BulletedList("Create an algorithm that can convert images to string art",
                             "Explore the linear systems and operations that make it possible",
                             "Explain limitations and assumptions of the algorithm", height=2, width=2, buff=0.1, dot_scale_factor=0.5, font_size=100)
        blist.move_to(LEFT*1)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        blist.scale(5)
        self.play(Write(blist))
        self.wait()

class PreviewProblem(Scene):
    def construct(self):
        strings = ImageMobject("Figure_1.png")
        normal = ImageMobject("inv.jpg")
        strings.move_to((0,-0.2, 0))
        normal.move_to((0,-0.2,0))

        q = Text("So, how do we do this?")
        q.move_to((0, 2.5, 0))
        self.play(Write(q, run_time=0.8))

        self.play(FadeIn(normal))
        self.add(normal)
        self.wait()
        self.play(Transform(normal, strings, run_time=4))

        self.wait(2)

        pixels = get_pixel_grid(np.array([[0, 0, 1, 1, 1, 0, 0],
                                          [0, 1, 1, 1, 1, 1, 0],
                                          [1, 1, 0, 1, 0, 1, 1],
                                          [1, 1, 1, 1, 1, 1, 1],
                                          [1, 0, 1, 1, 1, 0, 1],
                                          [0, 1, 0, 0, 0, 1, 0],
                                          [0, 0, 1, 1, 1, 0, 0]]))
        pixels.scale(1.8)
        pixels.move_to((0,0,0))

        self.remove(strings, normal)
        self.play(FadeOut(q))
        self.play(FadeIn(pixels))

        self.wait(2)

class IntroduceGrayscale(Scene):
    def construct(self):
        labeled_face = get_pixel_grid(np.array([[0, 0, 1, 1, 1, 0, 0],
                                          [0, 1, 1, 1, 1, 1, 0],
                                          [1, 1, 0, 1, 0, 1, 1],
                                          [1, 1, 1, 1, 1, 1, 1],
                                          [1, 0, 1, 1, 1, 0, 1],
                                          [0, 1, 0, 0, 0, 1, 0],
                                          [0, 0, 1, 1, 1, 0, 0]]), label=True)

        face = get_pixel_grid(np.array([[0, 0, 1, 1, 1, 0, 0],
                                          [0, 1, 1, 1, 1, 1, 0],
                                          [1, 1, 0, 1, 0, 1, 1],
                                          [1, 1, 1, 1, 1, 1, 1],
                                          [1, 0, 1, 1, 1, 0, 1],
                                          [0, 1, 0, 0, 0, 1, 0],
                                          [0, 0, 1, 1, 1, 0, 0]]))
        key = get_pixel_grid(np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]),label=True)

        face.scale(1.8)
        labeled_face.scale(1.8)
        face.move_to((0,0,0))
        labeled_face.move_to((0,0.8,0))

        self.add(face)
        self.wait()
        self.play(face.animate.move_to((0,0.8,0)))

        key.scale(1.8)
        key.next_to(face, DOWN, buff=0.5)

        self.play(Transform(face, labeled_face), Create(key))
        self.wait(5)

        self.play(*[FadeOut(mob, shift=LEFT*10) for mob in self.mobjects])


class IntroduceStrings(Scene):

    def construct(self):
        s1 = get_pixel_grid(np.array(vert))
        s1_labeled = get_pixel_grid(np.array(vert), label=True, small=True)
        s1.scale(1.5)
        s1_labeled.scale(1.5)
        s1.move_to((0, 0, 0))

        s2 = get_pixel_grid(np.array(horz))
        s2_labeled = get_pixel_grid(np.array(horz), label=True, small=True)
        s2.scale(1.5)
        s2_labeled.scale(1.5)
        s2.move_to((0, 0, 0))

        s3 = get_pixel_grid(np.array(tlbr))
        s3_labeled = get_pixel_grid(np.array(tlbr), label=True, small=True)
        s3.scale(1.5)
        s3_labeled.scale(1.5)
        s3.move_to((0, 0, 0))

        s4 = get_pixel_grid(np.array(bltr))
        s4_labeled = get_pixel_grid(np.array(bltr), label=True, small=True)
        s4.scale(1.5)
        s4_labeled.scale(1.5)
        s4.move_to((0, 0, 0))

        s1s2 = get_pixel_grid(np.array(cross))
        s1s2_labeled = get_pixel_grid(np.array(cross), label=True, small=True)
        s1s2.scale(1.5)
        s1s2_labeled.scale(1.5)
        s1s2.move_to((0, 0, 0))

        s3s4 = get_pixel_grid(np.array(diags))
        s3s4_labeled = get_pixel_grid(np.array(diags), label=True, small=True)
        s3s4.scale(1.5)
        s3s4_labeled.scale(1.5)
        s3s4.move_to((0, 0, 0))

        self.play(Create(s1), s1.animate.move_to((-1.8, 1.5, 0)))
        # self.wait(0.2)
        self.play(Create(s2), s2.animate.move_to((1.8, 1.5, 0)))
        # self.wait(0.2)
        self.play(Create(s3), s3.animate.move_to((-1.8, -1.5, 0)))
        # self.wait(0.2)
        self.play(Create(s4), s4.animate.move_to((1.8, -1.5, 0)))
        # self.wait(0.2)
        self.wait(3)

        s1_labeled.move_to((-1.8, 1.5, 0))
        s2_labeled.move_to((1.8, 1.5, 0))
        s3_labeled.move_to((-1.8, -1.5, 0))
        s4_labeled.move_to((1.8, -1.5, 0))

        self.play(Transform(s1, s1_labeled),
                  Transform(s2, s2_labeled),
                  Transform(s3, s3_labeled),
                  Transform(s4, s4_labeled))

        self.wait()

        self.play(*[mob.animate.shift(RIGHT*1.1) for mob in self.mobjects])

        self.wait()
        strings = VGroup()
        strings.add(s1_labeled, s2_labeled, s3_labeled, s4_labeled)
        br = Brace(strings, sharpness=1, direction=([-1,0,0])).shift(RIGHT*0.7)
        br_label = br.get_tex("Strings")
        self.play(Create(br), Create(br_label))

        self.wait(2)

        self.play(Uncreate(br), Uncreate(br_label))
        self.play(*[mob.animate.shift(LEFT * 3) for mob in self.mobjects])

        plus = Tex("+")
        plus2 = Tex("+")
        equal = Tex("=")
        equal2 = Tex("=")
        plus.next_to(s1_labeled, direction=RIGHT, buff=0)
        equal.next_to(s2_labeled, direction=RIGHT, buff=0)
        equal.shift(1.57*LEFT)
        plus.shift(1.57*LEFT)
        plus2.next_to(s3_labeled, direction=RIGHT, buff=0)
        equal2.next_to(s4_labeled, direction=RIGHT, buff=0)
        equal2.shift(1.57 * LEFT)
        plus2.shift(1.57 * LEFT)
        # plus.move_to(([(s1_labeled.get_center()-s2_labeled.get_center())/2 + s2_labeled.get_center()]))
        plus.scale(1.5)
        equal.scale(1.5)
        plus2.scale(1.5)
        equal2.scale(1.5)

        s1s2_labeled.next_to(equal)
        s1s2_labeled.shift(RIGHT*0.14)

        s3s4_labeled.next_to(equal2)
        s3s4_labeled.shift(RIGHT * 0.14)

        self.play(Create(plus), Create(plus2))
        self.play(Create(equal), Create(equal2))
        self.play(Create(s1s2_labeled), Create(s3s4_labeled))

        self.wait(2)

        self.play(Uncreate(plus), Uncreate(plus2))
        self.play(Uncreate(equal), Uncreate(equal2))
        self.play(Uncreate(s1s2_labeled), Uncreate(s3s4_labeled))

        self.play(*[mob.animate.shift(RIGHT * 2.2) for mob in self.mobjects])


        self.wait()


class ClearLabels(Scene):
    def construct(self):
        s1 = get_pixel_grid(np.array(vert))
        s1_labeled = get_pixel_grid(np.array(vert), label=True, small=True)
        s1.scale(1.5)
        s1_labeled.scale(1.5)
        s1.move_to((0, 0, 0))

        s2 = get_pixel_grid(np.array(horz))
        s2_labeled = get_pixel_grid(np.array(horz), label=True, small=True)
        s2.scale(1.5)
        s2_labeled.scale(1.5)
        s2.move_to((0, 0, 0))

        s3 = get_pixel_grid(np.array(tlbr))
        s3_labeled = get_pixel_grid(np.array(tlbr), label=True, small=True)
        s3.scale(1.5)
        s3_labeled.scale(1.5)
        s3.move_to((0, 0, 0))

        s4 = get_pixel_grid(np.array(bltr))
        s4_labeled = get_pixel_grid(np.array(bltr), label=True, small=True)
        s4.scale(1.5)
        s4_labeled.scale(1.5)
        s4.move_to((0, 0, 0))

        s1s2 = get_pixel_grid(np.array(cross))
        s1s2_labeled = get_pixel_grid(np.array(cross), label=True, small=True)
        s1s2.scale(1.5)
        s1s2_labeled.scale(1.5)
        s1s2.move_to((0, 0, 0))

        s3s4 = get_pixel_grid(np.array(diags))
        s3s4_labeled = get_pixel_grid(np.array(diags), label=True, small=True)
        s3s4.scale(1.5)
        s3s4_labeled.scale(1.5)
        s3s4.move_to((0, 0, 0))

        s1.move_to((-1.8, 1.5, 0))
        s2.move_to((1.8, 1.5, 0))
        s3.move_to((-1.8, -1.5, 0))
        s4.move_to((1.8, -1.5, 0))

        s1_labeled.move_to((-1.8, 1.5, 0))
        s2_labeled.move_to((1.8, 1.5, 0))
        s3_labeled.move_to((-1.8, -1.5, 0))
        s4_labeled.move_to((1.8, -1.5, 0))

        self.add(s1_labeled)
        self.add(s2_labeled)
        self.add(s3_labeled)
        self.add(s4_labeled)

        self.play(Transform(s1_labeled, s1),Transform(s2_labeled, s2),Transform(s3_labeled, s3),Transform(s4_labeled, s4))

        self.wait()

class IntroduceLinear(Scene):
    def construct(self):
        s1 = get_pixel_grid(np.array(vert))
        s1_labeled = get_pixel_grid(np.array(vert), label=True, small=True)
        s1.scale(1.5)
        s1_labeled.scale(1.5)
        s1.move_to((0, 0, 0))

        s2 = get_pixel_grid(np.array(horz))
        s2_labeled = get_pixel_grid(np.array(horz), label=True, small=True)
        s2.scale(1.5)
        s2_labeled.scale(1.5)
        s2.move_to((0, 0, 0))

        s3 = get_pixel_grid(np.array(tlbr))
        s3_labeled = get_pixel_grid(np.array(tlbr), label=True, small=True)
        s3.scale(1.5)
        s3_labeled.scale(1.5)
        s3.move_to((0, 0, 0))

        s4 = get_pixel_grid(np.array(bltr))
        s4_labeled = get_pixel_grid(np.array(bltr), label=True, small=True)
        s4.scale(1.5)
        s4_labeled.scale(1.5)
        s4.move_to((0, 0, 0))

        str1 = get_pixel_grid(np.array(vert).reshape(49,1))
        str1_labeled = get_pixel_grid(np.array(horz), label=True, small=True)
        str1.scale(1.5)
        str1_labeled.scale(1.5)
        str1.move_to((0, 0, 0))

        str2 = get_pixel_grid(np.array(vert).reshape(49, 1))
        str2_labeled = get_pixel_grid(np.array(vert), label=True, small=True)
        str2.scale(1.5)
        str2_labeled.scale(1.5)
        str2.move_to((0, 0, 0))

        str3 = get_pixel_grid(np.array(tlbr).reshape(49, 1))
        str3_labeled = get_pixel_grid(np.array(vert), label=True, small=True)
        str3.scale(1.5)
        str3_labeled.scale(1.5)
        str3.move_to((0, 0, 0))

        str4 = get_pixel_grid(np.array(bltr).reshape(49, 1))
        str4_labeled = get_pixel_grid(np.array(vert), label=True, small=True)
        str4.scale(1.5)
        str4_labeled.scale(1.5)
        str4.move_to((0, 0, 0))

        s1.move_to((-1.8, 1.5, 0))
        s2.move_to((1.8, 1.5, 0))
        s3.move_to((-1.8, -1.5, 0))
        s4.move_to((1.8, -1.5, 0))

        self.add(s1)
        self.add(s2)
        self.add(s3)
        self.add(s4)

        str1.scale(0.3)
        str2.scale(0.3)
        str3.scale(0.3)
        str4.scale(0.3)

        self.play(s1.animate.scale(0.4), s2.animate.scale(0.4), s3.animate.scale(0.4), s4.animate.scale(0.4))

        self.wait()

        group = VGroup(s1, s2, s3, s4)
        self.play(group.animate.set_x(0).arrange(buff=1).shift(LEFT*1.2))

        eq = MathTex("=").scale(0.8).next_to(s4, direction=RIGHT, buff=0.35)
        almost = MathTex("\\approx").scale(0.8).next_to(s4, direction=RIGHT, buff=0.35)

        pixels = get_pixel_grid(np.array([[0, 0, 1, 1, 1, 0, 0],
                                          [0, 1, 1, 1, 1, 1, 0],
                                          [1, 1, 0, 1, 0, 1, 1],
                                          [1, 1, 1, 1, 1, 1, 1],
                                          [1, 0, 1, 1, 1, 0, 1],
                                          [0, 1, 0, 0, 0, 1, 0],
                                          [0, 0, 1, 1, 1, 0, 0]])).scale(0.6).next_to(s4, direction=RIGHT, buff=1)

        strp = get_pixel_grid(np.array([[0, 0, 1, 1, 1, 0, 0],
                                        [0, 1, 1, 1, 1, 1, 0],
                                        [1, 1, 0, 1, 0, 1, 1],
                                        [1, 1, 1, 1, 1, 1, 1],
                                        [1, 0, 1, 1, 1, 0, 1],
                                        [0, 1, 0, 0, 0, 1, 0],
                                        [0, 0, 1, 1, 1, 0, 0]]).reshape(49, 1)).scale(1.5).next_to(s4, direction=RIGHT,
                                                                                                   buff=1)
        strp.scale(0.3)

        animations = [Create(MathTex("x_{1}").scale(0.8).next_to(s1, direction=LEFT, buff=0.1)),
                      Create(MathTex("x_{2}").scale(0.8).next_to(s2, direction=LEFT, buff=0.1)),
                      Create(MathTex("x_{3}").scale(0.8).next_to(s3, direction=LEFT, buff=0.1)),
                      Create(MathTex("x_{4}").scale(0.8).next_to(s4, direction=LEFT, buff=0.1)),
                      Create(MathTex("+").scale(0.8).next_to(s1, direction=RIGHT,buff=0.15)),
                      Create(MathTex("+").scale(0.8).next_to(s2, direction=RIGHT,buff=0.15)),
                      Create(MathTex("+").scale(0.8).next_to(s3, direction=RIGHT,buff=0.15)),
                      Create(eq),
                      Create(pixels)
                      ]

        self.play(*animations)

        self.wait(2)

        self.play(Transform(eq, almost))

        self.wait()

        str1.move_to(s1.get_center())
        str2.move_to(s2.get_center())
        str3.move_to(s3.get_center())
        str4.move_to(s4.get_center())
        strp.move_to(pixels.get_center())

        self.play(Transform(s1, str1),Transform(s2, str2),Transform(s3, str3),Transform(s4, str4), Transform(pixels, strp))

        self.wait(2)

        self.play(*[FadeOut(mob, shift=[UP*10]) for mob in self.mobjects])
        #
        self.wait()

        t = Text("Or").move_to([0,0,0])
        self.play(FadeIn(t, scale=1.5))
        self.wait()
        self.play(FadeOut(t, scale=0.5))

        full = MathTex("x_{1}\\vec{v_{1}}+x_{2}\\vec{v_{2}}+x_{3}\\vec{v_{3}}+x_{4}\\vec{v_{4}}=\\vec{b}")
        self.play(Create(full))

        self.wait()

        t2 = Text("Or more familiarly...")
        self.play(full.animate.shift(UP*2.5))
        self.play(FadeIn(t2, scale=1.5))
        self.play(FadeOut(t2, scale=0.5))

        self.wait()

        v1 = MathTex("\\vec{v_{1}}")
        v2 = MathTex("\\vec{v_{2}}").next_to(v1, direction=RIGHT)
        v3 = MathTex("\\vec{v_{3}}").next_to(v2, direction=RIGHT)
        v4 = MathTex("\\vec{v_{4}}").next_to(v3, direction=RIGHT)

        ls = [Line(v1.get_center() + [0,0.3,0],v1.get_center() + [0,0.9,0]),
              Line(v2.get_center() + [0,0.3,0],v2.get_center() + [0,0.9,0]),
              Line(v3.get_center() + [0,0.3,0],v3.get_center() + [0,0.9,0]),
              Line(v4.get_center() + [0,0.3,0],v4.get_center() + [0,0.9,0]),
              Line(v1.get_center() + [0,-0.3,0],v1.get_center() + [0,-0.9,0]),
              Line(v2.get_center() + [0,-0.3,0],v2.get_center() + [0,-0.9,0]),
              Line(v3.get_center() + [0,-0.3,0],v3.get_center() + [0,-0.9,0]),
              Line(v4.get_center() + [0,-0.3,0],v4.get_center() + [0,-0.9,0])]

        tot = VGroup(v1, *ls, v2, v3, v4)
        m = MobjectMatrix([[ls[0],ls[1],ls[2],ls[3]],
                           [v1, v2, v3, v4],
                           [ls[4],ls[5],ls[6],ls[7]]],left_bracket="(", right_bracket=")").scale(0.8)

        cs = MobjectMatrix([[MathTex("x_{1}")],[MathTex("x_{2}")],[MathTex("x_{3}")],[MathTex("x_{4}")]]).scale(0.8).next_to(m, direction=RIGHT)

        full = VGroup(cs, m, MathTex("=\\vec{b}").next_to(cs)).move_to([0,0,0])

        self.play(Create(full))

        self.wait(1)

        self.play(full.animate.shift(DOWN*1.8))
        self.play(full.animate.scale(0.7))

        b1 = Brace(m, sharpness=1, direction=DOWN)
        b1l = b1.get_tex("A")
        b2 = Brace(cs, sharpness=1, direction=DOWN)
        b2l = b2.get_tex("\\vec{x}")

        self.play(Create(b1), Create(b1l), Create(b2), Create(b2l))

        self.wait(2)

        fin = MathTex("A\\vec{x}=\\vec{b}").shift(UP*0.3)
        self.play(Create(fin))
        self.play(Indicate(fin))

        self.wait()

        self.play(*[FadeOut(mob, shift=[cos(10*PI*random()), sin(10*PI*random()), 0]) for mob in self.mobjects])

        self.wait()


class explainSolve(Scene):
    def construct(self):
        sys1 = MathTex("A\\vec{x}=\\vec{b}")
        sys2 = MathTex("A^{-1}A\\vec{x}=A^{-1}\\vec{b}")
        sys3 = MathTex("\\vec{x}=A^{-1}\\vec{b}")

        t1 = Text("Right?")
        t2 = Text("Not Quite...")

        alm = MathTex("\\vec{x} \\neq A^{-1}\\vec{b}")

        self.play(Create(sys1))
        self.wait(2)
        self.play(Transform(sys1, sys2, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        self.play(Transform(sys2, sys3, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        self.play(Transform(sys3, t1, replace_mobject_with_target_in_scene=True))
        self.wait()
        self.play(Transform(t1, t2, replace_mobject_with_target_in_scene=True))
        self.wait()
        self.play(Transform(t2, alm, replace_mobject_with_target_in_scene=True))
        self.wait()
        self.play(FadeOut(alm, scale=0.5))
        self.wait()

        title = Text("Least Sqaures Solution").move_to((0, 3, 0))
        ul = Underline(title)

        ls = [MathTex("A\\vec{x}=proj_{im(A)}(\\vec{b})"),
              MathTex("\\Rightarrow \\vec{b}-A\\vec{x}\\in im(A)^{\\perp}"),
              MathTex("\\Rightarrow\\vec{b}-A\\vec{x}\\in ker(A^{T})"),
              MathTex("\\Rightarrow\\vec{0}=A^{T}(\\vec{b}-A\\vec{x})=A^{T}\\vec{b}-A^{T}A\\vec{x}"),
              MathTex("\\Rightarrow A^{T}A\\vec{x}=A^{T}\\vec{b}"),
              MathTex("\\Rightarrow \\vec{x}=\\underbrace{(A^{T}A)^{-1}A^{T}}_{\\text{Psuedo-Inverse (pinv)}}\\vec{b}")]

        # norm = MathTex("\\vec{x}=(A^{T}A)^{-1}A^{T}\\vec{b}")
        norm = MathTex("\\vec{x}=pinv(\\vec{b})")
        l2 = MathTex("pinv = (A^{T}A)^{-1}A^{T}")

        ls[0].move_to([0,2,0])

        for i in range(1,len(ls)):
            ls[i].next_to(ls[i-1], direction=DOWN)


        self.play(Create(title), Create(ul))
        self.wait()

        self.play(*[Create(eq, run_time=2) for eq in ls])

        self.wait(2)

        self.play(*[FadeOut(ls[i], shift=UP*2) for i in range(len(ls)-1)], ls[-1].animate.shift(UP*2))
        norm.move_to(ls[-1].get_center())

        self.wait()

        self.play(Transform(ls[-1], norm))
        self.play(ls[-1].animate.shift(UP))
        l2.next_to(ls[-1], direction=DOWN)
        self.play(Create(l2))

        self.wait()

        self.play(*[FadeOut(mob, shift=[UP * 10]) for mob in self.mobjects])

        self.wait()

class Recap(Scene):

    def construct(self):
        title = Text("The String Art Algorithm").move_to((0, 3, 0))
        ul = Underline(title)

        self.play(Create(title), Create(ul))

        self.wait()


        blist = BulletedList("Take an input image and convert it to grayscale",
                             "Determine the basis of strings that will make the recreation",
                             "Save each individual string image as vector compressions of the canvas",
                             "Compress the grayscale images into vectors",
                             "Let the target vector equal b",
                             "Let A equal a matrix whose image is the basis of strings",
                             "Let x equal the vector of scalars denoting how many times\n each string should be added to the canvas",
                             "Solve for the least squares solution of x using the Psuedo-Inverse",
                             "Round the solution vector to whole numbers",
                             "Place strings on canvas according to closest solution").shift(LEFT*1.5 + DOWN*0.6).scale(0.6)

        self.play(Create(blist))

        self.wait()

        self.play(*[FadeOut(mob, scale=0.5) for mob in self.mobjects])

        self.wait()

class CodeDemo(Scene):
    def construct(self):
        code = '''
a = np.concatenate(vectors, axis=1)
target = Image.open("wolverine.png").convert("L")
b = np.asarray(target)
b = b.reshape((b.size, 1))
sol = np.linalg.pinv(a).dot(b - (255 * np.ones((250000, 1))))
      '''

        rendered_code = Code(code=code, tab_width=4, background="window",
                             language="Python", font="Monospace")

        yes = Text("Radical\nCode")

        self.play(Create(rendered_code))

        self.wait(3)

        rect = RoundedRectangle(corner_radius=0.5).move_to(rendered_code.get_center())

        self.play(Transform(rendered_code,yes), Create(rect))

        self.wait()

        a1 = Arrow(start=LEFT, end=RIGHT)
        a1.next_to(yes, direction=LEFT)

        i1 = ImageMobject("./wolverine.png")
        i1.next_to(a1, direction=LEFT)

        self.wait()

        a2 = Arrow(start=LEFT, end=RIGHT)
        a2.next_to(yes, direction=RIGHT)

        i2 = ImageMobject("./final.jpeg")
        i2.next_to(a2, direction=RIGHT)

        self.play(FadeIn(i1,scale=1), FadeIn(i2, scale=1), Create(a1), Create(a2))

        self.wait()




