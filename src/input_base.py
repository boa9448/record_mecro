from enum import IntEnum


class RecordType(IntEnum):
    KEYBOARD = 1
    MOUSE    = 2

    def to_string(self) -> str:
        if self == RecordType.KEYBOARD:
            return "keyboard"
        elif self == RecordType.MOUSE:
            return "mouse"
        else:
            raise ValueError("Invalid RecordType")

class KeyState(IntEnum):
    PRESS   = 1
    RELEASE = 2

    def to_string(self) -> str:
        if self == KeyState.PRESS:
            return "press"
        elif self == KeyState.RELEASE:
            return "release"
        else:
            raise ValueError("Invalid KeyState")


class MouseButton(IntEnum):
    LEFT = 1
    RIGHT = 4
    MIDDLE = 16

    @staticmethod
    def from_string(button_str):
        if button_str == "left":
            return MouseButton.LEFT
        elif button_str == "right":
            return MouseButton.RIGHT
        elif button_str == "middle":
            return MouseButton.MIDDLE
        else:
            raise ValueError("Invalid MouseButton")

    def to_string(self) -> str:
        if self == MouseButton.LEFT:
            return "left"
        elif self == MouseButton.RIGHT:
            return "right"
        elif self == MouseButton.MIDDLE:
            return "middle"
        else:
            raise ValueError("Invalid MouseButton")


class MouseState(IntEnum):
    PRESS = 0
    RELEASE = 1

    def to_string(self) -> str:
        if self == MouseState.PRESS:
            return "press"
        elif self == MouseState.RELEASE:
            return "release"
        else:
            raise ValueError("Invalid MouseState")