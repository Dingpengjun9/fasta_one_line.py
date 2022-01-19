n=0
long=0
a=0
t=0
c=0
g=0
nn=0
with open("E:/BGI/New Folder/data/test.fq/test.fq") as fq:
    lines=fq.readlines()
    for line in lines:
        n+=1
        if n%4==2:
            long+=len(line.strip())
            for bp in line:
                if bp =="A":
                    a += 1
                if bp =="C":
                    c += 1
                if bp == "T":
                    t += 1
                if bp == "G":
                    g += 1
                if bp =="N":
                    nn += 1
print(f'{int(n/4)} reads')
print(f'{long} bp')
print(f"A:{a}")
print(f"C:{c}")
print(f"G:{g}")
print(f"T:{t}")
print(f"N:{nn}")