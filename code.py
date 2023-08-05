from renderer import Renderer
import globals
from gametime import GameTime
from animationLogic import Logic
import time
from inputs import Inputs

lightObjects = []

gameTime: GameTime = GameTime()
logic: Logic = Logic(lightObjects)
renderer: Renderer = Renderer()
inputs: Inputs = Inputs()


while True:
    gameTime.loop()
    inputs.loop()
    logic.loop(lightObjects, gameTime, inputs)
    renderer.renderer(lightObjects)
    #time.sleep(globals.TIME_BETWEEN_FRAMES)
    #gameTime.print_state()
