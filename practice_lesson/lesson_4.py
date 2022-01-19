import sys

#读取gff、fasta文件
cflo_gff_location=sys.argv[1]
cm_fasta_location=sys.argv[2]
gene_outfile=sys.argv[3]
protein_outfile=sys.argv[4]
#cflo_gff_location='E:/BGI/New Folder/data/cflo_v3.3.gff/cflo_v3.3.gff'
#cm_fasta_location='E:/BGI/New Folder/data/cm.fa/cm.fa'
with open(cflo_gff_location) as cflo_gffs:
    cf_gff=cflo_gffs.readlines()
with open(cm_fasta_location) as cm:
    cm_fa=cm.readlines()


a=''
name=''
cm_fas={}
for line in cm_fa:
    if line[0]== ">":
        cm_fas[name] = a.replace('\n', '')
        name=line[:-1]
        a = ''
    else:
        a=a+line
cm_fas[name] = a.replace('\n', '')
del cm_fas['']


negative={"A":"T","C":"G","G":"C","T":"A","N":"N"}
b=''
gene={}
seq=''
for cflo in cf_gff:
    cflo_splits=cflo.split('\t')
    sca,ty,star,end,gene_name,neg=f'>{cflo_splits[0]}',cflo_splits[2],cflo_splits[3],cflo_splits[4],cflo_splits[8][7:],cflo_splits[6]
    if neg=="+":
        if gene_name==b:
            if ty =='CDS':
                seq=cm_fas[sca][int(star)-1:int(end)]
                gene[b]="".join([gene[b],seq])
        else:
            if gene_name[0]=='C':
                b=gene_name
                seq=''
                seq = seq + cm_fas[sca][int(star)-1:int(end) ]
                gene[b] =seq
    if neg =="-":
        if gene_name==b:
            if ty =='CDS':
                seq=cm_fas[sca][int(star)-1:int(end)]
                for seqs in seq:
                    seq_t=''.join([negative[seqs],seq_t])
                gene[b]="".join([seq_t,gene[b]])
                seq_t=''
        else:
            if gene_name[0]=='C':
                b=gene_name
                seq=''
                seq_t=''
                seq = seq + cm_fas[sca][int(star)-1:int(end) ]
                for seqs in seq:
                    seq_t=''.join([negative[seqs],seq_t])
                gene[b] =seq_t
                seq_t=''


gene_fa=open(gene_outfile,"w",encoding="utf-8")
for k,v in gene.items():
    gene_fa.write(">"+str(k[:-2])+"\n")
    gene_fa.write(str(v)+"\n")


standard ={
        'GCA' : 'A', 'GCC' : 'A', 'GCG' : 'A', 'GCT' : 'A',                      		  # Alanine
        'TGC' : 'C', 'TGT' : 'C',                                                           # Cysteine
        'GAC' : 'D', 'GAT' : 'D',                                                           # Aspartic Acid
        'GAA' : 'E', 'GAG' : 'E',                                                           # Glutamic Acid
        'TTC' : 'F', 'TTT' : 'F',                                                           # Phenylalanine
        'GGA' : 'G', 'GGC' : 'G', 'GGG' : 'G', 'GGT' : 'G',                               # Glycine
        'CAC' : 'H', 'CAT' : 'H',                                                           # Histidine
        'ATA' : 'I', 'ATC' : 'I', 'ATT' : 'I',                                             # Isoleucine
        'AAA' : 'K', 'AAG' : 'K',                                                           # Lysine
        'CTA' : 'L', 'CTC' : 'L', 'CTG' : 'L', 'CTT' : 'L', 'TTA' : 'L', 'TTG' : 'L',   # Leucine
        'ATG' : 'M',                                                                         # Methionine
        'AAC' : 'N', 'AAT' : 'N',                                                           # Asparagine
        'CCA' : 'P', 'CCC' : 'P', 'CCG' : 'P', 'CCT' : 'P',                               # Proline
        'CAA' : 'Q', 'CAG' : 'Q',                                                           # Glutamine
        'CGA' : 'R', 'CGC' : 'R', 'CGG' : 'R', 'CGT' : 'R', 'AGA' : 'R', 'AGG' : 'R',   # Arginine
        'TCA' : 'S', 'TCC' : 'S', 'TCG' : 'S', 'TCT' : 'S', 'AGC' : 'S', 'AGT' : 'S',   # Serine
        'ACA' : 'T', 'ACC' : 'T', 'ACG' : 'T', 'ACT' : 'T',                               # Threonine
        'GTA' : 'V', 'GTC' : 'V', 'GTG' : 'V', 'GTT' : 'V',                               # Valine
        'TGG' : 'W',                                                                         # Tryptophan
        'TAC' : 'Y', 'TAT' : 'Y',                                                           # Tyrosine
        'TAA' : '', 'TAG' : '', 'TGA' : ''                                              # Stop
        }
protein=''
n=0
protein_fa=open(protein_outfile,"w",encoding="utf-8")
for k,v in gene.items():
    protein_fa.write(">"+str(k[:-2])+"\n")
    for n in range(0,len(v),3):
        try:
            code=v[n:n+3]
            pro = standard[code]
        except:
            pass
        protein="".join([protein,pro])
    protein_fa.write(str(protein)+"\n")
    protein = ''

