import os, sys

os.system("cls||clear")

print(f"{'='*30} main.py {'='*30}\n")

# code imported from another module is executed when imported.
import module1

# Note __name__ is a module when ran from outside of module1.py 
# When module module1.py is ran -> __name__ = "__main__"

print(f"\n{'='*30} main.py {'='*30}")

# When importing a module - a reference will be created to sys.modules
print("globals_namespace")
print(globals()["module1"])

# When importing a module - it will be stored in sys.modules.
print("sys.modules")
print(sys.modules["module1"])