#获取每个clade对应node
import re
#获取每个node下所含物种
with open("E:/R/bill_trait_data/sp362_time.tree")as file:
    node_tree=file.read()
    node_tree=re.sub(r":\d*\.?\d*","",node_tree)
    sub_tree = {}
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
                    #spe = re.sub(r'\w+_\w+[:01]*', "", part[-start:])
                    spe = spe.replace(")N", ",)N").replace("(", "").replace(")", "").split(",")
                    while '' in spe:
                        spe.remove('')
                    node = node.replace(")", "").strip(",")
                    sub_tree[node] = spe
                    break

#获取每个目对应node
order_spe={}
with open("E:/Test/B10Kid_hal.tree.sorted")as order:
    lines=order.readlines()
    for line in lines:
        spec,order=line.split("\t")[-3],line.split("\t")[-2]
        if spec in node_tree:
            if order in order_spe.keys():
                order_spe[order].append(spec)
            else:
                order_spe[order]=[]
                order_spe[order].append(spec)

node_ord={}
node_ords={}
for node_name in sub_tree.keys():
    for order_name in order_spe.keys():
        i = 0
        if len(sub_tree[node_name])==len(order_spe[order_name]):
            for spec in order_spe[order_name]:
                if spec in sub_tree[node_name]:
                    i+=1
                    if i ==len(order_spe[order_name]):
                        node_ord[node_name]=order_name
                else:
                    continue

        if len(sub_tree[node_name])>=len(order_spe[order_name]):
            for spec in order_spe[order_name]:
                if spec in sub_tree[node_name]:
                    i+=1
                    if i ==len(order_spe[order_name]):
                        if node_name in node_ords.keys():
                            node_ords[node_name].append(order_name)
                        else:
                            node_ords[node_name]=[]
                            node_ords[node_name].append(order_name)
                else:
                    continue

with open("E:/Test/eggmass_info.fa","w",encoding="utf-8")as info:
    for key,value in node_ord.items():
        info.write(f"{key}\t{value}\n")
    for key, value in node_ords.items():
        info.write(f"{key}\t{value}\n")

with open("E:/Test/eggmass_3.fa","w",encoding="utf-8")as info:
    for key,value in sub_tree.items():
        if value!="":
            for i in value:
                if i in node_ord.keys():
                    value=re.sub(rf"{i}",rf"{node_ord[i]}",str(value))
                if i in node_ords.keys():
                    value=re.sub(rf"{i}",rf"{node_ords[i]}",value)
        if key not in node_ords.keys() and key not in node_ord.keys():
            info.write(f"{key}\t{value}\n")

