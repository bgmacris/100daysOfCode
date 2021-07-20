from explore import Explore, TreeRoot


tree_dir = TreeRoot('/home/pi/git-hub/100daysOfCode')

all = tree_dir.get_allDirs()
for dir in all:
    print("Name dir:", dir.get_datos())
    print("Files in dir:", dir.get_files())
    try:
        print("Dirs in dir:", [d.get_datos() for d in dir.get_hijos()], "\n")
    except:
        print("Dirs in dir:", dir.get_hijos(), "\n")
