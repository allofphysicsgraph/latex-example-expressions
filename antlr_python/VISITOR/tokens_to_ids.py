from collections import defaultdict
from file_utils import read_file
from nltk.tokenize import mwe
from os import listdir
from pudb import set_trace
from redbaron import RedBaron
from sys import argv
import re

files = [x for x in listdir(".") if re.findall("tex$", x)]
tokenizer = mwe.MWETokenizer(separator="")
data = read_file("ExprLexer.tokens")
data = data.splitlines()
id_2_token = defaultdict(list)
token_2_id = defaultdict(list)
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
        id_2_token[idx].append(match)
for k, v in id_2_token.items():
    print(k, v)
    if len(v) == 2:
        token_2_id[v[1]].append(k)
        token_2_id[v[1]].append(v[0])


# print(id_2_token)
# sort tokens by length
for tok in sorted(list(token_2_id.keys()), key=lambda x: -len(x)):
    token = tok.replace("\\\\", "\\")
    tokenizer.add_mwe(r"{}".format(token))

tex = read_file(argv[1])
lst = tokenizer.tokenize(tex)


def get_symbolic_name(tok):
    resp = token_2_id.get(r"{}".format(re.escape(tok)), tok)
    if isinstance(resp, list):
        return resp[-1]
    return resp


def get_token_id(tok):
    resp = token_2_id.get(r"{}".format(re.escape(tok)), tok)
    if isinstance(resp, list):
        return resp[0]
    if len(tok) == 1:
        resp = token_2_id.get(tok)
        if resp:
            resp = resp[0]
            return resp
    if tok == " ":
        return 100
    if tok == "\n":
        return 101
    if re.findall("^\d$", tok):
        return 102
    return -1


print([get_symbolic_name(x) for x in lst])
print("*" * 50)
print([get_token_id(x) for x in lst])
set_trace()
