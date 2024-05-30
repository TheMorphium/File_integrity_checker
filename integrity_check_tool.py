#!/usr/bin/python3

import os
import site
import sys

python_version = sys.version_info
python_lib_folder = f'/env/lib/python{sys.version_info[0]}.{sys.version_info[1]}/site-packages/'

site.addsitedir(os.curdir + python_lib_folder)


import sms_messaging

from dotenv import load_dotenv

