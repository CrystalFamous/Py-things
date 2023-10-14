import webbrowser

#Settings
Close = True
Extract3 = False #may/june/2017/p32
DownloadBool = True #9608/41/M/J/18
if Extract3 or DownloadBool:
    import requests,os

global paper_dict,pdf_locIN,pdf_locMS,pdf_locQP
paper_dict = {"9706": 0, "9609": 1, "9608": 2, "9618": 3, "9708": 4, "9709":5, "9702":6, "9700":7, "9701":8}
Paper = ["https://papers.gceguide.com/A%20Levels/Accounting%20(9706)/"
        ,"https://papers.gceguide.com/A%20Levels/Business%20(9609)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/"
        ,"https://papers.gceguide.com/A%20Levels/Economics%20(9708)/"
        ,"https://papers.gceguide.com/A%20Levels/Mathematics%20(9709)/"
        ,"https://papers.gceguide.com/A%20Levels/Physics%20(9702)/"
        ,"https://papers.gceguide.com/A%20Levels/Biology%20(9700)/"
        ,"https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/"]
pdf_locQP = 'C:\\Users\\Ebrah\\Downloads\\PDF\\qp'
pdf_locMS = 'C:\\Users\\Ebrah\\Downloads\\PDF\\ms'
pdf_locIN = 'C:\\Users\\Ebrah\\Downloads\\PDF\\in'
pdf = []
def acc():
    if Extract3:
        code = "9706"
        return code
    subject("9706", 0, "2015-2023")
def bus():
    if Extract3:
        code = "9609"
        return code
    subject("9609", 1, "2016-2023")  
def cs():
    print("Which subject code (Old/New)?")
    if Extract3 == False and DownloadBool == False:
        code = input().lower()
    if code in ["old", "o"]:
        if Extract3:
            code = "9608"
            return code
        else:
            subject("9608", 2, "2015-2022")
    else:
        if Extract3:
            code = "9618"
            return code
        else:
            subject("9618", 3, "2021-2023")
def eco():
    subject("9708", 4, "2010-2023")
def maths():
    subject("9709", 5, "2010-2023")
def phy():
    subject("9702", 6, "2010-2023")
def bio():
    subject("9700", 7, "2010-2023")
def chem():
    subject("9701", 8, "2010-2023")
def openlinks(*links: str):
    for link in links:
        webbrowser.open_new(link)
def routines():
    prompts = ["Enter year: ", "Which month? (s,w,m): ", "Which Paper: ", "qp or ms or both or all(insert sheet) or csP4(qp/ms/sf): "]
    inputs = []
    for prompt in prompts:
        user_input = input(prompt)
        if user_input == "reset":
            main()
        inputs.append(user_input)
    year, month, paper, choice = inputs
    mid = year[2:4]
    return year, mid, month, paper, choice
def subject(subject_code: str, subject_index: int, year_range: str):
    print(f"Which year? {year_range}")
    year, mid, month, paper, choice = routines()
    if choice in ["qp", "1", "ms", "2"]:
        Link = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_" + choice + "_" + paper + ".pdf"
        openlinks(Link)
    elif choice == "all":
        Link = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_qp_" + paper + ".pdf"
        Link2 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_ms_" + paper + ".pdf"
        Link3 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_in_" + paper + ".pdf"
        openlinks(Link, Link2, Link3)
    elif choice == "cs":
        Link = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_qp_" + paper + ".pdf"
        Link2 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_ms_" + paper + ".pdf"
        Link3 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_sf_" + paper + ".zip"
        openlinks(Link, Link2, Link3)
    else:
        Link2 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_qp_" + paper + ".pdf"
        Link3 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_ms_" + paper + ".pdf"
        openlinks(Link2, Link3)
    repeat()
def routinesv2(sub:str):
    P = sub[5:7]
    M = "s" if sub[8:11].lower() == "m/j" else ("m" if sub[8:11].lower() == "f/m" else "w")
    Y = str(int(sub[12:14]) + 2000)
    MID = sub[12:14]

    return P, M, Y, MID
def routinesv3(lines):
    P = lines[-3:-1]
    M = "s" if lines[0:3] == "may" else ("m" if lines[0:3] == "feb" else "w")
    Y = lines[-9:-5]
    MID = int(Y) - 2000
    MID = str(MID)
    return P,M,Y,MID
def extractv2(sub:str):
    paper_dict = {"9706": 0, "9609": 1, "9608": 2, "9618": 3, "9708": 4, "9709":5, "9702":6, "9700":7, "9701":8}
    Y = str(int(sub[6:8]) + 2000)
    if sub [:4] in paper_dict:
        choice = input("Do you want to open both(qp/ms) or all(in)? Y/N: ").lower()
        if choice == "n":
            if "qp" in sub:
                Link = Paper[paper_dict[sub[:4]]] + Y + "/" + sub + ".pdf"
                openlinks(Link)
            elif "ms" in sub:
                Link = Paper[paper_dict[sub[:4]]] + Y + "/" + sub + ".pdf"
                openlinks(Link)
            elif "in" in sub:
                Link = Paper[paper_dict[sub[:4]]] + Y + "/" + sub + ".pdf"
                openlinks(Link)
        else:
            Link = Paper[paper_dict[sub[:4]]] + Y + "/" + sub + ".pdf"
            sub = sub.replace("qp","ms")
            Link2 = Paper[paper_dict[sub[:4]]] + Y + "/" + sub + ".pdf"
            sub = sub.replace("ms","in")
            Link3 = Paper[paper_dict[sub[:4]]] + Y + "/" + sub + ".pdf"
            openlinks(Link,Link2,Link3)
def extract(sub:str):
    paper_dict = {"9706": 0, "9609": 1, "9608": 2, "9618": 3, "9708": 4, "9709":5, "9702":6, "9700":7, "9701":8}
    if sub[:4] in paper_dict:
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[paper_dict[sub[:4]]] + Y + "/" + sub[:4] + "_" + M + MID + "_ms_" + P + ".pdf"
        openlinks(Link)
        repeat()

def download(pdf,loc):
    global choice,pdf_locIN,pdf_locMS,pdf_locQP
    i = 0
    with open('searchthrough.txt','r') as file:
        li = file.readlines()
        total = len(li)
    file.close()
    for url in pdf:
        response = requests.get(url)
        if choice == "in" and response.status_code == 200:
            file_path = os.path.join(loc, os.path.basename(url))
            with open(file_path, 'wb') as f:
                f.write(response.content)
                i += 1
            print(f"{url[-18:]} successfully downloaded")
        elif choice == "in" and response.status_code != 200:
            print(f"{url[-18:]} NOT downloaded")
        if response.status_code == 200 and (choice == "ms" or choice == "qp"):
            file_path = os.path.join(loc, os.path.basename(url))
            with open(file_path, 'wb') as f:
                f.write(response.content)
                i += 1
            print(f"{url[-18:]} successfully downloaded")
        
    if i == total:
        print("All files downloaded successfully")
        print(f"{i} number of files were downloaded out of {total}")
    else:
        print(f"{i} number of files were downloaded out of {total}")
def searchfile3(sub:str,loc):
    global choice,pdf_locIN,pdf_locMS,pdf_locQP,paper_dict,pdf
    try:
        file = open("searchthrough.txt","r")
        for lines in file:
            lines = lines.lower().replace(' ',"")
            if extract == True:
                P,M,Y,MID = routinesv3(lines)
            elif DownloadBool == True:
                P,M,Y,MID = routinesv2(lines)
            if Extract3:
                code = choosesub(sub)
            elif DownloadBool:
                code = lines[0:4]
            
            if code in paper_dict:
                if choice == "qp":
                    Link = Paper[paper_dict[code]] + Y + "/" + code + "_" + M + MID + "_qp_" + P + ".pdf"
                elif choice == "ms":
                    Link = Paper[paper_dict[code]] + Y + "/" + code + "_" + M + MID + "_ms_" + P + ".pdf"
                elif choice == "in":
                    Link = Paper[paper_dict[code]] + Y + "/" + code + "_" + M + MID + "_in_" + P + ".pdf"
                pdf.append(Link)
        download(pdf,loc)
    except IOError:
        print("file not found")  
def extract3(sub):
    global pdf,pdf_locIN,pdf_locMS,pdf_locQP
    if Extract3 == False:
        print(f"Extract3 is {Extract3}")
    else:
        global choice,pdf 
        allchoice = [pdf_locQP, pdf_locIN, pdf_locMS]
        choice = input("qp/ms/in: ")
        if choice in ["qp", "ms", "in"]:
            loc = allchoice[["qp", "in", "ms"].index(choice)]
            if choice == "qp":
                searchfile3(sub,loc) 
            elif choice == "ms":
                searchfile3(sub,loc)
            elif choice == "in":
                searchfile3(sub,loc)
def downloadv2(sub):
    global pdf,pdf_locIN,pdf_locMS,pdf_locQP,choice
    if DownloadBool == False:
        print(f"DownloadBool is {DownloadBool}")
    else:
        allchoice = [pdf_locQP, pdf_locIN, pdf_locMS]
        choice = input("qp/ms/in: ")
        if choice in ["qp", "ms", "in"]:
            loc = allchoice[["qp", "in", "ms"].index(choice)]
            if choice == "qp":
                searchfile3(sub,loc) 
            elif choice == "ms":
                searchfile3(sub,loc)
            elif choice == "in":
                searchfile3(sub,loc)
        
    

        
def choosesub(sub):
    if sub in ["acc", "1", "accounting"]:
        code= acc()
    elif sub in ["bus", "2", "business"]:
        code= bus()
    elif sub in ["cs", "4", "computerscience", "computer science"]:
        code= cs()
    return code

def main():
    if Extract3 and DownloadBool == False:
        sub = input("Acc,Bus,Eco,Cs,Maths,Physics,Bio,Chem\nOtherwise enter full code: ").lower()
        if "_" in sub:
            extractv2(sub)
        elif sub in ["acc", "1", "accounting"]:
            acc()
        elif sub in ["bus", "2", "business"]:
            bus()
        elif sub in ["eco", "3", "economics"]:
            eco()
        elif sub in ["cs", "4", "computerscience", "computer science"]:
            cs()
        elif sub in ["maths", "5", "mathematics", "math"]:
            maths()
        elif sub in ["phy", "6", "physics"]:
            phy()
        elif sub in ["bio", "7", "biology"]:
            bio()
        elif sub in ["chem", "8", "chemistry"]:
            chem()
        else:
            extract(sub)
def repeat():
    if Close:
        exit()
    print("Do you want to search again?")
    reply = input()
    if reply == "yes" or reply == "y":
        main() 
if Extract3 == True:
        sub = input("Acc,Bus,Cs: ").lower().replace(" ","")
        extract3(sub)
elif DownloadBool == True:
    sub = input("Acc,Bus,Cs: ").lower().replace(" ","")
    downloadv2(sub)
else:
    main()
