#计算每个节点的累计正选择
import os
import re

ps_value={}
ars="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR/"
#ars="E:/Test/ASR/"
for i in range(0,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        if 1==1:
            try:
                with open (f"{ars}{num}/{filename}/pair_before.fa",encoding='utf-8') as fa:
                    lines=fa.readlines()
                    for line in lines:
                        value,node=int(line.split("\t")[-2]),line.split("\t")[-1].strip("\n")
                        if node in ps_value.keys():
                            ps_value[node]+=value
                        elif node not in ps_value.keys():
                            ps_value[node]=value
            except FileNotFoundError:
                print(f"{num}/{filename} not find")

path="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/03.convert"
with open(f"{path}/positive_before_part1.fa","w",encoding="utf-8")as pofile:
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


import re
ps_value={}
with open('E:/Test/convert/positive_part.fa')as file:
    lines=file.readlines()
    for line in lines:
        name,value=line.split("\t")[0],line.split("\t")[1].strip("\n")
        ps_value[name]=value

#转换成树
#node_tree="/hwfssz5/ST_DIVERSITY/B10K/USER/dengyuan/05.brain_size/pipeline_traits/config/node.tree"
node_tree="E:/Test/convert/node.tree"
with open(node_tree)as tree:
    trees=tree.read()
    for key,value in ps_value.items():
        #trees=re.sub(rf"{key}",rf"{key}:{value}",trees)
        trees = re.sub(rf"{key}", rf"{key}:1[&&NHX:psg={value}]", trees)

with open("E:/Test/convert/egg.tree","w",encoding="utf-8")as out_tree:
    out_tree.write(trees)

