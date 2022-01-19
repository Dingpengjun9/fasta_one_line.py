import re

gc = 0
scaffold = {}
scaffold_seq = {}
scaffold_cg = {}
scaffold_long = {}
total_long = 0
total_loc = 0
with open("E:/BGI/New Folder/data/cm.fa/cm.fa") as f:
    for block in f.read().split(">"):
        block_strip = block.replace('\n', '')
        try:
            if block_strip[0] == "s":
                sca_name = re.search("scaffold\d+", block_strip).group()

            elif block_strip[0] == 'C':
                sca_name = re.search("C\d+", block_strip).group()
        except:
            pass
        # 序列
        seq = block_strip.lstrip(sca_name)
        scaffold_seq[sca_name] = seq
        # 长度
        long = len(seq.strip())
        scaffold_long[sca_name] = long
        total_long += long
        # CG
        for bp in seq:
            if bp == 'C' or 'G':
                gc += 1
        scaffold_cg[sca_name] = gc
        # 酶切位点
        loc = seq.count('CCGGTCGACCGG')
        total_loc += loc
