from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel


class RunningLightsAnimation:
    MAX_ACCELERATION_CHANGE: float = 20
    MAX_SPEED: float = 10

    def initialize(self, lightObjects: []):
        lightObjects.clear()
        lightObjects.append(self.CreateLightObject([(255, 0, 0)], 3))
        lightObjects.append(self.CreateLightObject([(0, 255, 0), (255, 0, 0)], 3))
        lightObjects.append(self.CreateLightObject([(0, 0, 255)], 3))
        lightObjects.append(self.CreateLightObject(spread=3))
        lightObjects.append(self.CreateLightObject(spread=3))
        lightObjects.append(self.CreateLightObject(spread=3))
        for obj in lightObjects:
            obj.position = random.random() * globals.NUMBER_OF_PIXELS
            obj.speed = (random.random() * 2 - 1) * self.MAX_SPEED
            obj.acceleration = (random.random() * 2 - 1) * self.MAX_ACCELERATION_CHANGE

    def CreateLightObject(self, color: [] = None, spread: float = None):
        obj = LightObject()
        if color is None:
            for i in range(random.randint(1, 3)):
                if(random.random() < 0.33):

                    obj.colors.append(
                        (0, random.random() * 255, random.random() * 255)
                    )
                elif(random.random() < 0.33):
                    obj.colors.append(
                        ( random.random() * 255,0, random.random() * 255)
                    )
                else:
                    obj.colors.append(
                        ( random.random() * 255, random.random() * 255,0)
                    )
        else:
            obj.colors = color

        if spread is None:
            obj.spread = 1 + random.random() * 4
        else:
            obj.spread = spread

        obj.speed = random.random() * 5.0 * (random.random() - 1)
        return obj
    
    def loop(self, lightObjects: [], gameTime: GameTime, inputs: Inputs):
        if (
            inputs.button_A.on_press
            or inputs.button_A1.on_press
            or inputs.button_X.on_press
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
