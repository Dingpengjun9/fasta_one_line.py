#把上一lesson中得到的蛋白序列fasta文件(如名字叫Cflo.pep)，作为输入文件，编写一个脚本，把Cflo.pep切割成100个子文件，每个文件的序列条
# 数尽量相等，然后输出到一个叫split的目录下，子文件名可以是Cflo.pep.1、Cflo.pep.2、……、Cflo.pep.100。该perl脚本需要会自己判断split/目录
# 是否已经存在，如果不存在则自动创建。

#将某个文件切成序列条数相等的100份

import sys
import os
line=0
file_number=100
count=1
proteins=[]
input_file=sys.argv[1]
output_file=sys.argv[2]

#统计每个文件需要多少条序列
with open(input_file) as file:
    protein_read_file=file.read()
    number=protein_read_file.count('>')*2
    if number%file_number==0:
        part=number/file_number
        if part%2!=0:
            part-=1
    else:
        part = int(number / file_number)
        if part%2!=0:
            part-=1

#将文件切割并分到split目录下的100个文件内
with open('E:/BGI/New Folder/data/protein.fa') as file:
    protein_lines=file.readlines()
    for protein_line in protein_lines:
        line+=1
        proteins.append(protein_line)
        if line==part:
            try:
                with open(f'/split/{output_file}{count}.fa','w',encoding='utf-8')as out:
                    for protein in proteins:
                        out.write(protein)
            except:
                FileNotFoundError
                os.mkdir('/split')
                with open(f'/split/{output_file}{count}.fa', 'w', encoding='utf-8')as out:
                    for protein in proteins:
                        out.write(protein)
            line=0
            count+=1
            proteins=[]

