import os
from glob import glob
from zipfile import ZipFile

zip_dir  = "Data"

files = glob(os.path.join(zip_dir, '*.zip'))
for file in files:
    with ZipFile(file) as zf:
        zf.extractall(zip_dir)
        os.unlink(file)