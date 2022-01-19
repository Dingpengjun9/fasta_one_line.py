#依据蛋白质序列信息和gtf文件，提取相应蛋白质序列
import sys
gene_list_file=sys.argv[1]
gtf_file=sys.argv[2]
fa_file=sys.argv[3]
species=sys.argv[4]

#gene_list_file="C:/Users/dingdingche/Desktop/gene_list.txt"
#gtf_file="C:/Users/dingdingche/Desktop/Gallus_gallus.GRCg6a.104.gtf"
#fa_file="C:/Users/dingdingche/Desktop/Gallus_gallus.GRCg6a.pep.all.fa"

#1.读取基因列表，并转为大写
gene_list=[]
with open (gene_list_file) as gene_list_f:
    gene_list_lines=gene_list_f.readlines()
    for gene_list_line in gene_list_lines:
        gene=gene_list_line.strip("\n").upper()
        gene_list.append(gene)

#读取gtf文件，并提取相应最长转录本名称
trans_id={}
trans_length={}
with open(gtf_file) as gtf_f:
    gtf_lines=gtf_f.readlines()
    for gtf_line in gtf_lines:
        if gtf_line[0]=="#":
            pass
        else:
            type=gtf_line.split("\t")[2]
            if type == "transcript":
                start,end,attributes=int(gtf_line.split("\t")[3]),int(gtf_line.split("\t")[4]),gtf_line.split("\t")[-1]
                transcript_length=end-start
                gene_name,transcript_id=attributes.split(";")[4].split('"')[1],attributes.split(";")[2].split('"')[1]
                if gene_name.upper() in gene_list:
                    if gene_name not in trans_id.keys():
                        trans_id[gene_name]=transcript_id
                        trans_length[gene_name]=transcript_length
                    elif gene_name.upper() in gene_list:
                        if int(transcript_length) > int(trans_length[gene_name]):
                            trans_id[gene_name] = transcript_id
                            trans_length[gene_name] = transcript_length
                        else:
                            pass
#从fa文件中提取相应蛋白序列
record=False
trans_seq={}
with open(fa_file)as fa_f:
    fa_lines=fa_f.readlines()
    for fa_line in fa_lines:
        if fa_line[0] ==">":
            if record:
                trans_seq[trans_name] = seq
            record=False
            seq = ""
            trans_name=fa_line.split("transcript:")[1].split(".")[0]
            if trans_name in trans_id.values():
                record=True
        else:
            if record :
                seq += fa_line.strip("\n")
    if record:
        trans_seq[trans_name] = seq

with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/02.annotation/reference/{species}_seq.fa","w",encoding='utf-8') as out1:
    for k,v in trans_seq.items():
        out1.write(f">{k}\n{v}\n")
with open(f"/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/2.beak/02.annotation/reference/{species}_pair.fa","w",encoding='utf-8') as out2:
    for gene_n in gene_list:
        if gene_n in trans_id.keys():
            out2.write(f"{gene_n}\t{trans_id[gene_n]}\n")
        else:
            out2.write(f"{gene_n}\tNA\n")


