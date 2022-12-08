
# 1st Party Modules------------------------------------------------------------
import os
import re
from functools import lru_cache

# Type Annotations-------------------------------------------------------------
from typing import Generator


#------------------------------------------------------------------------------
@lru_cache(maxsize=32)
def get_files(obj: str, ID: str, pattern: str, ext: str = '.csv' ) -> Generator:
    # (SD|SI|SIP)\S\w+\S(\d+)(M|F|D|X)\S\w+\S(\d+)(M|F|D|X)(_cross_val_f1)
    # Iterate through the dictionary and get all files which end with csv
    # and begin 'experimentID'

    with os.scandir(obj) as it:
        for entry in it:
            if entry.name.startswith(ID+'-') and entry.name.endswith(ext) and \
                re.search(pattern, entry.name):
                print(entry)
                yield entry.path

            elif os.path.isdir(entry.path) and ("ignore" not in entry.name):
                yield from get_files(entry.path, ID, pattern)
            
            else:
                pass

