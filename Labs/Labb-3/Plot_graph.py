import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


class Plot:

    def __init__(self, *shapes: object) -> None:

        for shape in shapes:

            print(type(shape))

            if isinstance(shape, (float, int, str, list, bool)):
                print(f"Shapes need to be a object")

            if not hasattr(shape, "x") and hasattr(shape, "y"):
                print(f"object need to have a x and y pos")

        self.shapes = list(shapes)
        

    def graph(self):

        f,ax = plt.subplots(1,1, figsize=(8,5))
        ax.set_xlim((-50, 50))
        ax.set_ylim((-50, 50))
        
        for shape in self.shapes:

            rgb = np.random.rand(3,)

            if shape.__class__.__name__ == "Rektangel":
                print("draw shape")
                ax.add_patch(Rectangle((shape.x, shape.y), shape.width, shape.height, linewidth=2, edgecolor=rgb,facecolor='none', ))
                
        
        pass

    
        

    