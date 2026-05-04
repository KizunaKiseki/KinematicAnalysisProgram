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

def create_velocity_figures(crank_angle_plot: np.ndarray, array_V1 : np.ndarray, array_V2 : np.ndarray, array_V4 : np.ndarray, 
                            array_V5 : np.ndarray, array_V6 : np.ndarray, array_V7 : np.ndarray, array_Vfoot : np.ndarray, 
                            array_omegaB : np.ndarray, array_omegaJ : np.ndarray, array_omegaC : np.ndarray, 
                            array_omegaK : np.ndarray, array_omegaD : np.ndarray, array_omegaE : np.ndarray, 
                            array_omegaF : np.ndarray, array_omegaG : np.ndarray, array_omegaH : np.ndarray, 
                            array_omegaI : np.ndarray) -> tuple[list, list]:
    """
    Creates velocity figures for each point and returns their paths and names.
    
    Args:
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        array_V1 (np.ndarray): Velocity array for Point P1.
        array_V2 (np.ndarray): Velocity array for Point P2.
        array_V4 (np.ndarray): Velocity array for Point P4.
        array_V5 (np.ndarray): Velocity array for Point P5.
        array_V6 (np.ndarray): Velocity array for Point P6.
        array_V7 (np.ndarray): Velocity array for Point P7.
        array_Vfoot (np.ndarray): Velocity array for the foot point P7.
        array_omegaB (np.ndarray): Angular velocity array for Point B.
        array_omegaJ (np.ndarray): Angular velocity array for Point J.
        array_omegaC (np.ndarray): Angular velocity array for Point C.
        array_omegaK (np.ndarray): Angular velocity array for Point K.
        array_omegaD (np.ndarray): Angular velocity array for Point D.
        array_omegaE (np.ndarray): Angular velocity array for Point E.
        array_omegaF (np.ndarray): Angular velocity array for Point F.
        array_omegaG (np.ndarray): Angular velocity array for Point G.
        array_omegaH (np.ndarray): Angular velocity array for Point H.
        array_omegaI (np.ndarray): Angular velocity array for Point I.

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
    v4_figures(figure_path, figure_names, array_V4, crank_angle_plot)
    v5_figures(figure_path, figure_names, array_V5, crank_angle_plot)
    v6_figures(figure_path, figure_names, array_V6, crank_angle_plot)
    v7_figures(figure_path, figure_names, array_V7, crank_angle_plot)
    foot_figures(figure_path, figure_names, array_Vfoot, crank_angle_plot)
    
    # * Create Angular Velocity Figures for Each Link *
    omegaB_figures(figure_path, figure_names, array_omegaB, crank_angle_plot)
    omegaJ_figures(figure_path, figure_names, array_omegaJ, crank_angle_plot)
    omegaC_figures(figure_path, figure_names, array_omegaC, crank_angle_plot)
    omegaK_figures(figure_path, figure_names, array_omegaK, crank_angle_plot)
    omegaD_figures(figure_path, figure_names, array_omegaD, crank_angle_plot)
    omegaE_figures(figure_path, figure_names, array_omegaE, crank_angle_plot)
    omegaF_figures(figure_path, figure_names, array_omegaF, crank_angle_plot)
    omegaG_figures(figure_path, figure_names, array_omegaG, crank_angle_plot)
    omegaH_figures(figure_path, figure_names, array_omegaH, crank_angle_plot)
    omegaI_figures(figure_path, figure_names, array_omegaI, crank_angle_plot)
    
    
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


def v4_figures(figure_path : list, figure_names : list, array_V4 : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for Point P4 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V4 (np.ndarray): Velocity array for Point P4.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Point P4 !
    v4_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V4, 0, "P4", "Figure 36: Velocity of Point P4 vs Crank Angle (x-component)")
    v4_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V4, 1, "P4", "Figure 37: Velocity of Point P4 vs Crank Angle (y-component)")
    v4_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V4, "P4", "Figure 38: Speed of Point P4 vs Crank Angle")
    
    
    # Append V4 Figures to Figure Path
    figure_path.extend([v4_x_figure, v4_y_figure, v4_speed_figure])
    
    # Append V4 Figure Names to Figure Names List
    figure_names.extend(["P4_x_Vel", "P4_y_Vel", "P4_speed"])


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
    v5_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V5, 0, "P5", "Figure 32: Velocity of Point P5 vs Crank Angle (x-component)")
    v5_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V5, 1, "P5", "Figure 33: Velocity of Point P5 vs Crank Angle (y-component)")
    v5_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V5, "P5", "Figure 34: Speed of Point P5 vs Crank Angle")
    
    
    # Append V5 Figures to Figure Path
    figure_path.extend([v5_x_figure, v5_y_figure, v5_speed_figure])
    
    # Append V5 Figure Names to Figure Names List
    figure_names.extend(["P5_x_Vel", "P5_y_Vel", "P5_speed"])


def v6_figures(figure_path : list, figure_names : list, array_V6 : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for Point P6 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V6 (np.ndarray): Velocity array for Point P6.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Point P6 !
    v6_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V6, 0, "P6", "Figure 41: Velocity of Point P6 vs Crank Angle (x-component)")
    v6_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V6, 1, "P6", "Figure 42: Velocity of Point P6 vs Crank Angle (y-component)")
    v6_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V6, "P6", "Figure 43: Speed of Point P6 vs Crank Angle")
    
    
    # Append V6 Figures to Figure Path
    figure_path.extend([v6_x_figure, v6_y_figure, v6_speed_figure])
    
    # Append V6 Figure Names to Figure Names List
    figure_names.extend(["P6_x_Vel", "P6_y_Vel", "P6_speed"])


def v7_figures(figure_path : list, figure_names : list, array_V7 : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for Point P7 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V7 (np.ndarray): Velocity array for Point P7.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Point P7 !
    v7_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V7, 0, "P7", "Figure 46: Velocity of Point P7 vs Crank Angle (x-component)")
    v7_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V7, 1, "P7", "Figure 47: Velocity of Point P7 vs Crank Angle (y-component)")
    v7_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V7, "P7", "Figure 48: Speed of Point P7 vs Crank Angle")
    
    
    # Append V7 Figures to Figure Path
    figure_path.extend([v7_x_figure, v7_y_figure, v7_speed_figure])
    
    # Append V7 Figure Names to Figure Names List
    figure_names.extend(["P7_x_Vel", "P7_y_Vel", "P7_speed"])


def foot_figures(figure_path : list, figure_names : list, array_V_foot : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends velocity figure for the foot point P7 to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_V_foot (np.ndarray): Velocity array for the foot point P7.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Velocity Figures for Foot Point P7 !
    v_foot_x_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V_foot, 0, "Foot Point", "Figure 51: Velocity of Foot Point P7 vs Crank Angle (x-component)")
    v_foot_y_figure = _plot.plot_velocity_figure(crank_angle_plot, array_V_foot, 1, "Foot Point", "Figure 52: Velocity of Foot Point P7 vs Crank Angle (y-component)")
    v_foot_speed_figure = _plot.plot_speed_figure(crank_angle_plot, array_V_foot, "Foot Point", "Figure 53: Speed of Foot Point P7 vs Crank Angle")
    
    
    # Append Foot Point Figures to Figure Path
    figure_path.extend([v_foot_x_figure, v_foot_y_figure, v_foot_speed_figure])
    
    # Append Foot Point Figure Names to Figure Names List
    figure_names.extend(["Foot_x_Vel", "Foot_y_Vel", "Foot__speed"])


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
    omegaC_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaC, "C", "Figure 35: Angular Velocity of Link C vs Crank Angle")
    
    
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
    omegaK_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaK, "K", "Figure 36: Angular Velocity of Link K vs Crank Angle")
    
    
    # Append OmegaK Figure to Figure Path
    figure_path.extend([omegaK_figure])
    
    # Append OmegaK Figure Name to Figure Names List
    figure_names.extend(["K_angular_velocity"])
    
    
def omegaD_figures(figure_path : list, figure_names : list, array_omegaD : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link D to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaD (np.ndarray): Angular velocity array for Link D.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link D !
    omegaD_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaD, "D", "Figure 39: Angular Velocity of Link D vs Crank Angle")
    
    
    # Append OmegaD Figure to Figure Path
    figure_path.extend([omegaD_figure])
    
    # Append OmegaD Figure Name to Figure Names List
    figure_names.extend(["D_angular_velocity"])
    
    
def omegaE_figures(figure_path : list, figure_names : list, array_omegaE : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link E to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaE (np.ndarray): Angular velocity array for Link E.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link E !
    omegaE_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaE, "E", "Figure 40: Angular Velocity of Link E vs Crank Angle")
    
    
    # Append OmegaE Figure to Figure Path
    figure_path.extend([omegaE_figure])
    
    # Append OmegaE Figure Name to Figure Names List
    figure_names.extend(["E_angular_velocity"])
    
    
def omegaF_figures(figure_path : list, figure_names : list, array_omegaF : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link F to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaF (np.ndarray): Angular velocity array for Link F.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link F !
    omegaF_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaF, "F", "Figure 44: Angular Velocity of Link F vs Crank Angle")
    
    
    # Append OmegaF Figure to Figure Path
    figure_path.extend([omegaF_figure])
    
    # Append OmegaF Figure Name to Figure Names List
    figure_names.extend(["F_angular_velocity"])
    
    
def omegaG_figures(figure_path : list, figure_names : list, array_omegaG : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link G to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaG (np.ndarray): Angular velocity array for Link G.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link G !
    omegaG_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaG, "G", "Figure 45: Angular Velocity of Link G vs Crank Angle")
    
    
    # Append OmegaG Figure to Figure Path
    figure_path.extend([omegaG_figure])
    
    # Append OmegaG Figure Name to Figure Names List
    figure_names.extend(["G_angular_velocity"])
    
    
def omegaH_figures(figure_path : list, figure_names : list, array_omegaH : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link H to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaH (np.ndarray): Angular velocity array for Link H.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link H !
    omegaH_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaH, "H", "Figure 49: Angular Velocity of Link H vs Crank Angle")
    
    
    # Append OmegaH Figure to Figure Path
    figure_path.extend([omegaH_figure])
    
    # Append OmegaH Figure Name to Figure Names List
    figure_names.extend(["H_angular_velocity"])
    
def omegaI_figures(figure_path : list, figure_names : list, array_omegaI : np.ndarray, crank_angle_plot : np.ndarray) -> None:
    """
    Creates and appends angular velocity figure for Link I to the provided lists.
    
    Args:
        figure_path (list): List to append the figure path to.
        figure_names (list): List to append the figure name to.
        array_omegaI (np.ndarray): Angular velocity array for Link I.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
    """
    # ! Angular Velocity Figures for Link I !
    omegaI_figure = _plot.plot_angular_velocity_figure(crank_angle_plot, array_omegaI, "I", "Figure 50: Angular Velocity of Link I vs Crank Angle")
    
    
    # Append OmegaI Figure to Figure Path
    figure_path.extend([omegaI_figure])
    
    # Append OmegaI Figure Name to Figure Names List
    figure_names.extend(["I_angular_velocity"])