from globals import LightObject
import globals
from gametime import GameTime
import random
from inputs import Inputs
import neopixel
import Tween.Tween

class GroupAllObjectsAnimation:
    animationTime : float = 1.5
    startTime : float = 0
    toPosition: float
    initialPositions = []

    def __init__(self, toPosition: float):
        self.toPosition = toPosition

    def initialize(self, lightObjects: [], gameTime: GameTime):
        self.startTime = gameTime.total_time
        self.initialPositions = []
        for obj in lightObjects:
            self.initialPositions.append(obj.position)

    def loop(self, lightObjects: [], gameTime: GameTime):
        ratio = abs(self.startTime - gameTime.total_time) / self.animationTime
        if ratio > 1:
            ratio = 1
        for index, obj in enumerate(lightObjects):
            totalDistanceToMove = self.toPosition - self.initialPositions[index]
            distanceToMove = totalDistanceToMove * Tween.Tween.BounceEaseOut(ratio)
            obj.position = self.initialPositions[index] + distanceToMove  

