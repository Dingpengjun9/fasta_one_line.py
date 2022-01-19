import os
filenames=os.listdir("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/config/data")
path='/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape'
with open (f"{path}/shell/run_bayes.sh","w")as out1:
    pass


if 1==1:
    n=0
    for i in range(1,9):
        n+=0.5
        inter=int(n*100000000)
        burn=int(inter*0.1)
        for filename in filenames:
            for ii in range(1,6):
                with open (f"{path}/shell/run_bayes.sh","a")as out1:
                    out1.write(f"mkdir -p {path}/result/{filename}/{n}/{ii} && cd {path}/result/{filename}/{n}/{ii} &&"
                               f" /jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/egg_mass/software/BayesTraitsV3.0.2/BayesTraitsV3"
                               f" {path}/config/sp362_nex.tree {path}/config/data/{filename}"
                               f" < {path}/config/var/VarRates_{n}.txt\n")
        with open(f"{path}/config/var/VarRates_{n}.txt","w")as out2:
            out2.write(f"7\n2\nVarRates\nBurnin {burn}\nIterations {inter}\nLogFile VarRates\nRun")
