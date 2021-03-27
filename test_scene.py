from manim import *
from flower import FlowerBuddy

class TestScene(Scene):
    def construct(self):
        flower = FlowerBuddy()
        self.add(flower)
        self.play(Transform(flower, flower.generate_target().shift(DOWN)))
        self.play(flower.mouth.animate.o_mouth())