import sys
import os
path=sys.argv[1]
rr=sys.argv[2]
with open(f"{path}/run_R.sh","w",encoding="utf-8")as of1:
    pass

filenames=os.listdir(path)
for filename in filenames:
    if os.path.isdir(f"{path}/{filename}"):
        files=os.listdir(f"{path}/{filename}")
        for file in files:
            if os.path.isdir(f"{path}/{filename}/{file}"):
                with open(f"{path}/run_R.sh","a",encoding="utf-8")as of1:
                    of1.write(f"cd {path}/{filename}/{file} && Rscript {rr} {path}/{filename}/{file} {path}/{filename}\n")


