from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel
from noInteractionAnimation import NoInteractionAnimation
from groupAllObjectsAnimation import GroupAllObjectsAnimation



class Logic:
    state: int = 0
    noInteraction: NoInteractionAnimation
    groupAllObjectsAnimation: GroupAllObjectsAnimation

    def __init__(
        self,
        lightObjects: []
    ):
        lightObjects.append(self.CreateLightObject([(255, 0, 0)], 3))
        lightObjects.append(self.CreateLightObject([(0, 255, 0), (255, 0, 0)], 3))
        lightObjects.append(self.CreateLightObject([(0, 0, 255)], 3))
        lightObjects.append(self.CreateLightObject(spread=3))
        lightObjects.append(self.CreateLightObject(spread=3))
        lightObjects.append(self.CreateLightObject(spread=3))
        self.noInteraction = NoInteractionAnimation()
        self.noInteraction.initialize(lightObjects)
        self.groupAllObjectsAnimation = GroupAllObjectsAnimation(10)

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
        if inputs.button_B.on_press:
            self.groupAllObjectsAnimation.initialize(lightObjects, gameTime)
        if inputs.button_B.is_pressed:
            self.groupAllObjectsAnimation.loop(lightObjects, gameTime)
        else:
            self.noInteraction.loop(lightObjects, gameTime, inputs)

