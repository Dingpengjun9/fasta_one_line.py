import sys

vlist=[]
with open ("C:/Users/dingdingche/Desktop/turning.obj")as f:
    lines=f.readlines()
    for line in lines:
        if line[:2]== "v ":
            vline=line.replace(" ",",").replace("v,","").strip()
            vlist.append(vline)
with open("C:/Users/dingdingche/Desktop/turning.obj.out","w",encoding="utf-8")as out:
    for vl in vlist:
        out.write(f"{vl}\n")

vlist=[]
with open ("C:/Users/dingdingche/Desktop/cranium.ply.stl")as f:
    lines=f.readlines()
    for line in lines:
        if "vertex" in line:
            vline=line.replace("vertex",",").strip().replace(" ",",").rstrip(",")
            vlist.append(vline)
with open("C:/Users/dingdingche/Desktop/cranium.ply.out","w",encoding="utf-8")as out:
    for vl in vlist:
        out.write(f"{vl.strip(',')}\n")