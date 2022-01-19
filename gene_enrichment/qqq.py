aaa={}
b={}
c="any"
with open("E:/Test/enrich/Node122/axon_spe1.txt")as a:
    lines=a.readlines()
    for line in lines:
        name,spe=line.split("\t")[0],line.split("\t")[1].strip("\n").split(",")
        aaa[name]=spe
cc=list(aaa["GALGAL_R02932"])

ccc=list(cc)
for ii in cc:
    if ii == 'Nothoprocta_pentlandii':
        print("q")
    for k in aaa.keys():
        if ii not in aaa[k]:
            if ii in ccc:
                a=ccc.remove(ii)
                if ii =='Nothoprocta_pentlandii':
                    print("q")
                    print(ii in ccc)
ii ='Nothoprocta_pentlandii'