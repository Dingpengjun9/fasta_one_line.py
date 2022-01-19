import os

hyphy="/hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/HYPHYMP"
asbf="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/6.test_gap/AncestralSequences.bf"
out_file="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/6.test_gap/"
ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
#ars="C:/Users/dingdingche/Desktop/ASR/"
for i in range(0,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        for n in range(1,5):
            fit=f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}.fit"
            output=f"{ars}{num}/{filename}/clade{n}/ancestor.json"
            sh=f"{hyphy} {asbf} --fit {fit} --output {output} >{ars}{num}/{filename}/clade{n}/ance.log"
            with open(f"{out_file}ancestor_gap.sh","a",encoding="utf-8")as out:
                out.write(f"{sh}\n")

