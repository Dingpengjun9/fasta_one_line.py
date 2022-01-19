import os
psg=False
path="/jdfssz1/ST_EARTH/P18Z10200N0100/dingpengjun/gene"

filenames=os.listdir(path)
for filename in filenames:
    a, b = 0, 0
    if os.path.isdir(f"{path}/{filename}"):
        for i in range(1,7):
            print(f"{filename}")
            with open (f"{path}/{filename}/{i}/h1/h1.mlc") as h1:
                h1lines=h1.readlines()
                for h1line in h1lines:
                    if psg:
                        if "." not in h1line:
                            psg=False
                        if "." in h1line:
                            pass
                            #print(h1line.strip("\n"))
                    if "Positive sites for foreground lineages Prob" in h1line:
                        psg=True
                    if "lnL" in h1line:
                        h1num=h1line.split(":")[3].split(".")[0].strip()
            with open(f"{path}/{filename}/{i}/h0/h0.mlc") as h0:
                h0lines = h0.readlines()
                for h0line in h0lines:
                    if "lnL" in h0line[:3]:
                        h0num=h0line.split(":")[3].split(".")[0].strip()
            num =2*int(h1num)-2*int(h0num)
            if num<3.845:
                print(f"{i} error {int(h1num)}-{int(h0num)} {num}")
                a+=1
            if num >= 3.845:
                print(f"{i} ok {int(h1num)}-{int(h0num)} {num}")
                b+=1
    print("########")
    print(f"error :{a}")
    print(f"ok : {b}")