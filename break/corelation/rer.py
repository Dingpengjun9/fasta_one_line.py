import sys
import os
import re

gene_path=sys.argv[1]
trait_file=sys.argv[2]
out_file=sys.argv[3]
#trait_file="E:/beak/1dim\Measurement_data/ratio_log_bill_depth.txt"

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/shell/run{out_file}_r.sh","w")as out2:
    pass
with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/config/run{out_file}_r.tree", "w") as out3:
    pass

trait_d={}
with open(trait_file)as trait_f:
    trait_lines=trait_f.readlines()
    for trait_line in trait_lines:
        try:
            spe,trait=trait_line.strip().split("\t")
        except:
            spe, trait = trait_line.strip().split(" ")
        trait_d[spe]=trait

number_files=os.listdir(gene_path)
for number_file in number_files:
    gene_files=os.listdir(f"{gene_path}/{number_file}")
    for gene_file in gene_files:
        ome={}
        spe_names=''
        with open(f"{gene_path}/{number_file}/{gene_file}/{gene_file}.json.363node.rmOut.list")as omega_f:
        #with open(r"C:\Users\dingdingche\Desktop\GALGAL_R00076.json.363node.rmOut.rm0.rm1.rm5.list") as omega_f:
            omega_lines=omega_f.readlines()
            for omega_line in omega_lines:
                ospe,omega=omega_line.split("\t")[3],omega_line.split("\t")[2]
                ome[ospe] = omega
                if ospe in trait_d.keys():

                    spe_names+=f",{ospe}"
        if len(ome) <3:
            print(f"{gene_path}/{number_file}/{gene_file}/{gene_file}.json.363node.rmOut.rm0.rm1.rm5.list")
            continue
        spe_names=spe_names.strip(",")
        tree_command=f"/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/zsy/01.bin/tree_doctor -P "+f"{spe_names} "\
                "-n /jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/zsy/02.config/time.tree > " \
                 f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/config/rer_{out_file}.tree| sh"
        os.system(tree_command)

        with open (f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/config/rer_{out_file}.tree")as tree_f:
        #with open(f"C:/Users/dingdingche/Desktop/sp362.tree") as tree_f:
            oor_tree=tree_f.read()
            or_tree=oor_tree.strip("\n")
            or_tree = re.sub(r':\d+\.?\d*[e-]*\d*', "", or_tree)
            for kk,vv in ome.items():
                or_tree=re.sub(f'{kk}:?\d*\.?\d*', f"{kk}:{vv}", or_tree)
            #or_tree = re.sub(r'Node\d+', "", or_tree)

        with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/config/run{out_file}_r.tree", "a") as out3:
            out3.write(f"{gene_file}\t{or_tree}\n")

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/shell/run{out_file}_r.sh","a")as out2:
    out2.write(f"Rscript /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/rer.r "
                f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/06.rer/config/run{out_file}_r.tree "
                f"{trait_file}\n")


#/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/zsy/02.config/time.tree



