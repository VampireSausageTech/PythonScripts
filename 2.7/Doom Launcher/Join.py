import os, subprocess
os.chdir("/Users/admin/Documents/Doom/GZDoom")
ip=str(raw_input("What is the ip adress"))
multijoin=["gzdoom.exe", "-join", ip]
subprocess.call(multijoin)
