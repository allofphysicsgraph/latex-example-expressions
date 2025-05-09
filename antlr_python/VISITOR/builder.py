from nltk.tokenize import mwe
from pudb import set_trace
from redbaron import RedBaron
from sys import argv
import re
from os import listdir

files = [x for x in listdir(".") if re.findall("tex$", x)]
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

tokens = list(literalNames)
for tok in sorted(list(literalNames), key=lambda x: -len(x)):
    tok = str(tok).replace("'", "").strip()
    tok = str(tok).replace('"', "").strip()
    tokenizer.add_mwe(f"{tok}")
tokenizer.add_mwe(r"\\frac")
tokenizer.add_mwe(r"\\infty")
name_pairs = {}
for tpl in zip(literalNames[1:], symbolicNames[1:]):
    k, v = tpl
    k = str(k).strip().replace("'", "").replace('"', "")
    v = str(v).replace('"', "")
    name_pairs[k] = v

name_pairs[" "] = "WS"
name_pairs["\n"] = "NL"
name_pairs[r"\\frac"] = "FRAC"
name_pairs[r"\\infty"] = "INF"
name_pairs["!"] = "FACT"
for ix in range(10):
    name_pairs[str(ix)] = "DIGIT"
for f_name in files:
    with open(f_name, "r") as f:
        test_data = f.read()
        test_data = test_data.replace("\\", "\\\\")
        print(test_data)
        print([name_pairs.get(x, x) for x in tokenizer.tokenize(test_data)])
