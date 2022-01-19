import sys
file_name=sys.argv[1]
location=sys.argv[2]
sub_long=sys.argv[3]

trans= {"A":"G","G":'A','T':'C',"C":'T','-':'A'}


n=0
a=0
b=0
sub=0
file_data=''
with open(file_name)as f:
    lines=f.readlines()
    for line in lines:
        if line[0]==">":
            if line==">Gallus_gallus\n":
                a=1
                name=line
            else:
                a=0
                b=0

        if a==1:
            for bp in line :
                if bp!="\n":
                    n+=1
                    b=1
                    if n==int(location)+len(name)-1:
                        sub=1
                    if n==int(sub_long)+len(name):
                        sub=0
                    if sub==1:
                        bp=trans[bp]
                file_data+=bp
        else:
            file_data+=line
            if a==0 and b==1:
                print("too long")
                b=0

with open(f'{file_name}_trans_Gallus_gallus_{location}_{sub_long}',"w",encoding="utf-8")as out:
    out.write(file_data)

