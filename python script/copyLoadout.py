import os
import shutil

src_folder = r'C:\MechWarrior5Editor\MW5Mercs\Content\Objects\Mechs'
dst_folder = r'C:\Loadouts'

for root, dirs, files in os.walk(src_folder):
    for filename in files:
        if filename.endswith("_Loadout.json"):
            src_path = os.path.join(root, filename)
            dst_path = os.path.join(dst_folder, filename)
            shutil.copy(src_path, dst_path)
