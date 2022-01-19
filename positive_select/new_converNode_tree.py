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
    for part in parts:
        n+=1
        string +=f'{part})Node{n},'
    string=string.strip(",")
    return string

#去掉树上的node
def del_node(node_tree):
    line=re.sub(r'Node\d+,?',"",node_tree)
    return line

#去掉树上的数值
def del_value(value_tree):
    line=re.sub(r':\d+\.?\d*[e-]*\d*',"",value_tree)
    return line

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
    positive_file=sys.argv[2]
    version=sys.argv[3]

    #total_tree = "E:/Test/conver_tree/node.tree"
    #positive_file = "E:/Test/convert/no_error.fa"
    #version = "after"

    with open(total_tree)as tt_tree_file:
        tt_tree=tt_tree_file.read()
        [tt_min_co_ance,tt_sub_tree]=min_ance(tt_tree)

    psg={}
    with open(positive_file)as psg_file:
        lines=psg_file.readlines()
        for line in lines:
            parts=line.split("\t")
            gene,positive=parts[0],parts[1].strip("\n")
            psg[f"{gene}"]=positive.split(",")

    ps_value={}
    #ars = "/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR/"
    ars="E:/Test/ASR/"
    for i in range(0, 90):
        num = "{:0>3d}".format(i)
        filenames = os.listdir(rf"{ars}{num}")
        for filename in filenames:
            if 1==1:
                if os.path.exists(f"{ars}{num}/{filename}/ancestor.json"):
                    if os.path.getsize(f"{ars}{num}/{filename}/ancestor.json")!=0:
                        with open(f"{ars}{num}/{filename}/ancestor.json", encoding='utf-8') as js:
                            ancestor = json.load(js)
                            ge_tree = ancestor["tree"]
                            ge_trees = del_value(ge_tree)
                            try:
                                po_ge_tree = get_positive(ge_trees, psg[f"{filename}"])
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
                                    print(f"{filename}\t{tip1}\t{tip2}")
                                    quit()
                    else:
                        print(f"line 112 {num}/{filename}")
                else:
                    print(f"line 111 {num}/{filename}")


                with open(f'{ars}{num}/{filename}/pair_{version}.fa', 'w', encoding='utf-8') as out:
                    for key, value in pair.items():
                        out.write(f"{filename}\t{key.split(':')[0]}\t{key.split(':')[1]}\t{value}\n")
                    for ii in po_gene:
                        out.write(f"{filename}\t{ii.split(':')[0]}\t{ii.split(':')[1]}\t{ii.split(':')[0]}\n")

                with open(f'{ars}{num}/{filename}/positive_tree_{version}.tree', 'w', encoding='utf-8') as out_tree:
                    out_tree.write(po_ge_tree)

                with open (f"{ars}{num}/{filename}/pair_{version}.fa",encoding='utf-8') as fa:
                    lines=fa.readlines()
                    for line in lines:
                        p_value,node=int(line.split("\t")[-2]),line.split("\t")[-1].strip("\n")
                        if node in ps_value.keys():
                            ps_value[node]+=p_value
                        elif node not in ps_value.keys():
                            ps_value[node]=p_value

    path = "/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/03.convert"
    with open(f"{ars}/positive_part_{version}.fa", "w", encoding="utf-8") as pofile:
        for key, value in ps_value.items():
            pofile.write(f"{key}\t{value}\n")

