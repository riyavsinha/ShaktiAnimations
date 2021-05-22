from manim import *
import os
from custom_objects import *
from flower import FlowerBuddy, FlowerColor
from flower_animations import Blink, EyeSmile
from utils import BraceWithText


class DefScene(Scene):
    def construct(self):
        voters = flower_army()
        self.play((FadeIn(voters)))
        voters_brace = BraceWithText(voters, r'Voters $I$', direction=UP)
        self.play(ShowCreation(voters_brace))
        voter_brace = BraceWithText(voters[2], r'Voter $i$')
        self.play(FadeIn(voter_brace))
        voter_set_not = MathTex(r'i \in I').next_to(voters_brace, UP, buff=LARGE_BUFF)
        self.play(Write(voter_set_not))
        self.play(Indicate(voter_set_not))
        self.play(FadeOut(VGroup(voter_set_not, voter_brace)))
        voter_group = VGroup(voters, voters_brace)
        self.play(Transform(voters, voters.generate_target().scale(.6).shift(UP * 3)),
                  Transform(voters_brace, BraceWithText(voters.target, r'Voters $I$', direction=RIGHT)))
        props = proposals().shift(DOWN * .5)
        self.play(FadeIn(props))
        props_brace = BraceWithText(props, r'Proposals $X$', direction=UP)
        self.play(FadeIn(props_brace))
        prop_brace_x = BraceWithText(props[2], r'$x$')
        prop_brace_y = BraceWithText(props[4], r'$y$')
        self.play(FadeIn(prop_brace_x), FadeIn(prop_brace_y))
        self.play(FadeOut(VGroup(prop_brace_x, prop_brace_y)))
        self.play(Transform(props, props.generate_target().scale(.6).shift(DOWN * 2)),
                  Transform(props_brace, BraceWithText(props.target, r'Proposals $X$', direction=RIGHT)))
        voter = voters[3]
        self.play(FadeOut(VGroup(*voters[:3], *voters[4:])),
                  Transform(voter, voter.generate_target().move_to(UP * 3)),
                  Transform(voters_brace, BraceWithText(voter.target, r'Voter $i$', direction=RIGHT)))
        u_line = NumberLine(include_numbers=True)
        u_line_100_numbs = [(i - 7) * 10 for i in range(15)]
        u_line_100 = NumberLine(unit_size=.1, x_min=-80, x_max=80, numbers_with_elongated_ticks=u_line_100_numbs)
        u_line_100.add_numbers(*u_line_100_numbs)
        a_pointer_group = create_nl_pointer('A', u_line, 0)
        self.play(ShowCreation(u_line))
        self.play(FadeIn(a_pointer_group))
        u_arrow = Arrow(voter.get_bottom() + DOWN * .1, a_pointer_group.get_top() + UP * .1)
        u_func = MathTex(r'u_i: X \rightarrow R').next_to(u_arrow)
        self.play(ShowCreation(u_arrow), Write(u_func))
        self.play(*update_to(a_pointer_group, u_line, 2))
        self.play(*update_to(a_pointer_group, u_line, 6))
        self.play(Transform(u_line, u_line_100))
        self.play(*update_to(a_pointer_group, u_line_100, 50))
        u_ln3_func = MathTex(r'u_i: X \rightarrow L^{(3)}').next_to(u_arrow)
        ln_func = MathTex(r'L^{(n)} = \{-n,\dots,-1,0,1,\dots,n\}').scale(.7).next_to(u_arrow, LEFT)
        u_line_l3 = NumberLine(x_min=-3, x_max=3 + 1e-8, include_numbers=True)
        self.play(Write(ln_func))
        self.play(Transform(u_func, u_ln3_func),
                  Transform(u_line, u_line_l3),
                  *update_to(a_pointer_group, u_line_l3, 2))
        u_ln1_func = MathTex(r'u_i: X \rightarrow L^{(1)}').next_to(u_arrow)
        u_line_l1 = NumberLine(x_min=-1, x_max=1 + 1e-8, include_numbers=True)
        self.play(Transform(u_func, u_ln1_func),
                  Transform(u_line, u_line_l1),
                  *update_to(a_pointer_group, u_line_l1, 1))
        self.play(Transform(u_func, u_ln3_func),
                  Transform(u_line, u_line_l3),
                  *update_to(a_pointer_group, u_line_l3, 2),
                  FadeOut(ln_func))
        b_pointer_group = create_nl_pointer('FB', u_line_l3, -2)
        c_pointer_group = create_nl_pointer('C', u_line_l3, -1)
        d_pointer_group = create_nl_pointer('D', u_line_l3, 1)
        e_pointer_group = create_nl_pointer('E', u_line_l3, 3)
        self.play(FadeIn(b_pointer_group))
        self.play(FadeIn(c_pointer_group))
        self.play(FadeIn(d_pointer_group))
        self.play(FadeIn(e_pointer_group))
        # e_circle = Ellipse(1, 2).move_to(e_pointer_group[0])
        # high_text = Tex(r'"high": a\\proposal has the\\highest given score').scale(.7).move_to(UP * 3 + LEFT * 3.5)
        # high_def = MathTex(r'u_i(x) \geq u_i(y), \forall y\in X').scale(.7).next_to(high_text, DOWN)
        # high_box = SurroundingRectangle(VGroup(high_text, high_def), buff=MED_SMALL_BUFF)
        # self.play(ShowCreation(e_circle))
        # self.play(Write(high_text), Write(high_def), ShowCreation(high_box))
        # self.wait(2)
        # self.play(FadeOut(high_text), FadeOut(high_def), FadeOut(high_box), Uncreate(e_circle))
        # b_circle = Ellipse(1, 2).move_to(b_pointer_group[0])
        # low_text = Tex(r'"low": a\\proposal has the\\lowest given score').scale(.7).move_to(UP * 3 + LEFT * 3.5)
        # low_def = MathTex(r'u_i(x) \leq u_i(y), \forall y\in X').scale(.7).next_to(low_text, DOWN)
        # low_box = SurroundingRectangle(VGroup(low_text, low_def), buff=MED_SMALL_BUFF)
        # self.play(ShowCreation(b_circle))
        # self.play(Write(low_text), Write(low_def), ShowCreation(low_box))
        # self.wait(2)
        # self.play(FadeOut(low_text), FadeOut(low_def), FadeOut(low_box), Uncreate(b_circle))
        # self.play(
        #     *update_to(a_pointer_group, u_line_l3, 0),
        #     *update_to(b_pointer_group, u_line_l3, 0),
        #     *update_to(c_pointer_group, u_line_l3, 0),
        #     *update_to(d_pointer_group, u_line_l3, 0),
        #     *update_to(e_pointer_group, u_line_l3, 0),
        #     Transform(a_pointer_group[1],
        #               Tex(r'ABCDEF').move_to(u_line_l3.number_to_point(0)).align_to(a_pointer_group, UP)),
        #     FadeOutAndShift(VGroup(
        #         b_pointer_group[1],
        #         c_pointer_group[1],
        #     ), RIGHT),
        #     FadeOutAndShift(VGroup(
        #         d_pointer_group[1],
        #         e_pointer_group[1],
        #     ), LEFT)
        # )
        # null_text = Tex(r'"null": no\\score is greater\\than another').scale(.7).move_to(UP*3 + LEFT*3.5)
        # null_def = MathTex(r'u_i(x) = u_i(y), \forall x,y\in X').scale(.7).next_to(null_text, DOWN)
        # null_box = SurroundingRectangle(VGroup(null_text, null_def), buff=MED_SMALL_BUFF)
        # self.play(Write(null_text), Write(null_def), ShowCreation(null_box))
        # self.wait(2)
        # self.play(FadeOut(null_text), FadeOut(null_def), FadeOut(null_box))
        # self.play(
        #     update_to(a_pointer_group, u_line_l3, 1)[0],
        #     update_to(b_pointer_group, u_line_l3, 1)[0],
        #     update_to(c_pointer_group, u_line_l3, 1)[0],
        #     update_to(d_pointer_group, u_line_l3, 1)[0],
        #     update_to(e_pointer_group, u_line_l3, 1)[0],
        #     Transform(a_pointer_group[1],
        #               Tex(r'ABCDEF').move_to(u_line_l3.number_to_point(1)).align_to(a_pointer_group, UP)),
        # )
        # self.play(
        #     update_to(a_pointer_group, u_line_l3, 0)[0],
        #     update_to(b_pointer_group, u_line_l3, 0)[0],
        #     update_to(c_pointer_group, u_line_l3, 0)[0],
        #     update_to(d_pointer_group, u_line_l3, 0)[0],
        #     update_to(e_pointer_group, u_line_l3, 0)[0],
        #     Transform(a_pointer_group[1],
        #               Tex(r'ABCDEF').move_to(u_line_l3.number_to_point(0)).align_to(a_pointer_group, UP)),
        # )
        # self.play(
        #     *update_to(a_pointer_group, u_line_l3, 2),
        #     *update_to(b_pointer_group, u_line_l3, -2),
        #     *update_to(c_pointer_group, u_line_l3, -1),
        #     *update_to(d_pointer_group, u_line_l3, 1),
        #     *update_to(e_pointer_group, u_line_l3, 3),
        #     Transform(a_pointer_group[1],
        #               Tex(r'A').move_to(u_line_l3.number_to_point(2)).align_to(a_pointer_group, UP)),
        #     FadeInFrom(VGroup(
        #         b_pointer_group[1],
        #         c_pointer_group[1],
        #     ), RIGHT),
        #     FadeInFrom(VGroup(
        #         d_pointer_group[1],
        #         e_pointer_group[1],
        #     ), LEFT)
        # )
        self.play(
            FadeOut(VGroup(
                voter,
                voters_brace,
                u_arrow,
                u_func
            )))
        u_group = VGroup(
            a_pointer_group,
            b_pointer_group,
            c_pointer_group,
            d_pointer_group,
            e_pointer_group,
            u_line
        )
        self.play(u_group.animate.shift(UP * 3))
        # u_brace = BraceWithText(u_group, r'')
        h3 = VGroup(*[Tex(str(i)) for i in range(-3, 4)]).arrange(buff=LARGE_BUFF).next_to(u_line, DOWN,
                                                                                           buff=MED_LARGE_BUFF)
        h3_dividers = VGroup(*[Line(middle_of_point(h3[i].get_top(), h3[i + 1].get_top()),
                                    middle_of_point(h3[i].get_top(), h3[i + 1].get_top()) + DOWN * 3.3)
                               for i in range(6)])
        self.play(Write(h3), ShowCreation(h3_dividers))
        self.play(FadeOut(props_brace))
        self.play(props[0].animate.next_to(h3[5], DOWN))
        self.play(props[1].animate.next_to(h3[1], DOWN))
        self.play(props[2].animate.next_to(h3[2], DOWN))
        self.play(props[3].animate.next_to(h3[4], DOWN))
        self.play(props[4].animate.next_to(h3[6], DOWN))
        self.play(props[5].animate.next_to(props[1], DOWN))
        h3_buckets = VGroup(*[MathTex('H_i^{(' + str(i) + ')}') for i in range(-3, 4)]).scale(.6).arrange(
            buff=.65).next_to(
            u_line, DOWN,
            buff=MED_LARGE_BUFF)
        self.play(Transform(h3, h3_buckets))
        self.play(VGroup(props, h3, h3_dividers, u_group).animate.shift(DOWN * 2))
        b_dec = MathTex(r'B_i = \{H_i^{(-n)}, \dots, H_i^0, \dots, H_i^{(n)}\}').shift(UP * 3)
        b_rect = SurroundingRectangle(b_dec, buff=MED_SMALL_BUFF)
        self.play(Write(b_dec), ShowCreation(b_rect))
        self.wait(2)
        self.play(FadeOut(VGroup(b_dec, b_rect)))
        score_def = Tex(r'$s_i(x) = l$ if $x \in H_i^{(l)}, l \in L^{(n)}$').shift(UP * 3)
        score_rect = SurroundingRectangle(score_def, buff=MED_SMALL_BUFF)
        self.play(Write(score_def), ShowCreation(score_rect))
        self.wait(2)
        # self.play(Indicate(h3[1]), Indicate(props[1]))
        # self.play(Indicate(h3[1]), Indicate(props[5]))
        # self.play(Indicate(h3[2]), Indicate(props[2]))
        # self.play(Indicate(h3[4]), Indicate(props[3]))
        # self.play(Indicate(h3[5]), Indicate(props[0]))
        # self.play(Indicate(h3[6]), Indicate(props[4]))
        self.play(FadeOut(VGroup(score_def, score_rect)))
        nar_def = Tex(r'Sincere Voting (Narrow):\\A voter votes according to their true preferences').shift(UP * 3.3)
        nar_math = MathTex(r'u_i(x) = s_i(x), \forall x \in X').next_to(nar_def, DOWN)
        nar_text = VGroup(nar_def, nar_math).scale(.6)
        nar_box = SurroundingRectangle(nar_text, buff=MED_SMALL_BUFF)
        self.play(Write(nar_def), Write(nar_math), ShowCreation(nar_box))
        self.wait(2)
        self.play(Indicate(b_pointer_group), Indicate(props[1]))
        self.play(Indicate(b_pointer_group), Indicate(props[5]))
        self.play(Indicate(c_pointer_group), Indicate(props[2]))
        self.play(Indicate(d_pointer_group), Indicate(props[3]))
        self.play(Indicate(a_pointer_group), Indicate(props[0]))
        self.play(Indicate(e_pointer_group), Indicate(props[4]))
        self.play(FadeOut(VGroup(nar_def, nar_math, nar_box)))
        wide_def = Tex(r'Sincere Voting (Wide):\\A voter keeps relative order of preferences the same').shift(UP * 3.3)
        wide_math = Tex(r'If $u_i(x) > u_i(y)$ then $s_i(x) \geq s_i(y), x,y \in X$').next_to(wide_def, DOWN)
        wide_text = VGroup(wide_def, wide_math).scale(.6)
        wide_box = SurroundingRectangle(wide_text, buff=MED_SMALL_BUFF)
        self.play(Write(wide_def), Write(wide_math), ShowCreation(wide_box))
        self.wait(2)
        self.play(indicate_in(VGroup(d_pointer_group, a_pointer_group)))
        shift_prop(self, props[3], props[0])
        self.play(indicate_out(VGroup(d_pointer_group, a_pointer_group)))
        self.play(indicate_in(VGroup(b_pointer_group, c_pointer_group)))
        shift_prop(self, props[1], h3[0])
        shift_prop(self, props[5], props[1])
        shift_prop(self, props[2], h3[1])
        self.play(indicate_out(VGroup(b_pointer_group, c_pointer_group)))
        self.play(FadeOut(VGroup(wide_def, wide_math, wide_box)))
        self.play(FadeOut(VGroup(u_group, props, h3, h3_dividers)))


def shift_prop(scene: Scene, m: Mobject, t: Point):
    scene.play(m.animate.set_color(YELLOW))
    scene.play(CounterclockwiseTransform(m, m.generate_target().next_to(t, DOWN)))
    scene.play(m.animate.set_color(WHITE))


def indicate_in(m: Mobject):
    return Transform(m, m.generate_target().scale(1.1).set_color(YELLOW))


def indicate_out(m: Mobject):
    return Transform(m, m.generate_target().scale(10 / 11).set_color(WHITE))


def middle_of_point(p1, p2):
    return (p1 + p2) / 2


def create_nl_pointer(label: str, nl: NumberLine, init_number: int):
    score_pointer = Triangle(fill_color=WHITE, fill_opacity=1, stroke_color=WHITE)
    score_pointer.rotate_in_place(PI).scale(.2).move_to(nl.number_to_point(init_number), UP).shift(
        UP * score_pointer.height)
    score_pointer_label = Tex(label).next_to(score_pointer, UP)
    return VGroup(score_pointer, score_pointer_label)


def update_to(pointer_group: VGroup, line: NumberLine, number: int):
    point = line.number_to_point(number)
    ptr = pointer_group[0]
    return [Transform(ptr, ptr.generate_target().move_to(point, UP).shift(
        UP * ptr.height)),
            Transform(pointer_group[1], pointer_group[1].generate_target().next_to(ptr.target, UP))]


def flower_army():
    return VGroup(*map(lambda col: FlowerBuddy(col), list(FlowerColor.values()) * 2)).arrange().scale(.8)


def proposals():
    return VGroup(*map(lambda x: proposal(x + 1), range(6))).arrange()


def proposal(number: int):
    paper = Rectangle(WHITE, 2, 1.5)
    text = Tex(r'Proposal\\' + chr(ord('@') + number)).move_to(paper).scale(.6)
    return VGroup(paper, text)
