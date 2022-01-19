#将两个树的内部祖先节点对应起来
import re
import sys
import json
import os



#给没有祖先节点的树添加祖先节点
def make_node(no_node_tree):
    string = ''
    n=0
    parts=no_node_tree.split(")")
    #long=len(parts)
    for part in parts:
        n+=1
        #num=f"{ {0}:0{1}>d}".format(n,4)    怎么带变量格式化
        string +=f'{part})Node{n}'
    string=string.strip(",")
    return string

#去掉树上的node
def del_node(node_tree):
    line=re.sub(r'Node\d+',"",node_tree)
    return line

#去掉树上的数值
def del_value(value_tree):
    line=re.sub(r':\d+\.?\d*[e-]*\d*',"",value_tree)
    return line

with open("E:/beak/1dim/Measurement_data/sp362_time.tree")as tree_f:
    tree=tree_f.read()
    tree_a=del_node(tree)
    tree_b=make_node(tree_a)

#获取两物种最小共同祖先
def min_ance(node_tree):
    sub_tree={}
    min_co_ance={}
    #获取每个node下物种名
    nodes=re.findall(r'Node\d+:?\d*\.?\d*',node_tree)
    for node in nodes:
        part=node_tree.split(node)[0]
        re_piece = part[::-1]
        rnum,n,lnum=0,0,0
        for aa in re_piece:
            n += 1
            if aa == ")":
                rnum += 1
            if aa == "(":
                lnum += 1
                if lnum == rnum:
                    start = n
                    spe = re.sub(r'Node\d+[:01]*', "", part[-start:])
                    spe=spe.replace(")N",",)N").replace("(","").replace(")","").split(",")
                    while '' in spe:
                        spe.remove('')
                    node=node.replace(")","").strip(",")
                    sub_tree[node]=spe
                    break
        #获取两物种最小共同祖先
        for tip1 in sub_tree[node]:
            if tip1 not in min_co_ance.keys():
                min_co_ance[tip1] = {}
            for tip2 in sub_tree[node]:
                if tip1!=tip2:
                    if tip2  in min_co_ance[tip1]:
                        if len(sub_tree[node])>len(sub_tree[min_co_ance[tip1][tip2]]):
                            pass
                        elif len(sub_tree[node])<len(sub_tree[min_co_ance[tip1][tip2]]):
                                min_co_ance[tip1][tip2]=node
                    else:
                        min_co_ance[tip1][tip2] = node
    return [min_co_ance,sub_tree]

#标记正选择基因为1，其他为0
def get_positive(tree,positive=""):
    tree=re.sub(r"(?P<tip>\w+_\w+)",r"\g<tip>:0",tree)
    tree=re.sub(r"(?P<node>Node\d+)",r"\g<node>:0",tree)
    if positive=="":
        pass
    else:
        for gene in positive:
            tree=re.sub(rf"{gene}:0",f"{gene}:1",tree)
    return tree

if __name__ == "__main__":
    total_tree=sys.argv[1]
    #total_tree='E:/Test/conver_tree/node.tree'
    #gene_tree=sys.argv[2]
    positive_file=sys.argv[2]
    version=sys.argv[3]

    #total_tree = "E:/Test/conver_tree/node.tree"
    # gene_tree=sys.argv[2]
    #positive_file = "E:/Test/conver_tree/all_spe_node.fa"
    #version = "after"

    with open(total_tree)as tt_tree_file:
        tt_tree=tt_tree_file.read()
        [tt_min_co_ance,tt_sub_tree]=min_ance(tt_tree)

    psg={}
    with open(positive_file)as psg_file:
        lines=psg_file.readlines()
        for line in lines:
            parts=line.split("\t")
            gene,clade,positive=parts[0],parts[1],parts[2].strip("\n")
            psg[f"{gene}_{clade}"]=positive.split(",")

    ps_value={}
    ars = "/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
    #ars="E:/Test/ASR/"
    for i in range(0, 90):
        num = "{:0>3d}".format(i)
        filenames = os.listdir(rf"{ars}{num}")
        for filename in filenames:
            for nn in range(1, 5):
                if os.path.exists(f"{ars}{num}/{filename}/clade{nn}/ancestor.json"):
                    if os.path.getsize(f"{ars}{num}/{filename}/clade{nn}/ancestor.json")!=0:
                        with open(f"{ars}{num}/{filename}/clade{nn}/ancestor.json", encoding='utf-8') as js:
                            ancestor = json.load(js)
                            ge_tree = ancestor["tree"]
                            ge_trees = del_value(ge_tree)
                            try:
                                po_ge_tree = get_positive(ge_trees, psg[f"{filename}_clade{nn}"])
                            except KeyError:
                                po_ge_tree = get_positive(ge_trees)

                            [gene_min_co_tree, ge_sub_tree] = min_ance(po_ge_tree)
                            po_gene = re.findall(r"\w+_\w+:[01]", po_ge_tree)


                        pair = {}
                        for tip1 in gene_min_co_tree.keys():
                            for tip2 in gene_min_co_tree[tip1]:
                                try:
                                    if gene_min_co_tree[tip1][tip2] in pair.keys():
                                        if len(tt_sub_tree[pair[gene_min_co_tree[tip1][tip2]]]) > len(
                                                tt_sub_tree[tt_min_co_ance[tip1.split(":")[0]][tip2.split(":")[0]]]):
                                            pass
                                        elif len(tt_sub_tree[pair[gene_min_co_tree[tip1][tip2]]]) > len(
                                                tt_sub_tree[tt_min_co_ance[tip1.split(":")[0]][tip2.split(":")[0]]]):
                                            pair[gene_min_co_tree[tip1][tip2]] = tt_min_co_ance[tip1.split(":")[0]][
                                                tip2.split(":")[0]]
                                    elif gene_min_co_tree[tip1][tip2] not in pair.keys():
                                        pair[gene_min_co_tree[tip1][tip2]] = tt_min_co_ance[tip1[:-2]][tip2[:-2]]
                                except KeyError:
                                    print(f"{filename}_clade{nn}\t{tip1}\t{tip2}")
                                    quit()
                    else:
                        continue
                else:
                    continue


                with open(f'{ars}{num}/{filename}/clade{nn}/pair_{version}.fa', 'w', encoding='utf-8') as out:
                    for key, value in pair.items():
                        out.write(f"{filename}\tclade{nn}\t{key.split(':')[0]}\t{key.split(':')[1]}\t{value}\n")
                    for ii in po_gene:
                        out.write(f"{filename}\tclade{nn}\t{ii.split(':')[0]}\t{ii.split(':')[1]}\t{ii.split(':')[0]}\n")

                with open(f'{ars}{num}/{filename}/clade{nn}/positive_tree_{version}.tree', 'w', encoding='utf-8') as out_tree:
                    out_tree.write(po_ge_tree)

                with open (f"{ars}{num}/{filename}/clade{nn}/pair_{version}.fa",encoding='utf-8') as fa:
                    lines=fa.readlines()
                    for line in lines:
                        p_value,node=int(line.split("\t")[-2]),line.split("\t")[-1].strip("\n")
                        if node in ps_value.keys():
                            ps_value[node]+=p_value
                        elif node not in ps_value.keys():
                            ps_value[node]=p_value

    path = "/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/8.convernode"
    with open(f"{path}/positive_part_{version}.fa", "w", encoding="utf-8") as pofile:
        for key, value in ps_value.items():
            pofile.write(f"{key}\t{value}\n")



'''
    ancestorr=[]
    ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
    #ars="E:/Test/ASR/"
    for i in range(0,90):
        num="{:0>3d}".format(i)
        filenames = os.listdir(rf"{ars}{num}")
        for filename in filenames:
            for nn in range(1,5):
                ancestorr = []
                try:
                    with open (f"{ars}{num}/{filename}/clade{nn}/ancestor.json",encoding='utf-8') as js:
                        ancestor=json.load(js)
                        ge_tree=ancestor["tree"]
                        ge_trees=del_value(ge_tree)
                        try:
                            po_ge_tree=get_positive(ge_trees,psg[f"{filename}_clade{nn}"])
                        except KeyError:

                            po_ge_tree=get_positive(ge_trees)
                        [gene_min_co_tree,ge_sub_tree] = min_ance(po_ge_tree)
                        po_gene=re.findall(r"\w+_\w+:[01]",po_ge_tree)
                except FileNotFoundError or json.decoder.JSONDecodeError:
                    print(f"file\t{num}/{filename}\tclade{nn}")
                    break

                pair={}
                for tip1 in gene_min_co_tree.keys():
                    for tip2 in gene_min_co_tree[tip1]:
                        try:
                            if gene_min_co_tree[tip1][tip2] in pair.keys():
                                if len(tt_sub_tree[pair[gene_min_co_tree[tip1][tip2]]])>len(tt_sub_tree[tt_min_co_ance[tip1.split(":")[0]][tip2.split(":")[0]]]):
                                    pass
                                elif len(tt_sub_tree[pair[gene_min_co_tree[tip1][tip2]]])>len(tt_sub_tree[tt_min_co_ance[tip1.split(":")[0]][tip2.split(":")[0]]]):
                                    pair[gene_min_co_tree[tip1][tip2]]=tt_min_co_ance[tip1.split(":")[0]][tip2.split(":")[0]]
                            elif gene_min_co_tree[tip1][tip2] not in pair.keys():
                                pair[gene_min_co_tree[tip1][tip2]]=tt_min_co_ance[tip1[:-2]][tip2[:-2]]
                        except KeyError:
                            print(f"{filename}_clade{nn}\t{tip1}\t{tip2}")
                            quit()

                with open(f'{ars}{num}/{filename}/clade{nn}/pair.fa', 'w', encoding='utf-8') as out:
                    for key,value in pair.items():
                        out.write(f"{filename}\tclade{nn}\t{key.split(':')[0]}\t{key.split(':')[1]}\t{value}\n")
                    for ii in po_gene:
                        out.write(f"{filename}\tclade{nn}\t{ii.split(':')[0]}\t{ii.split(':')[1]}\t{ii.split(':')[0]}\n")
                with open(f'{ars}{num}/{filename}/clade{nn}/positive_tree.tree', 'w', encoding='utf-8') as out_tree:
                    out_tree.write(po_ge_tree)
'''

with open("E:/Test/enrich/Node122/trait_time.tree")as al:
    aa=al.read()
    aa=del_value(aa)
    aa=del_node(aa)
with open("E:/Test/enrich/Node122/h0.tree","w",encoding="utf-8")as hh:
    hh.write(aa)






