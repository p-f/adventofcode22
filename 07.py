#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
	fs = dict()
	root = '/'
	up = '..'
	dir_n = 'dir'
	pwd = [root]
	with open('7.input', 'r') as f:
		def add(size, name):
			path = tuple(pwd)
			print(f'Adding path {path}')
			if path not in fs:
				fs[path] = list()
			fs[path].append((name, int(size) if size != dir_n else size))
		while l := f.readline():
			parts = l.split()
			if parts[0] == '$':
				if parts[1] == 'cd':
					new_path = parts[2]
					if new_path == root:
						pwd = [root]
					elif new_path == up:
						pwd.pop()
					else:
						pwd.append(new_path)
				else:
					continue
			else:
				add(parts[0], parts[1])
		print(fs)
		for i in fs.keys():
			print("Dir", i)
	all_sizes = dict()
	def total_size(path):
		print(f'Finding total size of {path}')
		contents = fs[path]
		size = 0
		for elem in contents:
			if isinstance(elem[1], int):
				size += elem[1]
			else:
				size += total_size(path + (elem[0],))
		all_sizes[path] = size
		print(f'Total size {path}: {size}')
		return size
	total_size_all = total_size((root,))
	sum_all_bigger = 0
	req = 30000000 - (70000000 - total_size_all)
	print('Required: ', req)
	big_enough_for_deletion = list()
	for k, v in all_sizes.items():
		if k != (root,) and v < 100000:
			sum_all_bigger += v
		if v > req:
			big_enough_for_deletion.append((k,v,))
	print('Part 1 sum:', sum_all_bigger)
	print('Part 2:', min(big_enough_for_deletion, key=(lambda x:x[1])))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
