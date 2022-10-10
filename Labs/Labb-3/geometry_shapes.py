from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import math


class shapes:
    
    """
    A class used to represent an Shapes
    
    -----------------------------------

    Attributes:
    -----------
 

    x : int | float 
        represents the center of shape x position.

    y : int | float 
        represents the center of shape y position.

    -----------------------------------

    Propertis: 
    ----------

    x : int | float -> float 
        getter and setter for shape x positon.
    
    y : int | float -> float 
        getter and setter for shape y positon.

    -----------------------------------
    
    Methods: 
    --------

    plot_size(self): -> tuple(floats)
        calculates the plot x and y size based on positon and size of shape. 
    
    draw_graph(self): 
        plots and draws the shape on graph. 

    translate(self, x: int | float, y: int | float):
        moves the shape to a new position based on x and y.

    is_inside(self, x: int | float, y: int | float) -> bool:
        returns True or False depending on if given position is inside shape. 
    
    -----------------------------------
    
    """


    def __init__(self, x: int | float, y: int | float) -> None:
        """
        
        Parameters:
        -----------

        x : int | float 
        represents the center of shape x position.

        y : int | float 
        represents the center of shape y position.

        -----------------------------------

        """
        # Parameters 
        self.x = x
        self.y = y

    # property getter for x 
    @property
    def x(self):
        return self._x

    # setter for x 
    @x.setter
    def x(self, value):

        if not isinstance(value, (int, float)): # checks if value is a int or float.
            raise TypeError(
                f"X value need to be a int or float, not -> ({type(value)})" # error message. 
            )

        self._x = value # sets the x value to the in value. 

    # property getter for y
    @property
    def y(self):
        return self._y

    # setter for y 
    @y.setter
    def y(self, value):

        if not isinstance(value, (int, float)): # checks if value is a int or float.
            raise TypeError(
                f"Y value need to be a int or float, not -> ({type(value)})" # error message. 
            )

        self._y = value # sets the y value to the in value. 

    # Method that calculates the graph size. x-lim and y-lim.
    def plot_size(self):
        
        """
            calculates the plot x and y size based on positon and size of shape. 
            returns a Tupel of x and y (x, y)
            -----------------------------------
            
        """
        
        # checks if the shape is a rektangel or not. 
        if self.__class__.__name__ == "Rektangel":

            # sets the variables with offset. 
            x_size = self._x + self._width + 2
            y_size = self._y + self._height + 2

            # checks what side is the longest and makes that the size. 
            if x_size < y_size:
                x_size = y_size
            else:
                y_size = x_size

            return (x_size, y_size) # return the sizes. 

        else:

            # sets the variables with offset. 
            x_size = self._x + self.radius + 2
            y_size = self._y + self.radius + 2
            
            # checks what side is the longest and makes that the size. 
            if x_size < y_size:
                x_size = y_size
            else:
                y_size = x_size

            return (x_size, y_size) # returns the sizes.

    
    def draw_graph(self):

        """
        plots and draws the shape on graph.

        -----------------------------------
        """

        # creates a subplot 
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))

        # Gets the plot size from the plot_size method. 
        x_size, y_size = self.plot_size() 

        # sets the plot size / x and y lim. 
        ax.set_xlim((-x_size, x_size))
        ax.set_ylim((-y_size, y_size))

         # checks if the shape is a rektangel or not. 
        if self.__class__.__name__ == "Rektangel":
            
            # Draw the rektangel on the plot.
            ax.add_patch(
                Rectangle(
                    (self._x, self._y),
                    self._width,
                    self._height,
                    linewidth=2,
                    edgecolor="b",
                    facecolor="none",
                )
            )

        # checks if the shape is a Cirkel or not. 
        elif self.__class__.__name__ == "Cirkel":

            # draw the cirkel on the plot.
            ax.add_patch(
                Circle(
                    (self._x, self._y),
                    self._radius,
                    linewidth=2,
                    edgecolor="b",
                    facecolor="none",
                )
            )

    def translate(self, x: int | float, y: int | float):

        """
        moves the shape to a new position based on x and y.
        
    
        takes in a position of x and y. 
        
        -----------------------------------
        """

        # checks if x and y are int or float else -> error 
        if not isinstance(x, (int, float)):
            raise TypeError(f"x value need to be a int or float, not -> ({type(x)})") # error massage.
        if not isinstance(y, (int, float)):
            raise TypeError(f"y value need to be a int or float, not -> ({type(y)})") # error message. 

        # changes the x and y variables 
        self._x += x
        self._y += y
        
        # calls the draw_graph() method that redraw the graph. 
        self.draw_graph()

    def is_inside(self, x: int | float, y: int | float):

        """
        eturns True or False depending on if given position is inside shape. 


        takes in a position of x and y. 

        -----------------------------------
        """

        # checks if x and y are int or float else -> error 
        if not isinstance(x, (int, float)):
            raise TypeError(f"x value need to be a int or float, not -> ({type(x)})") # error massage.
        if not isinstance(y, (int, float)):
            raise TypeError(f"y value need to be a int or float, not -> ({type(y)})") # error massage.

        #checks if the shape is a rektangel 
        if self.__class__.__name__ == "Rektangel":
            # return True if point is inside of shape and False if outside.  
            return (
                abs(x) - abs(self._x + (self._width / 2)) < 0 # takes abs point x pos -  x abs of pos + (width/2).  
                and abs(y) - abs(self._y + (self._height / 2)) < 0 # takes abs point y pos -  y abs of pos + (height/2). 
            )

        # if not a rektangel 
        else:
            # return True if point is inside of shape and False if outside.
            return math.sqrt(pow(x - self._x, 2) + pow(y - self._y, 2)) < self._radius # checks if distance is less than radius. 

    # Overload metods 

    # == 
    def __eq__(self, other) -> bool:
        return (self.area == other.area) and (self.omkrets == other.omkrets)
    # > and <
    def __gt__(self, other) -> bool:
        return (self.area > other.area) and (self.omkrets > other.omkrets)
    # >= and <= 
    def __ge__(self, other) -> bool:
        return (self.area >= self.area) and (self.omkrets >= other.omkrets)




# TODO Validate floats and ints !!


class Rektangel(shapes):
    def __init__(
        self, x: int | float, y: int | float, width: int | float, height: int | float
    ) -> None:

        super().__init__(x, y)

        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError(f"width need to be a int or float, not -> ({type(value)})")
        elif value <= 0:
            raise ValueError(f"width need to be greater then zero, not -> ('{value}')")

        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError(f"height need to be a int or float, not -> ({type(value)})")
        elif value <= 0:
            raise ValueError(f"height need to be greater then zero, not -> ('{value}')")

        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def omkrets(self) -> float:
        return (self.width * 2) + (self.height * 2)

    def kvadrat(self) -> float:
        return self.width == self.height

    ##--------------------------------------------------------------------##

    def plot_graph(self) -> None:
        f, ax = plt.subplots(1, 1, figsize=(8, 5))
        ax.add_patch(
            Rectangle(
                (0.5, 0.5), 0.1, 0.1, linewidth=1, edgecolor="b", facecolor="none"
            )
        )

    ##--------------------------------------------------------------------##

    def __repr__(self) -> str:
        return f"rektangel: 'width' = {self.width} 'height' = {self.height}"

    def __str__(self) -> str:
        return f"rektangel!!!"  # TODO skriva text.


class Cirkel(shapes):
    def __init__(self, x: int | float, y: int | float, radius: int | float) -> None:
        super().__init__(x, y)

        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError(
                f"radius value need to be a int or float, not -> ({type(value)})"
            )
        elif value <= 0:
            raise ValueError(f"radius need to be greater then zero, not -> ('{value}')")

        self._radius = value

    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @property
    def omkrets(self) -> float:
        return 2 * math.pi * self._radius

    def enhets_Cirkel(self) -> float:
        return self.x == 0 and self.y == 0 and self._radius == 1

    def __repr__(self) -> str:
        return f"cirkel: 'radius' = {self._radius}"

    def __str__(self) -> str:
        return f"cirkel!!!"  # TODO skriva text.

