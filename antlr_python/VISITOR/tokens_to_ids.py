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
    #print(k, v)
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

TOKEN_CLASSES= {100:'WS',101:'NL',102:'DIGIT',103:'VAR'} 
def id_2_symbolic(idx):
    match = id_2_token.get(idx)
    if match:
        return match[0]
    return TOKEN_CLASSES.get(idx,idx)

#print([get_symbolic_name(x) for x in lst])
#print("*" * 50)
id_list = [get_token_id(x) for x in lst]
#ignore WS and NL for now
id_list = [x for x in id_list if x!=100]
id_list = [x for x in id_list if x!=101]

id_set = set(id_list)
#print(id_set)
alphabet = [chr(97+x) for x in range(min(len(id_set),26))]
#print(alphabet)
id_2_letter = {x:y for x,y in zip(list(id_set),list(alphabet))}
print(id_list)
inp = [id_2_letter.get(x) for x in id_list]
print(''.join(inp))
from sequitur3 import run_sequitur
out = run_sequitur(''.join(inp))

print(out)
letter_2_symbolic = {y:id_2_symbolic(x) for x,y in id_2_letter.items()}
out = out.replace('Usage','USAGE')
out = out.replace('Rule','RULE')
print(out)
for letter,symbol in letter_2_symbolic.items():
    out = out.replace(letter,symbol)
print(out)
