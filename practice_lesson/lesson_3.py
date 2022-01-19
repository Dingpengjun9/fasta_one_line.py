import re

count=0
cds_long={}

with open('E:/BGI/New Folder/data/cflo_v3.3.gff/cflo_v3.3.gff') as file:
    lines=file.readlines()
    for line in lines:
        lis=line.split("\t")
        if lis[2]=='mRNA':
            count+=1
            all_part_long = 0
            try:
                scaff_name=re.search("C\S+",lis[-1]).group()
            except:
                error=lis[-1]
        if lis[2]=='CDS':
            part_long=int(lis[4])-int(lis[3])
            all_part_long+=part_long
            cds_long[scaff_name]=all_part_long




