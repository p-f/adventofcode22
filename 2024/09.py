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

def hash_blocks(blocks):
    hash_val, hash_pos = 0, 0
    for block_id, block_count in blocks:
        hash_val += block_id * sum(range(hash_pos, hash_pos + block_count))
        hash_pos += block_count
    return hash_val

print(hash_blocks(get_blocks()))

# Part 2

def chunk_fs():
    for i, c in enumerate(fs_data):
        if i % 2 == 0:
            yield (i // 2, int(c))
        else:
            yield [None, int(c)]

fs = list(chunk_fs())
max_id = fs[-1][0] or fs[-2][0]

def compress_fs(fs_queue): # Unused
    i = 0
    while i < len(fs_queue):
        chunk = fs_queue[i]
        if chunk[0] is not None: # File
            yield chunk
            i += 1
            continue
        new_chunksize = chunk[1]
        merged_chunks = 1
        for j in range(i + 1, len(fs_queue)):
            chunk2 = fs_queue[j]
            if chunk2[0] is not None:
                break
            merged_chunks += 1
            new_chunksize += chunk2[1]
        yield [chunk[0], new_chunksize]
        i += merged_chunks

def defrag(fs_queue_in):
    head = 1
    moved = [False for _ in range(max_id + 1)]
    fs_queue = fs_queue_in
    def is_free(idx):
        return fs_queue[idx][0] is None and fs_queue[idx][1] > 0
    def move(fs_idx, new_idx):
        #print("Move", fs_idx, "to", new_idx)
        chunk_to_move = fs_queue[fs_idx]
        chunk_size = chunk_to_move[1]
        # Replace chunk with empty space
        fs_queue[fs_idx] = [None, chunk_size]
        # Shrink free space
        fs_queue[new_idx][1] -= chunk_size
        # Re-insert chunk and mark as moved
        fs_queue.insert(new_idx, chunk_to_move)
        moved[int(chunk_to_move[0])] = True
    while True:
        while not is_free(head):
            head += 1
            if head >= len(fs_queue):
                return
        # Find block to move
        any_moved = False
        for idx in range(len(fs_queue) - 1, head, -1):
            chunk_id, chunk_size = fs_queue[idx]
            if chunk_id is None or chunk_size == 0: continue
            if moved[chunk_id]: continue
            chunk_moved = False
            # Find fitting space
            for new_idx in range(head, idx):
                if not is_free(new_idx): continue
                chunk_candidate = fs_queue[new_idx]
                if chunk_candidate[1] >= chunk_size:
                    chunk_moved = True
                    move(idx, new_idx)
                    break
            moved[chunk_id] = True
            if chunk_moved:
                any_moved = True
                break
        if not any_moved: return
        #print(len(fs_queue), head)

defrag(fs)
def iter_fs(f):
    for chunk, chunk_size in f:
        yield chunk or 0, chunk_size
print(hash_blocks(iter_fs(fs)))

