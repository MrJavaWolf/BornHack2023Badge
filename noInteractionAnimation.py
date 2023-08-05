from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel


class NoInteractionAnimation:
    MAX_ACCELERATION_CHANGE: float = 20
    MAX_SPEED: float = 10

    def initialize(self, lightObjects: []):
        for obj in lightObjects:
            obj.position = random.random() * globals.NUMBER_OF_PIXELS
            obj.speed = (random.random() * 2 - 1) * self.MAX_SPEED
            obj.acceleration = (random.random() * 2 - 1) * self.MAX_ACCELERATION_CHANGE

    def loop(self, lightObjects: [], gameTime: GameTime, inputs: Inputs):
        if (
            inputs.button_A.on_press
            or inputs.button_A1.on_press
            or inputs.button_X.on_press
            or inputs.button_Y.on_press
            or inputs.button_B.on_press
        ):
            self.initialize(lightObjects)

        for obj in lightObjects:
            obj.position = obj.position + obj.speed * gameTime.delta_time
            if obj.position > globals.NUMBER_OF_PIXELS + globals.EXTRA_FRAME_SIZE:
                obj.position = -(globals.EXTRA_FRAME_SIZE - 1)
            elif obj.position < -globals.EXTRA_FRAME_SIZE:
                obj.position = globals.NUMBER_OF_PIXELS + globals.EXTRA_FRAME_SIZE - 1

            obj.acceleration = (
                obj.acceleration
                + (random.random() * 2 - 1)
                * self.MAX_ACCELERATION_CHANGE
                * gameTime.delta_time
            )
            obj.speed = (
                obj.speed
                + (random.random() * 2 - 1) * obj.acceleration * gameTime.delta_time
            )
            if obj.speed > self.MAX_SPEED:
                obj.speed = self.MAX_SPEED
                obj.acceleration = -obj.acceleration / 2

            if obj.speed < -self.MAX_SPEED:
                obj.speed = -self.MAX_SPEED
                obj.acceleration = -obj.acceleration / 2
