#计算每个节点的累计正选择
import os
import re

ps_value={}
ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
#ars="E:/Test/ASR/"
for i in range(0,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        for nn in range(1,5):
            try:
                with open (f"{ars}{num}/{filename}/clade{nn}/pair.fa",encoding='utf-8') as fa:
                    lines=fa.readlines()
                    for line in lines:
                        value,node=int(line.split("\t")[-2]),line.split("\t")[-1].strip("\n")
                        if node in ps_value.keys():
                            ps_value[node]+=value
                        elif node not in ps_value.keys():
                            ps_value[node]=value
            except FileNotFoundError:
                print(f"{num}/{filename}/clade{nn} not find")

path="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/8.convernode"
with open(f"{path}/positive_part1.fa","w",encoding="utf-8")as pofile:
    for key,value in ps_value.items():
        pofile.write(f"{key}\t{value}\n")


'''
#/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/7.filtrate/new_no_gap_no_outgroup_filtrate_positive.psg
psg = {}
with open("E:/Test/conver_tree/new_no_gap_no_outgroup_filtrate_positive.psg") as psg_file:
    lines = psg_file.readlines()
    for line in lines:
        parts = line.split("\t")
        gene, clade, positive = parts[0], parts[1], parts[2].strip("\n")
        psg[f"{gene}_{clade}"] = positive.split(",")

#path="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/8.convernode"
path="E:/Test/conver_tree"
a=0
part_po={}
with open(f"{path}/un_conver")as part:
    lines=part.readlines()
    for line in lines:
        a += 1
        gene=line.split("\t")[1].split("/")[1]
        clade=line.split('\t')[-1].strip('\n')
        name=f"{gene}_{clade}"
        try:
            print(f"{name}_{psg[name]}")
        except:
            KeyError

        try:
            for i in psg[name]:

                if i!="":
                    if i in ps_value.keys():
                        ps_value[node]+=1
                elif node not in ps_value.keys():
                    ps_value[node] = 1
        except:
            KeyError
            print(f"{name}")

'''




