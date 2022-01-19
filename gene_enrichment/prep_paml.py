import os
node='/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122'
path="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/gene"
with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/config/run_perp.sh","w",encoding="utf-8")as out:
    pass
with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/config/run.sh","w",encoding="utf-8")as aout:
    pass

filenames=os.listdir(path)
for filename in filenames:
    with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/config/run.sh","a",encoding="utf-8")as aout:
        aout.write(f"cd {path}/{filename}/h0 && /share/app/paml-4.8/bin/codeml {path}/{filename}/h0/h0.ctl\n")
        aout.write(f"cd {path}/{filename}/h1 && /share/app/paml-4.8/bin/codeml {path}/{filename}/h1/h1.ctl\n")


    with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/04.paml/test_Node122/config/run_perp.sh","a",encoding="utf-8")as out:
        out.write(f"cp {node}/h0.tree {path}/{filename}/h0/h0.tree && cp {node}/h1.tree {path}/{filename}/h1/h1.tree \n")
        out.write(f"cp {node}/hh.fa {path}/{filename}/h0/h0.fa && cp {node}/hh.fa {path}/{filename}/h1/h1.fa \n")
    with open(f"{path}/{filename}/h0/h0.ctl","w",encoding="utf-8") as ao:
        ao.write(f"seqfile = {path}/{filename}/h0/h0.fa\ntreefile = {path}/{filename}/h0/h0.tree\noutfile = {path}/{filename}/h0/h0.mlc\nnoisy = 3\nverbose = 1\nrunmode = 0\nseqtype = 1\nCodonFreq = 2\nclock = 0\nmodel = 2\nNSsites = 2\nicode = 0\nfix_kappa = 0\nkappa = 2\nfix_omega = 1 \nomega = 1")
    with open(f"{path}/{filename}/h1/h1.ctl","w",encoding="utf-8") as bo:
        bo.write(f"seqfile = {path}/{filename}/h1/h1.fa\ntreefile = {path}/{filename}/h1/h1.tree\noutfile = {path}/{filename}/h1/h1.mlc\nnoisy = 3\nverbose = 1\nrunmode = 0\nseqtype = 1\nCodonFreq = 2\nclock = 0\nmodel = 2\nNSsites = 2\nicode = 0\nfix_kappa = 0\nkappa = 2\nfix_omega = 0 \nomega = 1.5")





'''
with open("E:/Test/enrich/Node122/doctor_spe.txt")as af:
    aa=af.read()
    names=aa.split(",")

fa={}
with open("E:/Test/enrich/Node122/GALGAL_R02932_all_gap.fa")as bf:
    lines=bf.readlines()
    for line in lines:
        if line[0] ==">":
            nam=line.strip("\n")[1:]
            sting = ""
        else:
            sting+=line.strip("\n")
            fa[nam]=sting

with open("E:/Test/enrich/Node122/hh.fa","w",encoding="utf-8")as cf:
    for name in names:
        cf.write(f">{name}\n{fa[name]}\n")
'''