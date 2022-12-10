#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
	treemap = []
	with open('8.input', 'r') as f:
		while l:=f.readline():
			treemap.append(list(map(int, l.strip())))
	fieldsize = len(treemap)
	seemap_ind = [[(col == 0 or col == fieldsize - 1 or row == 0 or row == fieldsize -1) for col in range(fieldsize)]
		for row in range(fieldsize)]
	def isinmiddle(array, pos):
		center = array[pos]
		slice_l, slice_r = array[:pos], array[pos+1:]
		chk_left, chk_right = center > max(slice_l, default=0), center > max(slice_r, default=0)
		return chk_left or chk_right
	def seescore(array, pos):
		center = array[pos]
		slice_l, slice_r = array[:pos], array[pos+1:]
		right,left = 0,0
		for i in slice_r:
			if i < center:
				right += 1
			elif i >= center:
				right += 1
				break
		for i in slice_l[::-1]:
			if i < center:
				left +=1
			elif i >= center:
				left +=1
				break
		return left*right
	max_score = 0
	for row in range(1, fieldsize):
		for col in range(1, fieldsize):
			rowdata = treemap[row]
			coldata = [treemap[r][col] for r in range(fieldsize)]
			if isinmiddle(rowdata, col) or isinmiddle(coldata, row):
				seemap_ind[row][col]=True
			score = seescore(rowdata, col) * seescore(coldata, row)
			if score > max_score:
				max_score = score
	for line in seemap_ind:
		print(''.join(map(lambda x:'X' if x else ' ', line)))
	print("Sum:", sum(map(sum, seemap_ind)))
	print("Max score:", max_score)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
