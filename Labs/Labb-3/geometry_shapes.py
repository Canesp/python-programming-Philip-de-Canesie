from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import math

class shapes:
    
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y

    ##--------------------------------------------------------------------##

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        
        if not isinstance(value, (int, float)):
            raise TypeError(f"X value need to be a int or float, not -> ({type(value)})")
        
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        
        if not isinstance(value, (int, float)):
            raise TypeError(f"Y value need to be a int or float, not -> ({type(value)})")
    
        self._y = value

    def plot_size(self):

        if self.__class__.__name__ == "Rektangel":

            x_size = self._x + self._width + 2
            y_size = self._y + self._height + 2
            
            if x_size < y_size:
                x_size = y_size
            else:
                y_size = x_size
                
            return (x_size, y_size)

        else:

            x_size = self._x + self.radius + 2
            y_size = self._y + self.radius + 2

            if x_size < y_size:
                x_size = y_size
            else:
                y_size = x_size
                
            return (x_size, y_size)
    #TODO felhantering 
    def draw_graph(self):

        fig ,ax = plt.subplots(1,1, figsize=(8,8))

        x_size, y_size = self.plot_size()

        ax.set_xlim((-x_size, x_size))
        ax.set_ylim((-y_size, y_size))
        
        if self.__class__.__name__ == "Rektangel":

            ax.add_patch(Rectangle((self._x, self._y), self._width, self._height, linewidth=2, edgecolor="b",facecolor='none', ))

        elif self.__class__.__name__ == "Cirkel":

            ax.add_patch(Circle((self._x, self._y), self._radius, linewidth=2, edgecolor="b",facecolor='none', ))
    #TODO felhantering 
    def translation(self, x: int | float, y: int | float):

        self._x += x
        self._y += y

        self.draw_graph()
    #TODO felhantering 
    def check_point(self, x: int | float, y: int | float):

        if self.__class__.__name__ == "Rektangel":
            
            return abs(x) - abs(self._x + (self._width / 2)) < 0 and abs(y) - abs(self._y + (self._height / 2)) < 0
        
        else: 
            
            return math.sqrt(pow(x - self._x, 2) + pow(y - self._y, 2)) < self._radius

    ##--------------------------------------------------------------------##

    def __eq__(self, other) -> bool:
        return (self.area == other.area) and (self.omkrets == other.omkrets)

    def __gt__(self, other) -> bool:
        return (self.area > other.area) and (self.omkrets > other.omkrets)
    
    def __ge__(self, other) -> bool:
        return (self.area >= self.area) and (self.omkrets >= other.omkrets)

    ##--------------------------------------------------------------------##
    

        


#TODO Validate floats and ints !!

class Rektangel(shapes):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float) -> None:
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
        f,ax = plt.subplots(1,1, figsize=(8,5))
        ax.add_patch(Rectangle((0.5,0.5),0.1,0.1,linewidth=1,edgecolor='b',facecolor='none'))

    
    ##--------------------------------------------------------------------##

    def __repr__(self) -> str:
        return f"rektangel: 'width' = {self.width} 'height' = {self.height}"

    def __str__(self) -> str:
        return f"rektangel!!!" #TODO skriva text. 


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
            raise TypeError(f"radius value need to be a int or float, not -> ({type(value)})")
        elif value <= 0: 
            raise ValueError(f"radius need to be greater then zero, not -> ('{value}')")

        self._radius = value

    @property
    def area(self) -> float:
        return math.pi * (self._radius**2)

    @property 
    def omkrets(self) -> float:
        return (2 * math.pi * self._radius)


    def enhets_Cirkel(self) -> float:
        return self.x == 0 and self.y == 0 and self._radius == 1


    def __repr__(self) -> str:
        return f"cirkel: 'radius' = {self._radius}"

    def __str__(self) -> str:
        return f"cirkel!!!" #TODO skriva text. 
    


    



