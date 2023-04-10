import webbrowser
import keyboard
Paper = ["https://papers.gceguide.com/A%20Levels/Accounting%20(9706)/"
        ,"https://papers.gceguide.com/A%20Levels/Business%20(9609)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/"
        ,"https://papers.gceguide.com/A%20Levels/Economics%20(9708)/"]

def openlink(Link:str):
    webbrowser.open_new(str(Link))

def openlink2(Link2:str,Link3:str):
    webbrowser.open_new(str(Link2))
    webbrowser.open_new(str(Link3))

def routines():
    year = input()
    mid = year[2:4]
    print("Which month? (s,w,m)")
    month = input()
    print("Which Paper")
    paper = input()
    print("qp or ms or both")
    choice = input()
    return year,mid,month,paper,choice

def acc():
    print("Which year? 2015-2022")
    year,mid,month,paper,choice = routines()
    if choice == "qp" or choice == "1":
        Link = Paper[0]+ year+"/9706_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    elif choice == "ms" or choice == "2":
        Link = Paper[0]+ year+"/9706_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    else:
        Link2 = Paper[0]+ year+"/9706_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 = Paper[0]+ year+"/9706_"+ month + mid+"_ms_"+paper+".pdf"
        openlink2(Link2,Link3)
    repeat()

def bus():
    print("Which year? 2016-2022")
    year,mid,month,paper,choice = routines()
    if choice == "qp" or choice == "1":
        Link = Paper[1]+ year+"/9609_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    elif choice == "ms" or choice == "2":
        Link = Paper[1]+ year+"/9609_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    else:
        Link2 = Paper[1]+ year+"/9609_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 = Paper[1]+ year+"/9609_"+ month + mid+"_ms_"+paper+".pdf"
        openlink2(Link2,Link3)
    repeat()
    
def cs():
    i=0
   
    print("Which subject code (Old/New)?")
    code = input()
    if code == "old" or code =="O" or code== "Old" or code =="o":
        i=2
        year2 = "2015"
        code2 = "9608"
    else:
        i=3
        year2 = "2021"
        code2 = "9618"
    print("Which year? "+year2+"-2022")
    year,mid,month,paper,choice = routines()
    if choice == "qp" or choice == "ms":
        Link = Paper[i]+ year+"/"+code2+"_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    else:
        Link2 =  Paper[i]+ year+"/"+code2+"_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 =  Paper[i]+ year+"/"+code2+"_"+ month + mid+"_ms_"+paper+".pdf"
        openlink2(Link2,Link3)
    repeat()

def eco():
    print("Which year? 2010-2022")
    year,mid,month,paper,choice = routines()
    if choice == "qp" or choice == "1":
        Link = Paper[4]+ year+"/9708_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    elif choice == "ms" or choice == "2":
        Link = Paper[4]+ year+"/9708_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        openlink(Link)
    else:
        Link2 = Paper[4]+ year+"/9708_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 = Paper[4]+ year+"/9708_"+ month + mid+"_ms_"+paper+".pdf"
        openlink2(Link2,Link3)
    repeat()

def routinesv2(sub: str):
    P = sub[5:7]
    if sub[8:11] == "m/j" or sub[8:11] == "M/J":
        M = "s"
    else:
        M = "w"
    Y = str(int(sub[12:14]) + 2000)
    MID = sub[12:14]
    return P,M,Y,MID

def extract(sub:str): #9706/22/m/j/18
    if sub[:4] == "9706": #accounting
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[0]+ Y+"/9706_"+ M + MID+"_ms_"+P+".pdf"
        openlink(Link)
        repeat()
    elif sub[0:4] == "9609": #Business
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[1]+ Y+"/9609_"+ M + MID+"_ms_"+P+".pdf"
        openlink(Link)
        repeat()
    elif sub[0:4] == "9608": # Old CS
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[2]+ Y+"/9608_"+ M + MID+"_ms_"+P+".pdf"
        openlink(Link)
        repeat()
    elif sub[0:4] == "9618": # New CS
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[3]+ Y+"/9618_"+ M + MID+"_ms_"+P+".pdf"
        openlink(Link)
        repeat()
    elif sub[0:4] == "9708": #Economics
        P, M, Y, MID = routinesv2(sub)
        Link = Paper[4]+ Y+"/9708_"+ M + MID+"_ms_"+P+".pdf"
        openlink(Link)
        repeat()

def main():
    print("Which subject do you want?\nAcc,Bus,Eco,Cs\nOtherwise enter full code")
    sub = str(input())
    if sub == "Acc" or sub == "acc" or sub == "ACC" or sub == "1" or sub == "ACCOUNTING" or sub == "Accounting" or sub == "accounting":
        acc()
    elif sub == "Bus" or sub == "bus" or sub == "BUS" or sub == "2" or sub == "BUSINESS" or sub == "Business" or sub == "business":
        bus()
    elif sub == "Eco" or sub == "eco" or sub == "ECO" or sub == "3"or sub == "ECONOMICS" or sub == "Economics" or sub == "economics":
        eco()
    elif sub == "Cs" or sub == "cs" or sub == "CS" or sub == "4"or sub == "COMPUTERSCIENCE" or\
    sub == "Computerscience" or sub == "computerscience" or sub == "computer science":
        cs()
    else:
        extract(sub)
         
def repeat():
    print("Do you want to search again?")
    reply = input()
    if reply == "yes" or reply == "y":
        main()
main()

