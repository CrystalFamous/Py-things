import webbrowser
Close = True
Paper = ["https://papers.gceguide.com/A%20Levels/Accounting%20(9706)/"
        ,"https://papers.gceguide.com/A%20Levels/Business%20(9609)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/"
        ,"https://papers.gceguide.com/A%20Levels/Economics%20(9708)/"]
def openlinks(*links: str):
    for link in links:
        webbrowser.open_new(link)
def routines():
    prompts = ["Enter year: ", "Which month? (s,w,m): ", "Which Paper: ", "qp or ms or both: "]
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
    else:
        Link2 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_qp_" + paper + ".pdf"
        Link3 = Paper[subject_index] + year + "/" + subject_code + "_" + month + mid + "_ms_" + paper + ".pdf"
        openlinks(Link2, Link3)
    repeat()
def acc():
    subject("9706", 0, "2015-2022")
def bus():
    subject("9609", 1, "2016-2022")
def cs():
    print("Which subject code (Old/New)?")
    code = input().lower()
    if code in ["old", "o"]:
        subject("9608", 2, "2015-2022")
    else:
        subject("9618", 3, "2021-2022")
def eco():
    subject("9708", 4, "2010-2022")
def routinesv2(sub: str):
    P = sub[5:7]
    M = "s" if sub[8:11].lower() == "m/j" else "w"
    Y = str(int(sub[12:14]) + 2000)
    MID = sub[12:14]
    return P, M, Y, MID
def extract(sub:str):
    paper_dict = {"9706": 0, "9609": 1, "9608": 2, "9618": 3, "9708": 4}
    if sub[:4] in paper_dict:
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[paper_dict[sub[:4]]] + Y + "/" + sub[:4] + "_" + M + MID + "_ms_" + P + ".pdf"
        openlinks(Link)
        repeat()
def main():
    sub = input("Acc,Bus,Eco,Cs\nOtherwise enter full code: ").lower()
    
    if sub in ["acc", "1", "accounting"]:
        acc()
    elif sub in ["bus", "2", "business"]:
        bus()
    elif sub in ["eco", "3", "economics"]:
        eco()
    elif sub in ["cs", "4", "computerscience", "computer science"]:
        cs()
    else:
        extract(sub)
def repeat():
    if Close:
        exit()
    print("Do you want to search again?")
    reply = input()
    if reply == "yes" or reply == "y":
        main() 
main()
