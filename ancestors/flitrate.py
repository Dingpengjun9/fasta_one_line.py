#将正选择中含有local_error的物种删掉
import sys
positive_file=sys.argv[1]
error_file=sys.argv[2]

#positive_file='C:/Users/dingdingche/Desktop/ASR/all_error11.fa'
#error_file='C:/Users/dingdingche/Desktop/ASR/all_error.fa'


po_spec={}
with open(positive_file) as po_file:
    po_lines=po_file.readlines()
    for po_line in po_lines:
        gene,clade,spec=po_line.split("\t")[0],po_line.split("\t")[1],po_line.split("\t")[2].strip("\n")
        po_clade=f'{gene}-{clade}'
        po_spec[po_clade]=spec+","

error_gene={}
er_spec={}
with open(error_file) as er_file:
    er_lines=er_file.readlines()
    for er_line in er_lines:
        error=[]
        gene,clade,spec=er_line.split("\t")[0],er_line.split("\t")[1],er_line.split("\t")[2].strip("\n")
        er_clade=f'{gene}-{clade}'
        gene_lists=spec.split(",")
        try:
            for gene_list in gene_lists:
                if gene_list in po_spec[er_clade].split(","):
                    po_spec[er_clade]=po_spec[er_clade].replace(f"{gene_list},","")
                    po_spec[er_clade]=po_spec[er_clade].replace(",,",",")
                    error.append(gene_list)
                    error_gene[er_clade]=error
        except:
            pass

with open('/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/filtrate/new_filtrate_positive.psg','w',encoding="utf-8") as result:
    for key,value in po_spec.items():
        result.write(f'{key.split("-")[0]}\t{key.split("-")[1]}\t{value.strip(",")}\n')


with open('/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/filtrate/new_false_positive.psg','w',encoding="utf-8") as out:
    for key,value in error_gene.items():
        aa = str(value).replace("'", "").replace("[", "").replace("]", "")
        out.write(f'{key.split("-")[0]}\t{key.split("-")[1]}\t{aa.replace(" ","")}\n')
