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
from matplotlib.patches import Arc

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
LINK_P_COLOR = "#495057"

# Point Colors
POINT_COLOR = "#000000"  

# * Link N Line Style *
LINK_N_LINE_STYLE = '--'  

# * Link P Line Style *
LINK_P_LINE_STYLE = '--'


# * FUNCTION *
# ? ================================================================ ?



def math_label(label : str) -> str:
    """
    Converts a label into a math expression for plotting.
    
    ! Example:
        "Point P1" -> "Point_P1"
    
    Args:
        label (str) : The label to be converted.
        
    Returns:
        The converted label suitable for plotting.
    """
    return label.replace(" ", "_").replace("-", "_")


def crank_angle_label() -> str:
    """
    Returns a standardized label for the crank angle in degrees.
    
    Returns:
        The standardized label for the crank angle.
    """
    return r"Counter Clockwise Crank Angle $\theta_M$° , ↺"
    
    
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
    figure = pl.figure(figsize=(7, 7))
    
    # Create axis 
    axes = figure.add_subplot(1, 1, 1)
    axes.grid(True, linestyle='--', alpha=0.5)
    axes.tick_params(axis='both', labelsize=10)
    
    
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


def draw_path(axes: pl.axes, path_array: np.ndarray, label : str, color : str = PATH_COLOR, linewidth : float = 3.0, linestyle : str = '-') -> None:
    """
    Draw a path on the given axes.
    
    Args:
        axes (pl.axes) : Matplotlib axes object.
        path_array (np.ndarray) : Array of position points [x, y].
        label (str) : Path label.
        color (str) : Path color. Default is PATH_COLOR.
        linewidth (float) : Line width. Default is 3.0.
        linestyle (str) : Line style. Default is '-'.
    
    Returns:
        None
    """
    # Plot the path as a line connecting the points
    axes.plot(path_array[:, 0], path_array[:, 1], label=label, color=color, linewidth=linewidth, linestyle=linestyle)


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


def plot_mechanism_figure(title : str, links : list[dict], points : list[dict], paths : list[dict] = None, padding : float = 20.0) -> pl.figure:
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
    mechanism_axes.set_title(title, fontsize=14, fontweight='bold')
    mechanism_axes.set_xlabel(r"$x$ [mm]", fontsize=12)
    mechanism_axes.set_ylabel(r"$y$ [mm]", fontsize=12)
    
    # Draw paths if provided:
    if paths is not None:
        for path in paths:
            draw_path(mechanism_axes, path['array'], path['label'], path.get('color', PATH_COLOR), path.get('linewidth', 3.0), path.get('linestyle', '-'))
            
    # Draw links
    for link in links:
        draw_link(mechanism_axes, link['point_1'], link['point_2'], link['label'], link['color'], link.get('linestyle', '-'), link.get('linewidth', 2.0))
    
    # Draw points
    for point in points:
        draw_point(mechanism_axes, point['point'], point['label'], x_offset=point.get('x_offset', 6.0), y_offset=point.get('y_offset', 6.0))
    
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
    mechanism_axes.legend(loc = 'best', fontsize = 9)
    mechanism_figure.tight_layout()
    
    
    return mechanism_figure


def plot_position_figure(theta_array : np.ndarray, position_array : np.ndarray, coordinate_index : int, point_label : str, title : str) -> pl.figure:
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
    point_subscript = math_label(point_label)
    
    if coordinate_index == 0:
        coordinate_label = r"$P_x$"
        legend_label = rf"$P_{{x, {point_subscript}}}$"
    else:
        coordinate_label = r"$P_y$"
        legend_label = rf"$P_{{y, {point_subscript}}}$"
    
    # Set title and axes labels
    position_axes.set_title(title, fontsize=14, fontweight='bold')
    position_axes.set_xlabel(crank_angle_label(), fontsize=12)
    position_axes.set_ylabel(rf"{coordinate_label} [mm]", fontsize=12)
    
    # Plot the position vs. crank angle
    position_axes.plot(theta_array, position_array[:, coordinate_index], color=PATH_COLOR, linewidth=2.0, label=legend_label)
    
    # Create Legend & Layout
    position_axes.legend(loc = 'best', fontsize=10)
    position_figure.tight_layout()
    
    
    return position_figure


def plot_velocity_figure(theta_array : np.ndarray, velocity_array : np.ndarray, coordinate_index : int, point_label : str, title : str) -> pl.figure:
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
    point_subscript = math_label(point_label)
    
    if coordinate_index == 0:
        coordinate_label = r"$V_x$"
        legend_label = rf"$V_{{x, {point_subscript}}}$"
    else:
        coordinate_label = r"$V_y$"
        legend_label = rf"$V_{{y, {point_subscript}}}$"
        
    # Set title and axes labels
    velocity_axes.set_title(title, fontsize=14, fontweight='bold')
    velocity_axes.set_xlabel(crank_angle_label(), fontsize=12)
    velocity_axes.set_ylabel(rf"{coordinate_label} [mm/s]", fontsize=12)
    
    # Plot the velocity vs. crank angle
    velocity_axes.plot(theta_array, velocity_array[:, coordinate_index], color=PATH_COLOR, linewidth=2.0, label=legend_label)

    # Create Legend & Layout
    velocity_axes.legend(loc = 'best', fontsize=10)
    velocity_figure.tight_layout()
    
    
    return velocity_figure


def plot_speed_figure(theta_array : np.ndarray, velocity_array : np.ndarray, point_label : str, title : str) -> pl.figure:
    """
    General function for plotting speed vs. crank angle.
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        velocity_array (np.ndarray): Velocity array for a point.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    speed_figure, speed_axes = setup_figure()
    
    point_subscript = math_label(point_label)
    speed_array = np.linalg.norm(velocity_array, axis=1)
    
    # Set title and axes labels
    speed_axes.set_title(title, fontsize=14, fontweight='bold')
    speed_axes.set_xlabel(crank_angle_label(), fontsize=12)
    speed_axes.set_ylabel(rf"$|V_{{{point_subscript}}}|$ ", fontsize=12)
    
    # Plot the speed vs. crank angle
    speed_axes.plot(theta_array, speed_array, color=PATH_COLOR, linewidth=2.0, label=rf"$|V_{{{point_subscript}}}|$")
    
    # Create Legend & Layout
    speed_axes.legend(loc = 'best', fontsize=10)
    speed_figure.tight_layout()
    
    
    return speed_figure


def plot_angular_velocity_figure(theta_array : np.ndarray, omega_array : np.ndarray, point_label : str, title : str) -> pl.figure:
    """
    General function for plotting angular velocity vs. crank angle.
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        omega_array (np.ndarray): Angular velocity array for a point.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    omega_figure, omega_axes = setup_figure()
    
    # Get point subscript for legend label
    link_subscript = math_label(point_label)
    
    # Set title and axes labels
    omega_axes.set_title(title, fontsize=14, fontweight='bold')
    omega_axes.set_xlabel(crank_angle_label(), fontsize=12)
    omega_axes.set_ylabel(r"$\omega_{{{link_subscript}}}$ [rad/s]", fontsize=12)
    
    # Plot the angular velocity vs. crank angle
    omega_axes.plot(theta_array, omega_array, color=PATH_COLOR, linewidth=2.0, label=rf"$\omega_{{{link_subscript}}}$")
    
    # Create Legend & Layout
    omega_axes.legend(loc = 'best', fontsize=10)
    omega_figure.tight_layout()
    
    
    return omega_figure


def plot_acceleration_figure(theta_array : np.ndarray, acceleration_array : np.ndarray, coordinate_index : int, point_label : str, title : str) -> pl.figure:
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
    point_subscript = math_label(point_label)
    
    if coordinate_index == 0:
        coordinate_label = r"$A_x$"
        legend_label = rf"$A_{{x, {point_subscript}}}$"
    else:
        coordinate_label = r"$A_y$"
        legend_label = rf"$A_{{y, {point_subscript}}}$"
    
    # Set title and axes labels
    acceleration_axes.set_title(title, fontsize=14, fontweight='bold')
    acceleration_axes.set_xlabel(crank_angle_label(), fontsize=12)
    acceleration_axes.set_ylabel(rf"{coordinate_label} [mm/s$^2$]", fontsize=12)
    
    # Plot the acceleration vs. crank angle
    acceleration_axes.plot(theta_array, acceleration_array[:, coordinate_index], color=PATH_COLOR, linewidth=2.0, label=legend_label)
    
    
    # Create Legend & Layout
    acceleration_axes.legend(loc = 'best')
    acceleration_figure.tight_layout()
    
    
    return acceleration_figure


def plot_acceleration_magnitude_figure(theta_array : np.ndarray, acceleration_array : np.ndarray, point_label : str, title : str) -> pl.figure:
    """
    General function for plotting acceleration magnitude vs. crank angle.
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        acceleration_array (np.ndarray): Acceleration array for a point.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    acceleration_magnitude_figure, acceleration_magnitude_axes = setup_figure()
    
    # Get point subscript for legend label
    point_subscript = math_label(point_label)
    
    # Calculate acceleration magnitude
    acceleration_magnitude = np.linalg.norm(acceleration_array, axis=1)
    
    # Set title and axes labels
    acceleration_magnitude_axes.set_title(title, fontsize=14, fontweight='bold')
    acceleration_magnitude_axes.set_xlabel(crank_angle_label(), fontsize=12)
    acceleration_magnitude_axes.set_ylabel(r"$|A_{{{point_subscript}}}|$ [mm/s$^2$]", fontsize=12)
    
    # Plot the acceleration magnitude vs. crank angle
    acceleration_magnitude_axes.plot(theta_array, acceleration_magnitude, color=PATH_COLOR, linewidth=2.0, label=rf"$|A_{{{point_subscript}}}|$")
    
    # Create Legend & Layout
    acceleration_magnitude_axes.legend(loc = 'best', fontsize=10)
    acceleration_magnitude_figure.tight_layout()
    
    
    return acceleration_magnitude_figure


def plot_angular_acceleration_figure(theta_array : np.ndarray, alpha_array : np.ndarray, point_label : str, title : str) -> pl.figure:
    """
    General function for plotting angular acceleration vs. crank angle.
    
    Args:
        theta_array (np.ndarray): Crank rotation array in degrees.
        alpha_array (np.ndarray): Angular acceleration array for a point.
        point_label (str): Point label, such as P1, P2, or P5.
        title (str): Figure title.
    
    Returns:
        figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    angular_acceleration_figure, angular_acceleration_axes = setup_figure()
    
    # Get point subscript for legend label
    link_subscript = math_label(point_label)
    
    # Set title and axes labels
    angular_acceleration_axes.set_title(title, fontsize=14, fontweight='bold')
    angular_acceleration_axes.set_xlabel(crank_angle_label(), fontsize=12)
    angular_acceleration_axes.set_ylabel(r"$\alpha_{{{link_subscript}}}$ [rad/s$^2$]", fontsize=12)
    
    # Plot the angular acceleration vs. crank angle
    angular_acceleration_axes.plot(theta_array, alpha_array, color=PATH_COLOR, linewidth=2.0, label=rf"$\alpha_{{{link_subscript}}}$")
    
    # Create Legend & Layout
    angular_acceleration_axes.legend(loc = 'best', fontsize=10)
    angular_acceleration_figure.tight_layout()
    
    return angular_acceleration_figure


def plot_vector_figure(vector: np.ndarray, vector_label : str, title : str, x_label :str, y_label : str, units : str, theta_label: str = r"$\theta$") -> pl.figure:
    """
    Plots a single vector starting from the origin and includes the angle theta
    
    Args:
        vector (np.ndarray): Vector array with shape (n, 2) where n is the number of data points.
        vector_label (str): Label for the vector to be used in the legend.
        title (str): Figure title.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        units (str): Units to be displayed in the axis labels.
        theta_label (str): Label for the crank angle in the x-axis. Default is r"$\theta$".
    
    Returns:
        vector_figure (pl.figure) : Matplotlib figure object.
    """
    # Set up figure and axes
    vector_figure, vector_axes = setup_figure()
    
    # Components
    x_component = vector[0]
    y_component = vector[1]
    
    # Magnitude and angle
    magnitude = np.linalg.norm(vector)
    angle = np.degrees(np.arctan2(y_component, x_component))
    theta_display = angle if angle >= 0 else angle + 360
    
    # Draw x-axis and y-axis
    vector_axes.axhline(0, color='black', linewidth=1)
    vector_axes.axvline(0, color='black', linewidth=1)
    
    # Draw vector as an arrow
    vector_axes.quiver(0, 0, x_component, y_component, angles='xy', scale_units='xy', scale=1, color=PATH_COLOR, width = 0.005)
    
    # Add label near the tip of the vector
    vector_axes.annotate(vector_label, xy=(x_component, y_component), xytext=(8, 8), textcoords='offset points', fontsize=10, color=PATH_COLOR, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    # Arc radius
    max_value = max(abs(x_component), abs(y_component), 1.0)
    arc_radius = 0.35 * max_value
    
    # Draw Theta arc
    theta_arc = Arc((0, 0), width = 2 * arc_radius, height = 2 * arc_radius, angle=0, theta1=0, theta2=theta_display, color='gray', linewidth = 2.0)
    
    # Add a arrowhead at the end of the theta arc
    if theta_display > 0:
        theta_end = np.radians(theta_display)
        # Step back from the end of the arc to place the arrowhead
        theta_start = np.radians(theta_display - 8)   

        arc_arrow_start = np.array([arc_radius * np.cos(theta_start), arc_radius * np.sin(theta_start)])

        arc_arrow_end = np.array([arc_radius * np.cos(theta_end), arc_radius * np.sin(theta_end)])

        vector_axes.annotate("", xy=(arc_arrow_end[0], arc_arrow_end[1]), xytext=(arc_arrow_start[0], arc_arrow_start[1]),
            arrowprops=dict(arrowstyle="->", color="gray", lw=1.6, shrinkA=0, shrinkB=0))
    
    vector_axes.add_patch(theta_arc)
    
    # Place theta text at the midpoint of the arc
    theta_mid_angle = np.radians(theta_display / 2)
    theta_text_radius = arc_radius * 1.5
    theta_text_x = theta_text_radius * np.cos(theta_mid_angle)
    theta_text_y = theta_text_radius * np.sin(theta_mid_angle)
    
    vector_axes.text(theta_text_x, theta_text_y, theta_label, fontsize=12, color='gray', fontweight='bold', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    # Add magnitude and numerical angle in text box
    vector_axes.text(0.02, 0.95, f"|{vector_label}| = {magnitude:.2f} {units}\nθ = {theta_display:.2f}° ↺", transform=vector_axes.transAxes, verticalalignment='top', bbox=dict(facecolor='white', edgecolor='black', alpha=0.7))
    
    # Limits
    plot_limit = max_value * 1.5
    vector_axes.set_xlim(-plot_limit, plot_limit)
    vector_axes.set_ylim(-plot_limit, plot_limit)
    vector_axes.set_aspect('equal', adjustable='box')
    
    # Grid
    vector_axes.grid(True, linestyle='--', alpha=0.5)
    
    # Title and labels
    vector_axes.set_title(title, fontsize=14, fontweight='bold')
    vector_axes.set_xlabel(x_label, fontsize=12)
    vector_axes.set_ylabel(y_label, fontsize=12)
    
    # Layout
    vector_figure.tight_layout()
    
    
    return vector_figure