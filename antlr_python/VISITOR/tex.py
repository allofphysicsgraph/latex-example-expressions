from sys import argv
def get_file_checksum(file_name):
    try:
        import hashlib
        f = open(file_name, "rb")
        data = f.read()
        f.close()
        m = hashlib.md5()
        m.update(data)
        return {file_name: m.hexdigest(), "data": data.decode("utf-8")}
    except Exception as e:
        print(e)
cs = get_file_checksum(argv[1])
data = cs["data"].strip()
print(cs)
doc = f"""\\documentclass[]{{article}}
\\begin{{document}}
$$
{data}
$$
\\end{{document}}
"""
print(doc)
cs = cs[argv[1]]
f = open(f"{cs}.tex", "a+")
f.write(doc)
f.close()
