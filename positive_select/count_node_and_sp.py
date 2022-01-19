#统计
import sys
input_file=sys.argv[1]

long=0
n_node=0
n_tip=0

with open(input_file)as input:
    input_lines=input.readlines()
    for line in input_lines:
        num_node = 0
        num_tip = 0
        gene,nodes=line.split("\t")[0],line.split("\t")[1].split(",")
        long+=len(nodes)
        for node in nodes:
            if "Node" in node:
                n_node+=1
            elif "Node" not in node and node !="":
                n_tip+=1


print(f"{input_file}")
print(f"In total have {n_node} nodes and {n_tip} tips.")
print(f"total:{long}")


