import sys
ifile=sys.argv[1]
outfile=sys.argv[2]
aa={}
tt={}
cc={}
gg={}
nnn={}
name=""
long=0
a=0
t=0
c=0
g=0
nn=0
with open(ifile) as fa:
    lines=fa.readlines()
    for line in lines:
        if line[0]==">":
            aa[name]=a
            tt[name] = t
            gg[name] = g
            cc[name] = c
            nnn[name] = nn
            name=line[1:].strip("\n")
            long=0
            a=0
            t=0
            c=0
            g=0
            nn=0
        else:
            for bp in line:
                if bp =="A":
                    a += 1
                if bp =="C":
                    c += 1
                if bp == "T":
                    t += 1
                if bp == "G":
                    g += 1
                if bp =="N":
                    nn += 1
    aa[name] = a
    tt[name] = t
    gg[name] = g
    cc[name] = c
    nnn[name] = nn
    del aa[""]
    del tt[""]
    del cc[""]
    del gg[""]
    del nnn[""]
    with open (outfile,"w")as out:
        for k,v in aa.items():
            out.write(f"{k}\nA:{aa[name]}\tC:{cc[name]}\tT:{tt[name]}\tG:{gg[name]}\n")
