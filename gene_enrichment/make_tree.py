import re
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
    with open(f"{ars}/{vv}/{k}/positive_tree_after.tree") as bin:
        bline=bin.read()
        names=re.findall(r"\w+_\w+",bline)
        strings+=names
        strings=list(set(strings))
        name=str(names).replace("]","").replace("[","").replace("'","").replace(" ","")
        spes[k]=name
sss=list(strings)
for stri in strings:
    for kk,vvv in spes.items():
        if stri not in vvv:
            if stri in sss:
                sss.remove(stri)


with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/axon_spe.txt","w",encoding="utf-8")as aout:

    st=str(sss).replace("]","").replace("[","").replace("'","").replace(" ","")
    aout.write(f"commen spes:{st}\n")
    for key,val in spes.items():
        aout.write(f"{key}\t{val}\n")



