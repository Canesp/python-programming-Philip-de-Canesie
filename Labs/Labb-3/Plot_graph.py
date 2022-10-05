#import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle

class Plot:

    def __init__(self, *shape: object) -> None:

        if not hasattr(shape, 'self.width'):
            raise TypeError("Object need to have a attribute width")

        self.shape = shape

    