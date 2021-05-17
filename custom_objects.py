import os

from manim import Rectangle, Circle, Arc, VGroup, Line, SVGMobject, Ellipse, Tex
from manim.constants import *
from manim.utils.color import *

def lock_object():
    bar_flatness_shift = UP*.2
    lock = Rectangle(height=2, width=2)
    pad = Circle(radius=.5, color=WHITE)
    pad.move_to(lock)
    bar = Arc(arc_center=lock.get_top(), angle=TAU/2, radius=.8).shift(bar_flatness_shift)
    line1 = Line(start=bar.get_start(), end=bar.get_start()-bar_flatness_shift)
    line2 = Line(start=bar.get_end(), end=bar.get_end()-bar_flatness_shift)
    return VGroup(lock, pad, bar, line1, line2)

def decentralized_web():
    center = Circle(radius=.5, color=WHITE)
    sat_1 = Circle(radius=.25, color=WHITE).shift(UP*.5+LEFT+.2)
    edge_1 = Line(center, sat_1)
    sat_2 = Circle(radius=.35, color=WHITE).shift(UP*.3+RIGHT+.5)
    edge_2 = Line(center, sat_2)
    sat_3 = Circle(radius=.25, color=WHITE).shift(DOWN*.5+RIGHT+.2)
    edge_3 = Line(center, sat_3)
    edge_3_1 = Line(sat_2, sat_3)
    sat_4 = Circle(radius=.35, color=WHITE).move_to(center).shift(DOWN+LEFT*.75)
    edge_4 = Line(center, sat_4)
    return VGroup(center, sat_1, edge_1, sat_2, edge_2, sat_3, edge_3, edge_3_1, sat_4, edge_4)

def etc_dollar():
    etc = SVGMobject(os.path.join(os.getcwd(), 'assets', 'etc_logo.svg')).scale(.35)
    rect = Rectangle('#38b238', 1.1, 1.8)
    return VGroup(etc, rect)

def dollar():
    dol = Tex(r'\$', color='#85bb65').scale(1.4)
    rect = Rectangle('#85bb65', 1.1, 1.8)
    return VGroup(dol, rect)