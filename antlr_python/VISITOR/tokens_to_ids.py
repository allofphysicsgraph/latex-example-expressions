from file_utils import read_file
from sys import argv
from pudb import set_trace
import re

data = read_file("ExprLexer.tokens")
data = data.splitlines()
integer_ids = set()
from collections import defaultdict

token_mappings = defaultdict(list)
seen = set()
for line in data:
    idx = re.findall("=(\d+)$", line)
    if idx:
        idx = idx[0]
        idx = idx.strip()
        idx = int(idx)
        match = re.findall("(.*?)=\d+$", line)
        # print(match)
        if match:
            match = str(match[0]).replace('"', "").replace("'", "")
        token_mappings[idx].append(match)

print(token_mappings)
