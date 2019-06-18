#Code by Jake Feeney
room=[["interactable item", "required item", "Recived item", "Interact fail message", "Interact sucess message", "Interacted"], "item", ["enemy", "discription", "required weapon", "win message", "lose message"], "next room", "previous room"]
room1=[["locker","lockerkey","code","There is a locker with a lock on it that is not going to be picked", "You opened the locker with a key and got a peice of paper with a 4 diget number on it"], "none", "none", "room2", "none"]
room2=[["safe","code","key", "There is a safe with a 4 diget number.","You put in the number on the paper into the safe. The safe opened and you got a key."], "lockerkey", "none", "room3", "room1"]
room3=["none", "sword", "none", "room4", "room2"]
room4=[["exit","key","win","There is a locked door. There is a keyhole but no key.", "You escaped!\nYou win!"], "none", ["goblin", "There is a goblin with a knife that is about to attack you.", "sword", "The goblin jumped at you but you stabbed him before he could stab you.", "The goblin jumped at you and he stabbed you to death."], "none", "room3"]
gamemap=[["room1",room1],["room2", room2],["room3", room3],["room4",room4]]
roomnum=4
inventory=[]
currentroom=gamemap[0]
currentroomnum=0
helpmessage="Press f to move forward. Press b to move backward. Press l to loot a room. Press i to interact."

def interact():
    global inventory
    global currentroom
    item = currentroom[1][0]
    if istext(item):
        print("There is nothing to interact with in the room")
    else:
        if currentroom[1][0][1] in inventory:
            inventory.insert(0, currentroom[1][0][2])
            print(currentroom[1][0][4])
            currentroom[1][0]="none"
        else:
            print(currentroom[1][0][3])

def movenextroom(room):
    global gamemap
    global roomnum
    global currentroomnum
    global currentroom
    roomnum2=roomnum-1
    while roomnum2>-1:
        if gamemap[roomnum2][0] == room:
            currentroom=gamemap[roomnum2]
            currentroomnum=roomnum2
        roomnum2=roomnum2-1
    if istext(currentroom[1][2]) == False:
        fight(currentroom[1][2][0], currentroom[1][2][1], currentroom[1][2][2], currentroom[1][2][3], currentroom[1][2][4])

def loot(currentroom):
    global inventory
    item = currentroom[1][1]
    if item == "none":
        print("There is nothing in this room.")
    else:
        inventory.insert(0, item)
        message="You found a " + item + "!"
        print(message)
        currentroom[1][1]="none"

def moveforward():
    global gamemap
    global currentroom
    if currentroom[1][3] == "none":
        print("You cannot move forward.")
    else:
        movenextroom(currentroom[1][3])

def movebackward():
    global gamemap
    global currentroom
    if currentroom[1][4] == "none":
        print("You cannot move backward")
    else:
        movenextroom(currentroom[1][4])

def fight(enemy, description, weapon, win, lose):
    global inventory
    print description
    if weapon in inventory:
        print(win)
        currentroom[1][2]="none"
    else:
        print(lose)
        inventory.insert(0, "lose")
        print("You lose")

def istext(item):
    return isinstance(item, basestring)

print("Code by Jake Feeney")
print(helpmessage)
while True:
    if "win" not in inventory and "lose" not in inventory:
        key=raw_input(">")
        if key == "f":
            moveforward()
        elif key == "b":
            movebackward()
        elif key == "d":
            print(currentroom)
        elif key == "l":
            loot(currentroom)
        elif key == "i":
            interact()
        else:
            print(helpmessage)
