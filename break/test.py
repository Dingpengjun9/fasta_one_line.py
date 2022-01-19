import sys
infile=sys.argv[1]
outfile=sys.argv[2]

bayes="/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/egg_mass/software/BayesTraitsV3.0.2/BayesTraitsV3"
config="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/test/config"
with open (f"{outfile}","w",encoding="utf-8")as out:
    pass

with open (f"{infile}")as ain:
    alines=ain.readlines()
    for aline in alines:
        path =aline.strip("\n")
        name=path.split("/")[-1].strip("\n")
        dirr=f"/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/test/{name}"
        with open (f"{outfile}","a",encoding="utf-8")as aout:
            for nn in range(1,6) :
                aout.write(f"mkdir -p {dirr}/03/{nn} && cd {dirr}/03/{nn} && {bayes} {path}/tree.nexus {path}/trait.txt < {config}/VarRates03.txt && gzip VarRates.Output.trees\n")
                aout.write(f"mkdir -p {dirr}/07/{nn} && cd {dirr}/07/{nn} && {bayes} {path}/tree.nexus {path}/trait.txt < {config}/VarRates07.txt && gzip VarRates.Output.trees\n")
                aout.write(f"mkdir -p {dirr}/11/{nn} && cd {dirr}/11/{nn} && {bayes} {path}/tree.nexus {path}/trait.txt < {config}/VarRates11.txt && gzip VarRates.Output.trees\n")
                aout.write(f"mkdir -p {dirr}/16/{nn} && cd {dirr}/16/{nn} && {bayes} {path}/tree.nexus {path}/trait.txt < {config}/VarRates16.txt && gzip VarRates.Output.trees\n")
                aout.write(f"mkdir -p {dirr}/22/{nn} && cd {dirr}/22/{nn} && {bayes} {path}/tree.nexus {path}/trait.txt < {config}/VarRates22.txt && gzip VarRates.Output.trees\n")
