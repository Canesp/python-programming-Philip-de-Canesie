from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Rektangel:

    def __init__(self, x: float | int, y: float | int , width: float | int, height: float | int) -> None:
        
        if not isinstance(width, (int, float)):
            raise TypeError(f"width need to be a int or float, not ({type(width)})")

        if not isinstance(height, (int, float)):
            raise TypeError(f"height need to be a int or float, not ({type(height)})")

        if not isinstance(x, (int, float)):
            raise TypeError(f"x need to be a int or float, not ({type(x)})")

        if not isinstance(y, (int, float)):
            raise TypeError(f"y need to be a int or float, not ({type(y)})")

        if width < 1:
            raise ValueError(f"widht need to be greater than 0 not ({width})")
        
        if height < 1:
            raise ValueError(f"height need to be greater than 0 not ({height})")

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return self.width * self.height

    @property 
    def omkrets(self) -> float:
        return (self.width * 2) + (self.height * 2) 

    def __eq__(self, other) -> bool:
        return (self.area == other.area) and (self.omkrets == other.omkrets)

    def __gt__(self, other) -> bool:
        return (self.area > other.area) and (self.omkrets > other.omkrets)
    
    def __ge__(self, other) -> bool:
        return (self.area >= self.area) and (self.omkrets >= other.omkrets)

    ##--------------------------------------------------------------------##

    def plot_graph(self) -> None:
        f,ax = plt.subplots(1,1, figsize=(8,5))
        ax.add_patch(Rectangle((0.5,0.5),0.1,0.1,linewidth=1,edgecolor='b',facecolor='none'))

    
    ##--------------------------------------------------------------------##

    def __repr__(self) -> str:
        return f"rektangel: 'width' = {self.width} 'height' = {self.height}"

    def __str__(self) -> str:
        return f"rektangel!!!" #TODO skriva text. 

    



