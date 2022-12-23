import random as rndm
chs = ["Rock", "Paper", "Scissor"]
usrsatisfctn = False
while usrsatisfctn == False:
    usrpoint = 0
    cmppoint = 0
    for i in range(3):
        print('\t'"Ready for round", (i+1), "of 3")
        entrdusrinpt = input("Please Enter 1 for Rock, 2 for Paper and 3 for Scissor: ")
        if entrdusrinpt.isdigit():
            entrdusrinpt = int(entrdusrinpt)
            if entrdusrinpt>0 and entrdusrinpt<4:
                usrinpt = chs[entrdusrinpt-1]
            else:
                print("Invalid input, please enter a number between 1 and 3")
                break
        else:
            print("Invalid input, please enter a number between 1 and 3")
            break
        cmpinpt = rndm.choice(chs)
        if cmpinpt == usrinpt:
            usrpoint = usrpoint+1
            cmppoint = cmppoint+1
            print("What a draw !!"'\n')
        elif (cmpinpt == chs[0] and usrinpt == chs[2]) or (cmpinpt == chs[1] and usrinpt == chs[0]) or (cmpinpt == chs[2] and usrinpt == chs[1]):
            cmppoint = cmppoint+1
            print("Computer have won this round!! :( "'\n')
        elif (usrinpt == chs[0] and cmpinpt == chs[2]) or (usrinpt == chs[1] and cmpinpt == chs[0]) or (usrinpt == chs[2] and cmpinpt == chs[1]):
            usrpoint = usrpoint+1
            print("You have won this round!! ＜（＾－＾）＞ "'\n')
        else:
            print("Sorry, something went wrong ಠ_ಠ")
            break
    if usrpoint > cmppoint:
        print('\t''\t'"You have won this round!!", usrpoint, '-', cmppoint)
    elif cmppoint > usrpoint:
        print('\t''\t'"You have lost this round!!", cmppoint, '-', usrpoint)
    else:
        print('\t''\t'"this round was a draw!! :(")
    ask = input("Wanna play again (y/n): ")
    if ask == 'n':
        usrsatisfctn = True
        print("Byee then :)")
    else:
        usrsatisfctn = False