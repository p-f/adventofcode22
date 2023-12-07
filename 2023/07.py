# -*- coding: utf-8 -*-

from collections import Counter

cards_with_bids = []
with open('07.input', 'r') as f:
	while l:=f.readline():
		hand, bid = l.split()
		cards_with_bids.append((hand, int(bid),))

def score1(card):
	counts = Counter(list(card))
	frequencies = [t[1] for t in counts.items()]
	if 5 in frequencies: # Five of a kind
		return 7
	elif 4 in frequencies: # Four of a kind
		return 6
	elif 3 in frequencies and 2 in frequencies: # Full house
		return 5
	elif 3 in frequencies: # Three of a kind
		return 4
	elif sorted(frequencies) == [1, 2, 2]: # Two pair
		return 3
	elif 2 in frequencies: # One pair
		return 2
	else:
		return 1

card_scores = dict()
for num, c in enumerate('AKQJT98765432'[::-1]):
	card_scores[c] = num + 1

def score2(hand):
	return tuple(card_scores[c] for c in hand)

def hand_score_total(hand):
	return (score1(hand),) + score2(hand)

cards_with_bids.sort(key=lambda cb:hand_score_total(cb[0]))

sum_win = 0
for rank, card_bid in enumerate(cards_with_bids):
	card, bid = card_bid
	win_card = (1+rank) * bid
	print(card, win_card)
	sum_win += win_card
print('Total wins', sum_win)
