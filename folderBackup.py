import os,shutil

def backup(target,locations):
    for i in range(len(locations)):
        try:
            shutil.copytree(target,locations[i])
        except FileExistsError:
           shutil.rmtree(locations[i])
           shutil.copytree(target,locations[i]) 

backup("D:\\Programs\\Python\\foldertest",["F:\\backup loc\\MinecraftServerBackup"])

