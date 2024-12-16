#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from enum import Enum
from functools import wraps

def parse_numbers(inln: str, sep = None) -> List[int]:
	return list(map(int, inln.strip().split(sep)))

def parse_numbers_after_char(infile, sep=':'):
	return parse_numbers(infile.readline().split(sep)[1])

def chunks(infile):
	chunk = []
	while l:=infile.readline():
		l = l.strip()
		if l:
			chunk.append(l)
		else:
			if len(chunk) > 0:
				yield chunk
				chunk = []
	if len(chunk) > 0:
		yield chunk

def transpose(matrix):
	columns = len(matrix[0])
	transposed = []
	for c in range(columns):
		transposed.append([l[c] for l in matrix])
	return transposed

def pairs(v):
    for i in range(len(v) - 1):
        yield v[i], v[i + 1]

def coordinates(row, col):
    return row + 1j * col

def to_row_col(coord):
    return (int(coord.real), int(coord.imag))

class Direction(Enum):
    UP = coordinates(-1, 0)
    RIGHT = coordinates(0, 1)
    DOWN = coordinates(1, 0)
    LEFT = coordinates(0, -1)

    @classmethod
    def rotate(cls, d: 'Direction') -> 'Direction':
        if d == cls.UP:
            return cls.RIGHT
        elif d == cls.RIGHT:
            return cls.DOWN
        elif d == cls.DOWN:
            return cls.LEFT
        else:
            assert d == cls.LEFT
            return cls.UP

def dimension_checker(num_rows, num_cols):
    def check_dimensions_(coord):
        r, c = to_row_col(coord)
        return r >= 0 and c >= 0 and r < num_rows and c < num_cols
    return check_dimensions_

def coord_based(fun):
    @wraps(fun)
    def _coord_codec_applied(coord):
        _r, _c = to_row_col(coord)
        return coordinates(*fun(_r, _c))
    return _coord_codec_applied
