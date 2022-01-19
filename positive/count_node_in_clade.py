#统计
import sys
input_file=sys.argv[1]

long=0
clade1_node=0
clade1_tip=0
clade2_node=0
clade2_tip=0
clade3_node=0
clade3_tip=0
clade4_node=0
clade4_tip=0
n_node=0
n_tip=0

with open(input_file)as input:
    input_lines=input.readlines()
    for line in input_lines:
        num_node = 0
        num_tip = 0
        gene,clade,nodes=line.split("\t")[0],line.split("\t")[1],line.split("\t")[2].split(",")
        long+=len(nodes)
        for node in nodes:
            if "Node" in node:
                num_node+=1
                n_node+=1
            elif "Node" not in node and node !="":
                num_tip+=1
                n_tip+=1
        if clade=='clade1':
            clade1_node+=num_node
            clade1_tip+=num_tip
        if clade=='clade2':
            clade2_node+=num_node
            clade2_tip+=num_tip
        if clade=='clade3':
            clade3_node+=num_node
            clade3_tip+=num_tip
        if clade=='clade4':
            clade4_node+=num_node
            clade4_tip+=num_tip

print(f"{input_file}")
print(f"In total have {n_node} nodes and {n_tip} tips.")
print("#############################################")
print(f"clade1 have {clade1_node} nodes and {clade1_tip} tips.")
print(f"clade2 have {clade2_node} nodes and {clade2_tip} tips.")
print(f"clade3 have {clade3_node} nodes and {clade3_tip} tips.")
print(f"clade4 have {clade4_node} nodes and {clade4_tip} tips.")
print(f"total:{long}")


