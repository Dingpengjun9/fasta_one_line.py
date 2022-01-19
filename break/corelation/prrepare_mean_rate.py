import os
with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/shell/run_mean_egg.sh","w")as out:
    pass
bill_p="/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/egg/05.trait/result"
bill_tree="/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/egg/02.config/egg_time.tree"
bill_das=os.listdir(bill_p)
for bill_da in bill_das:
    if os.path.isdir(f"{bill_p}/{bill_da}"):
        bill_file_name=bill_da.split(".")[0]
        bill_times =os.listdir(f"{bill_p}/{bill_da}")
        if True:
            trait_f=f"{bill_p}/{bill_da}/3.0/3/{bill_file_name}3.0_data.txt"
            if os.path.exists(trait_f):
                with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/shell/run_mean_egg.sh","a")as out:
                    out.write(f"module load python/3.10.0 && python /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/shell/tree_mean_rate.py "
                            f"{bill_tree} {trait_f} /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/config/egg.txt\n")
            else:
                print(trait_f)



'''
with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/shell/run_mean.sh","w")as out:
    pass
bill_p="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/result"
bill_tree="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/config/sp362_time.tree"
bill_das=os.listdir(bill_p)
for bill_da in bill_das:
    if os.path.isdir(f"{bill_p}/{bill_da}"):
        bill_file_name=bill_da.split(".")[0]
        bill_times =os.listdir(f"{bill_p}/{bill_da}")
        for bill_time in bill_times:
            trait_f=f"{bill_p}/{bill_da}/{bill_time}/3/{bill_file_name}_tree.txt"
            if os.path.exists(trait_f):
                with open("/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/shell/run_mean.sh","a")as out:
                    out.write(f"module load python/3.10.0 && python /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/shell/tree_mean_rate.py "
                            f"{bill_tree} {trait_f} /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/03.shape/config/cc.txt\n")
            else:
                print(trait_f)
'''