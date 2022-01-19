import sys
import re
file=sys.argv[1]
outf=sys.argv[2]


with open(file)as tt_tree_file:
    lines=tt_tree_file.read()
    line = re.sub(r':\d+\.?\d*[e-]*\d*', "", lines)

with open(outf,"w")as out:
    out.write(line)