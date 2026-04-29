# -*- coding: utf-8 -*-
"""
TITLE = Kinematic Analysis Program ~ Vector Loop Analysis
DATE  = 2026.05.15
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
import os
import numpy as np
import matplotlib.pyplot as plt

# ! PROJECT MODULES !
import lib._PositionSolver as _PositionSolver
import lib._VelocitySolver as _VelocitySolver
import lib._AccelerationSolver as _AccelerationSolver

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

# LINK_N: Hypotenuse of LINK_A & LINK_L
LENGTH["LINK_N"] = np.sqrt(LENGTH["LINK_A"]**2 + LENGTH["LINK_L"]**2)

# MOTOR PARAMETERS
# * MOTOR REVOLUTION IS IN RPM *
# * MOTOR ANGULAR VELOCITY IS IN RAD/S *
# * MOTOR ALPHA IS IN RAD/S^2 *
MOTOR_REVOLUTION = 30.00                                  
MOTOR_ANGULAR_VELOCITY = (MOTOR_REVOLUTION * 2 * np.pi) / 60.00
MOTOR_ALPHA = 0.00

# ANGLES
# * ALL ANGLES ARE IN RAD *
THETA_M = np.linspace(0, 2 * np.pi, 360, endpoint=False)
THETA_N = np.arctan2(LENGTH["LINK_L"], LENGTH["LINK_A"])


# * MAIN *
# ? ================================================================ ?

def main():
    """
    Summary of what the main does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    # Initialize Lists to Store Figures and Figure Names
    figure_path = []
    figure_names = []
    
    
    
    
    
    
    # Create Figures Dictionary to save figures
    figures_dictionary = os.path.join(os.path.dirname(__file__), 'Figures')
    os.makedirs(figures_dictionary, exist_ok=True)
    
    # Save Figures to Figures Directory as PDF
    for figure, name in zip(figure_path, figure_names):
        figure_file_path = os.path.join(figures_dictionary, f'{name}.pdf')
        figure.savefig(figure_file_path)
        
        # Success Message for Saving Figure
        print(f"✅ {name} saved to {figure_file_path}")

       
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()