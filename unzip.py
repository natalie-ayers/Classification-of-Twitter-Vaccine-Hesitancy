import os
from glob import glob
from zipfile import ZipFile
zip_dir  = "Data"

def unzip_files():
    
    files = glob(os.path.join(zip_dir, '*.zip'))
    for file in files:
        name, indicator = file.split('.')
        print('start unpacking '+file+'...')
        with ZipFile(file) as zf:
            zf.extractall(zip_dir)
        print('unpacking done!')
        delete()
        #delete(delete_files)
    return

def delete():
    for file in os.listdir(zip_dir):
        if not file.endswith(".json") and '.' in file:
            print('delete ',file)
            os.unlink(os.path.join(zip_dir, file))

