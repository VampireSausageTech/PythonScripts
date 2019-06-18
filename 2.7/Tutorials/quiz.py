questions=["What is your favourite food?","What is your favourite game?","What is your favourite drink?"]
ans1=["1: Pizza","1: Halo Reach", "1: Coke"]
ans2=["2: Vegtables", "2: Pong", "2: Water"]
occ1=0
occ2=0
q=0
while q < len(questions):
    print(questions[q])
    print(ans1[q])
    print(ans2[q])
    ans=0
    while ans == 0:
        try:
            ans=int(raw_input("Enter 1 or 2 as numbers."))
            if ans == 1:
                occ1+=1
            elif ans == 2:
                occ2+=1
            else:
                ans=0
                print("Use either 1 or 2")
        except ValueError:
            print("Do not use text.")
    q+=1
if occ1 > occ2:
    print("You are like Jake")
else:
    print("You are not like Jake")
input("")
