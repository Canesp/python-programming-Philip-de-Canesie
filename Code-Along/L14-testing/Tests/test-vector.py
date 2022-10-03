import sys, os

print(__file__)

os.chdir(os.path.dirname(__file__))
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)

print(path_to_vector_module)

from vector import Vector