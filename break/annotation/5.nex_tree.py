import re

n=0
num={}
new_file="E:/WeChat/WeChat Files/wxid_c2506vkqqy8h22/FileStorage/File/2022-01/trait_time.tree"
with open(new_file)as new_f:
    lines=new_f.read()
    spes=re.findall(r"\w+_\w+",lines)
    for spe in spes:
        n+=1
        num[spe]= n
for key in num.keys():
    lines=re.sub(f"{key}",f"{num[key]}",lines)
tree=re.sub(r"Node\d+","",lines)

with open("C:/Users/dingdingche/Desktop/nex.tree","w")as out:
    out.write(r"#NEXUS")
    out.write("\nbegin trees;\n\ttranslate\n")
    for k,v in num.items():
        out.write(f"\t\t{v} {k},\n")
    out.write(f"\t\ttree UNTITLED = {tree}end;")
