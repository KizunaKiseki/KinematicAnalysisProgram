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
from lib._Velocity import append_angular_velocity_figures


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
        figure_name = f"{figure_id:02d}_{analysis_type}_{subject}_{extra}"
    else:
        figure_title = f"{figure_id}: {analysis_type} {subject}"
        figure_name = f"{figure_id:02d}_{analysis_type}_{subject}"
        
    # Clean File Name
    figure_name = (figure_name.replace(" ", "_").replace("-", "_").replace("+", ""). replace(":", "").replace(".", "").replace("(", "").replace(")", ""))
    
    
    return figure_title, figure_name


def append_point_acceleration_figures(acceleration_path : list, acceleration_names : list, figure_number : int, crank_angle_plot : np.ndarray, acceleration_array : np.ndarray, point_label : str) -> int:
    """
    Appends acceleration figures for a specific point to the acceleration path and names lists.
    
    Args:
        acceleration_path (list): List to store acceleration figure objects.
        acceleration_names (list): List to store acceleration figure file names.
        figure_number (int): Current figure number.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        acceleration_array (np.ndarray): Acceleration array for the specific point.
        point_label (str): Label for the point (e.g., "P1", "P2").
    
    Returns:
        figure_number (int): Updated figure number.
    """
    # ! Acceleration Figures for X-Component !
    title, name = make_figure_label(figure_number, "Acceleration", f"Point {point_label}", "X-Component")
    ax_figure = _plot.plot_acceleration_figure(crank_angle_plot, acceleration_array, 0, point_label, title)
    acceleration_path.append(ax_figure)
    acceleration_names.append(name)
    figure_number += 1
    
    # ! Acceleration Figures for Y-Component !
    title, name = make_figure_label(figure_number, "Acceleration", f"Point {point_label}", "Y-Component")
    ay_figure = _plot.plot_acceleration_figure(crank_angle_plot, acceleration_array, 1, point_label, title)
    acceleration_path.append(ay_figure)
    acceleration_names.append(name)
    figure_number += 1
    
    # ! Acceleration Figures for Magnitude !
    title, name = make_figure_label(figure_number, "Acceleration", f"Point {point_label}", "Magnitude")
    magnitude_figure = _plot.plot_acceleration_figure(crank_angle_plot, acceleration_array, 2, point_label, title)
    acceleration_path.append(magnitude_figure)
    acceleration_names.append(name)
    figure_number += 1
    
    
    return figure_number


def append_angular_acceleration_figures(acceleration_path : list, acceleration_names : list, figure_number : int, crank_angle_plot : np.ndarray, alpha_array : np.ndarray, link_label : str) -> int:
    """
    Appends one angular acceleration figure.
    
    Args:
        acceleration_path (list): List to store acceleration figure objects.
        acceleration_names (list): List to store acceleration figure file names.
        figure_number (int): Current figure number.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        alpha_array (np.ndarray): Angular acceleration array for the specific link.
        link_label (str): Label for the link (e.g., "B", "C").
        
    Returns:
        figure_number (int): Updated figure number.
    """
    # ! Angular Acceleration Figure for Link !
    title, name = make_figure_label(figure_number, "Acceleration", f"Link {link_label}", "Angular Acceleration")
    alpha_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, alpha_array, link_label, title)
    acceleration_path.append(alpha_figure)
    acceleration_names.append(name)
    figure_number += 1
    
    
    return figure_number 


def create_acceleration_figures(crank_angle_plot: np.ndarray, accel_P1: np.ndarray, accel_P2: np.ndarray, accel_P4: np.ndarray, accel_P5: np.ndarray, accel_P6: np.ndarray, accel_P7: np.ndarray, accel_Foot: np.ndarray, 
                                alphaB: np.ndarray, alphaJ: np.ndarray, alphaC: np.ndarray, alphaK: np.ndarray, alphaD: np.ndarray, alphaE: np.ndarray, alphaF: np.ndarray, alphaG: np.ndarray, alphaH: np.ndarray, alphaI: np.ndarray) -> tuple[list, list]:
    """
    Creates all acceleration analysis figures for the Theo Jansen mechanism.
    
    Args:
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
        accel_P1 (np.ndarray): Point P1 acceleration array.
        accel_P2 (np.ndarray): Point P2 acceleration array.
        accel_P4 (np.ndarray): Point P4 acceleration array.
        accel_P5 (np.ndarray): Point P5 acceleration array.
        accel_P6 (np.ndarray): Point P6 acceleration array.
        accel_P7 (np.ndarray): Point P7 acceleration array.
        accel_Foot (np.ndarray): Point Pfoot acceleration array.
        alphaB (np.ndarray): Link B angular acceleration array.
        alphaJ (np.ndarray): Link J angular acceleration array.
        alphaC (np.ndarray): Link C angular acceleration array.
        alphaK (np.ndarray): Link K angular acceleration array.
        alphaD (np.ndarray): Link D angular acceleration array.
        alphaE (np.ndarray): Link E angular acceleration array.
        alphaF (np.ndarray): Link F angular acceleration array.
        alphaG (np.ndarray): Link G angular acceleration array.
        alphaH (np.ndarray): Link H angular acceleration array.
        alphaI (np.ndarray): Link I angular acceleration array.
    
    Returns:
        figure_path (list): List of Matplotlib figure objects.
        figure_names (list): List of figure file names.
    """
    # Initialize lists to store figure paths and names
    acceleration_path = []
    acceleration_names = []
    figure_number = 1
    
    
    # ? Point Acceleration Figures ?
    point_acceleration_data = [
        ("P1", accel_P1),
        ("P2", accel_P2),
        ("P4", accel_P4),
        ("P5", accel_P5),
        ("P6", accel_P6),
        ("P7", accel_Foot)
    ]
    
    for point_label, accel_array in point_acceleration_data:
        figure_number = append_point_acceleration_figures(acceleration_path, acceleration_names, figure_number, crank_angle_plot, accel_array, point_label)
        
        
    # ? Angular Acceleration Figures ?
    angular_acceleration_data = [
        ("B", alphaB),
        ("J", alphaJ),
        ("C", alphaC),
        ("K", alphaK),
        ("D", alphaD),
        ("E", alphaE),
        ("F", alphaF),
        ("G", alphaG),
        ("H", alphaH),
        ("I", alphaI)
    ]
    
    for link_label, alpha_array in angular_acceleration_data:
        figure_number = append_angular_acceleration_figures(acceleration_path, acceleration_names, figure_number, crank_angle_plot, alpha_array, link_label)
    
        
    return acceleration_path, acceleration_names

