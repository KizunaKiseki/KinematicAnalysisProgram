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

# * VARIABLES *
# ? ================================================================ ?


# * FUNCTION *
# ? ================================================================ ?

def create_velocity_figures(array_V1 : np.ndarray, crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates velocity figures for each point and returns their paths and names.
    
    Args:
        array_V1 (np.ndarray): Velocity array for Point P1.
    
    Returns:
        tuple[list, list]: A tuple containing two lists:
            - figure_path (list): List of paths to the saved figures.
            - figure_names (list): List of figure names.
    
    Raises:
    """
    # Initialize lists to store figures and their names
    figure_path = []
    figure_names = []
    
    # * Create Velocity Figures for Each Point *
    v1_figures(figure_path, figure_names, array_V1, crank_angle_plot)
    
    return figure_path, figure_names
    
    
def v1_figures(figure_path : list, figure_names : list, array_V1 : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for Point P1 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V1 (np.ndarray): Velocity array for Point P1.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Point P1 !
    v1_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V1, 0, "P1", "Velocity of Point P1 vs Crank Angle (x-component)")
    v1_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V1, 1, "P1", "Velocity of Point P1 vs Crank Angle (y-component)")
    v1_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V1, "P1", "Speed of Point P1 vs Crank Angle")
    
    
    # Append V1 Figures to Figure Path
    figure_path.extend([v1_x_figure, v1_y_figure, v1_speed_figure])
    
    # Append V1 Figure Names to Figure Names List
    figure_names.extend(["P1_x_Vel", "P1_y_Vel", "P1_speed"])
    
    

def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass


def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass

def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass


def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass


def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass


def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass


def function_name():
    """
    Summary of what the function does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    
    
    
    pass
    



