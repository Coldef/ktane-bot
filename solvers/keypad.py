from constants import *
import partner

solutions = [
    [MODULE_KEYPAD_S1, MODULE_KEYPAD_S2, MODULE_KEYPAD_S3, MODULE_KEYPAD_S4, MODULE_KEYPAD_S5, MODULE_KEYPAD_S6,
     MODULE_KEYPAD_S7],

    [MODULE_KEYPAD_S8, MODULE_KEYPAD_S1, MODULE_KEYPAD_S7, MODULE_KEYPAD_S9, MODULE_KEYPAD_S10, MODULE_KEYPAD_S6,
     MODULE_KEYPAD_S11],

    [MODULE_KEYPAD_S12, MODULE_KEYPAD_S13, MODULE_KEYPAD_S9, MODULE_KEYPAD_S14, MODULE_KEYPAD_S15, MODULE_KEYPAD_S3,
     MODULE_KEYPAD_S10],

    [MODULE_KEYPAD_S16, MODULE_KEYPAD_S17, MODULE_KEYPAD_S18, MODULE_KEYPAD_S5, MODULE_KEYPAD_S14, MODULE_KEYPAD_S11,
     MODULE_KEYPAD_S19],

    [MODULE_KEYPAD_S20, MODULE_KEYPAD_S19, MODULE_KEYPAD_S18, MODULE_KEYPAD_S21, MODULE_KEYPAD_S17, MODULE_KEYPAD_S22,
     MODULE_KEYPAD_S23],

    [MODULE_KEYPAD_S16, MODULE_KEYPAD_S8, MODULE_KEYPAD_S24, MODULE_KEYPAD_S25, MODULE_KEYPAD_S20, MODULE_KEYPAD_S26,
     MODULE_KEYPAD_S27]
    ]
symbols = [
    MODULE_KEYPAD_S1,
    MODULE_KEYPAD_S2,
    MODULE_KEYPAD_S3,
    MODULE_KEYPAD_S4,
    MODULE_KEYPAD_S5,
    MODULE_KEYPAD_S6,
    MODULE_KEYPAD_S7,
    MODULE_KEYPAD_S8,
    MODULE_KEYPAD_S9,
    MODULE_KEYPAD_S10,
    MODULE_KEYPAD_S11,
    MODULE_KEYPAD_S12,
    MODULE_KEYPAD_S13,
    MODULE_KEYPAD_S14,
    MODULE_KEYPAD_S15,
    MODULE_KEYPAD_S16,
    MODULE_KEYPAD_S17,
    MODULE_KEYPAD_S18,
    MODULE_KEYPAD_S19,
    MODULE_KEYPAD_S20,
    MODULE_KEYPAD_S21,
    MODULE_KEYPAD_S22,
    MODULE_KEYPAD_S23,
    MODULE_KEYPAD_S24,
    MODULE_KEYPAD_S25,
    MODULE_KEYPAD_S26,
    MODULE_KEYPAD_S27,
]


def solve_keypad():
    correct_column = []
    loop = True
    while loop:
        ans = partner.ask_player(MODULE_KEYPAD_ASK_SYMBOLS)
        if ans == CANCEL_PHRASE:
            return
        # words = __find_symbols_from_string(ans, symbols)  # words are guaranteed to be in symbols list
        words = ans.split(MODULE_KEYPAD_NEXT)
        words = [s.strip() for s in words]
        if len(words) == 4:
            for col in solutions:
                if all(i in col for i in words):
                    correct_column = col
                    loop = False

    solution_list = []
    for s in correct_column:
        if s in words:
            solution_list.append(s)
    return " ".join(solution_list)


def __find_symbols_from_string(s, lst):
    found = []
    while s:
        loop = True
        i = 0
        while loop:
            curr = s[:i]
            if curr in lst:
                loop = False
                s = s[i:]
                found.append(curr)
            i += 1
    return found
