import sys
import os

gene_path=sys.argv[1]
trait_file=sys.argv[2]
out_file=sys.argv[3]
#trait_file="E:/beak/1dim\Measurement_data/ratio_log_bill_depth.txt"

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/shell/run{out_file}_r.sh","w")as out2:
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

        #input_txt=["spe","trait","omega"]
        input_txt = "specie\ttrait\tomega\n"
        spe_names=''
        with open(f"{gene_path}/{number_file}/{gene_file}/{gene_file}.json.363node.rmOut.rm0.rm1.rm5.list")as omega_f:
        #with open(r"C:\Users\dingdingche\Desktop\GALGAL_R00076.json.363node.rmOut.rm0.rm1.rm5.list") as omega_f:
            omega_lines=omega_f.readlines()
            for omega_line in omega_lines:
                ospe,omega=omega_line.split("\t")[1],omega_line.split("\t")[2]
                if ospe in trait_d.keys():
                    #input_txt=input_txt+[ospe,trait_d[ospe],omega]
                    input_txt = input_txt + f"{ospe}\t{trait_d[ospe]}\t{omega}\n"
                    spe_names+=f",{ospe}"
        spe_names=spe_names.strip(",")
        tree_command=f"mkdir -p /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/gene_new/{number_file}/{gene_file}/&& "\
                     "/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/zsy/01.bin/tree_doctor -P "+f"{spe_names} "\
                "-n /hwfssz5/ST_EARTH/P18Z10200N0100/dengyuan/00.birds/tree/63k_tree/ASTRAL.63430.species.reroot.sort.tree > " \
                 f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/gene_new/{number_file}/{gene_file}/{gene_file}_{out_file}.tree| sh"
        os.system(tree_command)

        with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/gene_new/{number_file}/{gene_file}/{gene_file}_{out_file}.txt","w")as out:
            out.write(input_txt)
        with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/shell/run{out_file}_r.sh","a")as out2:
            out2.write(f"Rscript /jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/pGLS.r "
                       f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/gene_new/{number_file}/{gene_file}/{gene_file}_{out_file}.tree "
                       f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/05.pgls/gene_new/{number_file}/{gene_file}/{gene_file}_{out_file}.txt\n")






