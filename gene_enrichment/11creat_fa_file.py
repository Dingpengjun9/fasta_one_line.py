import re
with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/doctor_spe.txt")as af:
    aa=af.read()
    names=aa.split(",")

fa={}
gene_path={}
with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/axon.txt")as ain:
    alines=ain.readlines()
    for aline in alines:
        gene,num=aline.split("\t")[0],aline.split("\t")[1]
        gene_path[gene]=num.strip("\n")
spes={}
strings=[]
ars="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR"
for k,v in gene_path.items():
    vv="{:0>3d}".format(int(v))
    with open(f"{ars}/{vv}/{k}/{k}_all_gap.fa") as bf:
        lines = bf.readlines()
        for line in lines:
            if line[0] == ">":
                nam = line.strip("\n")[1:]
                sting = ""
            else:
                sting += line.strip("\n")
                fa[nam] = sting
    for nn in range(1,3):
        with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/gene/{k}/h{nn}.fa", "w", encoding="utf-8") as cf:
            for name in names:
                cf.write(f">{name}\n{fa[name]}\n")