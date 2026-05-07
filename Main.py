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
import os

# ! PROJECT MODULES !
import lib._Plot as _plot
import lib._Solve as _solve
import lib._Position as _position
import lib._Velocity as _velocity
import lib._Acceleration as _acceleration
import lib._Vector as _vectors
import lib._Table as _table

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

# * FUNCTION *
# ? ================================================================ ?

def save_figures(figure_path : list, figure_names : list, folder_name : str) -> None:
    """
    Save figures to the specified folder.
    
    Args:
        figure_path (list) : List of Matplotlib figure objects.
        figure_names (list) : List of figure names corresponding to each figure object.
        folder_name (str) : Name of the folder to save the figures in.
    
    Returns:
        None

    """
    # Create Figures Dictionary to save figures
    figures_dictionary = os.path.join(os.path.dirname(__file__), 'Figures')
   
    # Create saved directory
    save_directory = os.path.join(figures_dictionary, folder_name)
    os.makedirs(save_directory, exist_ok=True)
    
    # Save Figures to Figures Directory as PNG
    for figure, name in zip(figure_path, figure_names):
        figure_file_path = os.path.join(save_directory, f'{name}.png')
        figure.savefig(figure_file_path, bbox_inches='tight', dpi=300)
        
        # Success Message for Saving Figure
        print(f"✅ {name} saved to {figure_file_path}")


def print_angular_quantity_summary(quantity_name: str, quantity_dictionary: dict) -> None:
    """
    Prints angular velocity or angular acceleration summary with direction.

    Args:
        quantity_name (str): Title for the quantity group.
        quantity_dictionary (dict): Dictionary of link labels and values.

    Returns:
        None
    """

    print("\n" + "=" * 60)
    print(quantity_name)
    print("=" * 60)

    for label, value in quantity_dictionary.items():
        if value > 1e-9:
            direction = "CCW"
        elif value < -1e-9:
            direction = "CW"
        else:
            direction = "0"

        if direction == "0":
            print(f"{label} = 0.000")
        else:
            print(f"{label} = {abs(value):.6f} ({direction})")

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
    mechanism_path = []
    mechanism_names = []
    
    position_path = []
    position_names = []
    
    velocity_path = []
    velocity_names = []
    
    acceleration_path = []
    acceleration_names = []
    
    vector_path = []
    vector_names = []
    
    table_path = []
    table_names = []
    
    # ! Solve across all crank angles !
    # Initialize array to store positions for each crank angle
    position_P1 = np.zeros((NUM_STEPS, 2))  
    position_P2 = np.zeros((NUM_STEPS, 2))
    position_P4 = np.zeros((NUM_STEPS, 2))
    position_P5 = np.zeros((NUM_STEPS, 2))
    position_P6 = np.zeros((NUM_STEPS, 2))
    position_P7 = np.zeros((NUM_STEPS, 2))
    
    # Initialize array to store velocity for each crank angle
    velocity_P1 = np.zeros((NUM_STEPS, 2))
    velocity_P2 = np.zeros((NUM_STEPS, 2))
    velocity_P4 = np.zeros((NUM_STEPS, 2))
    velocity_P5 = np.zeros((NUM_STEPS, 2))
    velocity_P6 = np.zeros((NUM_STEPS, 2))
    velocity_P7 = np.zeros((NUM_STEPS, 2))
    velocity_Foot = np.zeros((NUM_STEPS, 2))
    
    # Initialize array to store angular velocity for each crank angle
    omega_B = np.zeros(NUM_STEPS)
    omega_J = np.zeros(NUM_STEPS)
    omega_C = np.zeros(NUM_STEPS)
    omega_K = np.zeros(NUM_STEPS)
    omega_D = np.zeros(NUM_STEPS)
    omega_E = np.zeros(NUM_STEPS)
    omega_F = np.zeros(NUM_STEPS)
    omega_G = np.zeros(NUM_STEPS)
    omega_H = np.zeros(NUM_STEPS)
    omega_I = np.zeros(NUM_STEPS)
    
    # Initialize array to store acceleration for each crank angle
    acceleration_P1 = np.zeros((NUM_STEPS, 2))
    acceleration_P2 = np.zeros((NUM_STEPS, 2))
    acceleration_P4 = np.zeros((NUM_STEPS, 2))
    acceleration_P5 = np.zeros((NUM_STEPS, 2))
    acceleration_P6 = np.zeros((NUM_STEPS, 2))
    acceleration_P7 = np.zeros((NUM_STEPS, 2))
    acceleration_Foot = np.zeros((NUM_STEPS, 2))
    
    # Initialize array to store angular acceleration for each crank angle
    alpha_B = np.zeros(NUM_STEPS)
    alpha_J = np.zeros(NUM_STEPS)
    alpha_C = np.zeros(NUM_STEPS)
    alpha_K = np.zeros(NUM_STEPS)
    alpha_D = np.zeros(NUM_STEPS)
    alpha_E = np.zeros(NUM_STEPS)
    alpha_F = np.zeros(NUM_STEPS)
    alpha_G = np.zeros(NUM_STEPS)
    alpha_H = np.zeros(NUM_STEPS)
    alpha_I = np.zeros(NUM_STEPS)
    
    
    # * Loop through each crank angle and solve for each angle *
    for step, theta_m in enumerate(THETA_M_ARRAY):
        
        # ! Solve Position, Velocity & Acceleration for P1 !
        position_P1[step] = _solve.solve_position_P1(O4, LINK_M, theta_m)
        velocity_P1[step] = _solve.solve_velocity_P1(LINK_M, theta_m, OMEGA_M)
        acceleration_P1[step] = _solve.solve_acceleration_P1(LINK_M, theta_m, OMEGA_M, ALPHA_M)
        
        # ! Solve for Position, Velocity, & Acceleration for P2 !
        position_P2[step] = _solve.solve_position_P2(O2, position_P1[step], LINK_B, LINK_J)
        velocity_P2[step], omega_B[step], omega_J[step] = _solve.solve_velocity_P2(O2, position_P1[step], position_P2[step], velocity_P1[step])
        acceleration_P2[step], alpha_B[step], alpha_J[step] = _solve.solve_acceleration_P2(O2, position_P1[step], position_P2[step], acceleration_P1[step], omega_B[step], omega_J[step])
        
        # ! Solve for Position, Velocity, & Acceleration for P4 !
        position_P4[step] = _solve.solve_position_P4(O2, position_P2[step], LINK_D, LINK_E)
        velocity_P4[step], omega_D[step], omega_E[step] = _solve.solve_velocity_P4(O2, position_P2[step], position_P4[step], velocity_P2[step])
        acceleration_P4[step], alpha_D[step], alpha_E[step] = _solve.solve_acceleration_P4(O2, position_P2[step], position_P4[step], acceleration_P2[step], omega_D[step], omega_E[step])
        
        # ! Solve for Position, Velocity, & Acceleration for P5 !
        position_P5[step] = _solve.solve_position_P5(O2, position_P1[step], LINK_C, LINK_K)
        velocity_P5[step], omega_C[step], omega_K[step] = _solve.solve_velocity_P5(O2, position_P1[step], position_P5[step], velocity_P1[step])
        acceleration_P5[step], alpha_C[step], alpha_K[step] = _solve.solve_acceleration_P5(O2, position_P1[step], position_P5[step], acceleration_P1[step], omega_C[step], omega_K[step])
        
        # ! Solve for Position, Velocity, & Acceleration for P6 !
        position_P6[step] = _solve.solve_position_P6(position_P4[step], position_P5[step], LINK_F, LINK_G)
        velocity_P6[step], omega_F[step], omega_G[step] = _solve.solve_velocity_P6(position_P4[step], position_P5[step], position_P6[step], velocity_P4[step], velocity_P5[step])
        acceleration_P6[step], alpha_F[step], alpha_G[step] = _solve.solve_acceleration_P6(position_P4[step], position_P5[step], position_P6[step],acceleration_P4[step], acceleration_P5[step], omega_F[step], omega_G[step])
        
        # ! Solve for Position, Velocity, & Acceleration for P7 !
        position_P7[step] = _solve.solve_position_P7(position_P6[step], position_P5[step], LINK_H, LINK_I)
        velocity_P7[step], omega_H[step], omega_I[step] = _solve.solve_velocity_P7(position_P5[step], position_P6[step], position_P7[step], velocity_P5[step], velocity_P6[step])
        acceleration_P7[step], alpha_H[step], alpha_I[step] = _solve.solve_acceleration_P7(position_P5[step], position_P6[step], position_P7[step],acceleration_P5[step], acceleration_P6[step], omega_H[step], omega_I[step])
        
        # ! Solve for Velocity & Acceleration of Foot Point P7 !
        velocity_Foot[step] = _solve.solve_velocity_foot(position_P5[step], position_P7[step], velocity_P5[step], omega_I[step])
        acceleration_Foot[step] = _solve.solve_acceleration_foot(position_P5[step], position_P7[step], acceleration_P5[step], omega_I[step], alpha_I[step])
    
    
    # ! Create Position Figures for Each Point !
    #mechanism_path, mechanism_names, position_path, position_names = _position.create_position_figures(CRANK_ANGLE_PLOT, O2, O4, position_P1, position_P2, position_P4, position_P5, position_P6, position_P7)

    # ! Create Velocity Figures for Each Point !
    #velocity_path, velocity_names = _velocity.create_velocity_figures(CRANK_ANGLE_PLOT, velocity_P1, velocity_P2, velocity_P4, velocity_P5, velocity_P6, velocity_P7, velocity_Foot, omega_B, omega_J, omega_C, omega_K, omega_D, omega_E, omega_F, omega_G, omega_H, omega_I)
    
    # ! Create Acceleration Figures for Each Point !
    #acceleration_path, acceleration_names = _acceleration.create_acceleration_figures(CRANK_ANGLE_PLOT, acceleration_P1, acceleration_P2, acceleration_P4, acceleration_P5, acceleration_P6, acceleration_P7, acceleration_Foot, alpha_B, alpha_J, alpha_C, alpha_K, alpha_D, alpha_E, alpha_F, alpha_G, alpha_H, alpha_I)
    
    # ! Single Configuration Vector Figures for Each Point !
    #vector_path, vector_names = _vectors.create_vector_figures(0, velocity_P1, velocity_P2, velocity_P4, velocity_P5, velocity_P6, velocity_Foot, acceleration_P1, acceleration_P2, acceleration_P4, acceleration_P5, acceleration_P6, acceleration_Foot)
    
    # ! Create Summary Tables for Angular Velocity & Angular Acceleration !
    table_path, table_names = _table.create_angular_summary_tables(0, OMEGA_M, omega_B, omega_J, omega_C, omega_K, omega_D, omega_E, omega_F, omega_G, omega_H, omega_I, ALPHA_M, alpha_B, alpha_J, alpha_C, alpha_K, alpha_D, alpha_E, alpha_F, alpha_G, alpha_H, alpha_I, decimals=3)
    
    
    # ! Save Figures !
    save_figures(mechanism_path, mechanism_names, folder_name="MechanismFigures")
    save_figures(position_path, position_names, folder_name="PositionFigures")
    save_figures(velocity_path, velocity_names, folder_name="VelocityFigures")
    save_figures(acceleration_path, acceleration_names, folder_name="AccelerationFigures")
    save_figures(vector_path, vector_names, folder_name="VectorFigures")
    save_figures(table_path, table_names, folder_name="TableFigures")

    
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()