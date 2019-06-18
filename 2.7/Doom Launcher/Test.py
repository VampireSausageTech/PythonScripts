import os, subprocess
os.chdir("/Users/admin/Documents/Doom/GZDoom")
args=["gzdoom.exe", "-iwad", "DOOM.WAD", "-skill", "3", "-warp", "1", "1"]
multihost=["gzdoom.exe", "-iwad", "DOOM.WAD", "-skill", "3", "-warp", "1", "1", "-host", "2"]
#ip=str(raw_input("What is the ip adress"))
#multijoin=["gzdoom.exe", "-join", ip]
extraargs=["-iwad", "DOOM.WAD", "-skill", "3", "-warp", "1", "1"]
subprocess.call(args)
