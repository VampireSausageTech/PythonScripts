import random
def encrypt(password,msg):
    msg=msg.lower()
    if len(password) % 2 == 0:
        trans=list(password)
        num=0
        msglist=list(msg)
        while num < len(password)/2:
            char1=trans[2*num]
            char2=trans[2*num+1]
            char1occ=[]
            char2occ=[]
            #print char1
            #print char2
            index=0
            for c in msg:
                if c == char1:
                    char1occ.append(index)
                elif c == char2:
                    char2occ.append(index)
                index+=1
            for item in char1occ:
                msglist[item]=char2
            for item in char2occ:
                msglist[item]=char1
            num=num+1
        return("".join(msglist))
    else:
        return("Use a password with a even amount of characters.")

def generatepassword(chars):
    charslist=list(chars)
    passlist=[]
    while len(charslist) > 0:
        num=random.randint(1,len(charslist))
        passlist.append(charslist[num-1])
        del charslist[num-1]
    return "".join(passlist)
