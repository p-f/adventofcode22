# -*- coding: utf-8 -*-

field = []
line_start = 0
col_start = 0

with open('10.input', 'r') as f:
    lineno = 0
    while l:=f.readline():
        field.append(l.strip())
        s_pos = l.find('S')
        if s_pos >= 0:
            line_start = lineno
            col_start = s_pos
        lineno += 1

print('Start at', line_start, col_start)

N, E, S, W = (-1, 0,), (0, 1,), (1, 0,), (0, -1,)

TILES = {
    '|': [N, S],
    '-': [E, W],
    'L': [N, E],
    'J': [N, W],
    '7': [S, W],
    'F': [S, E],
    '.': [],
    'S': [N, E, S, W]
}

NO_LINES, NO_COLS = len(field), len(field[0])

def next_pos(lineno, colno):
    for step in TILES[field[lineno][colno]]:
        l_new, c_new = lineno + step[0], colno + step[1]
        if l_new in range(NO_LINES) and c_new in range(NO_COLS):
            yield l_new, c_new

distancemap = [[-1 for _ in range(NO_COLS)] for _ in range(NO_LINES)]

def bfs(line_start, col_start, next_pos_fn):
    queue = []
    distancemap[line_start][col_start] = 0
    queue.append((line_start, col_start,))
    while queue:
       l_pos, c_pos = queue.pop(0)
       for l_next, c_next in next_pos_fn(l_pos, c_pos):
           if distancemap[l_next][c_next] < 0:
               distancemap[l_next][c_next] = 1 + distancemap[l_pos][c_pos]
               queue.append((l_next, c_next,))

bfs(line_start, col_start, next_pos)

for l in distancemap:
    print(*l, sep='\t')

print('Farthest item: ', max(map(max, distancemap)))

from functools import reduce
all_nums = list(reduce(list.__add__, distancemap))
visited = [i for i in all_nums if i >= 0]
print(len(visited) / 2)
