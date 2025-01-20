import difflib

l = range(2, 10)
l1 = range(3, 12)
s = difflib.SequenceMatcher(None, list(l), list(l1))
for i, block in enumerate(s.get_matching_blocks()):
    if block.size > 0:
        print(l[block.a : block.a + block.size], l1[block.b : block.b + block.size])
