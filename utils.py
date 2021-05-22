from manim import *

def BraceWithText(mobj: Mobject, text: str, **kwargs):
    brace = Brace(mobj, **kwargs)
    brace_text = brace.get_text(text)
    return VGroup(brace, brace_text)