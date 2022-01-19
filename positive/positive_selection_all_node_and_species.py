#import sys
#gene_list=sys.argv[1]
'''
with open('/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/filtrate/all_positive.psg','w',encoding="utf-8")as out_file:
    out_file.write(f'#gene\tclade\tpositive\n')'''
posi={}

with open("/hwfssz5/ST_DIVERSITY/B10K/USER/dengyuan/05.brain_size/positive_selection/hyphy/nodes/gene.list")as file:
    lists=file.readlines()
    for list in lists:
        list_sp=list.split("\t")
        path=list_sp[1]
        genes=path.split("/")
        gene=genes[-1]
        for num in range(1,5):
            all_positive=[]
            name=f'{gene}-clade{num}'
            try:
                with open(f'{path}/clade{num}/absrel.log',encoding='utf-8')as log:
                    logs=reversed(log.readlines())
                    for line in logs:
                        if line[0]=="*":
                            if 'Node' not in line:
                                part=line.split(',')
                                all_positive.append(part[0][1:])
                                posi[name]=all_positive
                        else:
                            break
            except FileNotFoundError:
                pass
with open('/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/filtrate/all_positive.psg', 'w') as result:
    for key,value in posi.items():
        aa = str(value).replace("'", "").replace("[", "").replace("]", "")
        result.write(f'{key.split("-")[0]}\t{key.split("-")[1]}\t{aa.replace(" ","")}\n')
