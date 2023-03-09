import webbrowser

Paper = ["https://papers.gceguide.com/A%20Levels/Accounting%20(9706)/"
        ,"https://papers.gceguide.com/A%20Levels/Business%20(9609)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)/"
        ,"https://papers.gceguide.com/A%20Levels/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/"
        ,"https://papers.gceguide.com/A%20Levels/Economics%20(9708)/"]




def acc():
    print("Which year? 2015-2022")
    year = input()
    mid = year[2:4]
    print("Which month? (s,w,m)")
    month = input()
    print("Which Paper")
    paper = input()
    print("qp or ms or both")
    choice = input()
    if choice == "qp" or choice == "ms":
        Link = Paper[0]+ year+"/9706_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        webbrowser.open_new(str(Link))
    else:
        Link2 = Paper[0]+ year+"/9706_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 = Paper[0]+ year+"/9706_"+ month + mid+"_ms_"+paper+".pdf"
        webbrowser.open_new(str(Link2))
        webbrowser.open_new(str(Link3))
    repeat()

def bus():
    print("Which year? 2016-2022")
    year = input()
    mid = year[2:4]
    print("Which month? (s,w,m)")
    month = input()
    print("Which Paper")
    paper = input()
    print("qp or ms or both")
    choice = input()
    if choice == "qp" or choice == "ms":
        Link = Paper[1]+ year+"/9609_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        webbrowser.open_new(str(Link))
    else:
        Link2 =  Paper[1]+ year+"/9609_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 =  Paper[1]+ year+"/9609_"+ month + mid+"_ms_"+paper+".pdf"
        webbrowser.open_new(str(Link2))
        webbrowser.open_new(str(Link3))
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
    year = input()
    mid = year[2:4]
    print("Which month? (s,w,m)")
    month = input()
    print("Which Paper")
    paper = input()
    print("qp or ms or both")
    choice = input()
    if choice == "qp" or choice == "ms":
        Link = Paper[i]+ year+"/"+code2+"_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        webbrowser.open_new(str(Link))
    else:
        Link2 =  Paper[i]+ year+"/"+code2+"_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 =  Paper[i]+ year+"/"+code2+"_"+ month + mid+"_ms_"+paper+".pdf"
        webbrowser.open_new(str(Link2))
        webbrowser.open_new(str(Link3))
    repeat()

def eco():
    print("Which year? 2010-2022")
    year = input()
    mid = year[2:4]
    print("Which month? (s,w,m)")
    month = input()
    print("Which Paper")
    paper = input()
    print("qp or ms or both")
    choice = input()
    if choice == "qp" or choice == "ms":
        Link = Paper[4]+ year+"/9708_"+ month + mid+"_"+ choice+"_"+paper+".pdf"
        webbrowser.open_new(str(Link))
    else:
        Link2 = Paper[4]+ year+"/9708_"+ month + mid+"_qp_"+paper+".pdf"
        Link3 = Paper[4]+ year+"/9708_"+ month + mid+"_ms_"+paper+".pdf"
        webbrowser.open_new(str(Link2))
        webbrowser.open_new(str(Link3))
    repeat()


def main():
    print("Which subject do you want?")
    print("Acc,Bus,Eco,Cs")
    sub = input()
    if sub == "Acc" or sub == "acc" or sub == "ACC" or sub == "1" :
        acc()
    if sub == "Bus" or sub == "bus" or sub == "BUS" or sub == "2" :
        bus()
    if sub == "Eco" or sub == "eco" or sub == "ECO" or sub == "3":
        eco()
    if sub == "Cs" or sub == "cs" or sub == "CS" or sub == "4":
        cs()
    
def repeat():
    print("Do you want to search again?")
    reply = input()
    if reply == "yes" or reply == "y":
        main() 
        

main()







# query = str(x)

# for url in search(query):
#     print(url)
