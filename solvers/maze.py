import collections
from constants import *
import partner

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

Point = collections.namedtuple("Point", "x y")
Direction = collections.namedtuple("Direction", "coords dir")


def neighbors(maze, coor):
    for d in adjacent(coor):
        if 0 <= d.coords.x < len(maze[0]) and 0 <= d.coords.y < len(maze):
            if maze[d.coords.y][d.coords.x] in " *#":
                yield d


def adjacent(coor):
    yield Direction(Point(coor.x - 1, coor.y), "left")
    yield Direction(Point(coor.x, coor.y - 1), "up")
    yield Direction(Point(coor.x, coor.y + 1), "down")
    yield Direction(Point(coor.x + 1, coor.y), "right")


def node_coords_on_path(path):
    ret = []
    for e in path:
        ret.append(e.coords)
    return ret


def solve(maze, d, goal, final_path=None):
    pos = d.coords
    if final_path is None:
        final_path = [d]
    next_nodes = neighbors(maze, pos)
    if pos == goal:
        return final_path
    elif not next_nodes:
        return []
    else:
        for node in next_nodes:
            if node.coords not in node_coords_on_path(final_path):
                final_path.append(node)
                if solve(maze, node, goal, final_path):
                    return final_path
                final_path.pop()
    return []


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
    start_point = ans[0]
    goal_point = ans[1]
    a = solve(m, Direction(start_point, None), goal_point)
    p = [e.dir for e in a]
    formatted = []
    for i in range(1, len(p), 2):
        formatted.append(p[i])

    translated = " ".join(formatted)\
        .replace("up", MODULE_MAZE_UP) \
        .replace("down", MODULE_MAZE_DOWN) \
        .replace("left", MODULE_MAZE_LEFT) \
        .replace("right", MODULE_MAZE_RIGHT)

    return translated


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
    if len(raw) != 2:
        return False
    x = (int(raw[0]) - 1) * 2
    y = (int(raw[1]) - 1) * 2
    ret = Point(x, y)
    return ret


def ask_and_check_coords(q):
    raw = partner.ask_player(q).strip().replace(" ", "")
    if raw == CANCEL_PHRASE:
        return CANCEL_PHRASE
    if not raw.isdigit():
        partner.tell_player(ERROR_PHRASE)
        return False
    ret = coords(raw)
    if not ret:
        return False
    if ret.x < 0 or ret.x > 10 or ret.y < 0 or ret.y > 10:
        partner.tell_player(ERROR_PHRASE)
        return False
    return ret
