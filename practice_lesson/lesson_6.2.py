with open("blast.sh","w",encoding="utf-8") as blast:
    for i in range(0,100):
        if i<10:
            blast.write(f"blastall -p blastp -i smer.pep0{i} -d merge.pep -m 8\n")
        else:
            blast.write(f"blastall -p blastp -i smer.pep{i} -d merge.pep -m 8\n")
