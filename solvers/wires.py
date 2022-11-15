from constants import *
import colors_modules
import partner
import re


def solve_wires(even):
    """
    Solves the module wires. The player is asked to list the wire colors top down. (ex. blue blue white)
    :param even: The parity of the last digit of the bomb's serial number
    :return: Which wire should be cut as a string
    """
    arr = []
    loop = True
    while loop:
        ret = partner.ask_player(MODULE_WIRES_ASK_COLORS)
        if ret == CANCEL_PHRASE:
            return
        arr = re.split(" |-", ret)
        if 3 <= len(arr) <= 6:
            if all(i in colors_modules.colors for i in arr):
                loop = False
                for i in range(0, len(arr)):
                    arr[i] = colors_modules.colors_dict[arr[i]]

    if len(arr) == 3:
        if "red" not in arr:
            return MODULE_WIRES_CUT_SECOND
        elif arr[-1] == "white":
            return MODULE_WIRES_CUT_LAST
        elif arr.count("blue") > 1:
            return MODULE_WIRES_CUT_LAST + " " + COLOR_BLUE
        else:
            return MODULE_WIRES_CUT_LAST
    elif len(arr) == 4:
        if arr.count("red") > 1 and not even:
            return MODULE_WIRES_CUT_LAST + " " + COLOR_RED
        elif arr.count("red") == 0 and arr[-1] == "yellow":
            return MODULE_WIRES_CUT_FIRST
        elif arr.count("blue") == 1:
            return MODULE_WIRES_CUT_FIRST
        elif arr.count("yellow") > 1:
            return MODULE_WIRES_CUT_LAST
        else:
            return MODULE_WIRES_CUT_SECOND
    elif len(arr) == 5:
        if arr[-1] == "black" and not even:
            return MODULE_WIRES_CUT_FOURTH
        elif arr.count("red") == 1 and arr.count("yellow") > 1:
            return MODULE_WIRES_CUT_FIRST
        elif arr.count("black") == 0:
            return MODULE_WIRES_CUT_SECOND
        else:
            return MODULE_WIRES_CUT_FIRST
    elif len(arr) == 6:
        if arr.count("yellow") == 0 and not even:
            return MODULE_WIRES_CUT_THIRD
        elif arr.count("yellow") == 1 and arr.count("white") > 1:
            return MODULE_WIRES_CUT_FOURTH
        elif arr.count("red") == 0:
            return MODULE_WIRES_CUT_LAST
        else:
            return MODULE_WIRES_CUT_FOURTH

    return

