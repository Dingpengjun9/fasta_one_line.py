for n in range(1,100):

    num=str(n)
    file_name=f"E:/BGI/New Folder/data/pep/clfo.pep.{num}"
    out={}
    with open(file_name) as file:
        pep=file.readlines()
        for line in pep:
            if line[0]==">":
                name=line
            if line[0]=='M':
                out[name]=line
    with open(f"E:/BGI/New Folder/data/pep/clfo.pep.{num}.out","w",encoding="utf-8") as out_file:
        for k,v in out.items():
            out_file.write(str(k))
            out_file.write(str(v))



