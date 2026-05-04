# -*- coding: utf-8 -*-
"""
TITLE = [INSERT TITLE HERE]
DATE  = 2026.01.01
_____________________________________________________________________
DESCRIPTION:
1. [Insert Description Here]
2. ...
_____________________________________________________________________
AUTHOR : Nicholas Heling
"""

# * IMPORTS *
# ? ================================================================ ?

# ! PYTHON TEMPLATES & LIBRARIES !
import numpy as np

# ! PROJECT MODULES !
import lib._Plot as _plot


# * FUNCTION *
# ? ================================================================ ?

def create_position_figures(crank_angle_plot: np.ndarray, O2 : np.ndarray, O4: np.ndarray, array_P1: np.ndarray, 
                            array_P2: np.ndarray, array_P4: np.ndarray, array_P5: np.ndarray, 
                            array_P6: np.ndarray, array_P7: np.ndarray) -> tuple[list, list]:
    """
    Creates all position analysis figures for the Theo Jansen mechanism.
    
    Args:
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        array_P1 (np.ndarray): Point P1 position array.
        array_P2 (np.ndarray): Point P2 position array.
        array_P4 (np.ndarray): Point P4 position array.
        array_P5 (np.ndarray): Point P5 position array.
        array_P6 (np.ndarray): Point P6 position array.
        array_P7 (np.ndarray): Point P7 position array.

    Returns:
        figure_path (list): List of Matplotlib figure objects.
        figure_names (list): List of figure file names.
    """
    # Initialize lists to store figures and their names
    figure_path = []
    figure_names = []
    
    # * Create Position Figures for Each Point *
    p1_figures(figure_path, figure_names, O2, O4, array_P1, crank_angle_plot)
    p2_figures(figure_path, figure_names, O2, O4, array_P1, array_P2, crank_angle_plot)
    p4_figures(figure_path, figure_names, O2, array_P2, array_P4, array_P5, array_P6, crank_angle_plot)
    p5_figures(figure_path, figure_names, O2, O4, array_P1, array_P5, crank_angle_plot)
    p6_figures(figure_path, figure_names, O2, array_P4, array_P5, array_P6, array_P7, crank_angle_plot)
    p7_figures(figure_path, figure_names, O2, array_P5, array_P7, crank_angle_plot)
    
    return figure_path, figure_names


def p1_figures(figure_path: list, figure_names: list, O2: np.ndarray, O4: np.ndarray, 
               array_P1: np.ndarray, crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates and appends the position figure for point P1 to the provided lists.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        array_P1 (np.ndarray): Point P1 position array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Position Figures for P1 !
    ground_figure = _plot.plot_mechanism_figure(
        title = "Figure 1 : Ground Link",
        
        links = [
            {
                "point_1" : O2,
                "point_2" : O4,
                "label" : "Link N",
                "color" : _plot.LINK_N_COLOR,
                "linestyle" : _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1" : O4,
                "point_2" : array_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            }
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 8, "y_offset" : -4},
        ],
        
        paths = None,
        
        padding = 20.0   
    )
    
    p1_position_figure = _plot.plot_mechanism_figure(
        title = "Figure 2: Point P1 Position",
        
        links = [
            {
                "point_1" : O2,
                "point_2" : O4,
                "label" : "Link N",
                "color" : _plot.LINK_N_COLOR,
                "linestyle" : _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1" : O4,
                "point_2" : array_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            }
        ],
        
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 8, "y_offset" : -4},
        ],
        
        paths = [
            {
                "array" : array_P1,
                "label" : "P1 Path"
            }  
        ],
        
        padding = 20.0   
    )
    
    p1_x_figure = _plot.plot_position_figure(crank_angle_plot, array_P1, 0, "P1", "Figure 3: Point P1 x-Position vs. Crank Angle")
    p1_y_figure = _plot.plot_position_figure(crank_angle_plot, array_P1, 1, "P1", "Figure 4: Point P1 y-Position vs. Crank Angle")
    

    # Append P1 Figures to Figure Path
    figure_path.extend([ground_figure, p1_position_figure, p1_x_figure, p1_y_figure])
    
    # Append P1 Figure Names to Figure Names List
    figure_names.extend(["Ground_Link", "P1_Position", "P1_x_Position", "P1_y_Position"])


def p2_figures(figure_path: list, figure_names: list, O2: np.ndarray, O4: np.ndarray, 
               array_P1: np.ndarray, array_P2: np.ndarray, crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates and appends the position figure for point P2 to the provided lists.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        array_P1 (np.ndarray): Point P1 position array.
        array_P2 (np.ndarray): Point P2 position array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Position Figures for P2 ! 
    nm_bj_figure = _plot.plot_mechanism_figure(
        title = "Figure 5: Closed Loop NM + BJ",

        links = [
            {
                "point_1" : O2,
                "point_2" : O4,
                "label" : "Link N",
                "color" : _plot.LINK_N_COLOR,
                "linestyle" : _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1" : O4,
                "point_2" : array_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : array_P2[0],
                "label" : "Link B",
                "color" : _plot.LINK_B_COLOR,
            },
            
            {
                "point_1" : array_P1[0],
                "point_2" : array_P2[0],
                "label" : "Link J",
                "color" : _plot.LINK_J_COLOR,
            }
        
        ],
        
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 0, "y_offset" : -16},
            {"point" : array_P2[0], "label" : "P2", "x_offset" : -4, "y_offset" : 8},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    p2_position_figure = _plot.plot_mechanism_figure(
        title = "Figure 6: Point P2 Position",
        
        links = [
            {
                "point_1" : O2,
                "point_2" : O4,
                "label" : "Link N",
                "color" : _plot.LINK_N_COLOR,
                "linestyle" : _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1" : O4,
                "point_2" : array_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : array_P2[0],
                "label" : "Link B",
                "color" : _plot.LINK_B_COLOR,
            },
            
            {
                "point_1" : array_P1[0],
                "point_2" : array_P2[0],
                "label" : "Link J",
                "color" : _plot.LINK_J_COLOR,
            }
        
        ],
        
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 0, "y_offset" : -16},
            {"point" : array_P2[0], "label" : "P2", "x_offset" : 4, "y_offset" : 8},
        ],
        
        paths = [
            {   
                "array" : array_P2,
                "label" : "P2 Path"
            }
        ],
        
        padding = 20.0
    )

    P2_x_figure = _plot.plot_position_figure(crank_angle_plot, array_P2, 0, "P2", "Figure 7: Point P2 x-Position vs. Crank Angle")
    P2_y_figure = _plot.plot_position_figure(crank_angle_plot, array_P2, 1, "P2", "Figure 8: Point P2 y-Position vs. Crank Angle")
    
    
    # Append P2 Figures to Figure Path
    figure_path.extend([nm_bj_figure, p2_position_figure, P2_x_figure, P2_y_figure])
    
    # Append P2 Figure Names to Figure Names List
    figure_names.extend(["Closed_Loop_NM_BJ", "P2_Position", "P2_x_Position", "P2_y_Position"])


def p4_figures(figure_path: list, figure_names: list, O2: np.ndarray,
               array_P2: np.ndarray, array_P4: np.ndarray, array_P5 : np.ndarray, 
               array_P6: np.ndarray, crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates and appends the position figure for point P4 to the provided lists.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        O2 (np.ndarray): Fixed ground pivot O2.
        array_P2 (np.ndarray): Point P2 position array.
        array_P4 (np.ndarray): Point P4 position array.
        array_P5 (np.ndarray): Point P5 position array.
        array_P6 (np.ndarray): Point P6 position array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
     # ! Position Figures for P4 !
    bde_rigid_body_figure = _plot.plot_mechanism_figure(
        title = "Figure 13: Rigid Body BDE",
        
        links=[
            {
                "point_1": O2,
                "point_2": array_P2[0],
                "label": "Link B",
                "color": _plot.LINK_B_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P4[0],
                "label": "Link D",
                "color": _plot.LINK_D_COLOR,
            },
            {
                "point_1": array_P4[0],
                "point_2": array_P2[0],
                "label": "Link E",
                "color": _plot.LINK_E_COLOR,
            },
        ],

        points=[
            {"point": O2, "label": "O2", "x_offset": -10, "y_offset": -14},
            {"point": array_P2[0], "label": "P2", "x_offset": 4, "y_offset": 6},
            {"point": array_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    p4_position_figure = _plot.plot_mechanism_figure(
        title = "Figure 14: Point P4 Position",
        
        links=[
            {
                "point_1": O2,
                "point_2": array_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P4[0],
                "label": "Link D",
                "color": _plot.LINK_D_COLOR,
            },
            {
                "point_1": array_P4[0],
                "point_2": array_P6[0],
                "label": "Link F",
                "color": _plot.LINK_F_COLOR,
            },
            {
                "point_1": array_P5[0],
                "point_2": array_P6[0],
                "label": "Link G",
                "color": _plot.LINK_G_COLOR,
            },
        ],

        points=[
            {"point": O2, "label": "O2", "x_offset": -14, "y_offset": -14},
            {"point": array_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
            {"point": array_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": array_P6[0], "label": "P6", "x_offset": -0, "y_offset": 6},
        ],

        paths=[
            {
                "array": array_P4,
                "label": "P4 Path"
            }
        ],

        padding=20.0
    )
    
    P4_x_figure = _plot.plot_position_figure(crank_angle_plot, array_P4, 0, "P4", "Figure 15: Point P4 x-Position vs. Crank Angle")
    P4_y_figure = _plot.plot_position_figure(crank_angle_plot, array_P4, 1, "P4", "Figure 16: Point P4 y-Position vs. Crank Angle")
    
    
    # Append P4 Figures to Figure Path
    figure_path.extend([bde_rigid_body_figure, p4_position_figure, P4_x_figure, P4_y_figure])

    # Append P4 Figure Names to Figure Names List
    figure_names.extend(["Rigid_Body_BDE", "P4_Position", "P4_x_Position", "P4_y_Position"])
    

def p5_figures(figure_path: list, figure_names: list, O2: np.ndarray, O4: np.ndarray, 
               array_P1: np.ndarray, array_P5: np.ndarray, crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates and appends the position figure for point P5 to the provided lists.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        array_P1 (np.ndarray): Point P1 position array.
        array_P5 (np.ndarray): Point P5 position array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    # ! Position Figures for P5 !
    nm_ck_figure = _plot.plot_mechanism_figure(
        title = "Figure 9: Closed Loop NM + CK",
        links = [
            {
                "point_1" : O2,
                "point_2" : O4,
                "label" : "Link N",
                "color" : _plot.LINK_N_COLOR,
                "linestyle" : _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1" : O4,
                "point_2" : array_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : array_P5[0],
                "label" : "Link C",
                "color" : _plot.LINK_C_COLOR,
            },
            
            {
                "point_1" : array_P1[0],
                "point_2" : array_P5[0],
                "label" : "Link K",
                "color" : _plot.LINK_K_COLOR,
            }
        
        ],
        
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : 8.0, "y_offset" : 8.0},
            {"point" : O4, "label" : "O4", "x_offset" : -4.0, "y_offset" : 8.0},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : -4.0, "y_offset" : 8.0},
            {"point" : array_P5[0], "label" : "P5", "x_offset" : -4.0, "y_offset" : -16.0},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    p5_position_figure = _plot.plot_mechanism_figure(
        title = "Figure 10: Point P5 Position",
        links = [
            {
                "point_1" : O2,
                "point_2" : O4,
                "label" : "Link N",
                "color" : _plot.LINK_N_COLOR,
                "linestyle" : _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1" : O4,
                "point_2" : array_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : array_P5[0],
                "label" : "Link C",
                "color" : _plot.LINK_C_COLOR,
            },
            
            {
                "point_1" : array_P1[0],
                "point_2" : array_P5[0],
                "label" : "Link K",
                "color" : _plot.LINK_K_COLOR,
            }
        
        ],
        
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : 8.0, "y_offset" : 8.0},
            {"point" : O4, "label" : "O4", "x_offset" : -4.0, "y_offset" : 8.0},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : -4.0, "y_offset" : 8.0},
            {"point" : array_P5[0], "label" : "P5", "x_offset" : -4.0, "y_offset" : -16.0},
        ],
        
        paths = [
            {  
                "array" : array_P5,
                "label" : "P5 Path"
            }
        ],
        
        padding = 20.0
    )
    
    P5_x_figure = _plot.plot_position_figure(crank_angle_plot, array_P5, 0, "P5", "Figure 11: Point P5 x-Position vs. Crank Angle")
    P5_y_figure = _plot.plot_position_figure(crank_angle_plot, array_P5, 1, "P5", "Figure 12: Point P5 y-Position vs. Crank Angle")
    
    
    # Append P5 Figures to Figure Path
    figure_path.extend([nm_ck_figure, p5_position_figure, P5_x_figure, P5_y_figure])

    # Append P5 Figure Names to Figure Names List
    figure_names.extend(["Closed_Loop_NM_CK", "P5_Position", "P5_x_Position", "P5_y_Position"])

def p6_figures(figure_path: list, figure_names: list, O2: np.ndarray, array_P4: np.ndarray, array_P5: np.ndarray, 
               array_P6: np.ndarray, array_P7: np.ndarray, crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates and appends the position figure for point P6 to the provided lists.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        O2 (np.ndarray): Fixed ground pivot O2.
        array_P4 (np.ndarray): Point P4 position array.
        array_P5 (np.ndarray): Point P5 position array.
        array_P6 (np.ndarray): Point P6 position array.
        array_P7 (np.ndarray): Point P7 position array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """
    
    
    # ! Position Figures for P6 !
    ghi_rigid_body_figure = _plot.plot_mechanism_figure(
        title = "Figure 17: Rigid Body GHI",
        
        links=[
            {
                "point_1": array_P6[0],
                "point_2": array_P5[0],
                "label": "Link G",
                "color": _plot.LINK_G_COLOR,
            },
            {
                "point_1": array_P6[0],
                "point_2": array_P7[0],
                "label": "Link H",
                "color": _plot.LINK_H_COLOR,
            },
            {
                "point_1": array_P5[0],
                "point_2": array_P7[0],
                "label": "Link I",
                "color": _plot.LINK_I_COLOR,
            },
        ],

        points=[
            {"point": array_P5[0], "label": "P5", "x_offset": 8, "y_offset": -4},
            {"point": array_P6[0], "label": "P6", "x_offset": -4, "y_offset": 8},
            {"point": array_P7[0], "label": "P7", "x_offset": -8, "y_offset": -16},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    p6_position_figure = _plot.plot_mechanism_figure(
        title = "Figure 18: Point P6 Position",
        
        links=[
            {
                "point_1": O2,
                "point_2": array_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P4[0],
                "label": "Link D",
                "color": _plot.LINK_D_COLOR,
            },
            {
                "point_1": array_P4[0],
                "point_2": array_P6[0],
                "label": "Link F",
                "color": _plot.LINK_F_COLOR,
            },
            {
                "point_1": array_P5[0],
                "point_2": array_P6[0],
                "label": "Link G",
                "color": _plot.LINK_G_COLOR,
            },
        ],

        points=[
            {"point": O2, "label": "O2", "x_offset": -14, "y_offset": -14},
            {"point": array_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
            {"point": array_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": array_P6[0], "label": "P6", "x_offset": -0, "y_offset": 6},
        ],

        paths=[
            {
                "array": array_P6,
                "label": "P6 Path"
            }
        ],
        
        padding=20.0
    )
    
    P6_x_figure = _plot.plot_position_figure(crank_angle_plot, array_P6, 0, "P6", "Figure 19: Point P6 x-Position vs. Crank Angle")
    P6_y_figure = _plot.plot_position_figure(crank_angle_plot, array_P6, 1, "P6", "Figure 20: Point P6 y-Position vs. Crank Angle")

    
    
    # ! Parallel Mechanism Figure !
    parallel_mechanism_figure = _plot.plot_mechanism_figure(
    title="Figure 19: Local Loop O2-P4-P6-P5",

        links=[
            {
                "point_1": O2,
                "point_2": array_P4[0],
                "label": "Link D",
                "color": _plot.LINK_D_COLOR,
            },
            {
                "point_1": array_P4[0],
                "point_2": array_P6[0],
                "label": "Link F",
                "color": _plot.LINK_F_COLOR,
            },
            {
                "point_1": array_P5[0],
                "point_2": array_P6[0],
                "label": "Link G",
                "color": _plot.LINK_G_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
        ],

        points=[
            {"point": O2, "label": "O2", "x_offset": -10, "y_offset": 8},
            {"point": array_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
            {"point": array_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": array_P6[0], "label": "P6", "x_offset": -8, "y_offset": -16},
        ],
        
        paths = None,

        padding=20.0
    )

        
    # Append P6 Figures to Figure Path
    figure_path.extend([ghi_rigid_body_figure, p6_position_figure, P6_x_figure, P6_y_figure, parallel_mechanism_figure])

    
    # Append P6 Figure Names to Figure Names List
    figure_names.extend(["Rigid_Body_GHI", "P6_Position", "P6_x_Position", "P6_y_Position", "Parallel_Figure"]) 
    
    
def p7_figures(figure_path: list, figure_names: list, O2: np.ndarray, array_P5: np.ndarray, array_P7: np.ndarray, 
               crank_angle_plot: np.ndarray) -> tuple[list, list]:
    """
    Creates and appends the position figure for point P6 to the provided lists.
    
    Args:
        figure_path (list): List to store Matplotlib figure objects.
        figure_names (list): List to store figure file names.
        O2 (np.ndarray): Fixed ground pivot O2.
        array_P5 (np.ndarray): Point P5 position array.
        array_P7 (np.ndarray): Point P7 position array.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
    """  
    # ! Position Figures for P7 !
    foot_figure = _plot.plot_mechanism_figure(
        title="Figure 20: Foot Mechanism",
        
        links=[
            {
                "point_1": O2,
                "point_2": array_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": array_P5[0],
                "point_2": array_P7[0],
                "label": "Link I",
                "color": _plot.LINK_I_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P7[0],
                "label": "Reference P",
                "color": _plot.LINK_P_COLOR,
                "linestyle": _plot.LINK_P_LINE_STYLE,
                "linewidth": 2.0,
            },
        ],

        points=[
            {"point": O2, "label": "O2", "x_offset": -10, "y_offset": 4},
            {"point": array_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": array_P7[0], "label": "P7", "x_offset": -8, "y_offset": -14},
        ],

        paths = None,
        
        padding=20.0
        
    )
        
    p7_position_figure = _plot.plot_mechanism_figure(
        title="Figure 21: Point P7 Position",

        links=[
                        {
                "point_1": O2,
                "point_2": array_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": array_P5[0],
                "point_2": array_P7[0],
                "label": "Link I",
                "color": _plot.LINK_I_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P7[0],
                "label": "Reference P",
                "color": _plot.LINK_P_COLOR,
                "linestyle": _plot.LINK_P_LINE_STYLE,
                "linewidth": 2.0,
            },
        ],

        points=[
            {"point": O2, "label": "O2", "x_offset": -10, "y_offset": 8},
            {"point": array_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": array_P7[0], "label": "P7", "x_offset": -8, "y_offset": -14},
        ],

        paths=[
            {
                "array": array_P7,
                "label": "P7 Path",
            }
        ],

        padding=20.0
    )
    
    P7_x_figure = _plot.plot_position_figure(crank_angle_plot, array_P7, 0, "P7", "Figure 22: Point P7 x-Position vs. Crank Angle")
    P7_y_figure = _plot.plot_position_figure(crank_angle_plot, array_P7, 1, "P7", "Figure 23: Point P7 y-Position vs. Crank Angle")
    
    
    # Append P7 Figures to Figure Path
    figure_path.extend([foot_figure, p7_position_figure, P7_x_figure, P7_y_figure])
    
    # Append P7 Figure Names to Figure Names List
    figure_names.extend(["Foot_Mechanism", "P7_Position", "P7_x_Position", "P7_y_Position"])

