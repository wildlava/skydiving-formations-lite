import sys
import os

os.system('rm -rf ../assets/formations')
os.system('mkdir -p ../assets/formations/thumbs')

fp = open('../res/raw/formation_index.txt', 'r')
for line in fp:
    formation_id = line.strip().split(' ', 1)[0]
    os.system('ln -s ../../full_version/assets/formations/' + formation_id + '.png ../assets/formations/' + formation_id + '.png')
    os.system('ln -s ../../../full_version/assets/formations/thumbs/' + formation_id + '.png ../assets/formations/thumbs/' + formation_id + '.png')

fp.close()
