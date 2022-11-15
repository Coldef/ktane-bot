from constants import *
import colors_modules
import partner

texts = [MODULE_BUTTON_TEXT_ABORT, MODULE_BUTTON_TEXT_DETONATE, MODULE_BUTTON_TEXT_HOLD, MODULE_BUTTON_TEXT_PRESS]
texts_dict = {
    MODULE_BUTTON_TEXT_ABORT: "abort",
    MODULE_BUTTON_TEXT_DETONATE: "detonate",
    MODULE_BUTTON_TEXT_HOLD: "hold",
    MODULE_BUTTON_TEXT_PRESS: "press"
}


def solve_button(batteries, indicators):  # CAR, FRK
    loop = True
    while loop:
        ans = partner.ask_player(MODULE_BUTTON_ASK_BUTTON)  # color, text
        if ans == CANCEL_PHRASE:
            return
        words = ans.split(" ")
        if len(words) == 2:
            if words[0] in colors_modules.colors and words[1] in texts:
                words[0] = colors_modules.colors_dict[words[0]]
                words[1] = texts_dict[words[1]]
                loop = False
    color = words[0]
    text = words[1]

    if color == "blue" and text == "abort":
        return __hold_down()
    elif batteries > 1 and text == "detonate":
        return MODULE_BUTTON_PRESS_RELEASE
    elif color == "white" and indicators[0]:
        return __hold_down()
    elif batteries > 2 and indicators[1]:
        return MODULE_BUTTON_PRESS_RELEASE
    elif color == "yellow":
        return __hold_down()
    elif color == "red" and text == "hold":
        return MODULE_BUTTON_PRESS_RELEASE
    else:
        return __hold_down()
    return


def __hold_down():
    loop = True
    color = ""
    while loop:
        ret = partner.ask_player(MODULE_BUTTON_HOLD)
        if ret in colors_modules.colors:
            loop = False
            color = colors_modules.colors_dict[ret]

    if color == "blue":
        return MODULE_BUTTON_N4
    elif color == "white":
        return MODULE_BUTTON_N1
    elif color == "yellow":
        return MODULE_BUTTON_N5
    else:
        return MODULE_BUTTON_N1

    return
