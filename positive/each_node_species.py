gene_path={}
with open("/hwfssz5/ST_DIVERSITY/B10K/USER/dengyuan/05.brain_size/positive_selection/hyphy/nodes/gene.list")as file:
    lists=file.readlines()
    for list in lists:
        list_sp=list.split("\t")
        path=list_sp[1]
        genes=path.split("/")
        gene=genes[-1]
        gene_path[gene]=path

with open('each_node_species.psg','w',encoding="utf-8")as out_file:
    out_file.write(f'#gene\tclade\tNode\tp-value\tspecies\n')
import re
import json
import sys
nodelist=sys.argv[1]

with open(nodelist) as node_lists:
    node_lists_lines = node_lists.readlines()
    for node_lists_line in node_lists_lines:
        if node_lists_line[0]=="#":
            pass
        else:
            node_lists_part = node_lists_line.split("\t")
            gene_name,clade,node,p_value=node_lists_part[0],node_lists_part[1],node_lists_part[2].strip(),node_lists_part[3].strip()
            with open(f'{gene_path[gene_name]}/{clade}/{gene_name}_{clade}.fasta-gb.fna.ABSREL.json')as f:
                json_f=json.load(f)
                n = 0
                lnum = 0
                rnum = 0
                spe=[]

                tree=json_f['input']['trees']['0']
                tree_parts=tree.split(")")
                for tree_part in tree_parts:
                    n+=1
                    if tree_part[:len(node)]==node:
                        num=n
                        break
                n=0
                for aa in tree:
                    n+=1
                    if aa==")":
                        rnum+=1
                        if rnum==num-1:
                            stop=n
                            break
                n = 0
                rnum=0
                piece=tree[:stop]
                re_piece=piece[::-1]

                for aa in re_piece:
                    n+=1
                    if aa ==")":
                        rnum+=1
                    if aa=="(":
                        lnum+=1
                        if lnum==rnum:
                            start=n
                            n=0
                            lnum=0
                            rnum=0
                            break
                block=piece[-start:]
                species=re.findall(r"\w+_\w+",block)
                specie=str(species)[1:-1].replace('\'','')
                with open('each_node_species.psg', 'a')as result:
                    result.write(f'{gene_name}\t{clade}\t{node}\t{p_value}\t{specie}\n')



