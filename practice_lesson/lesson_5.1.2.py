import os
path = r'E:/BGI/New Folder/data/pep'
filenames = os.listdir(path)
for filename in filenames:
    num=filename[-6:-4]
    with open(f'E:/BGI/New Folder/data/pep/cflo.pep.{num}.sh',"w",encoding="utf-8") as sh:
        sh.write(f'python script1.py Cflo.pep.{num} >Cflo.pep.{num}.out')

