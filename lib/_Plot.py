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
        figure (pl.figure) : Matplotlib figure object.
        axes (pl.axes) : Matplotlib axes object. 
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
        axes (pl.axes) : Matplotlib axes object.
        point (np.ndarray) : Point coordinates [x, y].
        label (str) : Point label.
        x_offset (float) : Label offset in screen points. Default is 6.0.
        y_offset (float) : Label offset in screen points. Default is 6.0.
    
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
        axes (pl.axes) : Matplotlib axes object.
        point_1 (np.ndarray) : first point coordinates [x, y].
        point_2 (np.ndarray) : second point coordinates [x, y].
        label (str) : Link label.
        color (str) : Link color.
        linestyle (str) : Line style
        linewidth (float) : Line width. Default is 2.0.
    
    Returns:
        None
    """
    # Plot the link as a line between the two points
    axes.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], marker='o', color=color, 
              label=label, linestyle=linestyle, linewidth=linewidth)


def draw_path(axes: pl.axes, path_array: np.ndarray, label: str) -> None:
    """
    Draw a path on the given axes.
    
    Args:
        axes (pl.axes) : Matplotlib axes object.
        path_array (np.ndarray) : Array of position points [x, y].
        label (str) : Path label.
    
    Returns:
        None
    """
    # Plot the path as a line connecting the points
    axes.plot(path_array[:, 0], path_array[:, 1], label=label, color=PATH_COLOR, linewidth=3.0)


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


def plot_mechanism_figure(title : str, links : list[dict], points : list[dict], 
                          paths : list[dict], padding : float = 20.0) -> pl.figure:
    """
    General function to plot a mechanism position figure.
    
    Args:
        title (str) : Figure title to be displayed at the top of the plot.
        links (list[dict]) : List of links to draw.
        points (list[dict]) : List of points to draw and label.
        paths (list[dict]) : Optional list of paths to draw.
        padding (float) : Additional padding to add to the axis limits for better visualization. Default is 20.0 mm.
    
    Returns:
        figure (pl.figure) : A Matplotlib figure object containing the plot of the mechanism.
    """
    # Set up figure and axes
    mechanism_figure, mechanism_axes = setup_figure()
    
    # Axis title & labels
    mechanism_axes.set_title(title)
    mechanism_axes.set_xlabel("X [mm]")
    mechanism_axes.set_ylabel("Y [mm]")
    
    
    # Draw paths if provided:
    if paths is not None:
        for path in paths:
            draw_path(mechanism_axes, path['array'], path['label'])
            
    # Draw links
    for link in links:
        draw_link(mechanism_axes, link['point_1'], link['point_2'], link['label'], 
                  link['color'], link.get('linestyle', '-'), link.get('linewidth', 2.0))
    
    # Draw points
    for point in points:
        draw_point(mechanism_axes, point['point'], point['label'], 
                   x_offset=point.get('x_offset', 6.0), y_offset=point.get('y_offset', 6.0))
    
    # Collect all points for axes limits
    all_points = []
    
    for link in links:
        all_points.append(link['point_1'])
        all_points.append(link['point_2'])
    
    for point in points:
        all_points.append(point['point'])
        
    if paths is not None:
        for path in paths:
            all_points.extend(path['array'])
            
    # Set axes limits based on point locations
    set_axes_limits(mechanism_axes, all_points, padding=padding)
    
    # Create legend & layout
    mechanism_axes.legend(loc = 'best')
    mechanism_figure.tight_layout()
    
    
    return mechanism_figure


def plot_position_figure(theta_array : np.ndarray, position_array : np.ndarray, coordinate_index : int, 
                         point_label : str, title : str) -> pl.figure:
    """
    General function for plotting x or y position vs. crank angle. 
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        position_array (np.ndarray): Position array for a point.
        coordinate_index (int): 0 for x-position, 1 for y-position.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    position_figure, position_axes = setup_figure()
    
    # Choose coordinate label based on index
    coordinate_label = "X" if coordinate_index == 0 else "Y"
    
    # Set title and axes labels
    position_axes.set_title(title)
    position_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    position_axes.set_ylabel(f"{coordinate_label} [mm]")
    
    # Plot the position vs. crank angle
    position_axes.plot(theta_array, position_array[:, coordinate_index], color=PATH_COLOR, linewidth=2.0, label=f"{coordinate_label} {point_label}")
    
    # Create Legend & Layout
    position_axes.legend(loc = 'best')
    position_figure.tight_layout()
    
    
    return position_figure


def plot_velocity_figure(theta_array : np.ndarray, velocity_array : np.ndarray, coordinate_index : int,
                         point_label : str, title : str) -> pl.figure:
    """
    General function for plotting x or y velocity vs. crank angle. 
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        velocity_array (np.ndarray): Velocity array for a point.
        coordinate_index (int): 0 for x-velocity, 1 for y-velocity.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    velocity_figure, velocity_axes = setup_figure()
    
    # Choose coordinate label based on index
    coordinate_label = "Vx" if coordinate_index == 0 else "Vy"
    
    # Set title and axes labels
    velocity_axes.set_title(title)
    velocity_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    velocity_axes.set_ylabel(f"{coordinate_label} [mm/s]")
    
    # Plot the velocity vs. crank angle
    velocity_axes.plot(theta_array, velocity_array[:, coordinate_index], color=PATH_COLOR, linewidth=2.0, label=f"{coordinate_label} {point_label}")
    
    # Create Legend & Layout
    velocity_axes.legend(loc = 'best')
    velocity_figure.tight_layout()
    
    
    return velocity_figure


def plot_speed_figure(theta_array : np.ndarray, velocity_array : np.ndarray,
                         point_label : str, title : str) -> pl.figure:
    """
    General function for plotting speed vs. crank angle.
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        velocity_array (np.ndarray): Velocity array for a point.
        coordinate_index (int): 0 for x-velocity, 1 for y-velocity.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    speed_figure, speed_axes = setup_figure()
    
    # Set title and axes labels
    speed_axes.set_title(title)
    speed_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    speed_axes.set_ylabel(f"Speed [mm/s]")
    
    # Calculate speed as the magnitude of the velocity vector
    speed_array = np.linalg.norm(velocity_array, axis=1)
    
    # Plot the speed vs. crank angle
    speed_axes.plot(theta_array, speed_array, color=PATH_COLOR, linewidth=2.0, label=f"Speed {point_label}")
    
    # Create Legend & Layout
    speed_axes.legend(loc = 'best')
    speed_figure.tight_layout()
    
    
    return speed_figure



def plot_acceleration_figure(theta_array : np.ndarray, acceleration_array : np.ndarray, coordinate_index : int,
                         point_label : str, title : str) -> pl.figure:
    """
    General function for plotting x or y acceleration vs. crank angle. 
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        acceleration_array (np.ndarray): Acceleration array for a point.
        coordinate_index (int): 0 for x-acceleration, 1 for y-acceleration.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    acceleration_figure, acceleration_axes = setup_figure()
    
    # Choose coordinate label based on index
    coordinate_label = "Ax" if coordinate_index == 0 else "Ay"
    
    # Set title and axes labels
    acceleration_axes.set_title(title)
    acceleration_axes.set_xlabel("Clockwise Crank Angle Rotation [degrees]")
    acceleration_axes.set_ylabel(f"{coordinate_label} [mm/s²]")
    
    # Plot the acceleration vs. crank angle
    acceleration_axes.plot(theta_array, acceleration_array[:, coordinate_index], color=PATH_COLOR, linewidth=2.0, label=f"{coordinate_label} {point_label}")
    
    # Create Legend & Layout
    acceleration_axes.legend(loc = 'best')
    acceleration_figure.tight_layout()
    
    
    return acceleration_figure

