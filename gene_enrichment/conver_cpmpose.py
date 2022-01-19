jd="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/05.enrich/count_oulier_compose"
#jd="E:\Test\enrich"
conv={}
reconv={}
with open (f"{jd}/NCBI-011.function.GN")as ain:
    alines=ain.readlines()
    for aline in alines:
        galgal,gene=aline.split("\t")[0],aline.split("\t")[1]
        conv[galgal]=gene
        reconv[gene]=galgal

new_name={}
old_name={}
with open(f"{jd}/result/count_compose")as binf:
    blines=binf.readlines()
    for bline in blines:
        node,gals=bline.split("\t")[0],bline.split("\t")[-1].strip("\n").split(",")
        new_name[node]=[]
        old_name[node] = []
        for gal in gals:
            if conv[gal]== "NA":
                old_name[node].append(gal)
            else:
                new_name[node].append(conv[gal])

with open(f"{jd}/result/conver_compose","w",encoding="utf-8")as aout:
    for key in new_name.keys():
        new=str(new_name[key]).replace("[","").replace("]","").replace("'","").replace(" ","")
        old = str(old_name[key]).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
        aout.write(f"{key}\t{new}\t{old}\n")

#######################################
with open("")as cin:
    clines=cin.readlines()
    for cline in clines:
        gene_name=cline.strip("\n")
        f
