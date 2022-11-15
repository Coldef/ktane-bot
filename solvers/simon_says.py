from constants import *
import colors_modules
import partner


def solve_ss():
    vowel = None
    errors = None
    loop = True
    while loop:
        if vowel is None:
            vowel = __ask_vowel()
            if vowel == CANCEL_PHRASE:
                return
        if errors is None:
            errors = __ask_errors()
            if errors == CANCEL_PHRASE:
                return

        if errors is not None and vowel is not None:
            ans = partner.ask_player(MODULE_SS_ASK_COLOR)
            if ans == CANCEL_PHRASE:
                return
            words = ans.split(" ")
            if all(i in colors_modules.colors for i in words):
                for i in range(len(words)):
                    cur_color = words[i]

                    if vowel:
                        if errors == 0:
                            if cur_color == COLOR_RED:
                                words[i] = COLOR_BLUE
                            elif cur_color == COLOR_BLUE:
                                words[i] = COLOR_RED
                            elif cur_color == COLOR_GREEN:
                                words[i] = COLOR_YELLOW
                            elif cur_color == COLOR_YELLOW:
                                words[i] = COLOR_GREEN

                        elif errors == 1:
                            if cur_color == COLOR_RED:
                                words[i] = COLOR_YELLOW
                            elif cur_color == COLOR_BLUE:
                                words[i] = COLOR_GREEN
                            elif cur_color == COLOR_GREEN:
                                words[i] = COLOR_BLUE
                            elif cur_color == COLOR_YELLOW:
                                words[i] = COLOR_RED

                        elif errors == 2:
                            if cur_color == COLOR_RED:
                                words[i] = COLOR_GREEN
                            elif cur_color == COLOR_BLUE:
                                words[i] = COLOR_RED
                            elif cur_color == COLOR_GREEN:
                                words[i] = COLOR_YELLOW
                            elif cur_color == COLOR_YELLOW:
                                words[i] = COLOR_BLUE

                    else:
                        if errors == 0:
                            if cur_color == COLOR_RED:
                                words[i] = COLOR_BLUE
                            elif cur_color == COLOR_BLUE:
                                words[i] = COLOR_YELLOW
                            elif cur_color == COLOR_GREEN:
                                words[i] = COLOR_GREEN
                            elif cur_color == COLOR_YELLOW:
                                words[i] = COLOR_RED

                        elif errors == 1:
                            if cur_color == COLOR_RED:
                                words[i] = COLOR_RED
                            elif cur_color == COLOR_BLUE:
                                words[i] = COLOR_BLUE
                            elif cur_color == COLOR_GREEN:
                                words[i] = COLOR_YELLOW
                            elif cur_color == COLOR_YELLOW:
                                words[i] = COLOR_GREEN

                        elif errors == 2:
                            if cur_color == COLOR_RED:
                                words[i] = COLOR_YELLOW
                            elif cur_color == COLOR_BLUE:
                                words[i] = COLOR_GREEN
                            elif cur_color == COLOR_GREEN:
                                words[i] = COLOR_BLUE
                            elif cur_color == COLOR_YELLOW:
                                words[i] = COLOR_RED

            partner.tell_player(" ".join(words))

    return


def __ask_vowel():
    loop = True
    while loop:
        ans = partner.ask_player(MODULE_SS_ASK_VOWEL)
        if ans == CANCEL_PHRASE:
            return CANCEL_PHRASE
        if ans == YES:
            return True
        elif ans == NO:
            return False

    return


def __ask_errors():
    loop = True
    while loop:
        ans = partner.ask_player(MODULE_SS_ASK_ERRORS)
        if ans == CANCEL_PHRASE:
            return CANCEL_PHRASE
        if ans.isdigit():
            return int(ans)

    return
