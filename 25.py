#!/usr/bin/env python
# -*- coding: utf-8 -*-

snafu_codec = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
snafu_codec_rev = {v: k for k,v in snafu_codec.items()}

def decode_snafu(data):
	num = 0
	for i in range(len(data)):
		c = data[-1 - i]
		decoded = snafu_codec[c]
		num += decoded * (5**i)
	return num

def encode_snafu(num):
	max_power = 0
	while 5**max_power < num:
		max_power += 1
	base5 = [0 for _ in range(1 + max_power)]
	power = max_power
	while power >= 0:
		factor = num // (5**power)
		base5[power] = factor
		num = num % (5**power)
		power -= 1
	for power, factor in enumerate(base5):
		if factor > 2:
			base5[power + 1] += 1
			base5[power] = -5 + factor
	return ''.join(snafu_codec_rev[n] for n in base5[::-1]).lstrip('0')


with open('25.input', 'r') as f:
	sum_numbers = 0
	while l := f.readline():
		l = l.strip()
		sum_numbers += decode_snafu(l)
	print('Result sum:', sum_numbers, 'Snafu=', encode_snafu(sum_numbers))
