#import sys
#gene_list=sys.argv[1]
with open('dpj_gene.psg','w',encoding="utf-8")as out_file:
    out_file.write(f'#gene\tclade\tNode\tp-value\n')

with open("/hwfssz5/ST_DIVERSITY/B10K/USER/dengyuan/05.brain_size/positive_selection/hyphy/nodes/gene.list")as file:
    lists=file.readlines()
    for list in lists:
        list_sp=list.split("\t")
        path=list_sp[1]
        genes=path.split("/")
        gene=genes[-1]
        for num in range(1,5):
            try:
                with open(f'{path}/clade{num}/absrel.log',encoding='utf-8')as log:
                    logs=reversed(log.readlines())
                    for line in logs:
                        if line[0]=="*":
                            part=line.split(',')
                            if part[0][2:6]=='Node':
                                with open('dpj_gene.psg','a')as result:
                                    result.write(f'{gene}\tclade{num}\t{part[0][1:]}\t{part[1]}\n')
                        else:
                            break
            except:
                FileNotFoundError
                pass

