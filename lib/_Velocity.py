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
        figure_name = f"Figure{figure_number:02d}_{analysis_type}_{subject}_{extra}"
    else:
        figure_title = f"{figure_id}: {analysis_type} {subject}"
        figure_name = f"Figure{figure_number:02d}_{analysis_type}_{subject}"
        
    # Clean File Name
    figure_name = (figure_name.replace(" ", "_").replace("-", "_").replace("+", ""). replace(":", "").replace(".", "").replace("(", "").replace(")", ""))
    
    
    return figure_title, figure_name



def append_point_velocity_figures(velocity_path : list, velocity_names : list, figure_number : int, crank_angle_plot : np.ndarray, velocity_array : np.ndarray, point_label : str) -> int:
    """
    Appends velocity figures for a specific point to the velocity path and names lists.
    
    Args:
        velocity_path (list): List to store velocity figure objects.
        velocity_names (list): List to store velocity figure file names.
        figure_number (int): Current figure number.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        velocity_array (np.ndarray): Velocity array for the specific point.
        point_label (str): Label for the point (e.g., "P1", "P2").
    
    Returns:
        figure_number (int): Updated figure number.
    """
    # ! Velocity Figures for X-Component !
    title, name = make_figure_label(figure_number, "Velocity", f"Point {point_label}", "X-Component")
    vx_figure = _plot.plot_velocity_figure(crank_angle_plot, velocity_array, 0, point_label, title)
    velocity_path.append(vx_figure)
    velocity_names.append(name)
    figure_number += 1
    
    # ! Velocity Figures for Y-Component !
    title, name = make_figure_label(figure_number, "Velocity", f"Point {point_label}", "Y-Component")
    vy_figure = _plot.plot_velocity_figure(crank_angle_plot, velocity_array, 1, point_label, title)
    velocity_path.append(vy_figure)
    velocity_names.append(name)
    figure_number += 1
    
    # ! Velocity Figures for Speed !
    title, name = make_figure_label(figure_number, "Velocity", f"Point {point_label}", "Magnitude")
    speed_figure = _plot.plot_speed_figure(crank_angle_plot, velocity_array, point_label, title)
    velocity_path.append(speed_figure)
    velocity_names.append(name)
    figure_number += 1
    
    
    return figure_number


def append_angular_velocity_figures(velocity_path : list, velocity_names : list, figure_number : int, crank_angle_plot : np.ndarray, omega_array : np.ndarray, link_label : str) -> int:
    """
    Appends one angular velocity figure.
    
    Args:
        velocity_path (list): List to store velocity figure objects.
        velocity_names (list): List to store velocity figure file names.
        figure_number (int): Current figure number.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        omega_array (np.ndarray): Angular velocity array for the specific link.
        link_label (str): Label for the link (e.g., "B", "C").
        
    Returns:
        figure_number (int): Updated figure number.
    """
    # ! Angular Velocity Figure for Link !
    title, name = make_figure_label(figure_number, "Velocity", f"Link {link_label}", "Angular Velocity")
    omega_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, omega_array, link_label, title)
    velocity_path.append(omega_figure)
    velocity_names.append(name)
    figure_number += 1
    
    
    return figure_number 
    

def create_velocity_figures(crank_angle_plot: np.ndarray, velocity_P1 : np.ndarray, velocity_P2 : np.ndarray, velocity_P4 : np.ndarray, velocity_P5 : np.ndarray, velocity_P6 : np.ndarray, velocity_P7 : np.ndarray, velocity_foot : np.ndarray,
                            omegaB : np.ndarray, omegaJ : np.ndarray, omegaC : np.ndarray, omegaK : np.ndarray, omegaD : np.ndarray, omegaE : np.ndarray, omegaF : np.ndarray, omegaG : np.ndarray, omegaH : np.ndarray, omegaI : np.ndarray) -> tuple[list, list]:
    """
    Creates velocity figures for each point and returns their paths and names.
    
    Args:
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        velocity_P1 (np.ndarray): Velocity array for Point P1.
        velocity_P2 (np.ndarray): Velocity array for Point P2.
        velocity_P4 (np.ndarray): Velocity array for Point P4.
        velocity_P5 (np.ndarray): Velocity array for Point P5.
        velocity_P6 (np.ndarray): Velocity array for Point P6.
        velocity_P7 (np.ndarray): Velocity array for Point P7.
        velocity_foot (np.ndarray): Velocity array for the foot point P7.
        omegaB (np.ndarray): Angular velocity array for Link B.
        omegaJ (np.ndarray): Angular velocity array for Link J.
        omegaC (np.ndarray): Angular velocity array for Link C.
        omegaK (np.ndarray): Angular velocity array for Link K.
        omegaD (np.ndarray): Angular velocity array for Link D.
        omegaE (np.ndarray): Angular velocity array for Link E.
        omegaF (np.ndarray): Angular velocity array for Link F.
        omegaG (np.ndarray): Angular velocity array for Link G.
        omegaH (np.ndarray): Angular velocity array for Link H.
        omegaI (np.ndarray): Angular velocity array for Link I.

    Returns:
        figure_path (list): List of Matplotlib figure objects.
        figure_names (list): List of figure file names.
    
    Raises:
    """
    # Initialize lists to store figures and their names
    velocity_path = []
    velocity_names = []
    figure_number = 1
    
    # ? Point Velocity Figures ?
    point_velocity_data = [
        ("P1", velocity_P1),
        ("P2", velocity_P2),
        ("P4", velocity_P4),
        ("P5", velocity_P5),
        ("P6", velocity_P6),
        ("P7", velocity_foot)
    ]
    
    for point_label, velocity_array in point_velocity_data:
        figure_number = append_point_velocity_figures(velocity_path, velocity_names, figure_number, crank_angle_plot, velocity_array, point_label)
        
    # ? Angular Velocity Figures ?
    angular_velocity_data = [
        ("B", omegaB),
        ("J", omegaJ),
        ("C", omegaC),
        ("K", omegaK),
        ("D", omegaD),
        ("E", omegaE),
        ("F", omegaF),
        ("G", omegaG),
        ("H", omegaH),
        ("I", omegaI)
    ]
    
    for link_label, omega_array in angular_velocity_data:
        figure_number = append_angular_velocity_figures(velocity_path, velocity_names, figure_number, crank_angle_plot, omega_array, link_label)
    
    
    return velocity_path, velocity_names
