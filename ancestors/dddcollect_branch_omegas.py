#!/usr/bin/env
# we need the omega values to associate the selection pressure with traits
# here use the hyphy omegas as dN/dS
import json
import sys
import os
from absrel_json import AbsrelJson
from pprint import pprint
import concurrent.futures
from plot_alignment_slidingwindown_pairwiseIdent import calc_sliding_window_pairwise_identity, calc_overlaping_sliding_window_pairwise_identity

from Bio import AlignIO
import numpy as np
import pandas as pd

# get the all branch attributes
# clade info
##################################
# read in the clade species
##################################
def get_4clade_species(clade_f,clade,ances):          #制作每个clade所含物种的字典
    # input and clade species file
    # return a dict of clade species
    try:
        with open(ances) as ance_js:
            aance=json.load(ance_js)
    except:
        aance=[]

    clade_sps_dt = {}
    with open(clade_f) as f:
        for line in f:
            c,sps_str = line.rstrip().split(":")
            sps = sps_str.split(",")
            if c==clade:
                sps=sps+aance
            clade_sps_dt[c] = sps
    return clade_sps_dt
#clade_f = "../../../data/subclades/subclades_sps.txt"
#clade_f = "/home/c-dingpengjun/dingpengjun/ASR/000/GALGAL_R00001/clade1/subclades_sps.txt"
#clade_sps_dt = get_4clade_species(clade_f)
#pprint(clade_sps_dt)

def get_4clade_outgroup_species(clade_out_f):                          #输入每个clade的外群文件
    # input a clade out group files
    # return a dict with each clade's outgroup species used
    clade_in_sps_dt = {}
    with open(clade_out_f) as f:
        for line in f:
            line = line.rstrip()
            c, sps = line.split(" ")
            spsLst = sps.split(',')
            # here spsLst are the clade sps in other clades
            clade_in_sps_dt[c] = spsLst                                #把输入文件做成字典
    clade_out_sps_dt = {}
    # clade1 out  = clade2, clade3, clade4 in sps
    clades = list(clade_in_sps_dt.keys())
    for clade in clades:
        clade_out_sps = []
        for clade_in in clades:
            if clade_in != clade:
                clade_out_sps += clade_in_sps_dt[clade_in]
        clade_out_sps_dt[clade] = clade_out_sps                        #把每个clade外群之外的物种做成字典
    #pprint(clade_out_sps_dt)
    return clade_out_sps_dt

def get_4clade_ingroup_species(clade_sps_dt, clade_out_sps_dt):          #把每个clade不在其他物种外群的物种做成字典
    # input clade_sps_dt and clade_out_sps_dt of each clade
    # return only ingroup sps for each clade
    clade_in_sps_dt = {}
    for clade in clade_sps_dt:
        clade_in_sps = []
        for sp in clade_sps_dt[clade]:
            if sp not in clade_out_sps_dt[clade]:
                clade_in_sps.append(sp)
        clade_in_sps_dt[clade] = clade_in_sps
    return clade_in_sps_dt

#clade_out_f = "/hwfssz5/ST_DIVERSITY/B10K/USER/chenwanjun/1.b10k/09.global_selection_analysis/data/subclades/clade_outgroups.txt"
#clade_out_sps_dt = get_4clade_outgroup_species(clade_out_f)
#clade_in_sps_dt = get_4clade_ingroup_species(clade_sps_dt, clade_out_sps_dt)
#pprint(clade_in_sps_dt)

def filter_local_alignment_error(js, sp_pvalue_dt, clade_in_sps,ooo ,cutoff=0.5):
    # input a js, and all clade species tip pvalues
    # a dict store filtered by local alignment error check only for ingroup sps
    ingroup_sp_filtered_pvalue_dt = {}

    fna = js.get_input_alignment_file()
    fa = fna.replace(".fna","")
    # PSG species
    if os.path.isfile(ooo):
        print(ooo)
        aln = AlignIO.read(ooo,"fasta")
        pprint(sp_pvalue_dt)
        for sp in clade_in_sps:
            sp_pvalue = sp_pvalue_dt.get(sp, 'NA')
            print("In:",sp, sp_pvalue)
            if sp_pvalue != 'NA' and sp_pvalue < 0.05:
                print("#######")
                print(sp, sp_pvalue)
                # sp in ingroup and were test positive
                # non-overlaping pairwise identity matrix
                AlignIO.write(aln,"test,fasta","fasta")
                a = calc_sliding_window_pairwise_identity(aln, sp, 50)
                df = pd.DataFrame(a)
                print(df.shape)
                #pprint(a)
                # overlaping pairwise identity matrix
                a1 = calc_overlaping_sliding_window_pairwise_identity(aln, sp, 50)
                a1_df = pd.DataFrame(a1)
                #pprint(a1)
                df_median = np.median(df, axis=1)
                print(df_median)
                error_win_num = sum(df_median < cutoff)
                print(sp, "error_win_num: ",error_win_num)
                print("#########")


def handle_branch_attr(js, clade,ooo):
    # input an clade
    clade_sps = clade_sps_dt[clade]
    clade_out_sps = clade_out_sps_dt[clade]
    clade_in_sps = [sp for sp in clade_sps if sp not in clade_out_sps]
    # tips_attribu, tip only ,pvalue, omega, and rate_cat

    tips_attr_dt = js.get_branchAttributes()
    sp_pvalue_dt = {}
    sp_omega_dt = {}
    for sp in clade_sps:
        pvalue, omega, rate_cat = tips_attr_dt.get(sp, ("NA","NA","NA"))
        sp_pvalue_dt[sp] = pvalue
        sp_omega_dt[sp] = omega
    filter_local_alignment_error(js, sp_pvalue_dt, clade_in_sps,ooo)

    # return pvalues by the sorted species order
    pvalues = [ sp_pvalue_dt[sp] for sp in sorted(clade_sps) ]
    omegas =  [ sp_omega_dt[sp] for sp in sorted(clade_sps) ]

    return pvalues,omegas

# for each fa
# get to the hyphy out dir
# check if json file there and complete
# get the pvalue and branch omegas and also could do more local error filtering

# get the clade information to use data only in ingroup not outgroup
# and also consider PSGs in ingroup and not outgroup
# but how to compare the effect of this different handling???

def process_og(fa):
    # working function
    # input an fa, collect the hyphy pvalues and omegas
    ooo=fa
    og = os.path.basename(fa).split('_')[1]
    ogg=f"GALGAL_{og}"
    print(og)
    idx = int(og.replace("R",""))
    print(idx)
    folderID = "{:03d}".format(idx//200)
    ogDr = os.path.join(hyphyOutDr, folderID, ogg)
    # get clade from commandline
    #clade = "clade3"
    clade_sps = sorted(clade_sps_dt[clade])
    cladeDr = os.path.join(ogDr, clade)
    jsnFile = os.path.join(cladeDr, "{}_{}.fasta-gb.fna.ABSREL.json".format(ogg, clade))
    if os.path.isfile(jsnFile) and os.stat(jsnFile).st_size > 0:
        print(jsnFile)
        js = AbsrelJson(jsnFile)
        pvalues,omegas = handle_branch_attr(js, clade,ooo)
        pvaluesStr = ogg + ',' + ','.join(map(str, pvalues))
        omegasStr = ogg + ',' + ','.join(map(str,omegas))
        return pvaluesStr, omegasStr
    else:
        print("{} not have a completed ABSREL json file".format(fa), file=sys.stderr)

if __name__ == "__main__":

    faLstFile = sys.argv[1]
    clade = sys.argv[2]
    pppath=sys.argv[3]
    anc_js=sys.argv[4]

    clade_f = "/home/c-dingpengjun/dingpengjun/ASR/000/GALGAL_R00001/clade1/subclades_sps.txt"
    clade_sps_dt =get_4clade_species(clade_f,clade,anc_js)
    clade_out_f = "/hwfssz5/ST_DIVERSITY/B10K/USER/chenwanjun/1.b10k/09.global_selection_analysis/data/subclades/clade_outgroups.txt"
    clade_out_sps_dt = get_4clade_outgroup_species(clade_out_f)
    clade_in_sps_dt = get_4clade_ingroup_species(clade_sps_dt, clade_out_sps_dt)
    get_4clade_ingroup_species(clade_sps_dt, clade_out_sps_dt)

    clade_sps = sorted(clade_sps_dt[clade])
    hyphyOutDr = "/hwfssz5/ST_DIVERSITY/B10K/USER/chenwanjun/1.b10k/09.global_selection_analysis/run/run4_on_updated_cutoff_filter/hyphy_global_out"
    # get the jsonFile
    faLst = []
    with open(faLstFile) as f:
        faLst = f.read().rstrip().split("\n")

    pvalueLst = []
    omegaLst = []
    # use concurrent to run multithread to collect json files
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        res = executor.map(process_og, faLst)
    for r in res:
        #r not None
        if r:
            pvaluesStr,omegasStr = r
            pvalueLst.append(pvaluesStr)
            omegaLst.append(omegasStr)

    # output pvalues and omegas for clade tips
    pOutFile = f"{pppath}/{clade}.pvalues.summary"
    oOutFile = f"{pppath}/{clade}.omegas.summary"
    with open(pOutFile,"w") as POUT, open(oOutFile,"w") as OOUT:
        print("OG,"+",".join(clade_sps), file=POUT)
        print("\n".join(pvalueLst), file=POUT)

        print("OG,"+",".join(clade_sps), file=OOUT)
        print("\n".join(omegaLst), file=OOUT)

