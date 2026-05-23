import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11, board.GP20, board.GP21,
)
keyboard.row_pins = (board.GP12, board.GP13, board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.VOLD, KC.VOLU, KC.N1, KC.N2, KC.N3,   KC.N4,
        KC.N5,   KC.N6,   KC.N7, KC.N8, KC.N9,   KC.N0,

        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.C,
        KC.V, KC.U, KC.I, KC.O, KC.P, KC.LBRC,

        KC.A, KC.S, KC.D, KC.F, KC.G,    KC.N,
        KC.M, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
    ],
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.NKRO)