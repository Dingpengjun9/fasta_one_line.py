import os

ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
#ars="E:/Test/ASR/"
with open (f"{ars}rm_clade.sh","w",encoding='utf-8')as sh:
    pass
for i in range(1,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        for n in range(1,5):
            with open (f"{ars}rm_clade.sh","a",encoding='utf-8')as sh:
                sh.write(f"rm -r {ars}{num}/{filename}/clade{n}\n")