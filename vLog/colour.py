# All colours
# Styles
RESET = 0
BOLD = 1
GRAYED = 2
ITALIC = 3
UNDERLINE = 4
INVERTED = 7

# Colours
BLACK = 30
BLOOD = 31
GREEN = 32
GOLD = 33
BLUE = 34
MAGENTA = 35
CYAN = 36

# Light Colours
RED = 91
LIME = 92
YELLOW = 93
INDIGO = 94
PINK = 95
SKY = 96
WHITE = 97

# Highlighted
H_BLACK = 40
H_BLOOD = 41
H_GREEN = 42
H_GOLD = 43
H_BLUE = 44
H_MAGENTA = 45
H_CYAN = 46
H_WHITE = 47

# Light Highlighted
H_GRAY = 100
H_RED = 101
H_LIME = 102
H_YELLOW = 103
H_INDIGO = 104
H_PINK = 105
H_SKY = 106
H_CREAM = 107

# end All Colours

def col( c: int, s: int = 0, contrast_correction: bool = False ) -> str:
    if s == INVERTED and contrast_correction:  # Contrast correction
        match c:
            case 34:
                s = RESET
                c = H_BLUE
            case _:  # Not implemented solutions
                s = s
                c = c

    return f"\033[0;{s};{c}m"

def get_second_colour( colour:int ) -> int:  # CAN LARGELY BE UPGRADED
    match colour:
        # NORMAL Dark -> NORMAL Light
        case 31:
            return 91
        case 32:
            return 92
        case 33:
            return 93
        case 34:
            return 94
        case 35:
            return 95
        case 36:
            return 96
        # NORMAL Light -> NORMAL Dark
        case 91:
            return 31
        case 92:
            return 32
        case 93:
            return 33
        case 94:
            return 34
        case 95:
            return 35
        case 96:
            return 36
        # H Dark -> NORMAL Dark
        case 40:
            return 30
        case 41:
            return 31
        case 42:
            return 32
        case 43:
            return 33
        case 44:
            return 34
        case 45:
            return 35
        case 46:
            return 36
        # H Light -> NORMAL Light
        case 100:
            return 2
        case 101:
            return 91
        case 102:
            return 92
        case 103:
            return 93
        case 104:
            return 94
        case 105:
            return 95
        case 106:
            return 96
        case 107:
            return 97
        case _:
            return colour