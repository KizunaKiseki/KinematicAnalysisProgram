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


def append_mechanism_figures(mechanism_path : list, mechanism_names : list, figure_number : int, figure, mechanism_name : str) -> int:
    """
    Appends a mechanism figure to the mechanism path and names lists.
    
    Args:
        mechanism_path (list): List to store mechanism figure objects.
        mechanism_names (list): List to store mechanism figure file names.
        figure_number (int): Current figure number.
        figure: Matplotlib figure object to be appended.
        mechanism_name (str): Name of the mechanism for labeling the figure.
        
    Returns:
        figure_number (int): Updated figure number.
    """
    # ! Mechanism Figure !
    title, name = make_figure_label(figure_number, "Mechanism", mechanism_name)
    
    figure.axes[0].set_title(title, fontsize = 14, fontweight = "bold")
    
    mechanism_path.append(figure)
    mechanism_names.append(name)
    
    
    return figure_number + 1


def append_position_figures(position_path : list, position_names : list, figure_number : int, crank_angle_plot : np.ndarray, position_array : np.ndarray, point_label : str, path_figure) -> int:
    """
    Appends one angular acceleration figure.
    
    Args:
        position_path (list): List to store figure objects.
        position_names (list): List to store figure file names.
        figure_number (int): Current figure number.
        crank_angle_plot (np.ndarray): Array of crank angles for plotting.
        position_array (np.ndarray): Position array for the specific link.
        point_label (str): Label for the point (e.g., "P1", "P2").
        path_figure: Matplotlib figure object for the path.
        
    Returns:
        figure_number (int): Updated figure number.
    """
    # ! Position Figure for X-Component !
    title, name = make_figure_label(figure_number, "Position", f"Point {point_label}", "X-Component")
    px_figure = _plot.plot_position_figure(crank_angle_plot, position_array, 0, f"Point {point_label}", title)
    position_path.append(px_figure)
    position_names.append(name)
    figure_number += 1
    
    # ! Position Figure for Y-Component !
    title, name = make_figure_label(figure_number, "Position", f"Point {point_label}", "Y-Component")
    py_figure = _plot.plot_position_figure(crank_angle_plot, position_array, 1, f"Point {point_label}", title)
    position_path.append(py_figure)
    position_names.append(name)
    figure_number += 1
    
    # ! Position Figure for Path !
    title, name = make_figure_label(figure_number, "Position", f"Point {point_label}", "Path")
    
    path_figure.axes[0].set_title(title, fontsize = 14, fontweight = "bold")
    position_path.append(path_figure)
    position_names.append(name)
    figure_number += 1
    
    
    return figure_number 


def create_position_figures(crank_angle_plot: np.ndarray, O2 : np.ndarray, O4: np.ndarray, position_P1 : np.ndarray, position_P2 : np.ndarray, position_P4 : np.ndarray, position_P5 : np.ndarray, position_P6 : np.ndarray, position_P7 : np.ndarray) -> tuple[list, list, list, list]:
    """
    Creates all mechanism and position figures.
    
    Args:
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        position_P1 (np.ndarray): Position array for point P1.
        position_P2 (np.ndarray): Position array for point P2.
        position_P4 (np.ndarray): Position array for point P4.
        position_P5 (np.ndarray): Position array for point P5.
        position_P6 (np.ndarray): Position array for point P6.
        position_P7 (np.ndarray): Position array for point P7.

    Returns:
        mechanism_path (list): A list of Matplotlib figure objects for the mechanism figures.
        mechanism_names (list): A list of names corresponding to each mechanism figure.
        position_path (list): A list of Matplotlib figure objects for the position figures.
        position_names (list): A list of names corresponding to each position figure.
    """
    # Initialize lists to store figures and their names
    mechanism_path = []
    mechanism_names = []
    position_path = []
    position_names = []
    mechanism_number = 1
    position_number = 1
    
    
    # ? Mechanism Figures ?
    mechanism_number = create_mechanism_figures(mechanism_path, mechanism_names, mechanism_number, O2, O4, position_P1, position_P2, position_P4, position_P5, position_P6, position_P7)
    
    # ? Position Figures ?
    position_number = create_path_figures(position_path, position_names, position_number, crank_angle_plot, O2, O4, position_P1, position_P2, position_P4, position_P5, position_P6, position_P7)
    
    
    
    return mechanism_path, mechanism_names, position_path, position_names


def create_mechanism_figures(mechanism_path : list, mechanism_names : list, figure_number : int, O2 : np.ndarray, O4: np.ndarray, position_P1 : np.ndarray, position_P2 : np.ndarray, position_P4 : np.ndarray, position_P5 : np.ndarray, position_P6 : np.ndarray, position_P7 : np.ndarray) -> int:
    """
    Creates a mechanism figure and appends it to the mechanism path and names lists.
    
    Args:
        mechanism_path (list): List to store mechanism figure objects.
        mechanism_names (list): List to store mechanism figure file names.
        figure_number (int): Current figure number.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        position_P1 (np.ndarray): Position array for point P1.
        position_P2 (np.ndarray): Position array for point P2.
        position_P4 (np.ndarray): Position array for point P4.
        position_P5 (np.ndarray): Position array for point P5.
        position_P6 (np.ndarray): Position array for point P6.
        position_P7 (np.ndarray): Position array for point P7.
    
    Returns:
        figure_number (int): Updated figure number.
    """
    ground_mechanism_figure = _plot.plot_mechanism_figure(
        title = "",
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
                "point_2" : position_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : position_P1[0], "label" : "P1", "x_offset" : 8, "y_offset" : -4},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, ground_mechanism_figure, "Ground Mechanism")
    
    nm_bj_figure = _plot.plot_mechanism_figure(
        title = "",
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
                "point_2" : position_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : position_P2[0],
                "label" : "Link B",
                "color" : _plot.LINK_B_COLOR,
            },
            {
                "point_1" : position_P2[0],
                "point_2" : position_P1[0],
                "label" : "Link J",
                "color" : _plot.LINK_J_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : position_P1[0], "label" : "P1", "x_offset" : 8, "y_offset" : -4},
            {"point" : position_P2[0], "label" : "P2", "x_offset" : 8, "y_offset" : 8},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, nm_bj_figure, "Closed Loop NM-BJ")

    nm_ck_figure = _plot.plot_mechanism_figure(
        title = "",
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
                "point_2" : position_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : position_P5[0],
                "label" : "Link C",
                "color" : _plot.LINK_C_COLOR,
            },
            {
                "point_1" : position_P1[0],
                "point_2" : position_P5[0],
                "label" : "Link K",
                "color" : _plot.LINK_K_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : 8},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : 8},
            {"point" : position_P1[0], "label" : "P1", "x_offset" : -4, "y_offset" : 8},
            {"point" : position_P5[0], "label" : "P5", "x_offset" : -4, "y_offset" : -16},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, nm_ck_figure, "Closed Loop NM-CK")
    
    bde_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1" : O2,
                "point_2" : position_P2[0],
                "label" : "Link B",
                "color" : _plot.LINK_B_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : position_P4[0],
                "label" : "Link D",
                "color" : _plot.LINK_D_COLOR,
            },
            {
                "point_1" : position_P2[0],
                "point_2" : position_P4[0],
                "label" : "Link E",
                "color" : _plot.LINK_E_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -10, "y_offset" : -14},
            {"point" : position_P2[0], "label" : "P2", "x_offset" : 4, "y_offset" : 6},
            {"point" : position_P4[0], "label" : "P4", "x_offset" : -14, "y_offset" : 6},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, bde_figure, "Rigid Body BDE")
    
    parallel_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1" : O2,
                "point_2" : position_P4[0],
                "label" : "Link D",
                "color" : _plot.LINK_D_COLOR,
            },
            {
                "point_1" : position_P4[0],
                "point_2" : position_P6[0],
                "label" : "Link F",
                "color" : _plot.LINK_F_COLOR,
            },
            {
                "point_1" : position_P5[0],
                "point_2" : position_P6[0],
                "label" : "Link G",
                "color" : _plot.LINK_G_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : position_P5[0],
                "label" : "Link C",
                "color" : _plot.LINK_C_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -10, "y_offset" : 8},
            {"point" : position_P4[0], "label" : "P4", "x_offset" : -14, "y_offset" : 6},
            {"point" : position_P5[0], "label" : "P5", "x_offset" : 6, "y_offset" : -14},
            {"point" : position_P6[0], "label" : "P6", "x_offset" : -8, "y_offset" : -16},
        ],
            
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, parallel_figure, "Parallel Loop DF-GC")
    
    ghi_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1" : position_P6[0],
                "point_2" : position_P5[0],
                "label" : "Link G",
                "color" : _plot.LINK_G_COLOR,
            },
            {
                "point_1" : position_P6[0],
                "point_2" : position_P7[0],
                "label" : "Link H",
                "color" : _plot.LINK_H_COLOR,
            },
            {
                "point_1" : position_P5[0],
                "point_2" : position_P7[0],
                "label" : "Link I",
                "color" : _plot.LINK_I_COLOR,
            },
        ],
        points = [
            {"point" : position_P5[0], "label" : "P5", "x_offset" : 8, "y_offset" : -4},
            {"point" : position_P6[0], "label" : "P6", "x_offset" : -4, "y_offset" : 8},
            {"point" : position_P7[0], "label" : "P7", "x_offset" : -8, "y_offset" : -16},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, ghi_figure, "Rigid Body GHI")
    
    foot_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1" : O2,
                "point_2" : position_P5[0],
                "label" : "Link C",
                "color" : _plot.LINK_C_COLOR,
            },
            {
                "point_1" : position_P5[0],
                "point_2" : position_P7[0],
                "label" : "Link I",
                "color" : _plot.LINK_I_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : position_P7[0],
                "label" : "Link P",
                "color" : _plot.LINK_P_COLOR,
                "linestyle" : _plot.LINK_P_LINE_STYLE,
            }
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -10, "y_offset" : 4},
            {"point" : position_P5[0], "label" : "P5", "x_offset" : 6, "y_offset" : -14},
            {"point" : position_P7[0], "label" : "P7", "x_offset" : -8, "y_offset" : -14},
        ],
        
        paths = None,
        
        padding = 20.0
    )
    
    figure_number = append_mechanism_figures(mechanism_path, mechanism_names, figure_number, foot_figure, "Foot Mechanism")
    
    
    return figure_number


def create_path_figures(position_path : list, position_names : list, figure_number : int, crank_angle_plot: np.ndarray, O2 : np.ndarray, O4: np.ndarray, position_P1 : np.ndarray, position_P2 : np.ndarray, position_P4 : np.ndarray, position_P5 : np.ndarray, position_P6 : np.ndarray, position_P7 : np.ndarray) -> int:
    """
    Creates path figures for points P1, P2, P4, P5, P6, and P7 and appends them to the position path and names lists.
    
    Args:
        position_path (list): List to store figure objects.
        position_names (list): List to store figure file names.
        figure_number (int): Current figure number.
        crank_angle_plot (np.ndarray): Crank angle array used for plotting.
        O2 (np.ndarray): Fixed ground pivot O2.
        O4 (np.ndarray): Fixed crank pivot O4.
        position_P1 (np.ndarray): Position array for point P1.
        position_P2 (np.ndarray): Position array for point P2.
        position_P4 (np.ndarray): Position array for point P4.
        position_P5 (np.ndarray): Position array for point P5.
        position_P6 (np.ndarray): Position array for point P6.
        position_P7 (np.ndarray): Position array for point P7.
    
    Returns:
        figure_number (int): Updated figure number after appending all position figures.

    """
    p1_figure = _plot.plot_mechanism_figure(
        title = "",
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
                "point_2" : position_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : position_P1[0], "label" : "P1", "x_offset" : 8, "y_offset" : -4},
        ],
        
        paths = [
            {
                "array" : position_P1,
                "label" : "P1 Path"
            }
        ],
        
        padding = 20.0
    )
    
    figure_number = append_position_figures(position_path, position_names, figure_number, crank_angle_plot, position_P1, "P1", p1_figure)

    p2_figure = _plot.plot_mechanism_figure(
        title = "",
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
                "point_2" : position_P1[0],
                "label" : "Link M",
                "color" : _plot.LINK_M_COLOR,
            },
            {
                "point_1" : O2,
                "point_2" : position_P2[0],
                "label" : "Link B",
                "color" : _plot.LINK_B_COLOR,
            },
            {
                "point_1" : position_P1[0],
                "point_2" : position_P2[0],
                "label" : "Link J",
                "color" : _plot.LINK_J_COLOR,
            },
        ],
        points = [
            {"point" : O2, "label" : "O2", "x_offset" : -8, "y_offset" : -16},
            {"point" : O4, "label" : "O4", "x_offset" : -4, "y_offset" : -16},
            {"point" : position_P1[0], "label" : "P1", "x_offset" : 0, "y_offset" : -16},
            {"point" : position_P2[0], "label" : "P2", "x_offset" : 4, "y_offset" : 8},
        ],
        
        paths = [
            {
                "array" : position_P2,
                "label" : "P2 Path"
            }
        ],
        
        padding = 20.0
    )
    
    figure_number = append_position_figures(position_path, position_names, figure_number, crank_angle_plot, position_P2, "P2", p2_figure)
    
    p4_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1": O2,
                "point_2": position_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": O2,
                "point_2": position_P4[0],
                "label": "Link D",
                "color": _plot.LINK_D_COLOR,
            },
            {
                "point_1": position_P4[0],
                "point_2": position_P6[0],
                "label": "Link F",
                "color": _plot.LINK_F_COLOR,
            },
            {
                "point_1": position_P5[0],
                "point_2": position_P6[0],
                "label": "Link G",
                "color": _plot.LINK_G_COLOR,
            },
        ],
        points = [
            {"point": O2, "label": "O2", "x_offset": -10, "y_offset": 8},
            {"point": position_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
            {"point": position_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": position_P6[0], "label": "P6", "x_offset": -8, "y_offset": -16},
        ],
        
        paths = [
            {
                "array" : position_P4,
                "label" : "P4 Path"
            }
        ],
        
        padding = 20.0
    )
    
    figure_number = append_position_figures(position_path, position_names, figure_number, crank_angle_plot, position_P4, "P4", p4_figure)
    
    p5_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1": O2,
                "point_2": O4,
                "label": "Link N",
                "color": _plot.LINK_N_COLOR,
                "linestyle": _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1": O4,
                "point_2": position_P1[0],
                "label": "Link M",
                "color": _plot.LINK_M_COLOR,
            },
            {
                "point_1": O2,
                "point_2": position_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": position_P1[0],
                "point_2": position_P5[0],
                "label": "Link K",
                "color": _plot.LINK_K_COLOR,
            },
        ],
        points = [
            {"point": O2, "label": "O2", "x_offset": 8, "y_offset": 8},
            {"point": O4, "label": "O4", "x_offset": -4, "y_offset": 8},
            {"point": position_P1[0], "label": "P1", "x_offset": -4, "y_offset": 8},
            {"point": position_P5[0], "label": "P5", "x_offset": -4, "y_offset": -16},
        ],
        
        paths = [
            {
                "array" : position_P5,
                "label" : "P5 Path"
            }
        ],
        
        padding = 20.0
    )
    
    figure_number = append_position_figures(position_path, position_names, figure_number, crank_angle_plot, position_P5, "P5", p5_figure)
    
    p6_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1": O2,
                "point_2": position_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": O2,
                "point_2": position_P4[0],
                "label": "Link D",
                "color": _plot.LINK_D_COLOR,
            },
            {
                "point_1": position_P4[0],
                "point_2": position_P6[0],
                "label": "Link F",
                "color": _plot.LINK_F_COLOR,
            },
            {
                "point_1": position_P5[0],
                "point_2": position_P6[0],
                "label": "Link G",
                "color": _plot.LINK_G_COLOR,
            },
        ],
        points = [
            {"point": O2, "label": "O2", "x_offset": -14, "y_offset": -14},
            {"point": position_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
            {"point": position_P5[0], "label": "P5", "x_offset": 6, "y_offset": -14},
            {"point": position_P6[0], "label": "P6", "x_offset": 0, "y_offset": 6},
        ],
        
        paths = [
            {
                "array" : position_P6,
                "label" : "P6 Path"
            }
        ],
        
        padding = 20.0
    )
    
    figure_number = append_position_figures(position_path, position_names, figure_number, crank_angle_plot, position_P6, "P6", p6_figure)
    
    p7_figure = _plot.plot_mechanism_figure(
        title = "",
        links = [
            {
                "point_1": O2,
                "point_2": position_P5[0],
                "label": "Link C",
                "color": _plot.LINK_C_COLOR,
            },
            {
                "point_1": position_P5[0],
                "point_2": position_P7[0],
                "label": "Link I",
                "color": _plot.LINK_I_COLOR,
            },
            {
                "point_1": O2,
                "point_2": position_P7[0],
                "label": "Link P",
                "color": _plot.LINK_P_COLOR,
                "linestyle": _plot.LINK_P_LINE_STYLE,
            },
        ],
        points = [
            {"point": O2, "label": "O2", "x_offset": -10, "y_offset": 8},
            {"point": position_P5[0], "label": "P5", "x_offset": 6, "y_offset": 8},
            {"point": position_P7[0], "label": "P7", "x_offset": -8, "y_offset": -14},  
        ],
        
        paths = [
            {
                "array" : position_P7,
                "label" : "P7 Path"
            }
        ],
        
        padding = 20.0
    )
    
    figure_number = append_position_figures(position_path, position_names, figure_number, crank_angle_plot, position_P7, "P7", p7_figure)
    
    
    return figure_number
        
