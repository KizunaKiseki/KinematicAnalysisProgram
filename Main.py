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
    position_path = []
    velocity_path = []
    acceleration_path = []
    position_names = []
    velocity_names = []
    acceleration_names = []
    single_configuration_path = []
    single_configuration_names = []
    
    # ! Solve across all crank angles !
    # Initialize array to store positions for each crank angle
    array_P1 = np.zeros((NUM_STEPS, 2))  
    array_P2 = np.zeros((NUM_STEPS, 2))
    array_P4 = np.zeros((NUM_STEPS, 2))
    array_P5 = np.zeros((NUM_STEPS, 2))
    array_P6 = np.zeros((NUM_STEPS, 2))
    array_P7 = np.zeros((NUM_STEPS, 2))
    
    # Initialize array to store velocity for each crank angle
    array_V1 = np.zeros((NUM_STEPS, 2))
    array_V2 = np.zeros((NUM_STEPS, 2))
    array_V4 = np.zeros((NUM_STEPS, 2))
    array_V5 = np.zeros((NUM_STEPS, 2))
    array_V6 = np.zeros((NUM_STEPS, 2))
    array_V7 = np.zeros((NUM_STEPS, 2))
    array_Vfoot = np.zeros((NUM_STEPS, 2))
    
    # Initialize array to store angular velocity for each crank angle
    array_omegaB = np.zeros(NUM_STEPS)
    array_omegaJ = np.zeros(NUM_STEPS)
    array_omegaC = np.zeros(NUM_STEPS)
    array_omegaK = np.zeros(NUM_STEPS)
    array_omegaD = np.zeros(NUM_STEPS)
    array_omegaE = np.zeros(NUM_STEPS)
    array_omegaF = np.zeros(NUM_STEPS)
    array_omegaG = np.zeros(NUM_STEPS)
    array_omegaH = np.zeros(NUM_STEPS)
    array_omegaI = np.zeros(NUM_STEPS)
    
    # Initialize array to store acceleration for each crank angle
    array_A1 = np.zeros((NUM_STEPS, 2))
    array_A2 = np.zeros((NUM_STEPS, 2))
    array_A4 = np.zeros((NUM_STEPS, 2))
    array_A5 = np.zeros((NUM_STEPS, 2))
    array_A6 = np.zeros((NUM_STEPS, 2))
    array_A7 = np.zeros((NUM_STEPS, 2))
    array_Afoot = np.zeros((NUM_STEPS, 2))
    
    # Initialize array to store angular acceleration for each crank angle
    array_alphaB = np.zeros(NUM_STEPS)
    array_alphaJ = np.zeros(NUM_STEPS)
    array_alphaC = np.zeros(NUM_STEPS)
    array_alphaK = np.zeros(NUM_STEPS)
    array_alphaD = np.zeros(NUM_STEPS)
    array_alphaE = np.zeros(NUM_STEPS)
    array_alphaF = np.zeros(NUM_STEPS)
    array_alphaG = np.zeros(NUM_STEPS)
    array_alphaH = np.zeros(NUM_STEPS)
    array_alphaI = np.zeros(NUM_STEPS)
    
    
    # * Loop through each crank angle and solve for each angle *
    for step, theta_m in enumerate(THETA_M_ARRAY):
        # ? Solve for Point P1 across all Crank Angles ?
        array_P1[step] = _solve.solve_point_1(O4, LINK_M, theta_m)
        
        # ! Solve for Velocity of Point P1 across all Crank Angles !
        array_V1[step] = _solve.solve_velocity_1(LINK_M, theta_m, OMEGA_M)
        
        # * Solve for Acceleration of Point P1 across all Crank Angles *
        array_A1[step] = _solve.solve_acceleration_1(LINK_M, theta_m, OMEGA_M, ALPHA_M)
        
        # ? Solve for Point P2 across all Crank Angles ?
        array_P2[step] = _solve.solve_point_2(O2, array_P1[step], LINK_B, LINK_J)
        
        # ! Solve for Velocity & Angular Velocity of Point P2 across all Crank Angles !
        array_V2[step], array_omegaB[step], array_omegaJ[step] = _solve.solve_velocity_2(O2, array_P1[step], array_P2[step], 
                                                                                         array_V1[step])
        
        # * Solve for Acceleration of Point P2 across all Crank Angles *
        array_A2[step], array_alphaB[step], array_alphaJ[step] = _solve.solve_acceleration_2(O2, array_P1[step], array_P2[step],
                                                                                         array_A1[step], array_omegaB[step], array_omegaJ[step])
        
        # ? Solve for Point P4 across all Crank Angles ?
        array_P4[step] = _solve.solve_point_4(O2, array_P2[step], LINK_D, LINK_E)
        
        # ! Solve for Velocity & Angular Velocity of Point P4 across all Crank Angles !
        array_V4[step], array_omegaD[step], array_omegaE[step] = _solve.solve_velocity_4(O2, array_P2[step], array_P4[step], 
                                                                                         array_V2[step])
        
        # * Solve for Acceleration of Point P4 across all Crank Angles *
        array_A4[step], array_alphaD[step], array_alphaE[step] = _solve.solve_acceleration_4(O2, array_P2[step], array_P4[step],
                                                                                         array_A2[step], array_omegaD[step], array_omegaE[step])
        
        # ? Solve for Point P5 across all Crank Angles ?
        array_P5[step] = _solve.solve_point_5(O2, array_P1[step], LINK_C, LINK_K)
        
        # ! Solve for Velocity & Angular Velocity of Point P5 across all Crank Angles !
        array_V5[step], array_omegaC[step], array_omegaK[step] = _solve.solve_velocity_5(O2, array_P1[step], array_P5[step], 
                                                                                         array_V1[step])
        
        # * Solve for Acceleration of Point P5 across all Crank Angles *
        array_A5[step], array_alphaC[step], array_alphaK[step] = _solve.solve_acceleration_5(O2, array_P1[step], array_P5[step], 
                                                                                         array_A1[step], array_omegaC[step], array_omegaK[step])
        
        # ? Solve for Point P6 across all Crank Angles ?
        array_P6[step] = _solve.solve_point_6(array_P4[step], array_P5[step], LINK_F, LINK_G)
        
        # ! Solve for Velocity & Angular Velocity of Point P6 across all Crank Angles !
        array_V6[step], array_omegaF[step], array_omegaG[step] = _solve.solve_velocity_6(array_P4[step], array_P5[step], array_P6[step], 
                                                                                         array_V4[step], array_V5[step])
        
        # * Solve for Acceleration of Point P6 across all Crank Angles *
        array_A6[step], array_alphaF[step], array_alphaG[step] = _solve.solve_acceleration_6(array_P4[step], array_P5[step], array_P6[step],
                                                                                         array_A4[step], array_A5[step], array_omegaF[step], array_omegaG[step])
        
        # ? Solve for Point P7 across all Crank Angles ?
        array_P7[step] = _solve.solve_point_7(array_P6[step], array_P5[step], LINK_H, LINK_I)
        
        # ! Solve for Velocity & Angular Velocity of Point P7 across all Crank Angles !
        array_V7[step], array_omegaH[step], array_omegaI[step] = _solve.solve_velocity_7(array_P5[step], array_P6[step], array_P7[step], 
                                                                                         array_V5[step], array_V6[step])
        
        # * Solve for Acceleration of Point P7 across all Crank Angles *
        array_A7[step], array_alphaH[step], array_alphaI[step] = _solve.solve_acceleration_7(array_P5[step], array_P6[step], array_P7[step],
                                                                                         array_A5[step], array_A6[step], array_omegaH[step], array_omegaI[step])
        
        # ! Solve for Velocity of Foot Point P7 across all Crank Angles !
        array_Vfoot[step] = _solve.solve_velocity_foot(array_P5[step], array_P7[step], array_V5[step], array_omegaI[step])
        
        # * Solve for Acceleration of Foot Point P7 across all Crank Angles *
        array_Afoot[step] = _solve.solve_acceleration_foot(array_P5[step], array_P7[step], array_A5[step], array_omegaI[step], array_alphaI[step])
    
    # ! Create Position Figures for Each Point !
    #position_path, position_names = _position.create_position_figures(CRANK_ANGLE_PLOT, O2, O4, array_P1, array_P2, array_P4, array_P5, array_P6, array_P7)

    # ! Create Velocity Figures for Each Point !
    #velocity_path, velocity_names = _velocity.create_velocity_figures(CRANK_ANGLE_PLOT, array_V1, array_V2, array_V4, array_V5, array_V6, array_V7, array_Vfoot, array_omegaB, array_omegaJ, array_omegaC, array_omegaK, array_omegaD, array_omegaE, array_omegaF, array_omegaG, array_omegaH, array_omegaI)
    
    # ! Create Acceleration Figures for Each Point !
    #acceleration_path, acceleration_names = _acceleration.create_acceleration_figures(CRANK_ANGLE_PLOT, array_A1, array_A2, array_A4, array_A5, array_A6, array_A7, array_Afoot, array_alphaB, array_alphaJ, array_alphaC, array_alphaK, array_alphaD, array_alphaE, array_alphaF, array_alphaG, array_alphaH, array_alphaI)
    

    
    # ! Save Figures !
    save_figures(position_path, position_names, folder_name="Position")
    save_figures(velocity_path, velocity_names, folder_name="Velocity")
    save_figures(acceleration_path, acceleration_names, folder_name="Acceleration")

    
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()