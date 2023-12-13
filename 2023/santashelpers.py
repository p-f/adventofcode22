#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

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
