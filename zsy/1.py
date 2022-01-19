import os

aa={}
with open("/hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/nodes.txt")as file:
    lines=file.readlines()
    for line in lines:
        key,value=line.split("\t")[0],line.split("\t")[1].strip("\n")
        aa[key]=value

with open("/hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/duplication/out.sh","w",encoding="utf-8")as out:
    pass

with open("/hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/2.txt")as file:
    lines = file.readlines()
    for line in lines:
        names=line.split("/")[-1]
        name=names.split(".")[0]
        for tar,anc in aa.items():
            if anc==name:
                with open(line.strip())as in_file:
                    in_lines=in_file.readlines()
                    for in_line in in_lines:
                        in_name=in_line.split("\t")[0]
                        long=in_line.split("\t")[1]
                        nu=int(long)//1000000
                        num="{:0>3d}".format(nu)
                        if os.path.exists(f'/hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/duplication/{tar}/{num}'):
                            pass
                        else:
                            os.makedirs(f'/hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/duplication/{tar}/{num}')
                        with open("/hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/duplication/out.sh","a",encoding="utf-8")as out:
                            out.write(f"halAlignmentDepth /hwfssz5/ST_DIVERSITY/B10K/USER/fangqi/03.alignments/03.363birds/00.data/birds-final.hal {name} "
                                      f"--countDupes --targetGenomes {tar} --refSequence {in_name} "
                                      f"> /hwfssz5/ST_DIVERSITY/B10K/USER/zhangshiyan/duplication/{tar}/{num}/{name}.vs.{tar}.wig.{in_name}.wig "
                                      f"&& echo finish {name}.vs.{tar}.wig-{in_name}\n")

