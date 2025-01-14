from nltk.tokenize import mwe
from pudb import set_trace
from redbaron import RedBaron
from sys import argv
import re

tokenizer = mwe.MWETokenizer(separator="")

with open("ExprLexer.py", "r") as source:
    code = RedBaron(source.read())
# print(code)
node_list = code.find_all("assignment")
for node in node_list:
    if re.findall("literalNames", str(node.name)):
        literalNames = node.value
for node in node_list:
    if re.findall("symbolicNames", str(node.name)):
        symbolicNames = node.value

with open(argv[1], "r") as f:
    test_data = f.read()
for tok in sorted(list(literalNames), key=lambda x: -len(x)):
    tok = str(tok).replace("'", "").strip()
    tok = str(tok).replace('"', "").strip()
    tokenizer.add_mwe(f"{tok}")

name_pairs = {}
for tpl in zip(literalNames[1:], symbolicNames[1:]):
    k, v = tpl
    k = str(k).strip().replace("'", "").replace('"', "")
    v = str(v).replace('"', "")
    name_pairs[k] = v

name_pairs[" "] = "WS"
name_pairs["\n"] = "NL"
print(test_data)
print([name_pairs.get(x, x) for x in tokenizer.tokenize(test_data)])
