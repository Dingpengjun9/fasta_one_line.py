import os
import json

ancestorr=[]
ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
#ars="C:/Users/dingdingche/Desktop/ASR/"
for i in range(0,90):
    num="{:0>3d}".format(i)
    filenames = os.listdir(rf"{ars}{num}")
    for filename in filenames:
        for n in range(1,5):
            try:
                ancestorr = []
                with open (f"{ars}{num}/{filename}/clade{n}/ancestor.json") as js:
                    ancestor=json.load(js)
                    del ancestor['ancestral_sequences']["root"]

                    with open (f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_all_gap.fa","w",encoding="utf-8") as out:
                        for key,value in ancestor['ancestral_sequences'].items():
                            out.write(f">{key}\n")
                            out.write(f"{value}\n")
                            ancestorr.append(key)


                wanlaoshi="/hwfssz5/ST_DIVERSITY/B10K/USER/chenwanjun/1.b10k/09.global_selection_analysis/run/run4_on_updated_cutoff_filter/hyphy_global_out"
                #wanlaoshi="C:/Users/dingdingche/Desktop/wan"
                ti={}
                name=""
                seq=""
                with open (f"{wanlaoshi}/{num}/{filename}/clade{n}/{filename}_clade{n}.fasta-gb.fna")as tips_file:
                    tips=tips_file.readlines()
                    for tip in tips:
                        if tip[0]==">":
                            ti[name]=seq
                            name=tip
                            seq = ""
                        elif tip[0]=="(":
                            ti[name] = seq
                        else:
                            seq+=tip

                    del ti[""]

                with open (f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_all_gap.fa","a") as ance:
                    for key, value in ti.items():
                        ance.write(f"{key}")
                        ance.write(f"{value}")
                with open(f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_ancestor.json","w") as json_file:
                    json.dump(ancestorr,json_file)

                with open (f"{ars}{num}/{filename}/clade{n}/test.txt","w",encoding="utf-8") as txt:
                    txt.write(f"{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_all_gap.fa")
                with open (f"{ars}/test_all.sh","a")as sh:
                    sh.write(f"python /hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ars_py/dddcollect_branch_omegas.py "
                             f"{ars}{num}/{filename}/clade{n}/test.txt clade{n} {ars}{num}/{filename}/clade{n} {ars}{num}/{filename}/clade{n}/{filename}_clade{n}_ancestor.json "
                             f">{ars}{num}/{filename}/clade{n}/{filename}_clade{n}_test 2>{ars}{num}/{filename}/clade{n}/test.log\n")
            except:
                print(f"{filename}\tclade{n}")

