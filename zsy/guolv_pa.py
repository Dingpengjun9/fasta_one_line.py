import re
spe={}
with open("C:/Users/dingdingche/Desktop/sy.txt",encoding="utf-8")as inf:
    lines=inf.readlines()
    for line in lines:

        riname=[]
        name,syname=line.split("\t")[0],line.split("\t")[2].rstrip("\n")
        aname=name.replace("_"," ")

        synames=syname.split(",")
        for syna in synames:
            if syna[0]!= " ":
                if syna.split(" ")[0] :
                    if syna.split(" ")[0][-1]==".":
                        riname.append(syna)
                if len(syna.split(" "))==2  :
                    riname.append(syna)
        no_riname=list(set(riname))
        if aname in no_riname:
            no_riname.remove(aname)
        spe[name]=no_riname

with open ("C:/Users/dingdingche/Desktop/out.txt","w",encoding="utf-8")as out:
    for k,v in spe.items():
        aa=",".join(v)
        out.write(f"{k}\t{aa}\n")
