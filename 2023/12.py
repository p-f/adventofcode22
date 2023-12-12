# -*- coding: utf-8 -*-

from itertools import product
from santashelpers import parse_numbers

data = []

with open('12.input', 'r') as f:
    while l:=f.readline():
        row, groups = l.split()
        data.append((row.strip('.'), parse_numbers(groups, sep=','),))

def get_groups(row_data):
    group_size = 0
    groups = []
    for d in row_data:
        if d == '#': # Grow group
            group_size += 1
        elif group_size: # Cut off group
            groups.append(group_size)
            group_size = 0
    if group_size:
        groups.append(group_size)
    #print('Groups', groups)
    return groups

def assignment_possible(row_data, spaces, assignment, groups):
    assert len(assignment) == len(spaces)
    # Assign
    for idx in range(len(spaces)):
        row_data[spaces[idx]] = assignment[idx]
    # Probe
    valid = get_groups(row_data) == groups
    #print('Assignment', ''.join(row_data), valid)
    return valid

total_nr_comb = 0
for row, groups in data:
    spaces = [i for i in range(len(row)) if row[i] == '?']
    nr_comb = 0
    row_data = list(row)
    #print('Row', row, 'Groups', groups, 'Spaces', spaces)
    for assignment in product('.#', repeat=len(spaces)):
        if assignment_possible(row_data, spaces, assignment, groups):
            nr_comb += 1
    print(row, nr_comb)
    total_nr_comb += nr_comb

print('Total number of combinations', total_nr_comb)
