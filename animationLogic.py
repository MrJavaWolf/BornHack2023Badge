from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel
from runningLightsAnimation import RunningLightsAnimation
from groupAllObjectsAnimation import GroupAllObjectsAnimation
from glowAnimation import GlowAnimation
from throwAndCrashAnimation import ThrowAndCrashAnimation

class Logic:
    state: int = 0
    noInteraction: RunningLightsAnimation
    groupAllObjectsAnimation: GroupAllObjectsAnimation
    glowAnimation: GlowAnimation
    throwAndCrashAnimation: ThrowAndCrashAnimation

    def __init__(
        self,
        lightObjects: []
    ):
        self.noInteraction = RunningLightsAnimation()
        self.glowAnimation = GlowAnimation()
        #self.noInteraction.initialize(lightObjects)
        self.groupAllObjectsAnimation = GroupAllObjectsAnimation(10)
        self.throwAndCrashAnimation = ThrowAndCrashAnimation()
    
    
    def loop(self, lightObjects: [], gameTime: GameTime, inputs: Inputs):
        if inputs.button_B.on_press:
            self.groupAllObjectsAnimation.initialize(lightObjects, gameTime)
        elif inputs.button_B.is_pressed:
            self.groupAllObjectsAnimation.loop(lightObjects, gameTime)
        
        elif inputs.button_Y.on_press:
            self.glowAnimation.initialize(lightObjects, gameTime)
        elif inputs.button_Y.is_pressed:
            self.glowAnimation.loop(lightObjects, gameTime)
        
        else:
            #self.noInteraction.loop(lightObjects, gameTime, inputs)
            self.throwAndCrashAnimation.loop(lightObjects, gameTime, inputs)
