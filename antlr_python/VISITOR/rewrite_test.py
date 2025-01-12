from redbaron import RedBaron
from pudb import set_trace
from tqdm import tqdm


def read_file(f_name):
    with open(f_name, "r") as source_code:
        src = RedBaron(source_code.read())
    return src


exprVisitor = read_file("ExprParserVisitor.py")
test_code = read_file("test.py")


# get the index of class def
calc_class_index = 0
for ix in range(len(test_code)):
    if test_code[ix].name == "Calc":
        calc_class_index = ix

# store names of methods in class
test_code_names = []
for ix in range(len(test_code[calc_class_index])):
    resp = test_code[calc_class_index][ix]
    if resp.type == "def":
        print(resp.name)
        test_code_names.append(resp.name)

# get expr index
expr_index = 0
for ix in range(len(exprVisitor)):
    if exprVisitor[ix].name == "ExprParserVisitor":
        expr_index = ix


exprVisitor_method_names = []
for ix in range(len(exprVisitor[expr_index])):
    resp = exprVisitor[expr_index][ix]
    if resp.type == "def":
        exprVisitor_method_names.append(resp.name)
        if resp.name not in test_code_names:
            test_code[calc_class_index].append(resp)

# with open("test2.py", "w") as source_code:
#    source_code.write(test_code.dumps())


# Sort function in the class Calc by def_name using RedBaron
a = test_code[calc_class_index].copy()
func_names = []
for ix in tqdm(range(len(a))):
    if a[ix].type == "def":
        func_names.append(a[ix].name)

func_names = sorted(func_names)
code = func_names.copy()
for ix in tqdm(range(len(a))):
    if a[ix].type == "def":
        idx = func_names.index(a[ix].name)
        code[idx] = a[ix]

counter = 0
for ix in tqdm(range(len(a))):
    if a[ix].type == "def":
        if a[ix].name in func_names:
            a[ix] = code[counter]
            counter += 1

test_code[calc_class_index] = a
with open("test3.py", "w") as source_code:
    source_code.write(test_code.dumps())


for x in func_names:
    if x not in exprVisitor_method_names:
        print(f"{x} not in exprVisitor_method_names")
