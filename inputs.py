import board
from digitalio import DigitalInOut, Pull
from analogio import AnalogIn
from gamepadbutton import GamepadButton
import json
from collections import OrderedDict


# Setup the pins
BUTTON_A1_PIN = board.A1
BUTTON_A_PIN = board.BTN_A
BUTTON_B_PIN = board.BTN_B
BUTTON_X_PIN = board.BTN_X
BUTTON_Y_PIN = board.BTN_Y
ANALOG_X_PIN = board.A2
ANALOG_Y_PIN = board.A3


class Inputs:
    """Keeps track of the game pad's state"""

    button_A1: GamepadButton = GamepadButton()
    """Get the A1 button's state"""

    button_A: GamepadButton = GamepadButton()
    """Get the A button's state"""

    button_B: GamepadButton = GamepadButton()
    """Get the B button's state"""

    button_X: GamepadButton = GamepadButton()
    """Get the X button's state"""

    button_Y: GamepadButton = GamepadButton()
    """Get the Y button's state"""

    button_A_io: DigitalInOut
    """Read the raw digital input for the button"""

    button_B_io: DigitalInOut
    """Read the raw digital input for the button"""

    button_X_io: DigitalInOut
    """Read the raw digital input for the button"""

    button_Y_io: DigitalInOut
    """Read the raw digital input for the button"""

    def __init__(self):
        # Setup button inputs
        self.button_A_io = DigitalInOut(BUTTON_A_PIN)
        self.button_A1_io = DigitalInOut(BUTTON_A1_PIN)
        self.button_B_io = DigitalInOut(BUTTON_B_PIN)
        self.button_X_io = DigitalInOut(BUTTON_X_PIN)
        self.button_Y_io = DigitalInOut(BUTTON_Y_PIN)

        # Pull-up buttons
        self.button_A1_io.pull = Pull.UP
        self.button_A_io.pull = Pull.UP
        self.button_B_io.pull = Pull.UP
        self.button_X_io.pull = Pull.UP
        self.button_Y_io.pull = Pull.UP

        self.loop()

    def loop(self):
        """Call this exactly once per frame to keep the buttons states up to date"""

        self.button_A1.loop(self.read_button_value(self.button_A1_io))
        self.button_A.loop(self.read_button_value(self.button_A_io))
        self.button_B.loop(self.read_button_value(self.button_B_io))
        self.button_X.loop(self.read_button_value(self.button_X_io))
        self.button_Y.loop(self.read_button_value(self.button_Y_io))

    def read_button_value(self, button):
        """Reads the buttons value"""
        # The buttons are pulled up, meaning if they are not pushed they are set to True (High)
        # When the buttons are pressed they are set to False (Low)
        return not button.value

    def print_state(self):
        """Print the overall state of the game pad"""
        print(
            json.dumps(
                OrderedDict(
                    {
                        "A1": self.button_A.is_pressed,
                        "A": self.button_A.is_pressed,
                        "B": self.button_B.is_pressed,
                        "X": self.button_X.is_pressed,
                        "Y": self.button_Y.is_pressed,
                    }
                )
            )
        )

    def print_state_detailed(self):
        """Print the full state of the game pad"""
        print(
            json.dumps(
                OrderedDict(
                    {
                        "A1": self.button_A.__dict__,
                        "A": self.button_A.__dict__,
                        "B": self.button_B.__dict__,
                        "X": self.button_X.__dict__,
                        "Y": self.button_Y.__dict__,
                    }
                )
            )
        )
