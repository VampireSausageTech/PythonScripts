while True:
    #Init variables
    length=int(input("What length do you want the box to be?\n"))
    num=length**2
    digets=len(str(num))
    var1=0
    var2=0
    list1=[]
    x=0
    y=0
    startpos=[["tr",length-1,0],["tl",0,0],["bl",0,length-1],["br",length-1,length-1]]
    direction=[[-1,0,],[0,1,],[1,0,],[0,-1,]]
    dirinx=1
    output=[]

    #set starting position
    knowstart = False
    while knowstart == False:
        startin=input("\nWhere do you wish to start? (tr,tl,bl,br)\n")
        startinx=0
        while startinx != 4:
            if startpos[startinx][0] == startin:
                x=startpos[startinx][1]
                y=startpos[startinx][2]
                dirinx=startinx
                if startpos[startinx][0][1] == "r":
                    altdir=(dirinx+3)%4
                else:
                    altdir=(dirinx+3)%4
                knowstart=True
            startinx+=1

    #set default direction or alternate
    knowans = False
    while knowans == False:
        startin=input("\nDo you want to go anti-clockwise? (y/n)\n")
        if startin == "y":
            dirinx=altdir
            knowans=True
        elif startin == "n":
            knowans=True

    #set start in center or not
    knowans = False
    while knowans == False:
        startin=input("\nDo you want the biggest number in the centre? (y/n)\n")
        if startin == "y":
            dirinx=altdir
            center=True
            knowans=True
            numBackup=num
        elif startin == "n":
            center=False
            knowans=True
    
    #create an empty grid
    while var1 != length:
        list1.insert(0,[])
        while var2 != length:
            list1[0].insert(0,False)
            var2+=1
        var1+=1
        var2=0

    #fill the grid with the numbers
    while num != 0:
        num2=num
        if center == True:
            num2=numBackup-num+1
        list1[y][x]=num2
        num-=1
        nextx=x+direction[dirinx][0]
        nexty=y+direction[dirinx][1]
        if nextx == -1 or nextx == length or nexty == -1 or nexty == length or list1[nexty][nextx] != False:
            dirinx=(dirinx+1)%4
            if num != 0:
                num+=1
        else:
            x=nextx
            y=nexty

    #put the grid in a nicer looking format
    for row in list1:
        str1=""
        for number in row:
            num1=str(number)
            num2=digets-len(num1)
            while num2 != 0:
                str1+=" "
                num2-=1
            str1+=num1+" "
        output.insert(len(output),str1)

    #print the grid

    print("")
    for item in output:
        print(item)
    print("\n")
