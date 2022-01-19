import sys
file=sys.argv[1]

ps_value={}
ars="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/ASR/"
with open(file)as input:
    llines=input.readlines()
    for lline in llines:
        part=lline.split(" ")[0]
        try:
            with open(f"{ars}{part}/pair.fa", encoding='utf-8') as fa:
                lines = fa.readlines()
                for line in lines:
                    value, node = int(line.split("\t")[-2]), line.split("\t")[-1].strip("\n")
                    if node in ps_value.keys():
                        ps_value[node] += value
                    elif node not in ps_value.keys():
                        ps_value[node] = value
        except FileNotFoundError:
            print(f"{part} not find")

path="/hwfssz5/ST_DIVERSITY/B10K/USER/dingpengjun/100.c-dingpengjun/8.convernode"
with open(f"{path}/positive_part2.fa","w",encoding="utf-8")as pofile:
    for key,value in ps_value.items():
        pofile.write(f"{key}\t{value}\n")