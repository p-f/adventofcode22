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

def score1_withjokers(card, dbg):
	counts = Counter(list(card))
	frequencies = [t[1] for t in counts.items() if t[0] != 'J']  # Without joker
	num_jok = counts['J']
	def d(m):
		if dbg:
			print(m, counts, frequencies)
	if num_jok >= 4 or (5 - num_jok) in frequencies: # Five of a kind
		return 7
	elif (4 - num_jok) in frequencies: # Four of a kind
		d(f'4 of a kind with {num_jok} jokers')
		return 6
	# Must have <3 jokers, otherwise can make four/five of a kind
	# 2
	elif num_jok == 2:
		# 3 equal cards -> full house
		if 3 in frequencies:
			return 5
		# 2 equal cards -> could make four of a kind
		# all other different -> make three of a kind
		else:
			return 4
	# 1 Joker
	elif num_jok == 1:
		# 3 equals -> would have four of a kind
		# 2x2 equals -> can make full house
		# 1x2 equals -> three of a kind
		# all different -> one pair
		if 3 in frequencies:
			return 6
		elif sorted(frequencies)[::-1][:2] == [2,2]:
			return 5
		elif 2 in frequencies:
			return 4
		else:
			return 2
	# No Jokers
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

def hand_score_total(hand, with_joker=False, dbg=False):
	if with_joker:
		return (score1_withjokers(hand, dbg),) + score2(hand)
	return (score1(hand),) + score2(hand)

cards_with_bids.sort(key=lambda cb:hand_score_total(cb[0]))

def sum_win(cards):
	sw = 0
	for rank, card_bid in enumerate(cards):
		card, bid = card_bid
		win_card = (1+rank) * bid
		print(card, win_card)
		sw += win_card
	return sw

sum_win1 = sum_win(cards_with_bids)

print('Total wins', sum_win1)

## Part 2
for num, c in enumerate('AKQT98765432J'[::-1]):
	card_scores[c] = num + 1

cards_with_bids.sort(key=lambda cb:hand_score_total(cb[0], True))

#for hand, bid in cards_with_bids:
#	print("Hand", hand, "has", hand_score_total(hand, True, True))

print('Total wins with joker', sum_win(cards_with_bids))
