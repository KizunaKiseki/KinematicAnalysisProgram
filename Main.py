# -*- coding: utf-8 -*-
"""
TITLE =[Insert Title]
DATE  = 2026.05.15
_____________________________________________________________________
DESCRIPTION:
1. [Insert Description]
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
# Scale Factor
SCALE_FACTOR = 1.5

# Link Lengths in [mm]
LINK_A = 38.00 * SCALE_FACTOR
LINK_B = 41.50 * SCALE_FACTOR   
LINK_C = 39.30 * SCALE_FACTOR
LINK_D = 40.10 * SCALE_FACTOR
LINK_E = 55.80 * SCALE_FACTOR
LINK_F = 39.40 * SCALE_FACTOR
LINK_G = 36.70 * SCALE_FACTOR
LINK_H = 65.70 * SCALE_FACTOR
LINK_I = 49.00 * SCALE_FACTOR
LINK_J = 50.00 * SCALE_FACTOR
LINK_K = 61.90 * SCALE_FACTOR
LINK_L = 7.80 * SCALE_FACTOR
LINK_M = 15.00 * SCALE_FACTOR

# ! Ground Link between A & M in [mm] !
LINK_N = np.sqrt(LINK_A ** 2 + LINK_L ** 2)

# Gear Ratio in [mm]
SMALL_GEAR_DIAMETER = 9     # Motor Gear
LARGE_GEAR_DIAMETER = 54    # Crank Gear
GEAR_RATIO = LARGE_GEAR_DIAMETER / SMALL_GEAR_DIAMETER

# Input Speed in [RPM]
MOTOR_SPEED = 30
CRANK_SPEED = MOTOR_SPEED / GEAR_RATIO

# Angular Velocity in [rad/s]
OMEGA_M = - (CRANK_SPEED * 2 * np.pi) / 60 # ↻ , Negative sign indicates clockwise rotation
# Angular Acceleration in [rad/s^2]
ALPHA_M = 0     # Assuming constant speed

# Input Crank Angle in [degrees]
CRANK_ANGLE = 0

# Single Test Angle in [radians]
THETA_M_TEST = np.deg2rad(CRANK_ANGLE)

# Crank Angle Array [radians]
NUM_STEPS = 361
CRANK_ANGLE_ARRAY = np.linspace(CRANK_ANGLE, CRANK_ANGLE - 360, NUM_STEPS)
THETA_M_ARRAY = np.deg2rad(CRANK_ANGLE_ARRAY)


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
   

       
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()