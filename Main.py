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
CRANK_ANGLE_PLOT = np.linspace(0, CRANK_ANGLE + 360, NUM_STEPS)  


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

    # ! Solve for Ground Link !
    P1 = _solve.solve_point_1(O4, LINK_M, THETA_M_TEST)
    
    # ? Print Point P1 Position Results ?
    print(f"02 = {O2}")
    print(f"04 = {O4}")
    print(f"P1 = {P1}")

    # * Create Point P1 Figure *
    ground_figure = _plot.plot_ground_link(O2, O4, P1)
    figure_path.append(ground_figure)
    figure_names.append("Ground_Link_P1")
    
    # ! Solve for Point P1 across all Crank Angles !
    # Initialize array to store P1 positions for each crank angle
    array_P1 = np.zeros((NUM_STEPS, 2))  
    
    for step, theta_m in enumerate(THETA_M_ARRAY):
        array_P1[step] = _solve.solve_point_1(O4, LINK_M, theta_m)
    
    # * Create Point P1 Trajectory Figure *
    p1_trajectory_figure = _plot.plot_p1_trajectory(O2, O4, array_P1)
    figure_path.append(p1_trajectory_figure)
    figure_names.append("P1_Trajectory")
    
    # * Create Point P1 x-Position vs. Crank Angle Figure *
    p1_x_figure = _plot.plot_p1_x_figure(CRANK_ANGLE_PLOT, array_P1)
    figure_path.append(p1_x_figure)
    figure_names.append("P1_x_Position_vs_Crank_Angle")
    
    # * Create Point P1 y-Position vs. Crank Angle Figure *
    p1_y_figure = _plot.plot_p1_y_figure(CRANK_ANGLE_PLOT, array_P1)
    figure_path.append(p1_y_figure)
    figure_names.append("P1_y_Position_vs_Crank_Angle")
    
    
    # Create Figures Dictionary to save figures
    figures_dictionary = os.path.join(os.path.dirname(__file__), 'Figures')
    os.makedirs(figures_dictionary, exist_ok=True)
    
    # Save Figures to Figures Directory as PDF
    for figure, name in zip(figure_path, figure_names):
        figure_file_path = os.path.join(figures_dictionary, f'{name}.pdf')
        figure.savefig(figure_file_path, bbox_inches='tight')
        
        # Success Message for Saving Figure
        print(f"✅ {name} saved to {figure_file_path}")
    
       
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()