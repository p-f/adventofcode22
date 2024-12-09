#!/usr/bin/env python
# -*- coding: utf-8 -*-

fs_data = None
with open('09.input', 'r') as f:
    fs_data = f.readline().strip()

head, tail = 0, len(fs_data) - 1
def value(idx):
    return int(fs_data[idx])
def amount(idx):
    if idx % 2 == 0:
        return value(idx)
    else:
        return 0
def empty_amount(idx):
    if idx % 2 == 1:
        return value(idx)
    else:
        return 0

def get_blocks():
    head, tail = 0, len(fs_data) - 1
    rem_tail = amount(tail)
    to_fill_cur = 0
    while True:
        #print(fs_data)
        #print(head * ' ', 'h', sep='')
        #print(tail * ' ', 't', sep='')
        #print(head, tail, to_fill_cur, rem_tail)
        if head >= tail or head >= len(fs_data):
            break
        if head % 2 == 0: # File
            block_id = head // 2
            head += 1
            to_fill_cur = empty_amount(head)
            yield block_id, value(head - 1)
        else: # Space
            if to_fill_cur == 0:
                head += 1
                continue
            if rem_tail == 0:
                tail -= 1
                rem_tail = amount(tail)
                continue
            to_fill = min(rem_tail, to_fill_cur)
            rem_tail -= to_fill
            to_fill_cur -= to_fill
            filled_from_id = tail // 2
            yield filled_from_id, to_fill
    # Dangling last block
    if rem_tail:
        yield tail // 2, rem_tail

hash_val, hash_pos = 0, 0
for block_id, block_count in get_blocks():
    hash_val += block_id * sum(range(hash_pos, hash_pos + block_count))
    hash_pos += block_count

print(hash_val)
