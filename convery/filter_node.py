all_seq={}
with open ("C:/Users/dingdingche/Desktop/GALGAL_R00005_all_gap.fa")as all:
    lines=all.readlines()
    for line in lines:
        if line[0]==">":
            name=line.strip()
            seq=""
        else :
            seq+=line.strip()
            all_seq[name]=seq

with open ("C:/Users/dingdingche/Desktop/psg.txt")as psg:
    pline=psg.readline().strip()
    pnode=pline.split(",")

with open("C:/Users/dingdingche/Desktop/G005_filter.fa","w")as out:
    for k,v in all_seq.items():
        if k.strip('>') not in pnode and "Node" not in k:
            out.write(f"{k}\n{v}\n")
with open("C:/Users/dingdingche/Desktop/G005_filter_name.fa","w")as out2:
    for k,v in all_seq.items():
        if k.strip('>') not in pnode and "Node" not in k:
            out2.write(f"{k.strip('>')}\n")

import json
import re
with open("C:/Users/dingdingche/Desktop/ancestor.json")as jsons:
    aa=json.load(jsons)
    tree =aa["labeled_tree"]
    tree=re.sub(r':\d+\.?\d*[e-]*\d*',"",tree)
with open("C:/Users/dingdingche/Desktop/test.tree","w")as trees :
    trees.write(tree)