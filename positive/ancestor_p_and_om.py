import json

with open('C:/Users/dingdingche/Desktop/GALGAL_R00001_clade1.fasta-gb.fna.ABSREL.json')as f:
    js=json.load(f)
    for key in js['ancestral_sequences']:
        if key!='root':
            with open("ancestor_fa","a")as fa:
                pass


