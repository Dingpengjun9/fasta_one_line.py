import sys

in_file=sys.argv[1]
#in_file="E:/Test/convert/no_error.fa"
posi={}

with open(in_file)as infile:
    lines=infile.readlines()
    for line in lines:
        gene,po=line.split("\t")[0],line.split("\t")[1].rstrip("\n").rstrip(" ").split(",")
        pos=list(set(po))
        posi[gene]=pos

with open(f"{in_file}_rm",'w',encoding="utf-8") as out:
    for k,v in posi.items():
        value=str(v).replace("'","").replace(" ","")
        out.write(f"{k}\t{value[1:-1]}\n")