import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import numpy as np


class Plot:

    def __init__(self, *shapes: object) -> None:

        for shape in shapes:

            print(type(shape))

            if isinstance(shape, (float, int, str, list, bool)):
                print(f"Shape need to be a object")

            if not hasattr(shape, "x") and hasattr(shape, "y"):
                print(f"object need to have a x and y pos")

        self.shapes = list(shapes)
        

    def graph(self):

        f,ax = plt.subplots(1,1, figsize=(8,8))
        
        for shape in self.shapes:

            ax.add_patch(shape.get_plot())
        
        ax.autoscale()
        
        print(ax.get_xlim()[1])

        if ax.get_xlim() < ax.get_ylim():
            if ax.get_xlim()[0] > ax.get_xlim()[1]:
                ax.set_xlim(-ax.get_xlim()[0], ax.get_xlim()[0])
                ax.set_ylim(-ax.get_xlim()[0], ax.get_xlim()[0])
            else:
                ax.set_xlim(-ax.get_xlim()[1], ax.get_xlim()[1])
                ax.set_ylim(-ax.get_xlim()[1], ax.get_xlim()[1])
        else:
            if ax.get_ylim()[0] > ax.get_ylim()[1]:
                ax.set_xlim(-ax.get_ylim()[0], ax.get_ylim()[0])
                ax.set_ylim(-ax.get_ylim()[0], ax.get_ylim()[0])
            else:
                ax.set_xlim(-ax.get_ylim()[1], ax.get_ylim()[1])
                ax.set_ylim(-ax.get_ylim()[1], ax.get_ylim()[1])
        

    
        

    