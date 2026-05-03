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

def create_velocity_figures(crank_angle_plot: np.ndarray, array_V1 : np.ndarray, array_V2 : np.ndarray, array_V5 : np.ndarray, array_omegaB : np.ndarray, 
                            array_omegaJ : np.ndarray, array_omegaC : np.ndarray, array_omegaK : np.ndarray) -> tuple[list, list]:
    """
    Creates velocity figures for each point and returns their paths and names.
    
    Args:
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        array_V1 (np.ndarray): Velocity array for Point P1.
        array_V2 (np.ndarray): Velocity array for Point P2.
        array_V5 (np.ndarray): Velocity array for Point P5.
        array_omegaB (np.ndarray): Angular velocity array for Point B.
        array_omegaJ (np.ndarray): Angular velocity array for Point J.
        array_omegaC (np.ndarray): Angular velocity array for Point C.
        array_omegaK (np.ndarray): Angular velocity array for Point K.

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
    v2_figures(figure_path, figure_names, array_V2, crank_angle_plot)
    v5_figures(figure_path, figure_names, array_V5, crank_angle_plot)
    
    
    
    # * Create Angular Velocity Figures for Each Link *
    omegaB_figures(figure_path, figure_names, array_omegaB, crank_angle_plot)
    omegaJ_figures(figure_path, figure_names, array_omegaJ, crank_angle_plot)
    omegaC_figures(figure_path, figure_names, array_omegaC, crank_angle_plot)
    omegaK_figures(figure_path, figure_names, array_omegaK, crank_angle_plot)
    
    
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
    v1_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V1, 0, "P1", "Figure 24: Velocity of Point P1 vs Crank Angle (x-component)")
    v1_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V1, 1, "P1", "Figure 25: Velocity of Point P1 vs Crank Angle (y-component)")
    v1_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V1, "P1", "Figure 26: Speed of Point P1 vs Crank Angle")
    
    
    # Append V1 Figures to Figure Path
    figure_path.extend([v1_x_figure, v1_y_figure, v1_speed_figure])
    
    # Append V1 Figure Names to Figure Names List
    figure_names.extend(["P1_x_Vel", "P1_y_Vel", "P1_speed"])
    
    

def v2_figures(figure_path : list, figure_names : list, array_V2 : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for Point P2 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V2 (np.ndarray): Velocity array for Point P2.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Point P2 !
    v2_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V2, 0, "P2", "Figure 27: Velocity of Point P2 vs Crank Angle (x-component)")
    v2_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V2, 1, "P2", "Figure 28: Velocity of Point P2 vs Crank Angle (y-component)")
    v2_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V2, "P2", "Figure 29: Speed of Point P2 vs Crank Angle")
    
    
    # Append V2 Figures to Figure Path
    figure_path.extend([v2_x_figure, v2_y_figure, v2_speed_figure])
    
    # Append V2 Figure Names to Figure Names List
    figure_names.extend(["P2_x_Vel", "P2_y_Vel", "P2_speed"])
    

def v5_figures(figure_path : list, figure_names : list, array_V5 : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for Point P5 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V5 (np.ndarray): Velocity array for Point P5.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Point P5 !
    v5_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V5, 0, "P5", "Figure 27: Velocity of Point P5 vs Crank Angle (x-component)")
    v5_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V5, 1, "P5", "Figure 28: Velocity of Point P5 vs Crank Angle (y-component)")
    v5_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V5, "P5", "Figure 29: Speed of Point P5 vs Crank Angle")
    
    
    # Append V5 Figures to Figure Path
    figure_path.extend([v5_x_figure, v5_y_figure, v5_speed_figure])
    
    # Append V5 Figure Names to Figure Names List
    figure_names.extend(["P5_x_Vel", "P5_y_Vel", "P5_speed"])


def omegaB_figures(figure_path : list, figure_names : list, array_omegaB : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link B to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaB (np.ndarray): Angular velocity array for Link B.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link B !
    omegaB_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaB, "B", "Figure 30: Angular Velocity of Link B vs Crank Angle")
    
    
    # Append OmegaB Figure to Figure Path
    figure_path.extend([omegaB_figure])
    
    # Append OmegaB Figure Name to Figure Names List
    figure_names.extend(["B_angular_velocity"])


def omegaJ_figures(figure_path : list, figure_names : list, array_omegaJ : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link J to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaJ (np.ndarray): Angular velocity array for Link J.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link J !
    omegaJ_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaJ, "J", "Figure 31: Angular Velocity of Link J vs Crank Angle")
    
    
    # Append OmegaJ Figure to Figure Path
    figure_path.extend([omegaJ_figure])
    
    # Append OmegaJ Figure Name to Figure Names List
    figure_names.extend(["J_angular_velocity"])


def omegaC_figures(figure_path : list, figure_names : list, array_omegaC : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link C to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaC (np.ndarray): Angular velocity array for Link C.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link C !
    omegaC_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaC, "C", "Figure 32: Angular Velocity of Link C vs Crank Angle")
    
    
    # Append OmegaC Figure to Figure Path
    figure_path.extend([omegaC_figure])
    
    # Append OmegaC Figure Name to Figure Names List
    figure_names.extend(["C_angular_velocity"])
    
    
def omegaK_figures(figure_path : list, figure_names : list, array_omegaK : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link K to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaK (np.ndarray): Angular velocity array for Link K.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link K !
    omegaK_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaK, "K", "Figure 33: Angular Velocity of Link K vs Crank Angle")
    
    
    # Append OmegaK Figure to Figure Path
    figure_path.extend([omegaK_figure])
    
    # Append OmegaK Figure Name to Figure Names List
    figure_names.extend(["K_angular_velocity"])