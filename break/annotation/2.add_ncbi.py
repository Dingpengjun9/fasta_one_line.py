import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with open("C:/Users/dingdingche/Desktop/new_ncbi_pair.fa","w")as out1:
    pass

browser=webdriver.Chrome("D:\Driver\chromedriver.exe")
browser.get("https://www.ncbi.nlm.nih.gov/protein/")


with open("C:/Users/dingdingche/Desktop/error_pair.fa",encoding="utf-8")as error:
    err_lines=error.readlines()
    for err_line in err_lines:
        back=True
        spes,gene=err_line.split(" ")[0],err_line.split(" ")[1]
        if spes=="Taeniopygia_guttata":
            sp="TAEGUT"
        if spes=="Gallus_gallus":
            sp="GALGAL"

        find = browser.find_element(By.NAME, "term")
        find.send_keys(f"({gene}[Gene Name]) AND {spes}[Organism] ")
        find.submit()
        try:
            error_names = browser.find_elements(By.TAG_NAME, "span")
            for i in error_names:
                if "No items found." in i.text:
                    with open("C:/Users/dingdingche/Desktop/new_ncbi_pair.fa","a",encoding="utf-8")as out1:
                        out1.write(f"{spes}\t{gene}\tNA\n")
                    reset = browser.find_element(By.CLASS_NAME, "reset")
                    reset.click()
                    back=False

            if back:
                fasta_b = browser.find_element(By.NAME,
                                               "EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.SequenceViewer.Sequence_ViewerTitle.ReportShortCut")
                fasta_b.click()
                time.sleep(10)
                fa_seq = browser.find_element(By.TAG_NAME, "pre")
                fa_sss=fa_seq.text
                with open("C:/Users/dingdingche/Desktop/new_ncbi_pair.fa", "a",encoding="utf-8") as out1:
                    out1.write(f"{spes}\t{gene}\tOKKKK\n")
                with open(f"C:/Users/dingdingche/Desktop/new_{spes}.fa","a",encoding="utf-8") as out2:
                    out2.write(f">{sp}_{gene}\n{fa_sss}\n")
        except:
            aa_lengths=browser.find_elements(By.CLASS_NAME,"desc")
            n=-1
            aa_length=0
            for ii in aa_lengths:
                n+=1
                length=ii.text.split(" ")[0]
                if int(aa_length) < int(length):
                    aa_length=length
                    num=n
            fasta_buttons=browser.find_elements(By.LINK_TEXT,"FASTA")
            fasta_button=fasta_buttons[num]
            fasta_button.click()
            time.sleep(10)
            fa_seq = browser.find_element(By.TAG_NAME, "pre")
            fa_sss = fa_seq.text
            with open("C:/Users/dingdingche/Desktop/new_ncbi_pair.fa", "a", encoding="utf-8") as out1:
                out1.write(f"{spes}\t{gene}\tOKKKK\n")
            with open(f"C:/Users/dingdingche/Desktop/new_{spes}.fa", "a", encoding="utf-8") as out2:
                out2.write(f">{sp}_{gene}\n{fa_sss}\n")