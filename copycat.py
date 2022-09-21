#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/student/mycode/")

# The following line copies the file:
shutil.copy("research/sdn_network.txt", "research/sdn_network.txt.copy")

# Creates directory
shutil.copytree("research/", "research_backup/")

