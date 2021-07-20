import os


class TreeRoot:
    def __init__(self, root_path):
        root_path = Explore(root_path)
        self.all_directoris = [root_path]
        nodos_fronteras = []
        nodos_fronteras.append(root_path)
        max_iter = 3
        while nodos_fronteras != [] and max_iter != 0:
            max_iter -= 1
            directorio = nodos_fronteras.pop()

            files = [f.name for f in os.scandir(directorio.get_path()) if not(f.is_dir())]
            directorio.set_files(files)

            dirs = [f.name for f in os.scandir(directorio.get_path()) if f.is_dir()]
            hijos_d = [Explore(d) for d in dirs]
            directorio.set_hijos(hijos_d)
            self.all_directoris.extend(hijos_d)
            for n in hijos_d:
                nodos_fronteras.append(n)


    def get_allDirs(self):
        return self.all_directoris


    def get_rootPath(self):
        return self.root_path



class Explore:
    def __init__(self, dir, hijos=None):
        self.dir = dir
        self.files = None
        self.directoris = None
        self.hijos = None
        self.padre = None

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for i in self.hijos:
                i.padre = self
    def get_datos(self):
        return self.dir

    def set_files(self, files):
        self.files = files

    def get_files(self):
        return self.files

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def get_path(self):
        path = self.dir
        padre = self.padre
        while padre != None:
            path = f"{padre.dir}/{path}"
            padre = padre.padre
        return path



"""
### Day 33 ###

class ExploreEE:
    def __init__(self, dir):
        self.root_dirs = [f.path for f in os.scandir(dir) if f.is_dir()]
        self.dirs_dict = None
        self.padre = None
        self.hijo = None
        self.iterete_folders()

    def iterete_folders(self):
        visitados = []
        frontera = self.root_dirs
        dir = {}
        while frontera != []:
            nodo = frontera.pop(0)
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

"""
