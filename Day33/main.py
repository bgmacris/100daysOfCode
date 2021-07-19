from explore import Explore

exploreF = Explore('/home/pi/git-hub/100daysOfCode/')
exploreF.iterete_folders()

all = exploreF.get_all()
for key, item in all.items():
    print(key, item, "\n")

print("\n#### Buscar archivo ###\n")
print(exploreF.get_content_dir('Day1'), "\n")
print(exploreF.get_files_dir('Day1'), "\n")
print(exploreF.get_dirs_dir('Day1'), "\n")
