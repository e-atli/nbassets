import os
import glob

from pathlib import Path

for filename in Path('manufacturers').glob('**/mf_*'):
    print(filename)
    mf = filename.open()
    exec(mf.read())
    try:
        Manufacturer(slug=SLUG, name=NAME).save()
    except:
        print("!!! Manufacturer slug >"+SLUG+"< exists")

quit()
