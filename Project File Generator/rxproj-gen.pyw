from os import getcwd

cwd = getcwd() # Current working directory

with open(f"{cwd}\\Game.rxproj", "wb") as f:
    f.write(b"RPGXP 1.02")