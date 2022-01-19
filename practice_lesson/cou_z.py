seq=''
file_name='E:/BGI/New Folder/data/cm.fa/cm.fa'
with open(file_name) as fasta:
    lines=fasta.readlines()
    for line in lines:
        seq+=line.strip()

def ww(a,b):
    aa=int(a)+int(b)
    print(aa)
def www(aa):
    ee=aa*aa
    return ee
a=1
b=2
ww(a,b)