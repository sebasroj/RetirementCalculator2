# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:31:23 2015

@author: Seb
"""

import sys
from os.path import expanduser, join
import winshell
from win32com.client import Dispatch

pyw_executable = join(sys.prefix, "pythonw.exe")
shortcut_filename = "Finance101.lnk"
working_dir = expanduser(join('~','lsf_files'))
script_path = join(sys.prefix, "Scripts", "Can_I_retire2.py")

if sys.argv[1] == '-install':
    # Log output to a file (for test)
    f = open(r"C:\test.log",'w')
    print('Creating Shortcut', file=f)

    # Get paths to the desktop and start menu
    desktop_path = get_special_folder_path("CSIDL_COMMON_DESKTOPDIRECTORY")
    startmenu_path = get_special_folder_path("CSIDL_COMMON_STARTMENU")

    # Create shortcuts.
    for path in [desktop_path, startmenu_path]:
        create_shortcut(pyw_executable,
                    "A program to work with L-System Equations",
                    join(path, shortcut_filename),
                    script_path,working_dir)