"""
This script can be used to retrieve the files that are necessary for
populating the databases used in the demo version of ALEXIA.
"""

import urllib.request
import zipfile
from os import remove
from pathlib import Path

def request_file(url, filename, zipped=True):
    if zipped:
        urllib.request.urlretrieve(url, filename)
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('')
        # Removes hashfile (if generated)
        if Path(filename[:-4]+'.sha256sum').is_file():
            remove(filename[:-4]+'.sha256sum')
        elif Path(filename[:-3]+'xsd').is_file():
            remove(filename[:-3]+'xsd')
        # Removes zipfile
        remove(filename)
    else:
        urllib.request.urlretrieve(url, filename)


if __name__ == '__main__':
    pass
