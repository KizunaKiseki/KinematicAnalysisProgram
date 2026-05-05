# -*- coding: utf-8 -*-
"""
TITLE = [INSERT TITLE HERE]
DATE  = 2026.01.01
_____________________________________________________________________
DESCRIPTION:
1. [Insert Description Here]
2. ...
_____________________________________________________________________
HOW-TO:
-> Click on the button
-> ...
_____________________________________________________________________
UPDATES:
- [2026.02.02] - 1.1 ...
- [2026.01.01] - 1.0 RELEASE
_____________________________________________________________________
TO-DO:
- Describe Next Features
- ...
_____________________________________________________________________
AUTHOR : [Author]
"""

# * IMPORTS *
# ? ================================================================ ?

# ! PYTHON TEMPLATES & LIBRARIES !
import numpy as np

# ! PROJECT MODULES !
import lib._Plot as _plot



# * FUNCTION *
# ? ================================================================ ?

def create_vector_figures(step : int, array_V1 : np.ndarray, array_V2 : np.ndarray, array_V4 : np.ndarray, array_V5 : np.ndarray, 
                          array_V6 : np.ndarray, array_vFoot : np.ndarray, array_A1 : np.ndarray, 
                          array_A2 : np.ndarray, array_A4 : np.ndarray, array_A5 : np.ndarray, array_A6 : np.ndarray, 
                          array_aFoot : np.ndarray) -> tuple[list, list]:
    """
    Creates velocity and acceleration vectors figures for one crank position.
    
    Args:
        step (int): The current step of the analysis.
        array_V1 (np.ndarray): Velocity vector of link 1.
        array_V2 (np.ndarray): Velocity vector of link 2.
        array_V4 (np.ndarray): Velocity vector of link 4.
        array_V5 (np.ndarray): Velocity vector of link 5.
        array_V6 (np.ndarray): Velocity vector of link 6.
        array_vFoot (np.ndarray): Velocity vector of the foot.
        array_A1 (np.ndarray): Acceleration vector of link 1.
        array_A2 (np.ndarray): Acceleration vector of link 2.
        array_A4 (np.ndarray): Acceleration vector of link 4.
        array_A5 (np.ndarray): Acceleration vector of link 5.
        array_A6 (np.ndarray): Acceleration vector of link 6.
        array_aFoot (np.ndarray): Acceleration vector of the foot.
    
    Returns:
        vector_path (list): A list of matplotlib path objects for the velocity vectors.
        vector_names (list): A list of names corresponding to each velocity vector.
    
    Raises:
    """
    # Initialize lists to store vector paths and names
    vector_path = []
    vector_names = []
    
    # ! Velocity Vector Figures !
    velocity_vectors = {
        "P1": array_V1[step],
        "P2": array_V2[step],
        "P4": array_V4[step],
        "P5": array_V5[step],
        "P6": array_V6[step],
        "P7": array_vFoot[step]
    }
    
    for point_label, vector in velocity_vectors.items():
        figure = _plot.plot_vector_figure(vector=vector, vector_label=rf"$V_{{{point_label}}}$", title=f" Velocity Vector of Point {point_label}", x_label="Vx", y_label="Vy", units="mm/s", theta_label=rf"$\theta_{{V, {point_label}}}$")
    
        vector_path.append(figure)
        vector_names.append(f"{point_label}_Velocity_Vector")
    
    # ! Acceleration Vector Figures !
    acceleration_vectors = {
        "P1": array_A1[step],
        "P2": array_A2[step],
        "P4": array_A4[step],
        "P5": array_A5[step],
        "P6": array_A6[step],
        "P7": array_aFoot[step]
    }
    
    for point_label, vector in acceleration_vectors.items():
        figure = _plot.plot_vector_figure(vector=vector, vector_label=rf"$A_{{{point_label}}}$", title=f" Acceleration Vector of Point {point_label}", x_label="Ax", y_label="Ay", units="mm/s²", theta_label=rf"$\theta_{{A, {point_label}}}$")
        
        vector_path.append(figure)
        vector_names.append(f"{point_label}_Acceleration_Vector")
    
    
    return vector_path, vector_names

