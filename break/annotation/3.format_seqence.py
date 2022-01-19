import sys
gene_list=sys.argv[1]
fa_file=sys.argv[2]
out_file=sys.argv[3]
sp=sys.argv[4]

trans={}
with open(gene_list)as gene_list_f:
    gene_list_lines=gene_list_f.readlines()
    for gene_line in gene_list_lines:
        gene,ens=gene_line.strip("\n").split("\t")
        if ens=="NA":
            pass
        else:
            long_name=f"{sp}_{gene}"
            trans[ens]=long_name

sequences={}
with open(fa_file)as fa_f:
    fa_lines=fa_f.readlines()
    for fa_line in fa_lines:
        if fa_line[0]==">":
            seq=""
            seq_name=fa_line.strip(">").strip("\n")
        else:
            seq+=fa_line.strip("\n")
            sequences[seq_name]=seq

with open(out_file,"w")as out_f:
    for k in sequences.keys():
        out_f.write(f">{trans[k]}\n{sequences[k]}\n")





