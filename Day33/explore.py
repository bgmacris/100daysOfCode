import os


class Explore:
    def __init__(self, dir):
        self.root_dirs = [f.path for f in os.scandir(dir) if f.is_dir()]
        self.dirs_dict = None

    def iterete_folders(self):
        visitados = []
        frontera = self.root_dirs
        dir = {}
        while frontera != []:
            nodo = frontera.pop(0)
#            print(nodo, "\n")
            if nodo not in visitados:
                iter_dir = [f.path for f in os.scandir(nodo) if f.is_dir()]
                iter_files = [f.name for f in os.scandir(nodo) if not(f.is_dir())]
                if nodo not in dir:
                    dir[nodo] = {
                                 'files': iter_files,
                                 'dirs': iter_dir
                                }
                else:
                    dir[nodo]['files'].extend(iter_files)
                    dir[nodo]['dirs'].extend(iter_dir)
                frontera.extend(iter_dir)
                visitados.append(nodo)

        self.dirs_dict = dir


    def get_all(self):
        return self.dirs_dict


    def get_content_dir(self, search):
        for dir in self.dirs_dict:
            if search == dir.split('/')[-1]:
                return self.dirs_dict[dir]
        return -1


    def get_files_dir(self, search):
        content = self.get_content_dir(search)
        if content != -1:
            return content['files']
        return -1


    def get_dirs_dir(self, search):
        content = self.get_content_dir(search)
        if content != -1:
            return [dir.split('/')[-1] for dir in content['dirs']]
        return -1

