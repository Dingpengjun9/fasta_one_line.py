import re
ps_value={}
with open('E:/Test/convert/test.fa')as file:
    lines=file.readlines()
    for line in lines:
        name,value=line.split("\t")[0],line.split("\t")[1].strip("\n")
        ps_value[name]=value

#转换成树
#node_tree="/hwfssz5/ST_DIVERSITY/B10K/USER/dengyuan/05.brain_size/pipeline_traits/config/node.tree"
node_tree="E:/Test/conver_tree/node.tree"
with open(node_tree)as tree:
    trees=tree.read()
    for key,value in ps_value.items():
        #trees=re.sub(rf"{key}",rf"{key}:{value}",trees)
        trees = re.sub(rf"{key}", rf"{key}:1[&&NHX:psg={value}]", trees)

with open("E:/Test/convert/nhx_part_before_log_scal.tree","w",encoding="utf-8")as out_tree:
    out_tree.write(trees)
