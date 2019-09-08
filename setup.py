# -*- coding: utf-8 -*-
import sys
import os
from cx_Freeze import setup, Executable
 
# Dependencies are automatically detected, but it might need fine tuning.
path = sys.path.append(os.path.join("..", "..", "Modules"))

packages = ["tkinter","numpy","matplotlib","matplotlib.backends.backend_tkagg","tkinter.filedialog","sip","re","atexit","tkMessageBox"]
excludes = []
includefiles = ['How_to.wmv','Tradeticket.pdf','PFS.pdf']
buildOptions = dict(create_shared_zip=False)


#########Preparation for target file #################
base = None
if sys.platform == "win32":
    base = "Win32GUI"


# Change some default MSI options and specify the use of the above defined tables

options = {
            "include_msvcr": True,
            "packages": packages,
            "excludes": excludes,
            "include_files":includefiles
            
           }

file = Executable[(
            'Can_I_retire2.py',
            base=base,
            targetName = "Financial-Calc",
            compress = True


)]


##########SETUP####################

setup( 
    name="Retirement Calculator",
    version="1.1",
    description="Simple retirement calculator with a graph",
    options={"build_exe": options},
    executables=[file],
    #scripts=['postinstall.py]
    scripts=['crteshortcut.py']
)
