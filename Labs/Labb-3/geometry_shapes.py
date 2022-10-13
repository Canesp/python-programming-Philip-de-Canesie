from __future__ import annotations
from turtle import circle
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

    translate(self, x: int | float, y: int | float):
        moves the shape to a new position based on x and y.
    
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
    @property
    @abstractmethod 
    def area():
        pass

    # abstractmetod for omkrets.
    @property
    @abstractmethod
    def omkrets():
        pass
    
    # method for moving shape
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
    
    # __str__() overload
    def __str__(self) -> str:
        return f"Shape is class {self.__class__.__name__} and is a shape"

    # __repr__() overload
    def __repr__(self) -> str:
        return f"Shape: 'x' = {self._x} 'y' = {self._y}"


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

    is_inside() -> bool
        checks if a point is inside shape.
    
    get_plot() -> plot
        returns a plot with the given shape.
    
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
    def square(self) -> bool:
        """
        checks if the rectangle is a square.
        retruns True if is a square and False if not. 
        -----------------------------------

        """
        
        # returns True if width and height is the same. 
        return self.width == self.height

    def is_inside(self, x: int | float, y: int | float):

        """
        returns True or False depending on if given position is inside shape. 


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

        # gets the corner position (x, y)
        x1, y1 = (self._x - (self._width / 2)), (self._y - (self._height / 2))
        x2, y2 = (self._x + (self._width / 2)), (self._y + (self._height / 2))
        # returns True if x and y is inside corners 
        return (x1, y1) <= (x, y) <= (x2, y2)

    def get_plot(self):
        
        """

            returns a plot of shape.
            -----------------------------------
        
        """

        # makes a random color in rgb
        rgb = np.random.rand(3,)

        # returns the ploted rektangel
        return Rectangle(
            (self._x - (self._width / 2), self._y - (self._height / 2)),
            self._width,
            self._height,
            linewidth=2.5,
            edgecolor=rgb,
            facecolor="none",
        )

    # __str__() overload
    def __str__(self) -> str:
        return f"Rektangel is class {self.__class__.__name__} and is a square = {self.square()}"

    # __repr__() overload
    def __repr__(self) -> str:
        return f"Rektangel: 'x' = {self._x} 'y' = {self._y} 'width' = {self._width} 'height' = {self._height}"

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
    
    is_inside() -> bool
        checks if a point is inside shape.

    get_plot() -> plot
        returns a plot with the given shape.
    
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

        # returns True if x and y == 0 and radius == 1
        return self.x == 0 and self.y == 0 and self._radius == 1

    def is_inside(self, x: int | float, y: int | float):

        """
        returns True or False depending on if given position is inside shape. 


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
        
        # returns True if x and y is inside cirkel 
        return math.sqrt(pow(x - self._x, 2) + pow(y - self._y, 2)) <= self._radius

    def get_plot(self):

        """
        
            returns a plot of shape.
            -----------------------------------
        
        """
        # makes a random color in rgb
        rgb = np.random.rand(3,)

        # returns the ploted cirkel.
        return Circle(
            (self._x, self._y),
            self._radius,
            linewidth=2.5,
            edgecolor=rgb,
            facecolor="none",
        )

    # __str__() overload
    def __str__(self) -> str:
        return f"Cirkel is class {self.__class__.__name__} and is a enhets cirkel = {self.enhets_Cirkel()}"

    # __repr__() overload
    def __repr__(self) -> str:
        return f"Cirkel: 'x' = {self._x} 'y' = {self._y} 'radius' = {self._radius}"

class Cube(Rektangel):

    """
    A class used to represent an Cube
    
    -----------------------------------

    Attributes:
    -----------
 
    width : int | float 
        represents the width of the cube.

    height : int | float 
        represents the height of the cube.

    depth : int | float
        represents the depth of the cube.

    -----------------------------------

    Propertis: 
    ----------

    width : int | float -> float 
        getter and setter for rectangle width.
    
    height : int | float -> float 
        getter and setter for rectangle height.

    depth : int | float
        represents the depth of the cube.

    z : int | float -> float 
        getter and setter for z.

    area : -> float
        getter for the cube area.
    
    omkrets : -> float
        getter for the cube omkrets. 
    
    volym : -> float
        getter for the cube volym.

    -----------------------------------
    
    Methods: 
    --------

    is_cube() -> bool
        checks if cube is a square cube and returns a bool.

    is_inside() -> bool
        checks if a point is inside shape.
    
    translate() : none
        moves the shape by x, y and z
    
    -----------------------------------
    
    """

    def __init__(self, x: int | float, y: int | float,z: int | float, width: int | float, height: int | float, depth: int | float) -> None:
        
        """
        
        Parameters:
        -----------

        depth : int | float 
            represents the depth of the cube.

        -----------------------------------

        """
        
        super().__init__(x, y, width, height)

        # parameters 
        self.depth = depth
        self.z = z

    # property getter for z
    @property
    def z(self):
        return self._z

    # setter for z
    @z.setter
    def z(self, value):

        if not isinstance(value, (int, float)):  # checks if value is a int or float.
            raise TypeError(
                f"Z value need to be a int or float, not -> ({type(value)})"  # error message.
            )

        self._z = value  # sets the z value to the in value.

    # property getter for depth.
    @property
    def depth(self) -> float:
        return self._depth

    # property setter for depth.
    @depth.setter
    def depth(self, value):

        # checks if value is a int or float.
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"depth need to be a int or float, not -> ({type(value)})"
            )  # error message.
        elif value <= 0:
            raise ValueError(
                f"depth need to be greater then zero, not -> ('{value}')"
            )  # error message.

        # sets the depth to the value.
        self._depth = value

    # property getter for cube area.
    @property
    def area(self) -> float:
        return self._width * self._height * self._depth # returns the area of the cube.

    # property getter for cube omkrets.
    @property
    def omkrets(self) -> float:
        return (self._width * 4) + (self._height * 4) + (self._depth * 4) # returns the omkrets of cube.

    # property getter for cube volym 
    @property
    def volym(self) -> float:
        return (self._width * self._height * self._depth) # returns the volym of cube.

    # method for moving shape
    def translate(self, x: int | float, y: int | float, z: int | float):

        """
        moves the shape to a new position based on x, y and z.
        
    
        takes in a position of x, y and z. 
        
        -----------------------------------
        """

        # checks if z is a int or float else -> error
        if not isinstance(z, (int, float)):
            raise TypeError(
                f"z value need to be a int or float, not -> ({type(z)})"
            )  # error massage.

        super().translate(x, y)

        self._z += z # adds the z to position 
    
    # method to check 
    def is_inside(self, x: int | float, y: int | float, z: int | float):

        """
        returns True or False depending on if given position is inside shape. 


        takes in a position of x, y and z. 

        -----------------------------------
        """
        # checks if z is a int or float else -> error.
        if not isinstance(z, (int, float)):
            raise TypeError(
                f"z value need to be a int or float, not -> ({type(z)})"
            )  # error massage.

        # gets the corner position (z)
        z1, z2 = (self._z - (self._depth / 2)), (self._z + (self._depth / 2))
        
        # returns True if x, y and z is inside corners 
        return super().is_inside(x, y) and z1 <= z <= z2

    # method for checking if the shape is a cube.
    def is_cube(self) -> bool:
        """
        checks if the shape is a cube.
        retruns True if is a cube and False if not. 
        -----------------------------------

        """
        # returns True if width, height and depth is the same.
        return self._width == self._height == self._depth

    # __str__() overload
    def __str__(self) -> str:
        return f"Cube is class {self.__class__.__name__} and is a cube = {self.is_cube()}"

    # __repr__() overload
    def __repr__(self) -> str:
        return f"Cube: 'x' = {self._x} 'y' = {self._y} 'z' = {self._z} 'width' = {self._width} 'height' = {self._height} 'depth' = {self._depth}"

class Sphere(Cirkel): 

    """
    A class used to represent an sphere
    
    -----------------------------------

    Attributes:
    -----------

    radius : int | float -> float 
        getter and setter for sphere radius.

    -----------------------------------

    Propertis: 
    ----------

    z : int | float -> float 
        getter and setter for z.
    
    area : -> float
        getter for the sphere area.
    
    omkrets : -> float
        getter for the sphere omkrets. 
    
    volym : -> float
        getter for the sphere volym.

    -----------------------------------
    
    Methods: 
    --------

    is_unit_sphere() -> bool
        checks if sphere is a unit sphere and returns a bool.

    is_inside() -> bool
        checks if a point is inside shape.

    translate() : none
        moves the shape by x, y and z
    
    -----------------------------------
    
    """

    def __init__(self, x: int | float, y: int | float, z: int | float, radius: int | float) -> None:
        
        """
        
        Parameters:
        -----------

        z : int | float 
            represents the z position of the sphere.

        -----------------------------------

        """
        
        super().__init__(x, y, radius)

        #parameter 
        self.z = z

    # property getter for z
    @property
    def z(self):
        return self._z

    # setter for z
    @z.setter
    def z(self, value):

        if not isinstance(value, (int, float)):  # checks if value is a int or float.
            raise TypeError(
                f"Z value need to be a int or float, not -> ({type(value)})"  # error message.
            )

        self._z = value  # sets the z value to the in value.

    # property getter for sphere area.
    @property
    def area(self) -> float:
        return (4 * math.pi * self._radius**2) # returns the area of the sphere.
    
    # property getter for sphere omkrets.
    @property
    def omkrets(self) -> float:
        return (2 * math.pi * self._radius) # returns the omkrets of sphere.

    # property getter for sphere volym 
    @property
    def volym(self) -> float:
        return ((4 / 3) * math.pi * self._radius**3) # returns the volym of sphere.

    # method for moving shape
    def translate(self, x: int | float, y: int | float, z: int | float):

        """
        moves the shape to a new position based on x, y and z.
        
    
        takes in a position of x, y and z. 
        
        -----------------------------------
        """

        # checks if z is a int or float else -> error
        if not isinstance(z, (int, float)):
            raise TypeError(
                f"z value need to be a int or float, not -> ({type(z)})"
            )  # error massage.

        super().translate(x, y)

        self._z += z # adds the z to the old z. 

    # method to check if point is inside shape
    def is_inside(self, x: int | float, y: int | float, z: int | float):

        """
        returns True or False depending on if given position is inside shape. 


        takes in a position of x, y and z. 

        -----------------------------------
        """
        # checks if z is a int or float else -> error.
        if not isinstance(z, (int, float)):
            raise TypeError(
                f"z value need to be a int or float, not -> ({type(z)})"
            )  # error massage.
        
        # returns True if x, y and z is inside shape
        return ((pow(x - self._x, 2) + pow(y - self._y, 2) + pow(z - self._z, 2))**0.5) <= self._radius

    # method for checking if the sphere is a unit sphere.
    def is_unit_sphere(self) -> bool:
        """
        checks if the Sphere is a unit sphere.
        retruns True if is a unit sphere and False if not. 
        -----------------------------------

        """
        # returns true if x y z is 0 and radius == 1.
        return (self._x, self._y, self._z) == (0, 0, 0) and self._radius == 1

    # __str__() overload
    def __str__(self) -> str:
        return f"Sphere is class {self.__class__.__name__} and is a unit sphere = {self.is_unit_sphere()}"

    # __repr__() overload
    def __repr__(self) -> str:
        return f"Sphere: 'x' = {self._x} 'y' = {self._y} 'z' = {self._z} 'radius' = {self._radius}"

