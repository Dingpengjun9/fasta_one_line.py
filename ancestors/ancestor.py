import os
hyphy="/hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/HYPHYMP"
fit="/hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/tests/hbltests/libv3/support/FitMG94.bf"
new_route="/hwfssz5/ST_DIVERSITY/B10K/USER/chenwanjun/1.b10k/09.global_selection_analysis/run/run363/hyphy_363_global_out"
gene_list="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/1.new_positive/gene.list"
ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR"

for i in range(0,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{new_route}/{num}")
    for filename in filenames:
        with open(gene_list,"a",encoding="utf-8")as file:
            file.write(f'{new_route}/{num}/{filename}/sp363\n')


with open (gene_list) as f:
    lines=f.readlines()
    for line in lines:
        part=line.split("/")
        with open ('/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/1.new_positive/01.rebuild_ancestor/fit_all.sh',"a",encoding="utf-8")as o:
            o.write(f'{hyphy} {fit} CPU=1 --alignment {line.strip()}/{part[-2]}_sp363.fasta-gb.fna '
                    f'--output {ars}/{part[-3]}/{part[-2]}/{part[-2]}_sp363_fit.json >{ars}/{part[-3]}/{part[-2]}/fit.log '
                    f'--save-fit {ars}/{part[-3]}/{part[-2]}/{part[-2]}_sp363.fit '
                    f'&& /hwfssz5/ST_DIVERSITY/B10K/PUB/USER/chenwanjun/local/software/hyphy/hyphy-2.5.31/HYPHYMP /hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/5.ancestor_test/AncestralSequences.bf '
                    f'--fit {ars}/{part[-3]}/{part[-2]}/{part[-2]}_sp363.fit --output {ars}/{part[-3]}/{part[-2]}/ancestor.json \n')
