#!/usr/bin/env python
# -*- coding: utf-8 -*-

from santashelpers import coordinates, coord_based, to_row_col, parse_numbers, dimension_checker, Direction
from math import inf

FIELD_SIZE = 70
OBST_COUNT = 1024

obstr = set()
additional_obstr = list()

with open('18.input', 'r') as f:
    obst_nr = 0
    while l := f.readline():
        c, r = parse_numbers(l, ",")
        if obst_nr < OBST_COUNT:
            obstr.add(coordinates(r, c))
        else:
            additional_obstr.append(coordinates(r, c))
        obst_nr += 1

START_POS = coordinates(0, 0)
END_POS = coordinates(FIELD_SIZE, FIELD_SIZE)

def create_field(value):
    return [[value for _ in range(FIELD_SIZE + 1)] for _ in range(FIELD_SIZE + 1)]

in_field = dimension_checker(FIELD_SIZE + 1, FIELD_SIZE + 1)

distances = create_field(inf)

def neighbors(coord):
    for d in Direction:
        new_coord = d.value + coord
        if in_field(new_coord) and not new_coord in obstr:
            yield new_coord

#print("Obstructed", *map(to_row_col,obstr))

def dijkstra(exit_early = False, obstr=obstr, distances=distances):
    if exit_early: print("Running with", len(obstr))
    v_queue = list()
    for r in range(FIELD_SIZE + 1):
        for c in range(FIELD_SIZE + 1):
            coord = coordinates(r, c)
            if coord not in obstr:
                v_queue.append(coord)
    #print(*map(to_row_col, v_queue))
    distances[0][0] = 0
    def get_dist(co):
        r, c = to_row_col(co)
        return distances[r][c]
    def upd_dist(co, new_d):
        r, c = to_row_col(co)
        distances[r][c] = new_d
    while len(v_queue) > 0:
        u_coord = v_queue[0]
        u_dist = get_dist(u_coord)
        for u_candidate in v_queue:
            if (new_dist := get_dist(u_candidate)) < u_dist:
                u_coord = u_candidate
                u_dist = new_dist
        v_queue.remove(u_coord)
        if exit_early and u_coord == END_POS:
            return
        #print("u", to_row_col(u_coord))

        for u_neig in neighbors(u_coord):
            if u_neig not in v_queue: continue
            #print("neig", to_row_col(u_neig))
            if u_dist + 1 < get_dist(u_neig):
                upd_dist(u_neig, u_dist + 1)
                #print("update", to_row_col(u_neig), u_dist + 1)

dijkstra()

print(distances[FIELD_SIZE][FIELD_SIZE])

# Part 2
print("Remaining", len(additional_obstr))
obstr_start = set(obstr)

max_to_add = len(additional_obstr)

def does_obstr(additions):
    print("Trying with", additions)
    obstr2 = set(obstr_start)
    for i in range(additions):
        obstr2.add(additional_obstr[i])
    print("Last added", to_row_col(additional_obstr[additions - 1]))
    distances2 = create_field(inf)
    dijkstra(True, obstr2, distances2)
    #print(distances2)
    return distances2[FIELD_SIZE][FIELD_SIZE] == inf

low, high = 0, max_to_add
while low <= high:
    try_pos = (low + high) // 2
    if does_obstr(try_pos): # Search in lower
        print("Does obstruct")
        high = try_pos - 1
    else:
        print("Does not obstruct")
        low = try_pos + 1
