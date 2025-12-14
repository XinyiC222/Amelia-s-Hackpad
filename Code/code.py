import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros, Delay
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# ⭐ ENCODER SUPPORT - This enables the rotary encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Button pins
BUTTON_PINS = [board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
    pins=BUTTON_PINS,
    value_when_pressed=False,
)

# ⭐ ROTARY ENCODER CONFIGURATION
# Pins: A=GPIO26, B=GPIO29, Button=GPIO0
encoder_handler.pins = ((board.D26, board.D29, board.D0),)

# ⭐ VOLUME CONTROL MAPPING
# [clockwise, counter-clockwise, button press]
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),  # Volume Up/Down,  Mute
]

# RGB LEDs
rgb = RGB(
    pixel_pin=board.D6,
    num_pixels=2,
    hue_default=100,
)
keyboard.extensions.append(rgb)

# Your 4 button mappings
keyboard.keymap = [
    [
        # SW1 - Open Arc
        KC.Macro(
            Press(KC.LCMD),
            Tap(KC.SPACE),
            Release(KC.LCMD),
            Delay(100),
            "Arc",
            Delay(50),
            Tap(KC.ENTER),
        ),
        # SW2 - Open VS Code
        KC.Macro(
            Press(KC.LCMD),
            Tap(KC.SPACE),
            Release(KC.LCMD),
            Delay(100),
            "code",
            Delay(50),
            Tap(KC.ENTER),
        ),
        # SW3 - Save (Cmd+S)
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),
        # SW4 - photoshop
        KC.MACRO(
            Press(KC.LCMD),
            Tap(KC.SPACE),
            Release(KC.LCMD),
            Delay(100),
            "Photoshop",
            Delay(50),
            Tap(KC.ENTER),
        ),
    ]
]

if __name__ == "__main__":
    keyboard.go()
