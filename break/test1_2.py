import os
ccs=["03","07","11","16","22"]
zsy="/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/test"
pl="/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/egg_mass/bin/tree_avg_branchlen.pl"

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/test/config/run1_2.sh","a",encoding="utf-8")as out:
    pass
filenames = os.listdir(rf"{zsy}")
for filename in filenames:
    for cc in ccs:
        for ii in range(1,6):
            with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/test/config/run1_2.sh","a",encoding="utf-8")as out:
                out.write(f"gzip -d {zsy}/{filename}/{cc}/{ii}/VarRates.Output.trees.gz && perl {pl} {zsy}/{filename}/{cc}/{ii}/VarRates.Output.trees > {zsy}/{filename}/{cc}/{ii}/mean.tree\n")