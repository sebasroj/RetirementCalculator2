import os, winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
path = os.path.join(desktop, "Financial Calculator.lnk")
target = r"C:\Program Files\Retirement Calculator\Can_I_retire2.exe"
wDir = r"C:\Program Files\Retirement Calculator"
icon = r"C:\Program Files\Retirement Calculator\piggybank.ico"



shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()