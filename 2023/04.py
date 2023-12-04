# -*- coding: utf-8 -*-

from typing import List

def splitnum(instr: str) -> List[int]:
	return list(map(int, instr.split()))

def wins(card) -> int:
	winning, having = card
	return len(set(winning).intersection(set(having)))

def score(card) -> int:
	num_wins = wins(card)
	return 2**(num_wins - 1) if num_wins else 0

with open('04.input', 'r') as f:
	total_winscore = 0
	card_scores = []
	while l:=f.readline():
		card = tuple(map(splitnum, map(str.strip, l.split(':')[1].split('|'))))
		total_winscore += score(card)
		card_scores.append(wins(card))
	num_cards = [1 for _ in range(len(card_scores))]
	print('Total winscore:', total_winscore)
	for card_nr, card_score in enumerate(card_scores):
		card_times = num_cards[card_nr]
		print(f'Card #{1 + card_nr} (x{card_times}) (win score {card_score})')
		for next_card_nr in range(card_nr + 1, min(len(card_scores), card_nr + 1 + card_score)):
			print(f'Adding {card_times} to {1 + next_card_nr}')
			num_cards[next_card_nr] += card_times
	print('Total number of cards:', sum(num_cards))
