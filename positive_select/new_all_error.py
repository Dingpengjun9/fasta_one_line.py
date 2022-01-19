#提取所有local——error

import os
all_error={}
#ars="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/100.c-dingpengjun/ASR/"
ars="E:/Test/ASR/"
for i in range(0,1):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        if 1==1:
            error=[]
            if os.path.exists(f"{ars}{num}/{filename}/{filename}_test"):
                with open (f"{ars}{num}/{filename}/{filename}_test") as test:
                    lines=test.readlines()
                    for line in lines:
                        if "error_win_num:  0" in line :
                            name=line.split(" ")[0]
                            error.append(name)
                            all_error[f'{filename}']=error


filtrate="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/1.new_positive/02.count"
with open(f'{ars}/all_positive.fa','w',encoding="utf-8") as out:##################################
    for key, value in all_error.items():
        aa=str(value).replace("'","").replace("[","").replace("]","")
        out.write(f'{key}\t{aa.replace(" ","")}\n')


