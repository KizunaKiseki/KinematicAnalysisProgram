# -*- coding: utf-8 -*-
"""
TITLE = Kinematic Analysis Program ~ Vector Loop Analysis
DATE  = 2026.04.16
_____________________________________________________________________
DESCRIPTION:
1. Kinematic analysis program to determine velocities and accelerations of the pins.
2. The program will use vector loop analysis to solve for the unknowns in the mechanism.
3. The program will display the results through a graphical representation of the mechanism and a table of the results.
_____________________________________________________________________
AUTHOR : Nicholas Heling
"""

# * IMPORTS *
# ? ================================================================ ?

# ! PYTHON TEMPLATES & LIBRARIES !
import numpy as np

# ! PROJECT MODULES !


# * VARIABLES *
# ? ================================================================ ?

# LINK DIMENSIONS
# * ALL LINK DIMENSIONS ARE IN MM *
SCALE_FACTOR = 1.50    
LENGTH = {
    "LINK_A": 38.0 * SCALE_FACTOR,
    "LINK_B": 41.50 * SCALE_FACTOR,
    "LINK_C": 39.30 * SCALE_FACTOR,
    "LINK_D": 40.10 * SCALE_FACTOR,
    "LINK_E": 55.80 * SCALE_FACTOR,
    "LINK_F": 39.40 * SCALE_FACTOR,
    "LINK_G": 36.70 * SCALE_FACTOR,
    "LINK_H": 65.70 * SCALE_FACTOR,
    "LINK_I": 49.00 * SCALE_FACTOR,
    "LINK_J": 50.00 * SCALE_FACTOR,
    "LINK_K": 61.90 * SCALE_FACTOR,
    "LINK_L": 7.80 * SCALE_FACTOR,
    "LINK_M": 15.00 * SCALE_FACTOR,  
}

# MOTOR PARAMETERS
# * MOTOR REVOLUTION IS IN RPM *
# * MOTOR ANGULAR VELOCITY IS IN RAD/S *
MOTOR_REVOLUTION = 30.00                                           
MOTOR_ANGULAR_VELOCITY = (MOTOR_REVOLUTION * 2 * np.pi) / 60.00     


# * FUNCTION *
# ? ================================================================ ?

def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass


# * MAIN *
# ? ================================================================ ?

def main():
    """
    Summary of what the main does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    # Code Here
    
    
    pass

        
        
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()