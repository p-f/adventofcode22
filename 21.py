#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

refnames = re.compile('([a-z]+)')
with open('21.input', 'r') as f, open('_21_data.py', 'w') as tmp:
	while l:=f.readline():
		print('def ' + refnames.sub(r'\1()', l.strip()).replace(':', ': return'), file=tmp)


print('Root', int(__import__('_21_data').root()))
