from solvers import wires, button, keypad, simon_says, memory, maze
import partner
import colors_modules
from constants import *

"""
1. odota lausetta "puretaan pommi"
2. kysy "parillinen vai pariton" (sarjanumeron viimeinen numero)
3. kysy "montako paristoa" (sanoista numeroihin?)
4. kysy "palaako CAR ja FRK valo"
5. sano "valmis"

ohjelman kulku:
pelaaja sanoo "pura x" missä x on moduulin nimi:
    botti siirtyy ohjeistamaan moduulin purkua
    jos pelaaja sanoo peruutus sanan milloin tahansa, ohjelma siirtyy takaisin odottamaan moduulin valintaa
"""


def main():
    wait_for_start()

    ret = even_or_odd()
    if ret == EVEN:
        even = True
    else:
        even = False

    ret = num_of_batteries()
    batteries = int(ret)

    car_frk = indicators()

    partner.tell_player(READY)
    # SETUP DONE

    loop = True
    while True:
        answer = wait_for_module()
        if answer == BOMB_DEFUSED_PHRASE:
            partner.tell_player(BOMB_DEFUSED_RESPONSE)
            return
        words = answer.split(" ")
        if words[0] == MODULE_SELECTION_KEYWORD:
            module = " ".join(words[1:])
            print("module selected: " + module)
            if module == MODULE_WIRES:
                partner.tell_player(wires.solve_wires(even))
            elif module == MODULE_BUTTON:
                partner.tell_player(button.solve_button(batteries, car_frk))
            elif module == MODULE_KEYPAD:
                partner.tell_player(keypad.solve_keypad())
            elif module == MODULE_SIMON_SAYS:
                simon_says.solve_ss()
            elif module == MODULE_MEMORY:
                memory.solve_memory()
            elif module == MODULE_MAZE:
                partner.tell_player(maze.solve_maze())

    return


def wait_for_start():
    while True:
        ret = partner.listen()
        if ret == BOMB_START_PHRASE:
            partner.tell_player("selvä")
            return
        print("Waiting for player to ready up")
    return


def even_or_odd():
    while True:
        ret = partner.ask_player(EVEN_OR_ODD_QUESTION)
        if ret in [EVEN, ODD]:
            partner.tell_player(ret)
            return ret
    return


def num_of_batteries():
    while True:
        ret = partner.ask_player(NUM_OF_BATTERIES_QUESTION)
        if ret.isdigit():
            partner.tell_player(ret)
            return ret
    return


def indicators():
    while True:
        ret = partner.ask_player(INDICATORS_QUESTION)
        answers = ret.split(" ")
        if len(answers) == 2 and any(i in answers for i in [YES, NO]):
            partner.tell_player(ret)
            formatted = [False, False]
            formatted[0] = True if answers[0] == YES else False
            formatted[1] = True if answers[1] == YES else False
            return formatted
    return


def wait_for_module():
    while True:
        ans = partner.ask_player(MODULE_QUESTION)
        if ans == BOMB_DEFUSED_PHRASE:
            return ans
        words = ans.split(" ")
        if len(words) > 1:  # avoid index error
            if words[0] == MODULE_SELECTION_KEYWORD and " ".join(words[1:]) in colors_modules.modules:
                return ans
    return


main()
