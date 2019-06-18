import os, subprocess
os.chdir("/Users/admin/Documents/Doom/GZDoom")
multihost=["gzdoom.exe", "-iwad", "DOOM.WAD", "-skill", "3", "-warp", "1", "1", "-host", "2"]

subprocess.call(multihost)
