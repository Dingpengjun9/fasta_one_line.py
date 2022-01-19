count_scaff={}
file_name='E:/BGI/New Folder/data/cm.fa/cm.fa'
with open(file_name) as fasta:
    lines=fasta.readlines()
for line in lines:
    if line[0]=='>' :
        name=line[1:].strip()
        count_scaff[name]=0
    elif line[0]!='>':
        long=len(line.strip())
        count_scaff[name]+=long

with open ('E:/BGI/New Folder/data/cm.fa/cm.txt','w') as txts:
    for txt in count_scaff.keys():
        txts.write(f'{txt}\t{count_scaff[txt]}\n')
##########################################################################






