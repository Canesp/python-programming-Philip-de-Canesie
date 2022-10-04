import numpy as np

def trigenomitric_identity(angle: float) -> float:
    """ Calculate trig identity
    
        param:
        angle: angle in radians 

        return: trigonometric one
    
    """

    print("Running trigonometric_identity()")
    return np.cos(angle) ** 2 + np.sin(angle) ** 2

if __name__ == "__main__":
    print(trigenomitric_identity(42))
else: 
    print("You have imported me!!!")