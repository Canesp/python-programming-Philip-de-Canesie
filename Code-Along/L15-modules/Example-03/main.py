from importlib.resources import path
import sys, os
from turtle import clear

root_path = os.path.dirname(__file__)
path_folder1 = os.path.join(root_path, "folder_01")
path_folder2 = os.path.join(root_path, "folder_02")

os.system("cls||clear")
print("-"*70)

print()

print(path_folder1)

print()

print("-"*70)

sys.path.append(path_folder1)
sys.path.append(path_folder2)

import module1, module2