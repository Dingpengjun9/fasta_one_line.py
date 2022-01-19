##随机抽取每个基因的物种，来运行pmal

import sys
import re
import random
import os

target=["Corvus_brachyrhynchos","Corvus_cornix","Corvus_moneduloides","Aphelocoma_coerulescens"]
number=40
gene_path="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/gene"

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/radom/run.sh","w",encoding="utf-8")as sh:
    pass

#find full seqence and tree file
gene_files=os.listdir(gene_path)
for gene_file in gene_files:
    gene_num=gene_file[-5:]
    dir_number=int(int(gene_num)/200)
    dir_num='{:0>3}'.format(dir_number)
    tree_file=f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR/{dir_num}/{gene_file}/positive_tree_after.tree"
    fa_file=f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR/{dir_num}/{gene_file}/{gene_file}_all_gap.fa"
    with open(tree_file)as tree_f:
        tree_content=tree_f.readline()
        tree_content=re.sub(r'Node\d+', "", tree_content)
        tree_devalue = re.sub(r':\d+\.?\d*[e-]*\d*', "", tree_content)
    species=re.findall(r"\w+_\w+",tree_devalue)

    with open(fa_file)as fa_f:
        fa_lines=fa_f.readlines()
        sp_fa={}
        seq=""
        sp_name=""
        for fa_line in fa_lines:
            if fa_line[0]==">":
                sp_fa[sp_name] = seq
                sp_name=fa_line.replace(">","").replace("\n","")
                seq=""
            if fa_line[0]!=">":
                seq+=fa_line.replace("\n","")
        sp_fa[sp_name] = seq
        del sp_fa[""]
#
    for i in range(11,18):
        random.shuffle(species)
        spes=list(species)
        slist=[]
        for tar in target:
            if tar in spes:
                spes.remove(tar)
                slist.append(tar)
            else:
                print(f"{gene_path}/{gene_file}/{i}")
        slist = slist + spes[0:int(number)]
        species_name=str(slist).replace("[","").replace("'","").replace("]","").replace(" ","")
        os.system(f"mkdir -p {gene_path}/{gene_file}/{i}/h0/ && mkdir -p {gene_path}/{gene_file}/{i}/h1 && "
                  f"/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/egg_mass/bin/tree_doctor -P {species_name} "
                  f"-n /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/config/sp363.tree "
                  f"> {gene_path}/{gene_file}/{i}/hh.tree ")

        with open(f"{gene_path}/{gene_file}/{i}/hh.tree")as hhtree:
            htree_c=hhtree.read()
            htree_c = re.sub(r':\d+\.?\d*[e-]*\d*', "", htree_c)
            htree=re.sub(r"Aphelocoma_coerulescens\)","Aphelocoma_coerulescens) #1",htree_c)
        with open(f"{gene_path}/{gene_file}/{i}/h0/h0.tree","w",encoding="utf-8")as h0tree:
            h0tree.write(htree)
        with open(f"{gene_path}/{gene_file}/{i}/h1/h1.tree","w",encoding="utf-8")as h1tree:
            h1tree.write(htree)
        with open(f"{gene_path}/{gene_file}/{i}/h1/h1.fa","w",encoding="utf-8")as h1:
            for spe in slist:
                h1.write(f">{spe}\n{sp_fa[spe]}\n")
        with open(f"{gene_path}/{gene_file}/{i}/h0/h0.fa", "w", encoding="utf-8") as h0:
            for spe in slist:
                h0.write(f">{spe}\n{sp_fa[spe]}\n")
        with open(f"{gene_path}/{gene_file}/{i}/h0/h0.ctl", "w", encoding="utf-8") as ctl0:
            ctl0.write(f"seqfile = {gene_path}/{gene_file}/{i}/h0/h0.fa\n"
                            f"treefile = {gene_path}/{gene_file}/{i}/h0/h0.tree\n"
                            f"outfile = {gene_path}/{gene_file}/{i}/h0/h0.mlc\n"
                            f"noisy = 3\n"
                            f"verbose = 1\n"
                            f"runmode = 0\n"
                            f"seqtype = 1\n"
                            f"CodonFreq = 2\n"
                            f"clock = 0\n"
                            f"model = 2\n"
                            f"NSsites = 2\n"
                            f"icode = 0\n"
                            f"fix_kappa = 0\n"
                            f"kappa = 2\n"
                            f"fix_omega = 1 \n"
                            f"omega = 1")
        with open(f"{gene_path}/{gene_file}/{i}/h1/h1.ctl", "w", encoding="utf-8") as ctl1:
            ctl1.write(f"seqfile = {gene_path}/{gene_file}/{i}/h1/h1.fa\n"
                            f"treefile = {gene_path}/{gene_file}/{i}/h1/h1.tree\n"
                            f"outfile = {gene_path}/{gene_file}/{i}/h1/h1.mlc\n"
                            f"noisy = 3\n"
                            f"verbose = 1\n"
                            f"runmode = 0\n"
                            f"seqtype = 1\n"
                            f"CodonFreq = 2\n"
                            f"clock = 0\n"
                            f"model = 2\n"
                            f"NSsites = 2\n"
                            f"icode = 0\n"
                            f"fix_kappa = 0\n"
                            f"kappa = 2\n"
                            f"fix_omega = 0 \n"
                            f"omega = 1.5")
        with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/radom/run.sh","a",encoding="utf-8")as sh:
            sh.write(f"cd {gene_path}/{gene_file}/{i}/h1 && /share/app/paml-4.8/bin/codeml {gene_path}/{gene_file}/{i}/h1/h1.ctl\n"
                     f"cd {gene_path}/{gene_file}/{i}/h0 && /share/app/paml-4.8/bin/codeml {gene_path}/{gene_file}/{i}/h0/h0.ctl\n")