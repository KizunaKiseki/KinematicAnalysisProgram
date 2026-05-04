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

def create_acceleration_figures(crank_angle_plot: np.ndarray, array_A1 : np.ndarray, array_A2 : np.ndarray, array_A4 : np.ndarray, 
                                array_A5 : np.ndarray, array_A6 : np.ndarray, array_A7 : np.ndarray, array_Afoot : np.ndarray, 
                                array_alphaB : np.ndarray, array_alphaJ : np.ndarray, array_alphaC : np.ndarray, 
                                array_alphaK : np.ndarray, array_alphaD : np.ndarray, array_alphaE : np.ndarray, 
                                array_alphaF : np.ndarray, array_alphaG : np.ndarray, array_alphaH : np.ndarray, 
                                array_alphaI : np.ndarray) -> tuple[list, list]:
    """
    Creates all acceleration analysis figures for the Theo Jansen mechanism.
    
    Args:
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
        array_A1 (np.ndarray): Point P1 acceleration array.
        array_A2 (np.ndarray): Point P2 acceleration array.
        array_A4 (np.ndarray): Point P4 acceleration array.
        array_A5 (np.ndarray): Point P5 acceleration array.
        array_A6 (np.ndarray): Point P6 acceleration array.
        array_A7 (np.ndarray): Point P7 acceleration array.
        array_Afoot (np.ndarray): Point Pfoot acceleration array.
        array_alphaB (np.ndarray): Link B angular acceleration array.
        array_alphaJ (np.ndarray): Link J angular acceleration array.
        array_alphaC (np.ndarray): Link C angular acceleration array.
        array_alphaK (np.ndarray): Link K angular acceleration array.
        array_alphaD (np.ndarray): Link D angular acceleration array.
        array_alphaE (np.ndarray): Link E angular acceleration array.
        array_alphaF (np.ndarray): Link F angular acceleration array.
        array_alphaG (np.ndarray): Link G angular acceleration array.
        array_alphaH (np.ndarray): Link H angular acceleration array.
        array_alphaI (np.ndarray): Link I angular acceleration array.
    
    Returns:
        figure_path (list): List of Matplotlib figure objects.
        figure_names (list): List of figure file names.
    """
    # Initialize lists to store figure paths and names
    figure_path = []
    figure_names = []
    
    # * Create Acceleration Figures for each Point *
    a1_figures(figure_path, figure_names, array_A1, crank_angle_plot)
    a2_figures(figure_path, figure_names, array_A2, crank_angle_plot)
    a4_figures(figure_path, figure_names, array_A4, crank_angle_plot)
    a5_figures(figure_path, figure_names, array_A5, crank_angle_plot)
    a6_figures(figure_path, figure_names, array_A6, crank_angle_plot)
    
    
    # * Create Angular Acceleration Figures for Each Link *
    alphaB_figures(figure_path, figure_names, array_alphaB, crank_angle_plot)
    alphaJ_figures(figure_path, figure_names, array_alphaJ, crank_angle_plot)
    alphaC_figures(figure_path, figure_names, array_alphaC, crank_angle_plot)
    alphaK_figures(figure_path, figure_names, array_alphaK, crank_angle_plot)
    alphaD_figures(figure_path, figure_names, array_alphaD, crank_angle_plot)
    alphaE_figures(figure_path, figure_names, array_alphaE, crank_angle_plot)
    alphaF_figures(figure_path, figure_names, array_alphaF, crank_angle_plot)
    alphaG_figures(figure_path, figure_names, array_alphaG, crank_angle_plot)
    
    
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

def a2_figures(figure_path: list, figure_names: list, array_A2: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates acceleration figures for Point P2.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_A2 (np.ndarray): Point P2 acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Acceleration Figures for Point P2 !
    a2_x_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A2, 0, "P2", "Figure 57: P2 X-Acceleration vs Crank Angle")
    a2_y_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A2, 1, "P2", "Figure 58: P2 Y-Acceleration vs Crank Angle")
    a2_magnitude_figure = _plot.plot_acceleration_magnitude_figure(crank_angle_plot, array_A2, "P2", "Figure 59: P2 Acceleration Magnitude vs Crank Angle")


    # Append Figures
    figure_path.extend([a2_x_figure, a2_y_figure, a2_magnitude_figure])
    
    # Append Figure Names
    figure_names.extend(["a2_x_figure", "a2_y_figure", "a2_magnitude_figure"])


def a4_figures(figure_path: list, figure_names: list, array_A4: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates acceleration figures for Point P4.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_A4 (np.ndarray): Point P4 acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Acceleration Figures for Point P4 !
    a4_x_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A4, 0, "P4", "Figure 67: P4 X-Acceleration vs Crank Angle")
    a4_y_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A4, 1, "P4", "Figure 68: P4 Y-Acceleration vs Crank Angle")
    a4_magnitude_figure = _plot.plot_acceleration_magnitude_figure(crank_angle_plot, array_A4, "P4", "Figure 69: P4 Acceleration Magnitude vs Crank Angle")


    # Append Figures
    figure_path.extend([a4_x_figure, a4_y_figure, a4_magnitude_figure])
    
    # Append Figure Names
    figure_names.extend(["a4_x_figure", "a4_y_figure", "a4_magnitude_figure"])
    

def a5_figures(figure_path: list, figure_names: list, array_A5: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates acceleration figures for Point P5.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_A5 (np.ndarray): Point P5 acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Acceleration Figures for Point P5 !
    a5_x_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A5, 0, "P5", "Figure 62: P5 X-Acceleration vs Crank Angle")
    a5_y_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A5, 1, "P5", "Figure 63: P5 Y-Acceleration vs Crank Angle")
    a5_magnitude_figure = _plot.plot_acceleration_magnitude_figure(crank_angle_plot, array_A5, "P5", "Figure 64: P5 Acceleration Magnitude vs Crank Angle")


    # Append Figures
    figure_path.extend([a5_x_figure, a5_y_figure, a5_magnitude_figure])
    
    # Append Figure Names
    figure_names.extend(["a5_x_figure", "a5_y_figure", "a5_magnitude_figure"])
    

def a6_figures(figure_path: list, figure_names: list, array_A6: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates acceleration figures for Point P6.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_A6 (np.ndarray): Point P6 acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Acceleration Figures for Point P6 !
    a6_x_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A6, 0, "P6", "Figure 72: P6 X-Acceleration vs Crank Angle")
    a6_y_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A6, 1, "P6", "Figure 73: P6 Y-Acceleration vs Crank Angle")
    a6_magnitude_figure = _plot.plot_acceleration_magnitude_figure(crank_angle_plot, array_A6, "P6", "Figure 74: P6 Acceleration Magnitude vs Crank Angle")


    # Append Figures
    figure_path.extend([a6_x_figure, a6_y_figure, a6_magnitude_figure])
    
    # Append Figure Names
    figure_names.extend(["a6_x_figure", "a6_y_figure", "a6_magnitude_figure"])
    

def a7_figures(figure_path: list, figure_names: list, array_A7: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates acceleration figures for Point P7.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_A7 (np.ndarray): Point P7 acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Acceleration Figures for Point P7 !
    a7_x_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A7, 0, "P7", "Figure XX: P7 X-Acceleration vs Crank Angle")
    a7_y_figure = _plot.plot_acceleration_figure(crank_angle_plot, array_A7, 1, "P7", "Figure XX: P7 Y-Acceleration vs Crank Angle")
    a7_magnitude_figure = _plot.plot_acceleration_magnitude_figure(crank_angle_plot, array_A7, "P7", "Figure XX: P7 Acceleration Magnitude vs Crank Angle")


    # Append Figures
    figure_path.extend([a7_x_figure, a7_y_figure, a7_magnitude_figure])
    
    # Append Figure Names
    figure_names.extend(["a7_x_figure", "a7_y_figure", "a7_magnitude_figure"])    
    

def alphaB_figures(figure_path: list, figure_names: list, array_alphaB: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link B.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaB (np.ndarray): Link B angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link B !
    alphaB_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaB, "Link B", "Figure 60: Link B Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaB_figure)
    
    # Append Figure Name
    figure_names.append("alphaB_figure")
    
    
def alphaJ_figures(figure_path: list, figure_names: list, array_alphaJ: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link J.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaJ (np.ndarray): Link J angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link J !
    alphaJ_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaJ, "Link J", "Figure 61: Link J Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaJ_figure)
    
    # Append Figure Name
    figure_names.append("alphaJ_figure")


def alphaC_figures(figure_path: list, figure_names: list, array_alphaC: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link C.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaC (np.ndarray): Link C angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link C !
    alphaC_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaC, "Link C", "Figure 65: Link C Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaC_figure)
    
    # Append Figure Name
    figure_names.append("alphaC_figure")
    

def alphaK_figures(figure_path: list, figure_names: list, array_alphaK: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link K.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaK (np.ndarray): Link K angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link K !
    alphaK_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaK, "Link K", "Figure 66: Link K Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaK_figure)
    
    # Append Figure Name
    figure_names.append("alphaK_figure")
    
def alphaD_figures(figure_path: list, figure_names: list, array_alphaD: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link D.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaD (np.ndarray): Link D angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link D !
    alphaD_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaD, "Link D", "Figure 70: Link D Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaD_figure)
    
    # Append Figure Name
    figure_names.append("alphaD_figure")
    
    
def alphaE_figures(figure_path: list, figure_names: list, array_alphaE: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link E.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaE (np.ndarray): Link E angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link E !
    alphaE_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaE, "Link E", "Figure 71: Link E Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaE_figure)
    
    # Append Figure Name
    figure_names.append("alphaE_figure")
    
    
def alphaF_figures(figure_path: list, figure_names: list, array_alphaF: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link F.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaF (np.ndarray): Link F angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link F !
    alphaF_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaF, "Link F", "Figure XX: Link F Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaF_figure)
    
    # Append Figure Name
    figure_names.append("alphaF_figure")
    

def alphaG_figures(figure_path: list, figure_names: list, array_alphaG: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link G.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaG (np.ndarray): Link G angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link G !
    alphaG_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaG, "Link G", "Figure XX: Link G Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaG_figure)
    
    # Append Figure Name
    figure_names.append("alphaG_figure")
    
    
def alphaH_figures(figure_path: list, figure_names: list, array_alphaH: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link H.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaH (np.ndarray): Link H angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link H !
    alphaH_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaH, "Link H", "Figure XX: Link H Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaH_figure)
    
    # Append Figure Name
    figure_names.append("alphaH_figure")
    
    
def alphaI_figures(figure_path: list, figure_names: list, array_alphaI: np.ndarray, crank_angle_plot: np.ndarray):
    """
    Creates angular acceleration figures for Link I.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        array_alphaI (np.ndarray): Link I angular acceleration array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Angular Acceleration Figures for Link I !
    alphaI_figure = _plot.plot_angular_acceleration_figure(crank_angle_plot, array_alphaI, "Link I", "Figure XX: Link I Angular Acceleration vs Crank Angle")
    
    # Append Figure
    figure_path.append(alphaI_figure)
    
    # Append Figure Name
    figure_names.append("alphaI_figure")