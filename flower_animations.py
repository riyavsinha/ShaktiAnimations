
from manim.animation.transform import ApplyMethod
from manim.utils.rate_functions import squish_rate_func, there_and_back, linear, smooth
from flower import FlowerBuddy, FlowerMode

class Blink(ApplyMethod):
    def __init__(self, flower_buddy: FlowerBuddy, **kwargs):
        ApplyMethod.__init__(self, flower_buddy.eyes.blink, rate_func=squish_rate_func(there_and_back), **kwargs)

class EyeSmile(ApplyMethod):
    def __init__(self, flower_buddy: FlowerBuddy, **kwargs):
        ApplyMethod.__init__(self, flower_buddy.eyes.eye_smile, rate_func=there_and_back, **kwargs)

