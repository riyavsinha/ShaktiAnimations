from enum import auto

from manim import SVGMobject, Line, Mobject, Dot
from manim.utils.color import *
from manim.constants import *
from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from manim.mobject.geometry import Circle
from manim.utils.space_ops import get_norm
import os
from enum import Enum

class FlowerMode(Enum):
    INIT = 'INIT'
    SMILE = 'SMILE'
    WAVE = 'WAVE'
    PONDER = 'PONDER'
    SHRUG = 'SHRUG'
    SURPRISE = 'SURPRISE'


class FlowerBuddy(SVGMobject):

    def __init__(self, color=PINK, core_color='#feaaf8', **kwargs):
        # Initial properties
        self.parts_named = False
        self.flower_mode: FlowerMode = FlowerMode.INIT
        self.corner_scale_factor = 1
        self.start_corner = None
        self.left_arm_theta: float = 0
        self.right_arm_effective_angle: int = 0
        # Load file
        svg_file = os.path.join(os.getcwd(), 'flower_buddy.svg')
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        # Name parts
        # Post-load initializations
        self.color = color  # after load since SVGMobject init resets
        self.core_color = core_color
        if self.start_corner is not None:
            self.to_corner(self.start_corner)
        self.init_colors()
        # Sub class conversions
        FlowerMouth.convert_from_super(self.mouth)
        self.remove(*self.pupils)
        self.remove(*self.sclera)
        self.add(self.eyes)
        self.mouth.smile()

    def init_colors(self):
        if not self.parts_named:
            self.name_parts()
        SVGMobject.init_colors(self)
        self.body.set_color(self.color)
        self.mouth.set_fill(BLACK)
        try:
            self.core.set_color(self.core_color)
        except AttributeError:
            self.core.set_color('#feaaf8')
        self.eyes.initialize_colors()
        return self

    def copy(self):
        copy_mobject = SVGMobject.copy(self)
        # copy_mobject.name_parts()
        return copy_mobject

    def name_parts(self):
        self.right_arm: SVGMobject = self.submobjects[0]
        self.right_leg: SVGMobject = self.submobjects[1]
        self.left_leg: SVGMobject = self.submobjects[2]
        self.left_arm: SVGMobject = self.submobjects[3]
        self.head: SVGMobject = self.submobjects[4]
        self.stomach: SVGMobject = self.submobjects[5]
        self.core: SVGMobject = self.submobjects[6]
        self.body: VGroup = VGroup(self.right_leg, self.right_arm, self.left_leg, self.left_arm, self.head,
                                   self.stomach)
        self.sclera = [self.submobjects[7], self.submobjects[8]]
        self.pupils = [self.submobjects[9], self.submobjects[10]]
        self.eyes: FlowerEyes = FlowerEyes(self.sclera, self.pupils)
        self.mouth: FlowerMouth = self.submobjects[11]

    # ANIMATIONS

    def change_mode(self, mode: FlowerMode):
        if self.flower_mode == mode:
            return
        elif mode == FlowerMode.SMILE:
            self.flower_mode = mode
            self.smile()
            return
        elif mode == FlowerMode.WAVE:
            self.flower_mode = mode
        elif mode == FlowerMode.SURPRISE:
            self.flower_mode = mode
            self.o_mouth()
            return

    # Body

    def start_waving(self):
        self.left_arm.current_time = 0.000001
        start = self.left_arm.get_start()
        end = self.left_arm.get_end()

        def updater(mob, dt):
            self.left_arm.current_time += dt * 3
            new_angle = np.arcsin(np.sin(self.left_arm.current_time)) * 10 * DEGREES
            if new_angle > 0 and self.left_arm_theta >= 0:
                self.left_arm.rotate(new_angle - self.left_arm_theta, about_point=start)
            elif new_angle < 0 and self.left_arm_theta <= 0:
                self.left_arm.rotate(new_angle - self.left_arm_theta, about_point=end)
            elif new_angle > 0 and self.left_arm_theta < 0:
                self.left_arm.rotate(-self.left_arm_theta, about_point=end)
                self.left_arm.rotate(2 * new_angle - self.left_arm_theta, about_point=start)
            elif new_angle < 0 and self.left_arm_theta > 0:
                self.left_arm.rotate(-self.left_arm_theta, about_point=start)
                self.left_arm.rotate(2 * new_angle - self.left_arm_theta, about_point=end)
            self.left_arm_theta = new_angle

        self.add_updater(updater)

    def stop_waving(self):
        start = self.left_arm.get_start()
        end = self.left_arm.get_end()

        def updater(mob, dt):
            self.left_arm.current_time += dt * 3
            new_angle = np.arcsin(np.sin(self.left_arm.current_time)) * 10 * DEGREES
            if self.left_arm_theta == 0:
                if len(self.updaters) > 0:
                    self.remove_updater(self.updaters[0])
                return
            if new_angle > 0 and self.left_arm_theta >= 0:
                self.left_arm.rotate(new_angle - self.left_arm_theta, about_point=start)
                self.left_arm_theta = new_angle
            elif new_angle < 0 and self.left_arm_theta <= 0:
                self.left_arm.rotate(new_angle - self.left_arm_theta, about_point=end)
                self.left_arm_theta = new_angle
            elif new_angle > 0 and self.left_arm_theta < 0:
                self.left_arm.rotate(-self.left_arm_theta, about_point=end)
                self.left_arm_theta = 0
            elif new_angle < 0 and self.left_arm_theta > 0:
                self.left_arm.rotate(-self.left_arm_theta, about_point=start)
                self.left_arm_theta = 0

        self.remove_updater(self.updaters[0])
        self.add_updater(updater)

    def to_corner(self, vect=None, **kwargs):
        if vect is not None:
            SVGMobject.to_corner(self, vect, **kwargs)
        else:
            self.scale(self.corner_scale_factor)
            self.to_corner(DOWN + LEFT, **kwargs)
        return self

    def __iadd__(self, mobject):
        pass

    def __sub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def align_points_with_larger(self, larger_mobject):
        pass

    def __add__(self, mobject):
        pass


class FlowerMouth(SVGMobject):
    @classmethod
    def convert_from_super(cls, obj):
        obj.__class__ = FlowerMouth
        obj.original = obj.copy()

    def smile(self):
        self.reset_mouth()
        mouth_left_x = self.get_left()[0]
        middle_x = ((self.get_right()[0] - mouth_left_x) / 2) + mouth_left_x
        self.apply_function(
            lambda p: [p[0], abs(p[0] - middle_x) ** 2 + p[1], p[2]]
        )
        return self

    def ponder(self):
        self.reset_mouth()
        mouth_left_x = self.get_left()[0]
        self.apply_function(
            lambda p: [p[0] - (p[0] - mouth_left_x) / 2, p[1], p[2]]
        )
        return self

    def o_mouth(self):
        self.reset_mouth()
        middle_y = self.__middle_y()
        middle_x = self.__middle_x()
        y_symm = lambda y: -1 if y < middle_y else 1
        x_symm = lambda x: -1 if x > middle_x else 1
        self.apply_function(
            lambda p: [x_symm(p[0]) * self.__center_distance_x(p[0]) / 3 + p[0],
                       y_symm(p[1]) * self.__edge_distance_x(p[0]) / 1.3 + p[1], p[2]]
        )
        return self

    def reset_mouth(self):
        self.original.move_to(self)
        self.become(self.original)
        return self

    def __middle_x(self):
        mouth_left_x = self.get_left()[0]
        return ((self.get_right()[0] - mouth_left_x) / 2) + mouth_left_x

    def __middle_y(self):
        mouth_bottom_y = self.get_bottom()[1]
        return ((self.get_top()[1] - mouth_bottom_y) / 2) + mouth_bottom_y

    def __center_distance_x(self, x):
        middle_x = self.__middle_x()
        return abs(x - middle_x)

    def __edge_distance_x(self, x):
        mouth_left_x = self.get_left()[0]
        middle_x = self.__middle_x()
        middle_to_edge = middle_x - mouth_left_x
        return abs(self.__center_distance_x(x) - middle_to_edge)

class FlowerEyes(VGroup):
    def __init__(self, sclera, pupils):
        self.sclera_original = VGroup(*sclera)
        self.sclera = self.sclera_original.copy()
        self.pupils = VGroup(*pupils)
        VGroup.__init__(self, *self.sclera.submobjects, *self.pupils.submobjects)
        self.pupil_to_eye_width_ratio = 0.7
        self.pupil_dot_to_pupil_width_ratio = 0.3
        self.is_looking_direction_purposeful = False
        self.purposeful_looking_direction = UL
        self.init_pupils()

    def initialize_colors(self):
        self.sclera.set_fill(WHITE, opacity=1)
        self.pupils.set_fill(BLACK, opacity=1)

    def look(self, direction):
        self.reset()
        norm = get_norm(direction)
        if norm == 0:
            return
        direction /= norm
        self.purposeful_looking_direction = direction
        for pupil, sclera in zip(self.pupils.split(), self.sclera.split()):
            c = sclera.get_center()
            right = sclera.get_right() - c
            up = sclera.get_top() - c
            vect = direction[0] * right + direction[1] * up
            v_norm = get_norm(vect)
            p_radius = 0.5 * pupil.get_width()
            vect *= (v_norm - 0.75 * p_radius) / v_norm
            pupil.move_to(c + vect)
        self.pupils[1].align_to(self.pupils[0], DOWN)
        return self

    def look_at(self, point_or_mobject):
        if isinstance(point_or_mobject, Mobject):
            point = point_or_mobject.get_center()
        else:
            point = point_or_mobject
        self.look(point - self.sclera.get_center())
        return self

    def blink(self):
        eye_bottom_y = self.get_bottom()[1]
        self.apply_function(
            lambda p: [p[0], eye_bottom_y, p[2]]
        )
        return self

    def eye_smile(self):
        self.reset()
        eye_bottom_y = self.pupils.get_bottom()[1]
        middle_y = ((self.pupils.get_top()[1] - eye_bottom_y) / 2) + eye_bottom_y
        y_symm = lambda y: 1.2 if y < middle_y else 0
        self.pupils.apply_function(
            lambda p: [p[0], y_symm(p[1]) * (middle_y - p[1]) + p[1], p[2]]
        )
        self.sclera.scale(.9)
        return self

    def init_pupils(self):
        # Instead of what is drawn, make new circles.
        # This is mostly because the paths associated
        # with the eyes in all the drawings got slightly
        # messed up.
        for sclera, pupil in zip(self.sclera, self.pupils):
            pupil_r = sclera.get_width() / 2
            pupil_r *= self.pupil_to_eye_width_ratio
            dot_r = pupil_r
            dot_r *= self.pupil_dot_to_pupil_width_ratio

            new_pupil = Circle(
                radius=pupil_r,
                color=BLACK,
                fill_opacity=1,
                stroke_width=0,
            )
            dot = Circle(
                radius=dot_r,
                color=WHITE,
                fill_opacity=1,
                stroke_width=0,
            )
            new_pupil.move_to(pupil)
            pupil.become(new_pupil)
            dot.shift(
                new_pupil.get_boundary_point(UL) -
                dot.get_boundary_point(UL)
            )
            pupil.add(dot)

    def reset(self):
        # print(self.sclera_original.get_center())
        self.sclera_original.move_to(self.sclera)
        self.sclera.become(self.sclera_original)
        self.init_pupils()
        self.initialize_colors()
        return self
