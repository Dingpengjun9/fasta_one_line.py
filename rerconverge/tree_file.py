import re
bill={}
bill_file="E:/beak/1dim/Measurement_data/ratio_log_bill_depth.txt"
with open(bill_file)as bill_f:
    bill_lines=bill_f.readlines()
    for bill_line in bill_lines:
        spe,long=bill_line.split("\t")[0],bill_line.split("\t")[1].strip("\n")
        bill[spe]=long

trait_file="C:/Users/dingdingche/Desktop/GALGAL_R00076.json.363node.rmOut.list"
rate={}
with open(trait_file)as trait_f:
    t_lines=trait_f.readlines()
    for t_line in t_lines:
        name,dnds,typ=t_line.split("\t")[1],t_line.split("\t")[2],t_line.split("\t")[4].strip()
        if typ =="tip":
            rate[name]=dnds

tree_file="C:/Users/dingdingche/Desktop/positive_tree_after.tree"
with open(tree_file)as tree_f:
    tree_lines=tree_f.read()
for key in rate.keys():
    tree_lines=re.sub(f"{key}",f"{key}:{rate[key]}",tree_lines)

with open("C:/Users/dingdingche/Desktop/test.tree","w")as out:
    out.write(tree_lines)
with open("C:/Users/dingdingche/Desktop/test.fa","w")as out1:
    for k in rate.keys():
        out1.write(f"{k}\t{bill[k]}\n")
