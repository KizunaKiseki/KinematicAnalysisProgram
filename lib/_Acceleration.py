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

def create_acceleration_figures(crank_angle_plot: np.ndarray, array_A1 : np.ndarray) -> tuple[list, list]:
    """
    Creates all acceleration analysis figures for the Theo Jansen mechanism.
    
    Args:
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
        array_A1 (np.ndarray): Point P1 acceleration array.
    
    Returns:
        figure_path (list): List of Matplotlib figure objects.
        figure_names (list): List of figure file names.
    """
    # Initalize lists to store figure paths and names
    figure_path = []
    figure_names = []
    
    # * Create Acceleration Figures for each Point *
    a1_figures(figure_path, figure_names, array_A1, crank_angle_plot)
    
    
    # * Create Angular Acceleration Figures for Each Link *
    
    
    
    return figure_path, figure_names


def a1_figures(figure_path: list, figure_names: list, array_A1: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates acceleration figures for Point P1.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_A1 (np.ndarray): Point P1 acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Acceleration Figures for Point P1 !
    a1_x_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A1, 0, "P1", "Figure 54: P1 X-Acceleration vs Crank Angle")
    a1_y_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A1, 1, "P1", "Figure 55: P1 Y-Acceleration vs Crank Angle")
    a1_magnitude_figure = _plot.plot_acceleration_magnitude_figure(crank_angle_plot, array_A1, "P1", "Figure 56: P1 Acceleration Magnitude vs Crank Angle")


    # Append Figures
    figure_path.extend([a1_x_figure, a1_y_figure, a1_magnitude_figure])
    
    # Append Figure Names
    figure_names.extend(["a1_x_figure", "a1_y_figure", "a1_magnitude_figure"])


