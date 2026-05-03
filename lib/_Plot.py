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
import matplotlib.pyplot as pl

# ! PROJECT MODULES !


# * VARIABLES *
# ? ================================================================ ?

# * Color Scheme *
# Path Color
PATH_COLOR = "#460076"  

# Link Colors
LINK_B_COLOR = "#E76F51"
LINK_C_COLOR = "#C77DFF"
LINK_D_COLOR = "#FFD166"
LINK_E_COLOR = "#B8C0FF"
LINK_F_COLOR = "#D16D9E"
LINK_G_COLOR = "#7B6DCC"
LINK_H_COLOR = "#7A8FB5"
LINK_I_COLOR = "#BC6C25"
LINK_J_COLOR = "#577590"
LINK_K_COLOR = "#84A59D"
LINK_M_COLOR = "#F4A261"
LINK_N_COLOR = "#48CAE4"

# Point Colors
POINT_COLOR = "#000000"  

# * Link N Line Style *
LINK_N_LINE_STYLE = '--'  


# * FUNCTION *
# ? ================================================================ ?

def setup_figure() -> tuple[pl.figure, pl.axes]:
    """
    General function to set up a Matplotlib figure and axes with constant formatting for all plots.
    
    Args:
        None
    
    Returns:
        figure (pl.figure) : A Matplotlib figure object.
        axes (pl.axes) : A Matplotlib axes object with specific formatting applied. 
    
    Raises:
    """
    # Create figure
    figure = pl.figure(figsize=(9, 6))
    
    # Create axis 
    axes = figure.add_subplot(1, 1, 1)
    axes.grid(True, linestyle='--', alpha=0.5)
    
    
    return figure, axes


def draw_point(axes : pl.axes, point : np.ndarray, label : str, x_offset : float = 6.0, y_offset : float = 6.0) -> None:
    """
    Draw & Label a point on the given axes.
    
    Args:
        axes (pl.axes) : The Matplotlib axes to draw the point on.
        point (np.ndarray) : The (x, y) coordinates of the point to be drawn.
        label (str) : The label for the point to be displayed next to it on the plot.
        x_offset (float) : The horizontal offset for the label text from the point. Default is 6.0 mm.
        y_offset (float) : The vertical offset for the label text from the point. Default is 6.0 mm.
    
    Returns:
        None
    """
    # Draw the point
    axes.plot(point[0], point[1], 'o', color=POINT_COLOR, zorder=5)  
    
    # Label the point
    axes.annotate(label, xy=(point[0], point[1]), xytext=(x_offset, y_offset), textcoords='offset points', fontsize=10, 
                  color=POINT_COLOR, bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.2))


def draw_link(axes : pl.axes, point_1 : np.ndarray, point_2 : np.ndarray, label : str, 
              color : str, linestyle : str = '-', linewidth : float = 2.0) -> None:
    """
    Draw a link between two points on the given axes.
    
    Args:
        axes (pl.axes) : The Matplotlib axes to draw the link on.
        point_1 (np.ndarray) : The (x, y) coordinates of the first point.
        point_2 (np.ndarray) : The (x, y) coordinates of the second point.
        label (str) : The label for the link to be displayed next to it on the plot.
        color (str) : The color to use for the link (e.g., 'blue', 'red', etc.).
        line_style (str) : The style of the line (e.g., '-', '--', '-.', ':'). Default is '-'.
        linewidth (float) : The width of the line. Default is 2.0.
    
    Returns:
        None
    """
    # Plot the link as a line between the two points
    axes.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], marker='o', color=color, 
              label=label, linestyle=linestyle, linewidth=linewidth)


def set_axes_limits(axes : pl.axes, points : list[np.ndarray], padding : float = 10.0) -> None:
    """
    Automatically set axis limits based on point location. 
    
    Args:
        axes (pl.axes) : The Matplotlib axes to set the limits on.
        points (list[np.ndarray]) : A list of (x, y) coordinates for all points in the plot.
        padding (float) : Additional padding to add to the limits for better visualization. Default is 10.0 mm.
    
    Returns:
        None
    """
    # Extract x and y coordinates from points
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    # Set limits with padding
    axes.set_xlim(min(x_coords) - padding, max(x_coords) + padding)
    axes.set_ylim(min(y_coords) - padding, max(y_coords) + padding)


def plot_ground_link(O2 : np.ndarray, O4 : np.ndarray, P1 : np.ndarray) -> pl.figure:
    """
    Plot the Ground Link with the input crank position for a single crank angle.
    
    ! Figure 1 : Input Crank Position !
    
    Args:
        O2 (np.ndarray) : The (x, y) coordinates of Point O2, the fixed ground origin.
        O4 (np.ndarray) : The (x, y) coordinates of Point O4, the fixed crank origin.
        P1 (np.ndarray) : The (x, y) coordinates of Point P1, the crank pin at the end of link M.
    
    Returns:
        ground_figure (pl.figure) : A Matplotlib figure object containing the plot of the ground link.
    """
    # Set up figure and axes
    ground_figure, ground_axes = setup_figure()
    
    # Set title and axes labels
    ground_axes.set_title("Figure 1: Input Crank Position")
    ground_axes.set_xlabel("X [mm]")
    ground_axes.set_ylabel("Y [mm]")
    
    # Draw Links
    draw_link(ground_axes, O2, O4, "Link N", LINK_N_COLOR,  linestyle=LINK_N_LINE_STYLE)
    draw_link(ground_axes, O4, P1, "Link M", LINK_M_COLOR)

    # Draw Points
    draw_point(ground_axes, O2, "02", x_offset=-8.0, y_offset=-16.0)
    draw_point(ground_axes, O4, "04", x_offset=-4.0, y_offset=-16.0)
    draw_point(ground_axes, P1, "P1", x_offset=-4.0, y_offset=-16.0)
    
    # Set axes limits based on point locations
    set_axes_limits(ground_axes, [O2, O4, P1], padding=15.0)
    
    # Create Legend & Layout
    ground_axes.legend(loc = 'best')
    ground_figure.tight_layout()

    
    return ground_figure


def plot_p1_position(O2 : np.ndarray, O4 : np.ndarray, array_P1 : np.ndarray) -> pl.figure:
    """
    Plot the position of Point P1 over one full rotation of the crank.
    
    ! Figure 2 : Point P1 Position !

    Args:
        O2 (np.ndarray) : The (x, y) coordinates of Point O2, the fixed ground origin.
        O4 (np.ndarray) : The (x, y) coordinates of Point O4, the fixed crank origin.
        array_P1 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P1 at each crank angle.
    
    Returns:
        p1_position_figure (pl.figure) : A Matplotlib figure object containing the plot of Point P1's position.
    """
    # Set up figure and axes
    p1_position_figure, p1_position_axes = setup_figure()
    
    # Set title and axes labels
    p1_position_axes.set_title("Figure 2: Point P1 Position")
    p1_position_axes.set_xlabel("X [mm]")
    p1_position_axes.set_ylabel("Y [mm]")
    
    # Draw ground point and crank center
    draw_point(p1_position_axes, O2, "02")
    draw_point(p1_position_axes, O4, "04")
    
    # Draw Crank Path
    p1_position_axes.plot(array_P1[:, 0], array_P1[:, 1], label="Path P1", color=PATH_COLOR)
    
    # Draw starting crank position
    draw_link(p1_position_axes, O2, O4, "Link N", LINK_N_COLOR, LINK_N_LINE_STYLE)
    draw_link(p1_position_axes, O4, array_P1[0], "Link M", LINK_M_COLOR)
    
    # Set axes limits based on point locations
    set_axes_limits(p1_position_axes, [O2, O4, *array_P1], padding=15.0)
    
    # Create Legend & Layout
    p1_position_axes.legend(loc = 'best')
    p1_position_figure.tight_layout()
    
    
    return p1_position_figure


def plot_p1_x_figure(theta_m : np.ndarray, array_P1 : np.ndarray) -> pl.figure:
    """
    Plot the X-coordinate of Point P1 as a function of the crank angle.
    
    ! Figure 3 : P1 x-Position vs. Crank Angle !
    
    Args:
        theta_m (np.ndarray) : An array of crank angles in degrees.
        array_P1 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P1 at each crank angle.
    
    Returns:
        p1_x_figure (pl.figure) : A Matplotlib figure object containing the plot of Point P1's X-coordinate.
    """
    # Set up figure and axes
    p1_x_figure, p1_x_axes = setup_figure()
    
    # Set title and axes labels
    p1_x_axes.set_title("Figure 3: P1 x-Position vs. Crank Angle")
    p1_x_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    p1_x_axes.set_ylabel("X [mm]")
    
    # Plot X-coordinate of P1
    p1_x_axes.plot(theta_m, array_P1[:, 0], label="X P1", color=PATH_COLOR)
    
    # Create Legend
    p1_x_axes.legend(loc = 'best')
    
    # Tight Layout
    p1_x_figure.tight_layout()
    
    
    return p1_x_figure
    

def plot_p1_y_figure(theta_m : np.ndarray, array_P1 : np.ndarray) -> pl.figure:
    """
    Plot the Y-coordinate of Point P1 as a function of the crank angle.
    
    ! Figure 4 : P1 y-Position vs. Crank Angle !
    
    Args:
        theta_m (np.ndarray) : An array of crank angles in degrees.
        array_P1 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P1 at each crank angle.
    
    Returns:
        p1_y_figure (pl.figure) : A Matplotlib figure object containing the plot of Point P1's Y-coordinate.
    """
    # Set up figure and axes
    p1_y_figure, p1_y_axes = setup_figure()
    
    # Set title and axes labels
    p1_y_axes.set_title("Figure 4: P1 y-Position vs. Crank Angle")
    p1_y_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    p1_y_axes.set_ylabel("Y [mm]")
    
    # Plot Y-coordinate of P1
    p1_y_axes.plot(theta_m, array_P1[:, 1], label="Y P1", color=PATH_COLOR)
    
    # Create Legend & Layout
    p1_y_axes.legend(loc = 'best')
    p1_y_figure.tight_layout()
    
    
    return p1_y_figure


def plot_nm_bj_figure(O2 : np.ndarray, O4 : np.ndarray, P1 : np.ndarray, P2 : np.ndarray) -> pl.figure:
    """
    Plots the closed loop N + M = B + J for one crank angle.
        
    ! Figure 5 : Closed Loop N + M = B + J !
    
    Args:
        O2 (np.ndarray) : The (x, y) coordinates of Point O2, the fixed ground origin.
        O4 (np.ndarray) : The (x, y) coordinates of Point O4, the fixed crank origin.
        P1 (np.ndarray) : The (x, y) coordinates of Point P1, the crank pin at the end of link M.
        P2 (np.ndarray) : The (x, y) coordinates of Point P2, the upper joint connecting links B and J.
    
    Returns:
        nm_bj_figure (pl.figure) : A Matplotlib figure object containing the plot of the closed loop N + M = B + J.
    """
    # Set up figure and axes
    nm_bj_figure, nm_bj_axes = setup_figure()
    
    # Set title and axes labels
    nm_bj_axes.set_title("Figure 5: Closed Loop N + M = B + J")
    nm_bj_axes.set_xlabel("X [mm]")
    nm_bj_axes.set_ylabel("Y [mm]")
    
    # Draw Links
    draw_link(nm_bj_axes, O2, O4, "Link N", color = LINK_N_COLOR, linestyle=LINK_N_LINE_STYLE)
    draw_link(nm_bj_axes, O4, P1, "Link M", color = LINK_M_COLOR)
    draw_link(nm_bj_axes, O2, P2, "Link B", color = LINK_B_COLOR)
    draw_link(nm_bj_axes, P1, P2, "Link J", color = LINK_J_COLOR)
    
    # Draw Points
    draw_point(nm_bj_axes, O2, "02", x_offset=-8.0, y_offset=-16.0)
    draw_point(nm_bj_axes, O4, "04", x_offset=-4.0, y_offset=-16.0)
    draw_point(nm_bj_axes, P1, "P1", x_offset=-4.0, y_offset=-16.0)
    draw_point(nm_bj_axes, P2, "P2", x_offset=-4.0, y_offset=8.0)
    
    # Set axes limits based on point locations
    set_axes_limits(nm_bj_axes, [O2, O4, P1, P2], padding=15.0)
    
    # Create Legend & Layout
    nm_bj_axes.legend(loc = 'best')
    nm_bj_figure.tight_layout()
    
    
    return nm_bj_figure


def plot_p2_position(O2 : np.ndarray, O4 : np.ndarray, array_P1 : np.ndarray, array_P2 : np.ndarray) -> pl.figure:
    """
    Plot the position of Point P2 over one full rotation of the crank.
    
    ! Figure 6 : Point P2 Position !

    Args:
        O2 (np.ndarray) : The (x, y) coordinates of Point O2, the fixed ground origin.
        O4 (np.ndarray) : The (x, y) coordinates of Point O4, the fixed crank origin.
        array_P1 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P1 at each crank angle.
        array_P2 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P2 at each crank angle.
        
    Returns:
        p2_position_figure (pl.figure) : A Matplotlib figure object containing the plot of Point P2's position.
    """
    # Set up figure and axes
    p2_position_figure, p2_position_axes = setup_figure()
    
    # Set title and axes labels
    p2_position_axes.set_title("Figure 6: Point P2 Position")
    p2_position_axes.set_xlabel("X [mm]")
    p2_position_axes.set_ylabel("Y [mm]")
    
    # Draw Path of P2
    p2_position_axes.plot(array_P2[:, 0], array_P2[:, 1], label="Path P2", color=PATH_COLOR)
    
    # Draw starting crank position
    draw_link(p2_position_axes, O2, O4, "Link N", color = LINK_N_COLOR,  linestyle=LINK_N_LINE_STYLE)
    draw_link(p2_position_axes, O4, array_P1[0], "Link M", color = LINK_M_COLOR)
    draw_link(p2_position_axes, array_P1[0], array_P2[0], "Link J", color = LINK_J_COLOR)
    draw_link(p2_position_axes, O2, array_P2[0], "Link B", color = LINK_B_COLOR)

    
    # Draw ground point and crank center
    draw_point(p2_position_axes, O2, "02", x_offset=-8.0, y_offset=-16.0)
    draw_point(p2_position_axes, O4, "04", x_offset=-4.0, y_offset=-16.0)
    draw_point(p2_position_axes, array_P1[0], "P1", x_offset=-4.0, y_offset=-16.0)
    draw_point(p2_position_axes, array_P2[0], "P2", x_offset=-4.0, y_offset=8.0)
    
    # Set axes limits based on point locations
    set_axes_limits(p2_position_axes, [O2, O4, *array_P1, *array_P2], padding=15.0)
    
    # Create Legend & Layout
    p2_position_axes.legend(loc = 'best')
    p2_position_figure.tight_layout()
    
    
    return p2_position_figure


def plot_p2_x_figure(theta_m : np.ndarray, array_P2 : np.ndarray) -> pl.figure:
    """
    Plot the X-coordinate of Point P2 as a function of the crank angle.
    
    ! Figure 7 : P2 x-Position vs. Crank Angle !
    
    Args:
        theta_m (np.ndarray) : An array of crank angles in degrees.
        array_P2 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P2 at each crank angle.
    
    Returns:
        p2_x_figure (pl.figure) : A Matplotlib figure object containing the plot of Point P2's X-coordinate.
    """
    # Set up figure and axes
    p2_x_figure, p2_x_axes = setup_figure()
    
    # Set title and axes labels
    p2_x_axes.set_title("Figure 7: P2 x-Position vs. Crank Angle")
    p2_x_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    p2_x_axes.set_ylabel("X [mm]")
    
    # Plot X-coordinate of P2
    p2_x_axes.plot(theta_m, array_P2[:, 0], label="X P2", color=PATH_COLOR)
    
    # Create Legend & Layout
    p2_x_axes.legend(loc = 'best')
    p2_x_figure.tight_layout()
    
    
    return p2_x_figure
    

def plot_p2_y_figure(theta_m : np.ndarray, array_P2 : np.ndarray) -> pl.figure:
    """
    Plot the Y-coordinate of Point P2 as a function of the crank angle.
    
    ! Figure 8 : P2 y-Position vs. Crank Angle !
    
    Args:
        theta_m (np.ndarray) : An array of crank angles in degrees.
        array_P2 (np.ndarray) : An array of shape (NUM_STEPS, 2) containing the (x, y) coordinates of Point P2 at each crank angle.
    
    Returns:
        p2_y_figure (pl.figure) : A Matplotlib figure object containing the plot of Point P2's Y-coordinate.
    """
    # Set up figure and axes
    p2_y_figure, p2_y_axes = setup_figure()
    
    # Set title and axes labels
    p2_y_axes.set_title("Figure 8: P2 y-Position vs. Crank Angle")
    p2_y_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    p2_y_axes.set_ylabel("Y [mm]")
    
    # Plot Y-coordinate of P2
    p2_y_axes.plot(theta_m, array_P2[:, 1], label="Y P2", color=PATH_COLOR)
    
    # Create Legend & Layout
    p2_y_axes.legend(loc = 'best')
    p2_y_figure.tight_layout()
    
    
    return p2_y_figure


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