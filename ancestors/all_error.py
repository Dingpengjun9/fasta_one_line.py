#提取所有local——error

import os
all_error={}
ars="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR"
#ars="C:/Users/dingdingche/Desktop/ASR/"
for i in range(0,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        for n in range(1,5):
            error=[]
            if os.path.exists(f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_test"):
                with open (f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_test") as test:
                    lines=test.readlines()
                    for line in lines:
                        if "error_win_num:  0" in line :
                            name=line.split(" ")[0]
                            error.append(name)
                            all_error[f'{filename}-clade{n}']=error


filtrate="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/filtrate"
with open(f'{filtrate}/all_spe_node.fa','w',encoding="utf-8") as out:
    for key, value in all_error.items():
        aa=str(value).replace("'","").replace("[","").replace("]","")
        out.write(f'{key.split("-")[0]}\t{key.split("-")[1]}\t{aa.replace(" ","")}\n')


