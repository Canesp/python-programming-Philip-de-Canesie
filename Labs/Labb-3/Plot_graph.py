import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle


class PlotShapes:

    """
    A class used to plot shapes on a graph
    
    -----------------------------------

    Attributes:
    -----------

    shapes : object
        represents a list of objects to be ploted. 

    -----------------------------------
    
    Methods: 
    --------

    plot_graph()
        Plots the shapes on a graph.
    
    -----------------------------------
    
    """

    def __init__(self, *shapes: object) -> None:
        """
        
        Parameters:
        -----------

        shapes : object 
            represents a list of objects to be ploted. 
        -----------------------------------

        """

        # checks all the objects. 
        for shape in shapes:
            # checks if it is a object or not. 
            if isinstance(shape, (float, int, str, list, bool)):
                raise TypeError(f"Shape need to be a object") # error massage.

            # checks if the object have "get_plot()" method.
            if not hasattr(shape, "get_plot"):
                raise TypeError(f"Object need to have 'get_plot()' method, (class = '{shape.__class__.__name__}' dont have 'get_plot()')") # error massage.

        self.shapes = list(shapes) # puts the objects in a list. 
        

    def plot_graph(self):

        """
        
        Plots the diffrent shapes on the graph 
        -----------------------------------

        """

        # makes a subplot. 
        f,ax = plt.subplots(1,1, figsize=(8,8))

        # moves the spines to the middle.
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')

        #removes the right and top spines.
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        # call the get_plot() from objects and plots them. 
        for shape in self.shapes:
            # plots the shapes. 
            ax.add_patch(shape.get_plot())
        
        ax.autoscale() # scales the graph so all shapes can be seen. 

        # gets the graph size. 
        x1, x2 = ax.get_xlim()
        y1, y2 = ax.get_ylim()
        x1 = abs(x1)
        x2 = abs(x2)
        y1 = abs(y1)
        y2 = abs(y2)

        # makes the graph sides the same size by taking the longest side.  
        if x1 or x2 > y1 or y2: # checks which side is the longes x or y. 
            if x1 > x2: # checks if right or left side of x is longer. 
                ax.set_xlim(-x1, x1) # sets the size x and y 
                ax.set_ylim(-x1, x1)
            else:
                ax.set_xlim(-x2, x2) # sets the size x and y 
                ax.set_ylim(-x2, x2)
        else:
            if y1 > y2: # checks if top or lower side of y is longer. 
                ax.set_xlim(-y1, y1) # sets the size x and y 
                ax.set_ylim(-y1, y1)
            else:
                ax.set_xlim(-y2, y2) # sets the size x and y 
                ax.set_ylim(-y2, y2)
        

    
        

    