from constants import *
import partner


def solve_memory():
    sequences = [0, 1, 2, 3, 4]  # 5 stages
    for i in range(len(sequences)):
        ans = partner.ask_player(MODULE_MEMORY_STAGE + " " + str(i + 1)).strip().replace(" ", "")
        if ans == CANCEL_PHRASE:
            return
        display_number = int(ans[0])
        buttons = ans[1:]

        if i == 0:
            if display_number == 1 or display_number == 2:
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + "2")
                sequences[i] = (buttons[1], "2")  # (number, place) will be (str, str)
            elif display_number == 3:
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + "3")
                sequences[i] = (buttons[2], "3")
            elif display_number == 4:
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + "4")
                sequences[i] = (buttons[3], "4")
        elif i == 1:
            if display_number == 1:
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + "4")
                sequences[i] = ("4", str(buttons.find("4") + 1))
            elif display_number == 2 or display_number == 4:
                place = sequences[0][1]  # first stage answer's place
                number = str(buttons[int(place) - 1])
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + place)
                sequences[i] = (number, place)
            elif display_number == 3:
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + "1")
                sequences[i] = (buttons[0], "1")
        elif i == 2:
            if display_number == 1:
                number = sequences[1][0]  # second stage answer's number
                place = str(buttons.find(number) + 1)
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + number)
                sequences[i] = (number, place)
            elif display_number == 2:
                number = sequences[0][0]  # second stage answer's number
                place = str(buttons.find(number) + 1)
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + number)
                sequences[i] = (number, place)
            elif display_number == 3:
                number = str(buttons[2])
                place = str(3)
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + place)
                sequences[i] = (number, place)
            elif display_number == 4:
                number = "4"
                place = str(buttons.find(number) + 1)
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + number)
                sequences[i] = (number, place)
        elif i == 3:
            if display_number == 1:
                number = sequences[0][0]
                place = sequences[0][1]
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + place)
                sequences[i] = (number, place)
            elif display_number == 2:
                number = str(buttons[0])
                place = "1"
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + place)
                sequences[i] = (number, place)
            elif display_number == 3 or display_number == 4:
                number = sequences[1][0]
                place = sequences[1][1]
                partner.tell_player(MODULE_MEMORY_PRESS_P + " " + place)
                sequences[i] = (number, place)
        elif i == 4:
            if display_number == 1:
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + sequences[0][0])
            elif display_number == 2:
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + sequences[1][0])
            elif display_number == 3:
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + sequences[3][0])
            elif display_number == 4:
                partner.tell_player(MODULE_MEMORY_PRESS_N + " " + sequences[2][0])

    return

