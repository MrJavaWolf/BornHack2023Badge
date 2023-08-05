



from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel
import Tween.Tween

class GlowLightObject(LightObject):
    brightnessFrom: float
    brightnessTo: float
    startTime: float
    endTime: float

class GlowAnimation:
    numberOfLightGlows : int = 10
    min_glow_change_time: float = 1.5
    max_glow_change_time: float = 10
    
    def initialize(self, lightObjects: [], gameTime: GameTime):
        lightObjects.clear()
        for i in range(self.numberOfLightGlows):
            lightObjects.append(self.CreateLightObject(gameTime))

    def CreateLightObject(self, gameTime: GameTime, color: [] = None, spread: float = None):
        obj = GlowLightObject()
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
        
        obj.brightnessFrom = random.random()
        obj.brightnessTo = random.random()
        obj.startTime = gameTime.total_time
        obj.endTime = gameTime.total_time + self.min_glow_change_time + random.random() * (self.max_glow_change_time - self.min_glow_change_time) 
        obj.position = random.random() * globals.NUMBER_OF_PIXELS

        return obj


    def loop(self, lightObjects: [], gameTime: GameTime):

        for index, obj in enumerate(lightObjects):
            ratio =  (gameTime.total_time - obj.startTime) / (obj.endTime - obj.startTime)
            if ratio <= 1:
                tweenedRatio = Tween.Tween.cubicout(ratio)
                obj.brightness = self.translate(tweenedRatio, 0, 1, obj.brightnessFrom, obj.brightnessTo)
            else:
                obj.brightness = obj.brightnessTo 
                obj.brightnessFrom = random.random()
                obj.brightnessTo = random.random()
                obj.startTime = gameTime.total_time
                obj.endTime = gameTime.total_time + self.min_glow_change_time + random.random() * (self.max_glow_change_time - self.min_glow_change_time) 

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)