ad={}
with open ("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/03.convert/add.fa")as add:
    lines=add.readlines()
    for line in lines:
        gene, value=line.split("\t")[-1],line.split("\t")[-2]
        ad[gene]=value

noerrer={}
with open ("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/03.convert/positive_part_after.fa")as after:
    lines=after.readlines()
    for line in lines:
        name,v=line.split("\t")[0],line.split("\t")[1]
        if name in ad.keys():
            noerrer[name]=int(v)+1
        else:
            noerrer[name]=v

with open ("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/03.convert/ad_positive_part_after.fa","w")as out:
    for key,val in noerrer.items():
        out.write(f"{key}\t{val}\n")
