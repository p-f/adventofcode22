#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  02.py


rock = {'A', 'X'}
paper = {'B', 'Y'}
scissors = {'C', 'Z'}

def score(left, right):
	score_point = 0
	if right in rock:
		score_point = 1
	elif right in paper:
		score_point = 2
	else:
		score_point = 3
	if (left in rock and right in paper) or (left in paper and right in scissors) or (left in scissors and right in rock):
		score_point += 6
	elif (left in rock and right in rock) or (left in paper and right in paper) or (left in scissors and right in scissors):
		score_point += 3
	return score_point


def dec(it):
	if it in rock:
		return 0
	elif it in paper:
		return 1
	else:
		return 2

scores_gamerule = [0, 3, 6]

game_map = dict()
# lose, tie, win
game_map[0] = [2, 0, 1]
game_map[1] = [0, 1, 2]
game_map[2] = [1, 2, 0]

def score2(left, right):
	idx = dec(right)
	print('Outcome: ', idx)
	score_round = scores_gamerule[idx] #score for lose/tie/win
	print('Score for outcome', score_round)
	gm = game_map[dec(left)] # rock, paper, scissors
	print('Game map', gm)
	pick = gm[idx]
	print('Pick score', pick)
	return score_round + pick + 1

def get_score_from_line(line):
	parts = line.strip().split()
	if len(parts) != 2:
		raise ValueError('Unexpected size ' + parts)
	score = score2(parts[0], parts[1])
	print(score)
	return score

def main(args):
	with open('2.input', 'r') as f:
		score_total = 0
		while l := f.readline():
			score_total += get_score_from_line(l)
	print(score_total)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
