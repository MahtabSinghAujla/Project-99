import time
import os
import shutil

path=input('Give File to be Deleted: ')
days=int(input('Give Number of Days'))
seconds=time.time()-(days*24*60*60)

deleted={}
deleted['files']=0
deleted['folders']=0

def remove_folder(path):
    if not shutil.rmtree(path) :
        print(f'{path} is removed successfully')
    else :
        print(f'Unable to delete '+path)

def remove_file(path):
    if not shutil.rmtree(path) :
        print(f'{path} is removed successfully')
    else :
        print(f'Unable to delete '+path)

def getFileFolderAge (path) :
    ctime=os.stat(path).st_ctime
    return ctime

if os.path.exists(path) :
    for root_folder,folders,files in os.walk(path) :
        if seconds>=getFileFolderAge(root_folder) :
            remove_folder(root_folder)
            deleted['folders']+=1
        else :
            for folder in folders:
                folder_path=os.path.join(root_folder,folder)
                if seconds>=getFileFolderAge(folder_path) :
                    remove_folder(folder_path)
                    deleted['folders']+=1
            for file in files:
                file_path=os.path.join(root_folder,file)
                if seconds>=getFileFolderAge(file_path) :
                    remove_file(file_path)
                    deleted['files']+=1
    else :
        if seconds>=getFileFolderAge(path) :
            remove_file(path)
            deleted['folders']+=1
else :
    print(f'"{path}" is not found')
    deleted['files']+=1
    print(deleted['files']+' files and '+deleted['folders']+' folders have been deleted')
