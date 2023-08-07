from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel


class ThrowAndCrashAnimationObject(LightObject):
    pass


class ThrowAndCrashAnimationEffectObject(LightObject):
    pass


class ThrowAndCrashAnimation:

    def createColor(self):
        if(random.random() < 0.33):
            return (0, 0, 150)
        elif(random.random() < 0.33):
            return (0, 150, 0)
        else:
            return (150, 0, 0)

    def createLightObj(self):
        obj = ThrowAndCrashAnimationObject()
        obj.speed = 40
        obj.acceleration = -25
        obj.colors.append(self.createColor())
        obj.spread = 2
        obj.position = 0
        obj.brightness = 1
        return obj

    def createExplosionObj(self, maxSpeed: float):
        obj = ThrowAndCrashAnimationEffectObject()
        obj.speed = 10 + (maxSpeed - 10) * random.random()
        obj.acceleration = -25
        obj.colors.append(self.createColor())
        obj.spread = 2
        obj.position = 0
        obj.brightness = 1
        return obj

    def loop(self, lightObjects: [], gameTime: GameTime, inputs: Inputs):
        if inputs.button_X.on_press:
            lightObjects.append(self.createLightObj())

        for obj in lightObjects:
            if type(obj) is ThrowAndCrashAnimationObject:
                obj.position = obj.position + obj.speed * gameTime.delta_time
                obj.speed = obj.speed + obj.acceleration * gameTime.delta_time
                if obj.position < -obj.spread:
                    lightObjects.remove(obj)
                    self.explode(obj, lightObjects)

                for obj2 in lightObjects:
                    if obj == obj2:
                        continue
                    if type(obj2) is ThrowAndCrashAnimationObject:
                        if abs(obj2.position - obj.position) < 1:
                            if obj.spread > obj2.spread:
                                self.combine(obj, obj2)
                                lightObjects.remove(obj2)
                            else:
                                self.combine(obj2, obj)
                                lightObjects.remove(obj)

            if type(obj) is ThrowAndCrashAnimationEffectObject:
                obj.position = obj.position + obj.speed * gameTime.delta_time
                obj.speed = obj.speed + obj.acceleration * gameTime.delta_time
                obj.brightness = random.random()
                if obj.speed < 0:
                    lightObjects.remove(obj)
                obj.brightness = obj.brightness - 0.7 * gameTime.delta_time

    def combine(self, obj, obj2):
        obj.spread = obj.spread + obj2.spread
        obj.speed = 25
        obj.colors[0] = (obj.colors[0][0] + obj2.colors[0][0],
                         obj.colors[0][1] + obj2.colors[0][1],
                         obj.colors[0][2] + obj2.colors[0][2])

    def explode(self, obj, lightObjects):
        for x in range(obj.spread):
            lightObjects.append(self.createExplosionObj(40))
