import time
import board
import neopixel

FPS = 60
TIME_BETWEEN_FRAMES = 1 / FPS
NUMBER_OF_PIXELS = 45
EXTRA_FRAME_SIZE = 15
pixel = neopixel.NeoPixel(board.A0, NUMBER_OF_PIXELS, auto_write=False)
pixel.brightness = 0.4


class LightObject:
    position: float = 0
    colors: [] = []
    upDirection: bool = True
    brightness: float = 1
    speed: float = 3
    acceleration: float = 0.2
    spread: float = 2

    def __init__(self):
        self.colors = []
