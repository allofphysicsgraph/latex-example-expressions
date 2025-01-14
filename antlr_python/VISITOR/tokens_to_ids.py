from collections import defaultdict
from file_utils import read_file
from pudb import set_trace
from sys import argv
import re

data = read_file("ExprLexer.tokens")
data = data.splitlines()
token_mappings = defaultdict(list)
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
