# coding: utf-8

from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need fine tuning.
#all_pack = ["os", "pandas", "numpy", "datetime", "tqdm", "zipfile", "tkinter"]
build_exe_options = {"packages": ["os", "pandas", "numpy", "tqdm", "tkinter"]}

# GUI applications require a different base on Windows
# the default is for a console application

base = None

#if sys.platform == "win32":
#    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = "C:/Users/.../AppData/Local/Programs/Python/Python37-32/tcl/tcl8.6"
os.environ['TK_LIBRARY'] =  "C:/Users/.../AppData/Local/Programs/Python/Python37-32/tcl/tk8.6"                                     
setup(  name = input("Name: "),
        version = input("Version: "),
        description = input("Description: "),
        options = {"build_exe": build_exe_options},
        executables = [Executable(input("Executable: "), base=base)])
