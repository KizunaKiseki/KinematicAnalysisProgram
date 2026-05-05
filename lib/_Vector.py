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

def make_figure_label(figure_number: int, analysis_type : str, subject : str, extra : str = "") -> tuple[str, str]:
    """
    Creates a standardized figure title and file name.
    
    Args:
        figure_number (int): Figure number.
        analysis_type (str): Type of analysis (e.g., "Position", "Velocity", "Acceleration").
        subject (str): Subject of the figure (e.g., "P1", "P2").
        extra (str, optional): Additional information for the figure title. Defaults to "".
    
    Returns:
        figure_title (str): Title displayed on the figure.
        figure_name (str): File name used when saving the plot.
    """
    
    figure_id = f"Figure {figure_number:02d}"
    
    if extra:
        figure_title = f"{figure_id}: {analysis_type} {subject} {extra}"
        figure_name = f"Figure{figure_id:02d}_{analysis_type}_{subject}_{extra}"
    else:
        figure_title = f"{figure_id}: {analysis_type} {subject}"
        figure_name = f"Figure{figure_id:02d}_{analysis_type}_{subject}"
        
    # Clean File Name
    figure_name = (figure_name.replace(" ", "_").replace("-", "_").replace("+", ""). replace(":", "").replace(".", "").replace("(", "").replace(")", ""))
    
    
    return figure_title, figure_name


def append_vector_figures(vector_path : list, vector_names : list, figure_number : int, vector_array : np.ndarray, point_label : str, vector_type : str) -> int:
    """
    Appends one velocity or acceleration vector figure.
    
    Args:
        vector_path (list): List to append the figure path to.
        vector_names (list): List to append the figure name to.
        figure_number (int): Current figure number for labeling.
        vector_array (np.ndarray): Array containing the vector data for all points and steps.
        point_label (str): Label of the point for which the vector is being plotted (e.g., "P1").
        vector_type (str): Type of vector being plotted ("Velocity" or "Acceleration").
        
    Returns:
        figure_number (int): Updated figure number after appending the new figure.
        
    Raises:
        ValueError: If the vector_type is not "Velocity" or "Acceleration".
    """
    title, name = make_figure_label(figure_number, "Vector", f"Point {point_label}", vector_type)
    
    if vector_type == "Velocity":
        vector_symbol = "V"
        vector_label = rf"${vector_symbol}_{{{point_label}}}$"
        x_label = r"$V_x$ [mm/s]"
        y_label = r"$V_y$ [mm/s]"
        units = "mm/s"
        theta_label = rf"$\theta_{{V, {point_label}}}$"
    elif vector_type == "Acceleration":
        vector_symbol = "A"
        vector_label = rf"${vector_symbol}_{{{point_label}}}$"
        x_label = r"$A_x$ [mm/s²]"
        y_label = r"$A_y$ [mm/s²]"
        units = "mm/s²"
        theta_label = rf"$\theta_{{A, {point_label}}}$"
    else:
        raise ValueError("Invalid vector type. Must be 'Velocity' or 'Acceleration'.")
    
    figure = _plot.plot_vector_figure(vector_array, vector_label, title, x_label, y_label, units, theta_label)
    vector_path.append(figure)
    vector_names.append(name)
    figure_number += 1
    
    
    return figure_number
    
    
def create_vector_figures(step : int, velocity_P1 : np.ndarray, velocity_P2 : np.ndarray, velocity_P4 : np.ndarray, velocity_P5 : np.ndarray, velocity_P6 : np.ndarray, velocity_Foot : np.ndarray, 
                          accel_P1 : np.ndarray, accel_P2 : np.ndarray, accel_P4 : np.ndarray, accel_P5 : np.ndarray, accel_P6 : np.ndarray, accel_Foot : np.ndarray) -> tuple[list, list]:
    """
    Creates velocity and acceleration vectors figures for one crank position.
    
    Args:
        step (int): The current step of the analysis.
        velocity_P1 (np.ndarray): Velocity vector of point P1.
        velocity_P2 (np.ndarray): Velocity vector of point P2.
        velocity_P4 (np.ndarray): Velocity vector of point P4.
        velocity_P5 (np.ndarray): Velocity vector of point P5.
        velocity_P6 (np.ndarray): Velocity vector of point P6.
        velocity_Foot (np.ndarray): Velocity vector of the foot.
        accel_P1 (np.ndarray): Acceleration vector of point P1.
        accel_P2 (np.ndarray): Acceleration vector of point P2.
        accel_P4 (np.ndarray): Acceleration vector of point P4.
        accel_P5 (np.ndarray): Acceleration vector of point P5.
        accel_P6 (np.ndarray): Acceleration vector of point P6.
        accel_Foot (np.ndarray): Acceleration vector of the foot.
    
    Returns:
        vector_path (list): A list of matplotlib path objects for the velocity vectors.
        vector_names (list): A list of names corresponding to each velocity vector.
    
    Raises:
    """
    # Initialize lists to store vector paths and names
    vector_path = []
    vector_names = []
    figure_number = 1
    
    # ? Velocity Vector Figures ?
    velocity_vector_data = [
        ("P1", velocity_P1),
        ("P2", velocity_P2),
        ("P4", velocity_P4),
        ("P5", velocity_P5),
        ("P6", velocity_P6),
        ("P7", velocity_Foot)
    ]   
    
    for point_label, velocity_array in velocity_vector_data:
        figure_number = append_vector_figures(vector_path, vector_names, figure_number, velocity_array, point_label, "Velocity")
        
    # ? Acceleration Vector Figures ?
    acceleration_vector_data = [
        ("P1", accel_P1),
        ("P2", accel_P2),
        ("P4", accel_P4),
        ("P5", accel_P5),
        ("P6", accel_P6),
        ("P7", accel_Foot)
    ]
    
    for point_label, acceleration_array in acceleration_vector_data:
        figure_number = append_vector_figures(vector_path, vector_names, figure_number, acceleration_array, point_label, "Acceleration")
        
    
    return vector_path, vector_names

