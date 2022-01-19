import sys
file_name=sys.argv[1]
out_name=sys.argv[2]

seq={}
name=''
seqs=''
with open(file_name)as f:
    lines =f.readlines()
for line in lines:
    if line[0]==">":
        name=line
    else:
        lll=line.replace("\n","")
        seqs="".join([seqs,lll])
        seq[name] = seqs
with open(out_name,"w",encoding="utf-8") as out:
    for k,v in seq.items():
        out.write(str(k))
        out.write(str(v))



