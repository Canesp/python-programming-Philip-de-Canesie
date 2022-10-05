from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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

    @x.setter
    def y(self, value):
        
        if not isinstance(value, (int, float)):
            raise TypeError(f"Y value need to be a int or float, not -> ({type(value)})")

        self._y = value

    ##--------------------------------------------------------------------##

    def __eq__(self, other) -> bool:
        return (self.area == other.area) and (self.omkrets == other.omkrets)

    def __gt__(self, other) -> bool:
        return (self.area > other.area) and (self.omkrets > other.omkrets)
    
    def __ge__(self, other) -> bool:
        return (self.area >= self.area) and (self.omkrets >= other.omkrets)

    ##--------------------------------------------------------------------##
    

        




class Rektangel(shapes):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float) -> None:
        super().__init__(x, y)

        self.width = width
        self.height = height
       

    @property
    def area(self) -> float:
        return self.width * self.height

    @property 
    def omkrets(self) -> float:
        return (self.width * 2) + (self.height * 2) 

    ##--------------------------------------------------------------------##

    def plot_graph(self) -> None:
        f,ax = plt.subplots(1,1, figsize=(8,5))
        ax.add_patch(Rectangle((0.5,0.5),0.1,0.1,linewidth=1,edgecolor='b',facecolor='none'))

    
    ##--------------------------------------------------------------------##

    def __repr__(self) -> str:
        return f"rektangel: 'width' = {self.width} 'height' = {self.height}"

    def __str__(self) -> str:
        return f"rektangel!!!" #TODO skriva text. 

    



