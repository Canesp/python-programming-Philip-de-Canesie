from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import math
from abc import abstractmethod, ABC
import numpy as np


class shapes(ABC):

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

        if not isinstance(value, (int, float)):  # checks if value is a int or float.
            raise TypeError(
                f"X value need to be a int or float, not -> ({type(value)})"  # error message.
            )

        self._x = value  # sets the x value to the in value.

    # property getter for y
    @property
    def y(self):
        return self._y

    # setter for y
    @y.setter
    def y(self, value):

        if not isinstance(value, (int, float)):  # checks if value is a int or float.
            raise TypeError(
                f"Y value need to be a int or float, not -> ({type(value)})"  # error message.
            )

        self._y = value  # sets the y value to the in value.

    # abstractmetod for area.
    @abstractmethod
    def area():
        pass

    # abstractmetod for omkrets.
    @abstractmethod
    def omkrets():
        pass

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

            return (x_size, y_size)  # return the sizes.

        else:

            # sets the variables with offset.
            x_size = self._x + self.radius + 2
            y_size = self._y + self.radius + 2

            # checks what side is the longest and makes that the size.
            if x_size < y_size:
                x_size = y_size
            else:
                y_size = x_size

            return (x_size, y_size)  # returns the sizes.

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
            raise TypeError(
                f"x value need to be a int or float, not -> ({type(x)})"
            )  # error massage.
        if not isinstance(y, (int, float)):
            raise TypeError(
                f"y value need to be a int or float, not -> ({type(y)})"
            )  # error message.

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
            raise TypeError(
                f"x value need to be a int or float, not -> ({type(x)})"
            )  # error massage.
        if not isinstance(y, (int, float)):
            raise TypeError(
                f"y value need to be a int or float, not -> ({type(y)})"
            )  # error massage.

        # checks if the shape is a rektangel
        if self.__class__.__name__ == "Rektangel":
            # return True if point is inside of shape and False if outside.
            return (
                abs(x) - abs(self._x + (self._width / 2))
                < 0  # takes abs point x pos -  x abs of pos + (width/2).
                and abs(y) - abs(self._y + (self._height / 2))
                < 0  # takes abs point y pos -  y abs of pos + (height/2).
            )

        # if not a rektangel
        else:
            # return True if point is inside of shape and False if outside.
            return (
                math.sqrt(pow(x - self._x, 2) + pow(y - self._y, 2)) < self._radius
            )  # checks if distance is less than radius.

    # Overload metods
    # TODO felhantering
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
    """
    A class used to represent an Rectangel
    
    -----------------------------------

    Attributes:
    -----------
 

    width : int | float 
        represents the width of the rectangle.

    height : int | float 
        represents the height of the rectangle.

    -----------------------------------

    Propertis: 
    ----------

    width : int | float -> float 
        getter and setter for rectangle width.
    
    height : int | float -> float 
        getter and setter for rectangle height.

    area : -> float
        getter for the rectangle area.
    
    omkrets : -> float
        getter for the rectangle omkrets. 

    -----------------------------------
    
    Methods: 
    --------

    kvadrat() -> bool
        checks if rectangel is a square and returns a bool.
    
    -----------------------------------
    
    """

    def __init__(
        self, x: int | float, y: int | float, width: int | float, height: int | float
    ) -> None:

        """
        
        Parameters:
        -----------

        width : int | float 
        represents the width of the rectangle.

        height : int | float 
        represents the height of the rectangle.

        -----------------------------------

        """
        # sends the x, y to super class.
        super().__init__(x, y)

        # Parameters
        self.width = width
        self.height = height

    # property getter for width.
    @property
    def width(self) -> float:
        return self._width

    # property setter for width.
    @width.setter
    def width(self, value):

        # checks if value is a int or float.
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"width need to be a int or float, not -> ({type(value)})"
            )  # error message.
        elif value <= 0:
            raise ValueError(
                f"width need to be greater then zero, not -> ('{value}')"
            )  # error message.

        # sets the width to the value.
        self._width = value

    # property getter for height.
    @property
    def height(self) -> float:
        return self._height

    # property setter for height.
    @height.setter
    def height(self, value):

        # checks if value is a int or float.
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"height need to be a int or float, not -> ({type(value)})"
            )  # error message.
        elif value <= 0:
            raise ValueError(
                f"height need to be greater then zero, not -> ('{value}')"
            )  # error message.

        # sets the height to the value.
        self._height = value

    # property getter for rectangel area.
    @property
    def area(self) -> float:
        return self.width * self.height  # returns the area of the rektangle.

    # property getter for rectangle omkrets.
    @property
    def omkrets(self) -> float:
        return (self.width * 2) + (self.height * 2)  # returns the omkrets of rectangle.

    # method for checking if the rectangle is a square.
    def kvadrat(self) -> bool:
        """
        checks if the rectangle is a square.
        retruns True if is a square and False if not. 
        -----------------------------------

        """
        return self.width == self.height

    def get_plot(self):

        rgb = np.random.rand(3,)

        return Rectangle(
            (self._x, self._y),
            self._width,
            self._height,
            linewidth=2.5,
            edgecolor=rgb,
            facecolor="none",
        )

    # __repr__() overload
    def __repr__(self) -> str:
        return f"rektangel: 'width' = {self.width} 'height' = {self.height}"

    # __str__() overload
    def __str__(self) -> str:
        return f"rektangel!!!"  # TODO skriva text.


class Cirkel(shapes):

    """
    A class used to represent an Cirkel 
    
    -----------------------------------

    Attributes:
    -----------
 

    radius : int | float 
        represents the radius of the cirkel.

    
    -----------------------------------

    Propertis: 
    ----------

    radius : int | float -> float 
        getter and setter for cirkle radius.

    area : -> float
        getter for the cirkel area.
    
    omkrets : -> float
        getter for the cirkel omkrets. 

    -----------------------------------
    
    Methods: 
    --------

    enhets_Cirkel() -> bool
        checks if cirkel is a enhets cirkel and returns a bool.
    
    -----------------------------------
    
    """

    def __init__(self, x: int | float, y: int | float, radius: int | float) -> None:

        """
        
        Parameters:
        -----------

        radius : int | float 
        represents the radius of the cirkel.

        -----------------------------------

        """
        # sends the x, y to super class.
        super().__init__(x, y)

        # Parameter
        self.radius = radius

    # property getter for radius.
    @property
    def radius(self):
        return self._radius

    # propert setter for radius
    @radius.setter
    def radius(self, value):

        # checks if value is a int or float.
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"radius value need to be a int or float, not -> ({type(value)})"  # error message.
            )
        elif value <= 0:
            raise ValueError(
                f"radius need to be greater then zero, not -> ('{value}')"
            )  # error message.

        # sets the radius to the value.
        self._radius = value

    # property getter for area.
    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    # property getter for omkrets.
    @property
    def omkrets(self) -> float:
        return 2 * math.pi * self._radius

    # method to check if cirkel == a enhets cirkel.
    def enhets_Cirkel(self) -> bool:
        """
        checks if the cirkel is a enhets cirkel.
        retruns True if cirkel is and False if not. 
        -----------------------------------

        """

        return self.x == 0 and self.y == 0 and self._radius == 1

    def get_plot(self):

        rgb = np.random.rand(3,)

        return Circle(
            (self._x, self._y),
            self._radius,
            linewidth=2.5,
            edgecolor=rgb,
            facecolor="none",
        )

    # __repr__() overload
    def __repr__(self) -> str:
        return f"cirkel: 'radius' = {self._radius}"

    # __str__() overload
    def __str__(self) -> str:
        return f"cirkel!!!"  # TODO skriva text.

