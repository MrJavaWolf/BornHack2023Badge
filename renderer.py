import globals
import neopixel
import Tween.Tween


class Renderer:
    def renderer(self, objs: []):
        for i in range(0, globals.NUMBER_OF_PIXELS):
            globals.pixel.fill((0,0,0))

        for obj in objs:
            for objColorIndex, objColor in enumerate(obj.colors):
                for spread in range((int)(obj.spread * 2)):
                    pixelIndex = (int)(obj.position + spread - obj.spread / 2)

                    if pixelIndex >= globals.NUMBER_OF_PIXELS or pixelIndex < 0:
                        continue
                    distanceBrightness = self.DistanceToBrightness(
                        (float)(pixelIndex),
                        (float)(obj.position) + (float)(objColorIndex),
                        obj.spread
                    )
                    
                    globals.pixel[pixelIndex] = self.AddColors(
                        globals.pixel[pixelIndex],
                        self.ApplyBrightness(objColor, distanceBrightness * obj.brightness),
                    )
        globals.pixel.show()

    def AddColor(self, c1, c2):
        result = c1 + c2
        if result > 255:
            return 255
        else:
            return result

    def AddColors(self, c1: neopixel.RGB, c2: neopixel.RGB):
        return (
            self.AddColor(c1[0], c2[0]),
            self.AddColor(c1[1], c2[1]),
            self.AddColor(c1[2], c2[2]),
        )

    def ApplyBrightness(self, c1: neopixel.RGB, brightness: float):
        return (c1[0] * brightness, c1[1] * brightness, c1[2] * brightness)

    def DistanceToBrightness(self, num1: float, num2: float, spread: float):
        distance = abs(num1 - num2)
        if distance > spread:
            return 0
        res = Tween.Tween.sineout(distance / spread)
        return res



    # def renderer(self, objs: []):
    #     for i in range(0, globals.NUMBER_OF_PIXELS):
    #         globals.pixel[i] = (0, 0, 0)
    #         for obj in objs:
    #             for objColorIndex, objColor in enumerate(obj.colors):
                    
    #                 if i < obj.position + objColorIndex - obj.spread or i > obj.position + objColorIndex + obj.spread:
    #                     continue

    #                 distanceBrightness = self.DistanceToBrightness(
    #                     (float)(i),
    #                     (float)(obj.position) + (float)(objColorIndex),
    #                     obj.spread,
    #                 )
    #                 if distanceBrightness == 0:
    #                     continue

    #                 globals.pixel[i] = self.AddColors(
    #                     globals.pixel[i],
    #                     self.ApplyBrightness(objColor, distanceBrightness),
    #                 )
    #     globals.pixel.show()
