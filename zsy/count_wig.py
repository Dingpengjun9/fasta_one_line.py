import sys
import os
import re

duplication="/jdfssz1/ST_EARTH/P18Z10200N0100/zhangshiyan/duplication"
inf={}
input_file=sys.argv[1]
with open(input_file)as infile:
    lls=infile.readlines()
    for ll in lls:
        fn,sn=ll.split(" ")[0],ll.split(" ")[1].strip("\n")
        inf[sn]=fn

for son_node,father_node in inf.items():
    filenames = os.listdir(rf"{duplication}/{father_node}/{son_node}")
    with open(f"{duplication}/result.txt","w",encoding='utf-8') as out:
        pass

    for filename in filenames:
        wigs=os.listdir(rf"{duplication}/{father_node}/{son_node}/{filename}")
        for wig in wigs:
            n=-1
            pair={}
            sum=0
            gg = False
            with open(f"{duplication}/{father_node}/{son_node}/{filename}/{wig}") as file:
                lines=file.readlines()
                for line in lines:
                    n+=1
                    if line[0] =="f":
                        string=""
                        chrom=line.split(" ")[1].replace("chrom=","")
                    elif line[0] !="f":
                        line=line.rstrip("\n")
                        if int(line) > 1:
                            gg =True
                        if gg :
                            string += line
                            sum += int(line)
                            if len(string) > 4:
                                if re.match(r"[01]{5}",string[-5:]):
                                    gg=False
                                    string=string[:-5]
                                    if len(string) > 99:
                                        end =n-5
                                        sum=sum-5-int(string[-1])
                                        aver=int(sum)/len(string)
                                        average=('%.5f' % aver)
                                        start=int(end)-len(string)+1
                                        pair[start]=f"{str(end)}-{average}"
                                        string=""
                                        sum=0
                                    else:
                                        string=""
                                        sum=0
                                if n == len(lines) - 1:
                                    gg = False
                                    if len(string) > 99:
                                        for i in len(string):
                                            if string[-i] <2:
                                                sum=sum-string[-1]
                                        end = n
                                        aver = int(sum) / len(string)
                                        average = ('%.5f' % aver)
                                        start = int(end) - len(string) + 1
                                        pair[start] = f"{str(end)}-{average}"
                                        string = ""
                                        sum = 0
                                    else:
                                        string = ""
                                        sum = 0
            with open(f"{duplication}/result.txt","a",encoding='utf-8') as out:
                for k,v in pair.items():
                    stop,average_value=v.split("-")[0],v.split("-")[1]
                    long=int(stop)-int(k)+1
                    out.write(f"{son_node}\t{chrom}\t{k}\t{stop}\t{long}\t{average_value}\n")
for a in range(6):
    print(a)

a="a"
b="b"
b+=a