import encrypter as enc

message=raw_input("What is the message you want to encrypt/decrypt?")
randompassword=raw_input("Do you want me to make a random password?\nEnter y or n.")
randompassword=randompassword.lower()
if randompassword == "y":
    password = enc.generatepassword("abcdefghijklmnopqrstuvwxyz .!;,?")
    print "Your password is:'"+password+"' It is contained in the single quotes"
else:
    password=raw_input("Copy and paste your password here:")

print "The message is:'"+enc.encrypt(password,message)+"' It is contained in the single quotes."
