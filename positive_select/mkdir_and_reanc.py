import os
import re

hyphy="/hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/HYPHYMP"
fit="/hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/tests/hbltests/libv3/support/FitMG94.bf"
filenames = os.listdir(rf"/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/1.new_positive/01.rebuild_ancestor/fit_all.sh.7158.qsub")
filename=str(filenames)

with open("/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/1.new_positive/01.rebuild_ancestor/add_dir.sh", "w",encoding="utf-8") as sh:
    pass


names=re.findall(fr"work_\d+.sh.e\d+",filename)
for name in names:
    with open(f"/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/1.new_positive/01.rebuild_ancestor/fit_all.sh.7158.qsub/{name}") as file:
        lines=file.readlines()
        if lines != "":
            for line in lines:
                try:
                    dir_name=line.split(":")[2][:-8]
                    gene_name=line.split("/")[-2]
                    #os.makedirs(dir_name)
                except:
                    print(f"{name}\t{line}")
                with open("/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/1.new_positive/01.rebuild_ancestor/add_dir.sh","a",encoding="utf-8") as sh:
                    sh.write(f'mkdir -p {dir_name} && '
                             f'{hyphy} {fit} CPU=1 --alignment /hwfssz5/ST_DIVERSITY/B10K/USER/chenwanjun/1.b10k/09.global_selection_analysis/run/run363/hyphy_363_global_out/{dir_name.split("/")[-2]}/{dir_name.split("/")[-1]}/sp363/{gene_name}_sp363.fasta-gb.fna '
                        f'--output {dir_name}/{gene_name}_sp363_fit.json >{dir_name}/fit.log '
                        f'--save-fit {dir_name}/{gene_name}_sp363.fit '
                        f'&& /hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/HYPHYMP /hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/5.ancestor_test/AncestralSequences.bf '
                        f'--fit {dir_name}/{gene_name}_sp363.fit --output {dir_name}/ancestor.json \n')

'''
n=7
aa="work_00007.sh.e302456"
b=fr"work_0000{n}.sh.e\d+"
name=re.search(b,aa).group()
'''