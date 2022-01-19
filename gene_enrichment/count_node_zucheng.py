import sys
import os

out_genelisy=sys.argv[1]
ars="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR"

out_gene={}
with open(out_genelisy)as ain:
    alines=ain.readlines()
    for aline in alines:
        out_gene[aline.strip()]=[0]

for dir_num in range(0,90):
    r_dir_num="{:0>3d}".format(int(dir_num))
    filenames=os.listdir(rf"{ars}/{r_dir_num}")
    for filename in filenames:
        if os.path.exists(f"{ars}/{r_dir_num}/{filename}/pair_after.fa"):
            with open(f"{ars}/{r_dir_num}/{filename}/pair_after.fa")as infile:
                lines=infile.readlines()
                for line in lines:
                    ponum,allnode=line.split("\t")[-2],line.split("\t")[-1].strip()
                    if allnode in out_gene.keys() and int(ponum) == 1:
                        out_gene[allnode].append(filename)
                        out_gene[allnode][0]+=1
        else:
            print(f"{r_dir_num}/{filename}/pair_after.fa\tnot exist")

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/05.enrich/count_oulier_compose/result/count_compose","w",encoding="utf-8")as aout:
    for key,val in out_gene.items():
        value=str(val).replace("[","").replace("]","").replace("'","").replace(" ","")
        aout.write(f"{key}\t{value[:3]}\t{value[4:]}\n")