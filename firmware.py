import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
 
keyboard = KMKKeyboard()
 
# ---------------------------------------------------------------------------
# MATRIX PINS  (per schematic: C0-C9 = GP2-GP11, R0-R2 = GP12-GP14)
# ---------------------------------------------------------------------------
keyboard.col_pins = (
    board.GP2, board.GP3, board.GP4,  board.GP5,  board.GP6,
    board.GP7, board.GP8, board.GP9,  board.GP10, board.GP11,
)
keyboard.row_pins = (board.GP12, board.GP13, board.GP14)
# COL2ROW for diodes pointing column -> row. Flip to ROW2COL otherwise.
keyboard.diode_orientation = DiodeOrientation.COL2ROW
 
# ---------------------------------------------------------------------------
# ENCODERS  (per schematic: A1/B1 = GP15/GP16, A2/B2 = GP17/GP18)
# Switches are read through the matrix (row 3 cols 4 & 5),
# so pin_button is None.
# Tuple format: (pin_a, pin_b, pin_button, is_inverted)
# Flip is_inverted to True if the direction comes out reversed.
# ---------------------------------------------------------------------------
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP15, board.GP16, None, False),  # Encoder 1 (mute)
    (board.GP17, board.GP18, None, False),  # Encoder 2 (video)
)
# Per layer, per encoder: (counter-clockwise, clockwise)
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),  # Encoder 1: volume down / up
        (KC.VOLD, KC.VOLU),  # Encoder 2: volume down / up
    ),
]
keyboard.modules.append(encoder_handler)
 
# ---------------------------------------------------------------------------
# OLED -- 0.96" SSD1306 128x64 on I2C0 (GP0=SDA, GP1=SCL).
# If it shows up at 0x3D instead of 0x3C, change device_address.
# ---------------------------------------------------------------------------
display = Display(
    display=SSD1306(
        sda=board.GP0,
        scl=board.GP1,
        device_address=0x3C,
    ),
    width=128,
    height=64,
    entries=[
        TextEntry(text='sten0', x=64, y=32, x_anchor='M', y_anchor='M'),
    ],
)
keyboard.extensions.append(display)
 
# ---------------------------------------------------------------------------
# VIDEO TOGGLE KEYCODE
# Default: Alt+V (Zoom on Windows/Linux). Edit to match your app:
#   Zoom (macOS):    KC.LCMD(KC.LSFT(KC.V))
#   MS Teams (Win):  KC.LCTL(KC.LSFT(KC.O))
#   MS Teams (Mac):  KC.LCMD(KC.LSFT(KC.O))
#   Google Meet:     KC.LCTL(KC.E)   (KC.LCMD(KC.E) on macOS)
# ---------------------------------------------------------------------------
VIDEO = KC.LALT(KC.V)
 
# ---------------------------------------------------------------------------
# KEYMAP -- row 3 cols 4 & 5 are the encoder switches.
# ---------------------------------------------------------------------------
keyboard.keymap = [
    [
        # row 1
        KC.Q,  KC.W,  KC.E,  KC.R,    KC.T,   KC.Y,  KC.U,  KC.I,  KC.Y,    KC.P,
        # row 2
        KC.A,  KC.S,  KC.D,  KC.F,    KC.T,   KC.O,  KC.J,  KC.K,  KC.L,    KC.SCLN,
        # row 3
        KC.N2, KC.C,  KC.V,  KC.MUTE, VIDEO,  KC.N,  KC.M,  KC.N8, KC.QUOT, KC.LBRC,
    ],
]
 
if __name__ == '__main__':
    keyboard.go()
