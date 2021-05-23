from manim import *
import os
from custom_objects import *
from flower import FlowerBuddy, FlowerColor
from flower_animations import Blink, EyeSmile
from utils import BraceWithText


class DefSingleVoterScene(Scene):
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


class DefBallotScene(Scene):
    def construct(self):
        voters = flower_army().shift(UP * .5)
        self.play((FadeIn(voters)))
        B = ballots()
        [B[i].next_to(voters[i], DOWN) for i in range(6)]
        self.play(FadeIn(B))
        B_def = Tex(r'Ballot Profile:\\The set of ballots for all voters').shift(UP * 3.3)
        B_math = MathTex(r'B = (B_i)_{i \in I}').next_to(B_def, DOWN)
        B_text = VGroup(B_def, B_math).scale(.8)
        B_box = SurroundingRectangle(B_text, buff=MED_SMALL_BUFF)
        B_brace = BraceWithText(B, r'$B$')
        self.play(Write(B_def), Write(B_math), ShowCreation(B_box))
        self.play(FadeIn(B_brace))
        self.wait(2)
        self.play(FadeOut(VGroup(B_def, B_math, B_box, B_brace)))
        Bmi_def = Tex(r'Ballot Profile without $i$:\\The set of ballots excluding voter $i$').shift(UP * 3.3)
        Bmi_math = MathTex(r'B_{-i} = B \setminus B_i').next_to(Bmi_def, DOWN)
        Bmi_text = VGroup(Bmi_def, Bmi_math).scale(.8)
        Bmi_box = SurroundingRectangle(Bmi_text, buff=MED_SMALL_BUFF)
        Bmi_brace = BraceWithText(B, r'$B_{-4}$')
        self.play(Write(Bmi_def), Write(Bmi_math), ShowCreation(Bmi_box))
        self.play(FadeOut(VGroup(voters[3], B[3])))
        self.play(FadeIn(Bmi_brace))
        self.wait(2)
        self.play(FadeOut(VGroup(Bmi_def, Bmi_math, Bmi_box, Bmi_brace)))
        self.play(FadeIn(VGroup(voters[3], B[3])))
        score_def = Tex(
            r'Score of Proposal $x$:\\The score of a proposal is the sum of scores given by each voter').shift(UP * 3.3)
        score_math = MathTex(r's(x,B) =', r'\sum_{i \in I} s_i(x)', r'=',
                             r'\sum_{l \in L} l \cdot \#\{i \in I : x \in H_i^{(l)}\}').next_to(score_def, DOWN)
        score_text = VGroup(score_def, score_math).scale(.7)
        score_box = SurroundingRectangle(score_text, buff=MED_SMALL_BUFF)
        self.play(Write(score_def), Write(score_math), ShowCreation(score_box))
        self.play(indicate_in(score_math[1]))
        self.play(FadeOut(B))
        self.play(voters.animate.shift(DOWN * 1.5))
        score_boards = VGroup(*[hold_obj(score_board(v), voters[i]) for i, v in enumerate([-2, 1, 3, 3, 1, 3])])
        self.play(FadeIn(score_boards))
        score_eq = MathTex(r'-2 + 1 + 3 + 3 + 1 + 3', r'= 1(-2) + 2(1) + 3(3)').move_to(
            middle_of_point(score_boards.get_top(), score_box.get_bottom()))
        self.play(Write(score_eq[0]))
        self.play(indicate_in(score_math[3]), indicate_out(score_math[1]))
        voters_with_boards = VGroup(*map(lambda x: VGroup(*x), zip(list(voters), list(score_boards))))
        self.play(voters_with_boards.animate.shift(DOWN).scale(.6))
        h_score_boards = VGroup(*[score_board(v) for v in range(-3, 4)]).arrange(buff=LARGE_BUFF).next_to(score_eq,
                                                                                                          DOWN)
        self.play(FadeIn(h_score_boards))
        self.play(voters_with_boards[0].animate.next_to(h_score_boards[1], DOWN),
                  voters_with_boards[4].animate.next_to(h_score_boards[4], DOWN),
                  voters_with_boards[5].animate.next_to(h_score_boards[6], DOWN))
        self.play(voters_with_boards[1].animate.next_to(voters_with_boards[4], DOWN, buff=0),
                  voters_with_boards[3].animate.next_to(voters_with_boards[5], DOWN, buff=0))
        self.play(voters_with_boards[2].animate.next_to(voters_with_boards[3], DOWN, buff=0))
        self.play(FadeOut(score_boards))
        self.play(Write(score_eq[1]))
        self.wait(2)
        self.play(FadeOut(VGroup(score_def, score_math, score_box, score_eq, h_score_boards, voters)))


class DefScene(Scene):
    def construct(self):
        # Acceptable Proposals
        acc_def = Tex(r'Acceptable Candidate:\\A proposal whose score is at least 10\% of the number of voters').shift(
            UP * 3.3)
        acc_math = MathTex(r's(x,B) \geq 0.1 \cdot |I|').next_to(acc_def, DOWN)
        acc_text = VGroup(acc_def, acc_math).scale(.9)
        acc_box = SurroundingRectangle(acc_text, buff=MED_SMALL_BUFF)
        self.play(Write(acc_def), Write(acc_math), ShowCreation(acc_box))
        self.wait(2)
        accex_voters = VGroup(Tex('100'), FlowerBuddy(FlowerColor['PINK']).scale(.5)).arrange().next_to(acc_box, DOWN,
                                                                                                        buff=MED_LARGE_BUFF)
        self.play(FadeIn(accex_voters))
        self.play(FadeOut(VGroup(acc_def, acc_math, acc_box, accex_voters)))
        # Common Budget
        cb_def = Tex(r'Common Budget $M$: Total budget for funding projects').shift(
            UP * 3.3)
        cb_math = Tex(r'Budget of $x$: $m(x) (\leq M)$').next_to(cb_def, DOWN)
        cb_text = VGroup(cb_def, cb_math).scale(.9)
        cb_box = SurroundingRectangle(cb_text, buff=MED_SMALL_BUFF)
        self.play(Write(cb_def), Write(cb_math), ShowCreation(cb_box))
        self.wait(2)
        M_box = Rectangle(WHITE, 1, 12)
        M_text = Tex(r'Budget $M$ = 12').move_to((M_box))
        M = VGroup(M_box, M_text)
        ma = prop_budget('A', 3)
        mb = prop_budget('B', 5)
        mc = prop_budget('C', 4)
        md = prop_budget('D', 6)
        me = prop_budget('E', 4)
        mf = prop_budget('F', 2)
        m_top_row = VGroup(ma, mc, me).arrange().next_to(M, DOWN)
        m_bot_row = VGroup(mb, md, mf).arrange().next_to(m_top_row, DOWN)
        self.play(FadeIn(M))
        self.play(FadeIn(m_top_row))
        self.play(FadeIn(m_bot_row))
        self.play(FadeOut(VGroup(cb_def, cb_math, cb_box)))
        # Exhausting the budget
        exhaust_def = Tex(
            r'"Exhausting the Common Budget $M$": A subset of proposals that are within the common budget, but have no room for any other proposal').shift(
            UP * 3.4)
        exhaust_math = MathTex(r'S \subset X: &\sum_{x \in S} m(x) \leq M \\',
                               r'\forall y \in X \setminus S: &\sum_{x \in S} m(x) + m(y) > M').next_to(exhaust_def,
                                                                                                        DOWN)
        exhaust_text = VGroup(exhaust_def, exhaust_math).scale(.6)
        exhaust_box = SurroundingRectangle(exhaust_text, buff=MED_SMALL_BUFF)
        self.play(Write(exhaust_def), Write(exhaust_math), ShowCreation(exhaust_box))
        self.wait(2)
        self.play(indicate_in(exhaust_math[0]))
        ms = VGroup(ma, mb, mc, md, me, mf)
        self.play(ma.animate.move_to(M.get_left(), aligned_edge=LEFT).shift(DOWN * .14))
        self.play(mc.animate.next_to(ma, RIGHT, buff=0))
        self.play(indicate_out(exhaust_math[0]), indicate_in(exhaust_math[1]))
        self.play(mf.animate.next_to(mc, RIGHT, buff=0))
        self.play(Transform(me, me.generate_target().next_to(mf, RIGHT, buff=0), rate_func=there_and_back, run_time=2))
        self.play(indicate_out(exhaust_math[1]))
        self.play(FadeOut(VGroup(exhaust_def, exhaust_math, exhaust_box, ms)))


class DefProcedureScene(Scene):
    def construct(self):
        bseq_def = Tex('Ballot Sequence')
        bseq_eq = MathTex(r'&x_1, x_2, \dots, x_k \in X\\',
                          r'&s(x_1, B) \geq s(x_2, B) \geq \dots \geq s(x_k, B)').next_to(bseq_def, DOWN)
        bseq_text = VGroup(bseq_def, bseq_eq).shift(UP * 3.3)
        bseq_box = SurroundingRectangle(bseq_text, buff=MED_SMALL_BUFF)
        self.play(Write(bseq_text), ShowCreation(bseq_box))
        prop_score_cost = [
            ['A', 1, 3],
            ['B', 2, 5],
            ['C', 4, 4],
            ['D', 2, 6],
            ['E', 3, 4],
            ['F', 3, 2]
        ]
        table = text_table(prop_score_cost).shift(DOWN*1.75 + RIGHT*2)
        table_row = VGroup(Tex('Proposals'), Tex('Scores'), Tex('Costs')).arrange(DOWN, buff=LARGE_BUFF).next_to(table, LEFT, buff=LARGE_BUFF)
        self.play(FadeIn(VGroup(table, table_row)))
        sorted_prop_score_cost = sorted(table, key=lambda x: int(x[1].get_tex_string()), reverse=True)
        curlocs = list(map(lambda x: x.get_center(), table))
        self.play(*[r.animate.move_to(curlocs[sorted_prop_score_cost.index(r)]) for r in table])



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


def ballots():
    return VGroup(*map(lambda x: ballot(x + 1), range(6))).arrange()


def ballot(number: int):
    paper = Rectangle(WHITE, 2, 1.5)
    text = MathTex(r'B_' + str(number)).move_to(paper).scale(.6)
    return VGroup(paper, text)


def proposals():
    return VGroup(*map(lambda x: proposal(x + 1), range(6))).arrange()


def proposal(number: int):
    paper = Rectangle(WHITE, 2, 1.5)
    text = Tex(r'Proposal\\' + chr(ord('@') + number)).move_to(paper).scale(.6)
    return VGroup(paper, text)


def score_board(number: int):
    stick = Line(DOWN * .25, ORIGIN)
    board = Rectangle(r'#e3e3e3', .5, .5, fill_opacity=1).move_to(stick.get_top(), aligned_edge=DOWN)
    text = Tex(str(number), color='#6c00a1').move_to(board)
    return VGroup(stick, board, text)


def hold_obj(obj, flower):
    obj.move_to(flower.right_arm.get_center(), aligned_edge=DOWN).shift(RIGHT * .2 + UP * .1)
    return obj


def prop_budget(letter, amt):
    rect = Rectangle('#880000', 1, amt, stroke_color=WHITE, stroke_width=1, fill_opacity=1)
    prop_txt = Tex(letter).scale(.5).next_to(rect, DOWN, buff=SMALL_BUFF)
    cost_txt = Tex(str(amt)).move_to(rect)
    return VGroup(rect, prop_txt, cost_txt)

def text_table(arr):
    return VGroup(
        *map(lambda row: VGroup(*map(lambda s: Tex(str(s)), row)).arrange(DOWN, buff=LARGE_BUFF),
             arr)
    ).arrange(buff=LARGE_BUFF)