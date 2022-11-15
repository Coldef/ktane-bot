'''
import collections

from constants import *
import partner

# strange result:
# 34, 41, 32, 56


maze_1 =    [['*',' ','*',' ','*','X','*',' ','*',' ','*'],
             [' ','X','X','X',' ','X',' ','X','X','X','X'],
             ['#','X','*',' ','*','X','*',' ','*',' ','*'],
             [' ','X',' ','X','X','X','X','X','X','X',' '],
             ['*','X','*',' ','*','X','*',' ','*',' ','#'],
             [' ','X','X','X',' ','X',' ','X','X','X',' '],
             ['*','X','*',' ','*',' ','*','X','*',' ','*'],
             [' ','X','X','X','X','X','X','X','X','X',' '],
             ['*',' ','*',' ','*','X','*',' ','*','X','*'],
             [' ','X','X','X',' ','X',' ','X','X','X',' '],
             ['*',' ','*','X','*',' ','*','X','*',' ','*']]

maze_2 =    [['*',' ','*',' ','*','X','*',' ','*',' ','*'],
             ['X','X',' ','X','X','X',' ','X',' ','X','X'],
             ['*',' ','*','X','*',' ','*','X','#',' ','*'],
             [' ','X','X','X',' ','X','X','X','X','X',' '],
             ['*','X','*',' ','*','X','*',' ','*',' ','*'],
             [' ','X',' ','X','X','X',' ','X','X','X',' '],
             ['*',' ','#','X','*',' ','*','X','*','X','*'],
             [' ','X','X','X',' ','X','X','X',' ','X',' '],
             ['*','X','*','X','*','X','*',' ','*','X','*'],
             [' ','X',' ','X',' ','X',' ','X','X','X',' '],
             ['*','X','*',' ','*','X','*',' ','*',' ','*']]

maze_3 =    [['*',' ','*',' ','*','X','*','X','*',' ','*'],
             [' ','X','X','X',' ','X',' ','X',' ','X',' '],
             ['*','X','*','X','*','X','*',' ','*','X','*'],
             ['X','X',' ','X',' ','X','X','X','X','X',' '],
             ['*',' ','*','X','*','X','*',' ','*','X','*'],
             [' ','X',' ','X',' ','X',' ','X',' ','X',' '],
             ['*','X','*','X','*','X','#','X','*','X','#'],
             [' ','X',' ','X',' ','X',' ','X',' ','X',' '],
             ['*','X','*',' ','*','X','*','X','*','X','*'],
             [' ','X','X','X','X','X',' ','X',' ','X',' '],
             ['*',' ','*',' ','*',' ','*','X','*',' ','*']]

maze_4 =    [['#',' ','*','X','*',' ','*',' ','*',' ','*'],
             [' ','X',' ','X','X','X','X','X','X','X',' '],
             ['*','X','*','X','*',' ','*',' ','*',' ','*'],
             [' ','X',' ','X',' ','X','X','X','X','X',' '],
             ['*','X','*',' ','*','X','*',' ','*','X','*'],
             [' ','X','X','X','X','X',' ','X','X','X',' '],
             ['#','X','*',' ','*',' ','*',' ','*',' ','*'],
             [' ','X','X','X','X','X','X','X','X','X',' '],
             ['*',' ','*',' ','*',' ','*',' ','*','X','*'],
             [' ','X','X','X','X','X','X','X',' ','X',' '],
             ['*',' ','*',' ','*','X','*',' ','*','X','*']]

maze_5 =    [['*',' ','*',' ','*',' ','*',' ','*',' ','*'],
             ['X','X','X','X','X','X','X','X',' ','X',' '],
             ['*',' ','*',' ','*',' ','*',' ','*','X','*'],
             [' ','X','X','X','X','X',' ','X','X','X','X'],
             ['*',' ','*','X','*',' ','*','X','#',' ','*'],
             [' ','X',' ','X','X','X','X','X',' ','X',' '],
             ['*','X','*',' ','*',' ','*','X','*','X','*'],
             [' ','X','X','X','X','X',' ','X','X','X',' '],
             ['*','X','*',' ','*',' ','*',' ','*','X','*'],
             [' ','X',' ','X','X','X','X','X','X','X',' '],
             ['*','X','*',' ','*',' ','#',' ','*',' ','*']]

maze_6 =    [['*','X','*',' ','*','X','*',' ','#',' ','*'],
             [' ','X',' ','X',' ','X','X','X',' ','X',' '],
             ['*','X','*','X','*','X','*',' ','*','X','*'],
             [' ','X',' ','X',' ','X',' ','X','X','X',' '],
             ['*',' ','*','X','*','X','*','X','*',' ','*'],
             [' ','X','X','X','X','X',' ','X',' ','X','X'],
             ['*',' ','*','X','*',' ','*','X','*','X','*'],
             ['X','X',' ','X',' ','X',' ','X',' ','X',' '],
             ['*',' ','*','X','#','X','*','X','*',' ','*'],
             [' ','X','X','X','X','X',' ','X','X','X',' '],
             ['*',' ','*',' ','*',' ','*','X','*',' ','*']]

maze_7 =    [['*',' ','#',' ','*',' ','*','X','*',' ','*'],
             [' ','X','X','X','X','X',' ','X',' ','X',' '],
             ['*','X','*',' ','*','X','*',' ','*','X','*'],
             [' ','X',' ','X','X','X','X','X','X','X',' '],
             ['*',' ','*','X','*',' ','*','X','*',' ','*'],
             ['X','X','X','X',' ','X','X','X',' ','X','X'],
             ['*',' ','*','X','*',' ','*',' ','*','X','*'],
             [' ','X',' ','X',' ','X','X','X','X','X',' '],
             ['*','X','*','X','*',' ','*',' ','*','X','*'],
             [' ','X','X','X','X','X','X','X',' ','X',' '],
             ['*',' ','#',' ','*',' ','*',' ','*',' ','*']]

maze_8 =    [['*','X','*',' ','*',' ','#','X','*',' ','*'],
             [' ','X',' ','X','X','X',' ','X',' ','X',' '],
             ['*',' ','*',' ','*','X','*',' ','*','X','*'],
             [' ','X','X','X','X','X','X','X','X','X',' '],
             ['*','X','*',' ','*',' ','*',' ','*','X','*'],
             [' ','X',' ','X','X','X','X','X',' ','X',' '],
             ['*','X','*',' ','#','X','*',' ','*',' ','*'],
             [' ','X','X','X',' ','X','X','X','X','X','X'],
             ['*','X','*','X','*',' ','*',' ','*',' ','*'],
             [' ','X',' ','X','X','X','X','X','X','X','X'],
             ['*',' ','*',' ','*',' ','*',' ','*',' ','*']]

maze_9 =   [['*','X','*',' ','*',' ','*',' ','*',' ','*'],
            [' ','X',' ','X','X','X','X','X',' ','X',' '],
            ['*','X','*','X','#',' ','*','X','*','X','*'],
            [' ','X',' ','X',' ','X','X','X',' ','X',' '],
            ['*',' ','*',' ','*','X','*',' ','*','X','*'],
            [' ','X','X','X','X','X',' ','X','X','X',' '],
            ['*','X','*','X','*',' ','*','X','*',' ','*'],
            [' ','X',' ','X',' ','X','X','X','X','X',' '],
            ['#','X','*','X','*','X','*',' ','*','X','*'],
            [' ','X',' ','X',' ','X',' ','X',' ','X','X'],
            ['*',' ','*','X','*',' ','*','X','*',' ','*']]

mazes = [maze_1, maze_2, maze_3, maze_4, maze_5, maze_6, maze_7, maze_8, maze_9]


def solve_maze():
    m = False
    while not m:
        m = find_maze()
        if m == CANCEL_PHRASE:
            return

    ans = False
    while not ans:
        ans = start_end()
        if ans == CANCEL_PHRASE:
            return

    s_x = ans[0][0]
    s_y = ans[0][1]
    e_x = ans[1][0]
    e_y = ans[1][1]

    pathing(m, s_x, s_y, e_x, e_y)

    return ""


def pathing(maze, start_x, start_y, end_x, end_y, current_path=None, prev_dir=None):
    if current_path is None:
        path = current_path
    if start_x == end_x and start_y == end_y:
        stringified = " ".join(current_path)
        output(stringified)
        return ""  # current_path  # found path

    if prev_dir == "down":
        move_down(maze, start_x, start_y, end_x, end_y, path)
        move_left(maze, start_x, start_y, end_x, end_y, path)
        move_right(maze, start_x, start_y, end_x, end_y, path)
    elif prev_dir == "up":
        move_up(maze, start_x, start_y, end_x, end_y, path)
        move_left(maze, start_x, start_y, end_x, end_y, path)
        move_right(maze, start_x, start_y, end_x, end_y, path)
    elif prev_dir == "left":
        move_up(maze, start_x, start_y, end_x, end_y, path)
        move_left(maze, start_x, start_y, end_x, end_y, path)
        move_down(maze, start_x, start_y, end_x, end_y, path)
    elif prev_dir == "right":
        move_up(maze, start_x, start_y, end_x, end_y, path)
        move_down(maze, start_x, start_y, end_x, end_y, path)
        move_right(maze, start_x, start_y, end_x, end_y, path)
    elif prev_dir is None:
        move_up(maze, start_x, start_y, end_x, end_y, path)
        move_down(maze, start_x, start_y, end_x, end_y, path)
        move_left(maze, start_x, start_y, end_x, end_y, path)
        move_right(maze, start_x, start_y, end_x, end_y, path)

    return


def move_down(maze, start_x, start_y, end_x, end_y, current_path):
    new_path = current_path
    if start_y + 1 >= len(maze) or maze[start_y + 1][start_x] == "X":  # out of bounds or wall
        return
    else:  # if moving down is valid
        prev_dir = "down"
        if maze[start_y + 1][start_x] in "*#":
            new_path.append("down")
        pathing(maze, start_x, start_y + 1, end_x, end_y, new_path, prev_dir)
    return


def move_up(maze, start_x, start_y, end_x, end_y, current_path):
    new_path = current_path
    if start_y - 1 < 0 or maze[start_y - 1][start_x] == "X":
        return
    else:
        prev_dir = "up"
        if maze[start_y - 1][start_x] in "*#":
            new_path.append("up")
        pathing(maze, start_x, start_y - 1, end_x, end_y, new_path, prev_dir)
    return


def move_left(maze, start_x, start_y, end_x, end_y, current_path):
    new_path = current_path
    if start_x - 1 < 0 or maze[start_y][start_x - 1] == "X":
        return
    else:
        prev_dir = "left"
        if maze[start_y][start_x - 1] in "*#":
            new_path.append("left")
        pathing(maze, start_x - 1, start_y, end_x, end_y, new_path, prev_dir)
    return


def move_right(maze, start_x, start_y, end_x, end_y, current_path):
    new_path = current_path
    if start_x + 1 >= len(maze[0]) or maze[start_y][start_x + 1] == "X":
        return
    else:
        prev_dir = "right"
        if maze[start_y][start_x + 1] in "*#":
            new_path.append("right")
        pathing(maze, start_x + 1, start_y, end_x, end_y, new_path, prev_dir)
    return


def find_maze():
    c1 = ask_and_check_coords(MODULE_MAZE_C1)
    if c1 == CANCEL_PHRASE:
        return CANCEL_PHRASE
    if not c1:
        return False

    c2 = ask_and_check_coords(MODULE_MAZE_C2)
    if c2 == CANCEL_PHRASE:
        return CANCEL_PHRASE
    if not c2:
        return False

    for maze in mazes:
        if maze[c1[1]][c1[0]] == "#" and maze[c2[1]][c2[0]] == "#":
            return maze
    partner.tell_player(ERROR_PHRASE)
    return False


def start_end():
    start = ask_and_check_coords(MODULE_MAZE_START)
    if start == CANCEL_PHRASE:
        return CANCEL_PHRASE
    if not start:
        return False

    end = ask_and_check_coords(MODULE_MAZE_END)
    if end == CANCEL_PHRASE:
        return CANCEL_PHRASE
    if not end:
        return False

    return start, end


def coords(raw):  # raw in form xy. ex. "41". returns tuple (x, y) compatible with maze variables
    x = (int(raw[0]) - 1) * 2
    y = (int(raw[1]) - 1) * 2
    ret = (x, y)
    return ret


def ask_and_check_coords(q):
    raw = partner.ask_player(q).strip().replace(" ", "")
    if raw == CANCEL_PHRASE:
        return CANCEL_PHRASE
    if not raw.isdigit():
        partner.tell_player(ERROR_PHRASE)
        return False
    ret = coords(raw)
    if ret[0] < 0 or ret[0] > 10 or ret[1] < 0 or ret[1] > 10:
        partner.tell_player(ERROR_PHRASE)
        return False
    return ret


def output(s):
    translated = s.replace("up", MODULE_MAZE_UP) \
        .replace("down", MODULE_MAZE_DOWN) \
        .replace("left", MODULE_MAZE_LEFT) \
        .replace("right", MODULE_MAZE_RIGHT)
    partner.tell_player(translated)
    return
'''
