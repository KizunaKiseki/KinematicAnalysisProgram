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
import os
import numpy as np
import matplotlib.pyplot as plt

# ! PROJECT MODULES !
import lib._Plot as _plot
import lib._Solve as _solve
import lib._Position as _position

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
OMEGA_M = - (CRANK_SPEED * 2 * np.pi) / 60      # ↻ , Negative sign indicates clockwise rotation

# Angular Acceleration in [rad/s^2]
ALPHA_M = 0                                     # Assuming constant speed

# Input Crank Angle in [degrees]
CRANK_ANGLE = 0

# Single Test Angle in [radians]
THETA_M_TEST = np.deg2rad(CRANK_ANGLE)

# Crank Angle Array [radians]
NUM_STEPS = 361
CRANK_ANGLE_ARRAY = np.linspace(CRANK_ANGLE, CRANK_ANGLE - 360, NUM_STEPS)  # ↻ , from 0° to -360°
THETA_M_ARRAY = np.deg2rad(CRANK_ANGLE_ARRAY)

# Ground Points
O2 = np.array([0.0, 0.0])    
O4 = np.array([LINK_A, LINK_L]) 

# Figures Aesthetics Tweaks
CRANK_ANGLE_PLOT = np.linspace(0, CRANK_ANGLE - 360, NUM_STEPS)  


# * MAIN *
# ? ================================================================ ?

def main():
    """
    Summary of what the main does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    # Initialize figure_path & figure_names lists for saving figures
    figure_path = []
    figure_names = []
    
    # ! Solve across all crank angles !
    # Initialize array to store positions for each crank angle
    array_P1 = np.zeros((NUM_STEPS, 2))  
    array_P2 = np.zeros((NUM_STEPS, 2))
    array_P4 = np.zeros((NUM_STEPS, 2))
    array_P5 = np.zeros((NUM_STEPS, 2))
    array_P6 = np.zeros((NUM_STEPS, 2))
    array_P7 = np.zeros((NUM_STEPS, 2))
    
    # * Loop through each crank angle and solve for each position *
    for step, theta_m in enumerate(THETA_M_ARRAY):
        # ? Solve for Point P1 across all Crank Angles ?
        array_P1[step] = _solve.solve_point_1(O4, LINK_M, theta_m)
        
        # ? Solve for Point P2 across all Crank Angles ?
        array_P2[step] = _solve.solve_point_2(O2, array_P1[step], LINK_B, LINK_J)
        
        # ? Solve for Point P4 across all Crank Angles ?
        array_P4[step] = _solve.solve_point_4(O2, array_P2[step], LINK_D, LINK_E)
        
        # ? Solve for Point P5 across all Crank Angles ?
        array_P5[step] = _solve.solve_point_5(O2, array_P1[step], LINK_C, LINK_K)
        
        # ? Solve for Point P6 across all Crank Angles ?
        array_P6[step] = _solve.solve_point_6(array_P4[step], array_P5[step], LINK_F, LINK_G)
        
        # ? Solve for Point P7 across all Crank Angles ?
        array_P7[step] = _solve.solve_point_7(array_P6[step], array_P5[step], LINK_H, LINK_I)
    
    # ! Create Position Figures for Each Point !
    figure_path, figure_names = _position.create_position_figures(O2, O4, array_P1, array_P2, array_P4, array_P5, 
                                                                  array_P6, array_P7, CRANK_ANGLE_PLOT)
    

    # Create Figures Dictionary to save figures
    figures_dictionary = os.path.join(os.path.dirname(__file__), 'Figures')
    os.makedirs(figures_dictionary, exist_ok=True)
    
    # Save Figures to Figures Directory as PDF
    for figure, name in zip(figure_path, figure_names):
        figure_file_path = os.path.join(figures_dictionary, f'{name}.png')
        figure.savefig(figure_file_path, bbox_inches='tight', dpi=300)
        
        # Success Message for Saving Figure
        print(f"✅ {name} saved to {figure_file_path}")
    
       
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()