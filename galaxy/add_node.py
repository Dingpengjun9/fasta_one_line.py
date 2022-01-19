import sys
import re
file=sys.argv[1]
outf=sys.argv[2]


with open(file)as tt_tree_file:
    lines=tt_tree_file.read()
    string = ''
    n = 0
    parts = lines.split(")")
    # long=len(parts)
    for part in parts:
        n += 1
        # num=f"{ {0}:0{1}>d}".format(n,4)    怎么带变量格式化
        string += f'{part})Node{n},'
    string = string.strip(",")

with open(outf,"w")as out:
    out.write(string)