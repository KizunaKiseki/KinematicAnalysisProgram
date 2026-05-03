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


def draw_point(axes : pl.axes, point : np.ndarray, label : str) -> None:
    """
    Draw & Label a point on the given axes.
    
    Args:
        axes (pl.axes) : The Matplotlib axes to draw the point on.
        point (np.ndarray) : The (x, y) coordinates of the point to be drawn.
        label (str) : The label for the point to be displayed next to it on the plot.
    
    Returns:
        None
    """
    # Draw the point
    axes.plot(point[0], point[1], 'ko', zorder=5)  
    
    # Label the point
    axes.text(point[0], point[1], f" {label}", fontsize=10)



def draw_link(axes : pl.axes, point_1 : np.ndarray, point_2 : np.ndarray, label : str) -> None:
    """
    Draw a link between two points on the given axes.
    
    Args:
        axes (pl.axes) : The Matplotlib axes to draw the link on.
        point_1 (np.ndarray) : The (x, y) coordinates of the first point.
        point_2 (np.ndarray) : The (x, y) coordinates of the second point.
        label (str) : The label for the link to be displayed next to it on the plot.
    
    Returns:
        None
    """
    # Plot the link as a line between the two points
    axes.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], marker='o', label=label)



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
    draw_link(ground_axes, O2, O4, "Link N: 02 to 04")
    draw_link(ground_axes, O4, P1, "Link M: 04 to P1")
    
    # Draw Points
    draw_point(ground_axes, O2, "02")
    draw_point(ground_axes, O4, "04")
    draw_point(ground_axes, P1, "P1")
    
    # Set axes limits based on point locations
    set_axes_limits(ground_axes, [O2, O4, P1], padding=15.0)
    
    # Create Legend
    ground_axes.legend(loc = 'best')
    
    # Tight Layout
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
    p1_position_axes.plot(array_P1[:, 0], array_P1[:, 1], label="path of P1")
    
    # Draw starting crank position
    draw_link(p1_position_axes, O4, array_P1[0], "Starting Link M")
    
    # Set axes limits based on point locations
    set_axes_limits(p1_position_axes, [O2, O4, *array_P1], padding=15.0)
    
    # Create Legend
    p1_position_axes.legend(loc = 'best')
    
    # Tight Layout
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
    p1_x_axes.plot(theta_m, array_P1[:, 0], label="X-coordinate of P1")
    
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
    p1_y_axes.plot(theta_m, array_P1[:, 1], label="Y-coordinate of P1")
    
    # Create Legend
    p1_y_axes.legend(loc = 'best')
    
    # Tight Layout
    p1_y_figure.tight_layout()
    
    
    return p1_y_figure


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