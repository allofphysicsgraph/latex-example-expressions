from redbaron import RedBaron
from pudb import set_trace


def read_file(f_name):
    with open(f_name, "r") as source_code:
        src = RedBaron(source_code.read())
    return src


exprVisitor = read_file("ExprVisitor.py")

test_code = read_file("test.py")

test_code_names = []
for ix in range(len(test_code[16])):
    resp = test_code[16][ix]
    if resp.type == "def":
        print(resp.name)
        test_code_names.append(resp.name)

for ix in range(len(exprVisitor[3])):
    resp = exprVisitor[3][ix]
    if resp.type == "def":
        if resp.name not in test_code_names:
            test_code[16].append(resp)

with open("test2.py", "w") as source_code:
    source_code.write(test_code.dumps())


# Sort function in the class Calc by def_name using RedBaron
a = test_code[16].copy()
func_names = []
for ix in range(len(a)):
    if a[ix].type == "def":
        func_names.append(a[ix].name)

func_names = sorted(func_names)
code = func_names.copy()
for ix in range(len(a)):
    if a[ix].type == "def":
        idx = func_names.index(a[ix].name)
        code[idx] = a[ix]

counter = 0
for ix in range(len(a)):
    if a[ix].type == "def":
        if a[ix].name in func_names:
            a[ix] = code[counter]
            counter += 1

test_code[16] = a
with open("test3.py", "w") as source_code:
    source_code.write(test_code.dumps())
