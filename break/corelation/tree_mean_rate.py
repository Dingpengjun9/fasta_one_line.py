#计算时间树上的平均速度
import re
import sys
time_tree=sys.argv[1]
trait_file=sys.argv[2]
aa_file=sys.argv[3]
#aa_file="E:/WeChat/WeChat Files/wxid_c2506vkqqy8h22/FileStorage/File/2022-01/cc.txt"
#split_part=sys.argv[3]
#time_tree="E:/R/bill_trait_data/sp362_time.tree"
#trait_file="E:/WeChat/WeChat Files/wxid_c2506vkqqy8h22/FileStorage/File/2022-01/ratio_log_bill_nares_tree1.0.txt"
split_part=1
aaa={}
with open(aa_file)as aa_f:
    in_lines = aa_f.readlines()
    for line in in_lines:
        try:
            nnum, nname = line.strip("\n").split("\t")
        except:
            nnum, nname = line.strip("\n").split(" ")
        aaa[nnum]=nname
#获取每个节点的子节点
##获取每个node下所含物种
with open(time_tree)as file:
    node_tree=file.read()
    node_tree=re.sub(r":\d*\.?\d*","",node_tree)
    sub_tree = {}
    sub_tree_node = {}
    # 获取每个node下物种名
    nodes = re.findall(r'Node\d+:?\d*\.?\d*', node_tree)
    for node in nodes:
        part = node_tree.split(node)[0]
        re_piece = part[::-1]
        rnum, n, lnum = 0, 0, 0
        for aa in re_piece:
            n += 1
            if aa == ")":
                rnum += 1
            if aa == "(":
                lnum += 1
                if lnum == rnum:
                    start = n
                    spe=part[-start:]
                    #spe = re.sub(r'Node\d+[:01]*', "", part[-start:])
                    sspe = re.sub(r'\w+_\w+[:01]*', "", part[-start:])
                    sspe = sspe.replace(")N", ",)N").replace("(", "").replace(")", "").split(",")
                    spe = spe.replace(")N", ",)N").replace("(", "").replace(")", "").split(",")
                    while '' in spe:
                        spe.remove('')
                    node = node.replace(")", "").strip(",")
                    while '' in sspe:
                        sspe.remove('')
                    sub_tree[node] = spe
                    sub_tree_node[node] = sspe
                    break
node_pair={}
for k1 in sub_tree.keys():
    tras={}
    for k2 in sub_tree.keys():
        if len(sub_tree[k1])>len(sub_tree[k2]):
            if set(sub_tree[k1]) > set(sub_tree[k2]):
                if k1 in node_pair.keys():
                    for k3 in node_pair[k1]:
                        if set(sub_tree[k2]) > set(sub_tree[k3]):
                            node_pair[k1].remove(k3)
                            node_pair[k1].append(k2)
                else:
                    node_pair[k1]=[]
                    node_pair[k1].append(k2)
    if sub_tree_node[k1]:
        another=list(set(sub_tree_node[k1])-set(sub_tree_node[node_pair[k1][0]]))
        another.remove(node_pair[k1][0])
        for k4 in sub_tree_node.keys():
            aattend=list(set(sub_tree_node[k4]))+[k4]
            if set(aattend) ==set(another):
                node_pair[k1].append(k4)
for k5 in sub_tree.keys():
    if k5 not in node_pair.keys():
        node_pair[k5]=sub_tree[k5]
#获取时间信息
spe_time={}
with open(time_tree)as time_f:
    time_line=time_f.read()
    time_line=re.sub(";[\n]?",f":{split_part*2}",time_line)
    time_line=re.sub("\(","",time_line)
    time_line=re.sub("\)",",",time_line)
    spes=time_line.split(",")
    for line in spes:
        tip,time_num=line.split(":")
        spe_time[tip]=time_num

stas={}
max_length=0
for k6 in node_pair.keys():
    length=0

    father=k6
    for i in range(1,1000):
        son = node_pair[father][0]
        length += float(spe_time[son])
        if node_pair[father][0] in node_pair.keys():
            father = node_pair[father][0]
        else:
            stas[k6]=length
            if length >max_length:
                max_length =length
            break
for k8 in spe_time.keys():
    if k8 not in stas.keys():
        stas[k8]=0

#读取性状
rate={}
with open(trait_file)as trait_f:
    trait_lines=trait_f.readlines()
    for trait_line in trait_lines:
        if trait_line[:4] =="node":
            trait_len=len(trait_line.split(" "))
            trait_type=trait_line.split(" ")[2].split("_")[1]
        else:
            nnn,mrate=trait_line.split(" ")[0],trait_line.split(" ")[-2].strip(" ")
            label=aaa[nnn]
            rate[label]=mrate


result={}
max_length=int(max_length)+split_part
for ii in range(0,max_length,split_part):
    leng_sum=0
    num=0
    ii2=ii+split_part
    for k7 in stas.keys():
        if ii in range(int(stas[k7]+1),int(stas[k7]+float(spe_time[k7])+1)) or ii2 in range(int(stas[k7]+1),int(stas[k7]+float(spe_time[k7])+1)) or (ii <stas[k7] and ii2 >stas[k7]+float(spe_time[k7])):

            leng_sum+=float(rate[k7])
            num+=1
    mean_rate=leng_sum/num
    mean_i=str((ii+ii2)/2)
    result[mean_i]=mean_rate

part_outfile="/".join(trait_file.split("/")[:-1])
out_file=part_outfile+f"/{trait_type}_out.txt"
#out_file=part_outfile+f"/trait_type_out.txt"
with open(out_file,"w")as out:
    for kk,vv in result.items():
        out.write(f"{kk}\t{vv}\n")

