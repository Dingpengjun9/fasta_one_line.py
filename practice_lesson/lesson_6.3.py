import sys
input_name=sys.argv[1]
output_name=sys.argv[2]

pairs={}
score1=0
with open(input_name) as file:
    lines=file.readlines()
    for line_split in lines:
        line=line_split.split("\t")
        query,subject,score=line[0],line[1],line[-1][:-1]
        if query==subject:
            score1=0
        if query!=subject:
            if int(float(score)) > int(float(score1)):
                pairs[query] = subject
                score1=score


orthlog={}
for k,v in pairs.items():
    try:
        if pairs[v]==k:
            orthlog[k]=v
            pairs[v]=''
    except:
        pass

with open(output_name,"w",encoding="utf-8") as out:
    for k,v in orthlog.items():
        out.write(f'{str(k)} {str(v)}\n')

