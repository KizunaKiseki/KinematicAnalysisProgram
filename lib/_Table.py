# -*- coding: utf-8 -*-
"""
TITLE = Table Figures for Theo Jansen Mechanism
DATE  = 2026.05.15
_____________________________________________________________________
DESCRIPTION:
1. Functions to create standardized figure titles and file names for table analysis.
2. Functions to create and format table figures.
_____________________________________________________________________
AUTHOR : Nicholas Heling
"""

# * IMPORTS *
# ? ================================================================ ?

# ! PYTHON TEMPLATES & LIBRARIES !
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# * VARIABLES *
# ? ================================================================ ?
TITLE_BAR_COLOR = '#D9D9D9'
HEADER_BACKGROUND_COLOR = '#000000'
HEADER_TEXT_COLOR = '#FFFFFF'
BODY_BACKGROUND_1 = '#DCEAF7'
BODY_BACKGROUND_2 = '#C7DDF0'
INPUT_BACKGROUND = "#C6E0B4"
EDGE_COLOR = '#000000'

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
    if extra:
        figure_title = f"{analysis_type} {subject} {extra}"
        figure_name = f"Figure{figure_number:02d}_{analysis_type}_{subject}_{extra}"
    else:
        figure_title = f"{analysis_type} {subject}"
        figure_name = f"Figure{figure_number:02d}_{analysis_type}_{subject}"
        
    # Clean File Name
    figure_name = (figure_name.replace(" ", "_").replace("-", "_").replace("+", "").replace(":", "")
                   .replace(".", "").replace("(", "").replace(")", "").replace("θ", "theta")
                   .replace("α", "alpha").replace("ω", "omega").replace("°", "deg").replace("=", ""))
    
    
    return figure_title, figure_name



def format_magnitude(value: float, precision: int = 3) -> str:
    """
    Formats a magnitude value with a positive values
    
    Args:
        value (float): The value to format.
        precision (int, optional): The number of decimal places to include. Defaults to 3.
    
    Returns:
        formatted_value (str): The formatted magnitude value as a string with a positive sign.
    """
    
    return f"{abs(value):.{precision}f}"


def get_rotation_direction(value: float, tolerance: float = 1e-9) -> str:
    """
    Determines the angular direction from the sign convection.
    
    Positive = CCW
    Negative = CW
    Zero = 0
    
    Args:
        value (float): The value to evaluate for rotation direction.
        tolerance (float, optional): A small threshold to consider values as zero. Defaults to 1e-9.
    
    Returns:
        str: "CCW" for counterclockwise, "CW" for clockwise, and "0" for no rotation.
    """
    if value > tolerance:
        return "CCW"
    elif value < -tolerance:
        return "CW"
    else:
        return "-"
    

def create_table_figure(title: str, column_labels: list[str], table_data: list[list[str]]) -> plt.Figure:
    """
    Creates a table figure using matplotlib.
    
    Args:
        title (str): The title of the table figure.
        column_labels (list[str]): The labels for the table columns.
        table_data (list[list[str]]): The data to be displayed in the table.
    
    Returns:
        plt.Figure: The matplotlib figure containing the table.
    """
    # Create Table Figure and Axes
    table_figure, table_axes = plt.subplots(figsize=(8, len(table_data) * 0.5 + 1))
    table_axes.axis('off')  
    
    # Set Table Title
    table_axes.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Title Bar
    table_axes.add_patch(Rectangle((0.02, 0.865), 0.96, 0.115, facecolor=TITLE_BAR_COLOR, edgecolor=EDGE_COLOR, transform=table_axes.transAxes))
    
    # Create Axes for Table
    table_axes.text(0.5, 0.92, title, ha='center', va='center', fontsize=20, fontweight='bold', family='serif', transform=table_axes.transAxes)
    
    # Create Table
    table = table_axes.table(cellText=table_data, colLabels=column_labels, cellLoc='center', loc='center', colWidths=[0.22, 0.56, 0.26], bbox=[0.02, 0.02, 0.96, 0.80])
    
    # Table Scale
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    
    # Number of Rows and Columns
    num_rows, num_cols = len(table_data), len(column_labels)
    
    # Style Header Row
    for column_index in range(num_cols):
        cell = table[0, column_index]
        cell.set_facecolor(HEADER_BACKGROUND_COLOR)
        cell.set_edgecolor(EDGE_COLOR)
        cell.set_linestyle('solid')
        cell.set_text_props(color=HEADER_TEXT_COLOR, weight='bold', family='serif')
        
    # Style Body Rows
    for row_index in range(1, num_rows + 1):
        for column_index in range(num_cols):
            cell = table[row_index, column_index]
            cell.set_edgecolor(EDGE_COLOR)
            cell.set_linewidth(1.1)

            # Higlight Input Row Link M
            if row_index == 1:
                cell.set_facecolor(INPUT_BACKGROUND)
                cell.set_text_props(weight='bold', family='serif')
            else:
                if row_index % 2 == 0:
                    cell.set_facecolor(BODY_BACKGROUND_1)
                else:
                    cell.set_facecolor(BODY_BACKGROUND_2)
                    
                cell.set_text_props(family='serif')
                
            # Bold Link Names
            if column_index == 0:
                cell.set_text_props(weight='bold', family='serif')
                
    table_figure.tight_layout()
    
    
    return table_figure


def append_angular_velocity_table(table_path: list, table_names: list, figure_number: int, step: int, omega_M : np.ndarray, omega_B : np.ndarray, omega_J: np.ndarray, omega_C: np.ndarray, Omega_K: np.ndarray, Omega_D: np.ndarray, Omega_E: np.ndarray, Omega_F: np.ndarray, Omega_G: np.ndarray, Omega_H: np.ndarray, Omega_I: np.ndarray, decimals : int = 3) -> int:
    """
    Appends an angular velocity summary table.
    
    Args:
        table_path (list): List to store the table figure paths.
        table_names (list): List to store the table names.
        figure_number (int): The current figure number to be updated.
        step (int): The current step of the analysis.
        omega_M (np.ndarray): Angular velocity array for Link M.
        omega_B (np.ndarray): Angular velocity array for Link B.
        omega_J (np.ndarray): Angular velocity array for Link J.
        omega_C (np.ndarray): Angular velocity array for Link C.
        Omega_K (np.ndarray): Angular velocity array for Link K.
        Omega_D (np.ndarray): Angular velocity array for Link D.
        Omega_E (np.ndarray): Angular velocity array for Link E.
        Omega_F (np.ndarray): Angular velocity array for Link F.
        Omega_G (np.ndarray): Angular velocity array for Link G.
        Omega_H (np.ndarray): Angular velocity array for Link H.
        Omega_I (np.ndarray): Angular velocity array for Link I.
        decimals (int, optional): Number of decimal places for formatting. Defaults to 3.
    
    Returns:
        figure_number (int): Updated figure number after appending the table.
    """
    # Create Table Title and Name
    title, name = make_figure_label(figure_number, "Table", "Angular Velocity, ω", "θ_M = 0°")
    
    # Define Table Column Labels and Data
    column_labels = ["Link", "Angular Velocity (ω) [rad/s]", "Direction"]
    
    # Collect Angular Velocity Data for Each Link at the Current Step
    omega_data = [
        ("M", omega_M),
        ("B", omega_B[step]),
        ("J", omega_J[step]),
        ("C", omega_C[step]),
        ("K", Omega_K[step]),
        ("D", Omega_D[step]),
        ("E", Omega_E[step]),
        ("F", Omega_F[step]),
        ("G", Omega_G[step]),
        ("H", Omega_H[step]),
        ("I", Omega_I[step])
    ]
    
    table_data = []
    
    # Format Data for Table
    for link_label, value in omega_data:
        table_data.append([f"Link {link_label}", f"{format_magnitude(value, decimals)}", get_rotation_direction(value)])
    
    
    # ! Create Table Figure for Angular Velocity  !
    table_figure = create_table_figure(f"Table ANGULAR VELOCITY", column_labels, table_data)
    
    table_figure.axes[0].set_title(title, fontsize=1, color="white")
    
    table_path.append(table_figure)
    table_names.append(name)
    
    
    return figure_number + 1
    

def append_angular_acceleration_table(table_path: list, table_names: list, figure_number: int, step: int, alpha_M : np.ndarray, alpha_B : np.ndarray, alpha_J: np.ndarray, alpha_C: np.ndarray, Alpha_K: np.ndarray, Alpha_D: np.ndarray, Alpha_E: np.ndarray, Alpha_F: np.ndarray, Alpha_G: np.ndarray, Alpha_H: np.ndarray, Alpha_I: np.ndarray, decimals : int = 3) -> int:
    """
    Appends an angular acceleration summary table.
    
    Args:
        table_path (list): List to store the table figure paths.
        table_names (list): List to store the table names.
        figure_number (int): The current figure number to be updated.
        step (int): The current step of the analysis.
        alpha_M (np.ndarray): Angular acceleration array for Link M.
        alpha_B (np.ndarray): Angular acceleration array for Link B.
        alpha_J (np.ndarray): Angular acceleration array for Link J.
        alpha_C (np.ndarray): Angular acceleration array for Link C.
        Alpha_K (np.ndarray): Angular acceleration array for Link K.
        Alpha_D (np.ndarray): Angular acceleration array for Link D.
        Alpha_E (np.ndarray): Angular acceleration array for Link E.
        Alpha_F (np.ndarray): Angular acceleration array for Link F.
        Alpha_G (np.ndarray): Angular acceleration array for Link G.
        Alpha_H (np.ndarray): Angular acceleration array for Link H.
        Alpha_I (np.ndarray): Angular acceleration array for Link I.
        decimals (int, optional): Number of decimal places for formatting. Defaults to 3.
    
    Returns:
        figure_number (int): Updated figure number after appending the table.
    """
    # Create Table Title and Name
    title, name = make_figure_label(figure_number, "Table", "Angular Acceleration, α", "θ_M = 0°")
    
    # Define Table Column Labels and Data
    column_labels = ["Link", "Angular Acceleration (α) [rad/s²]", "Direction"]
    
    # Collect Angular Acceleration Data for Each Link at the Current Step
    alpha_data = [
        ("M", alpha_M),
        ("B", alpha_B[step]),
        ("J", alpha_J[step]),
        ("C", alpha_C[step]),
        ("K", Alpha_K[step]),
        ("D", Alpha_D[step]),
        ("E", Alpha_E[step]),
        ("F", Alpha_F[step]),
        ("G", Alpha_G[step]),
        ("H", Alpha_H[step]),
        ("I", Alpha_I[step])
    ]
    
    table_data = []
    
    # Format Data for Table
    for link_label, value in alpha_data:
        table_data.append([f"Link {link_label}", f"{format_magnitude(value, decimals)}", get_rotation_direction(value)])
    
    
    # ! Create Table Figure for Angular Acceleration  !
    table_figure = create_table_figure(f"Table ANGULAR ACCELERATION", column_labels, table_data)
    
    table_figure.axes[0].set_title(title, fontsize=1, color="white")
    
    table_path.append(table_figure)
    table_names.append(name)
    
    
    return figure_number + 1



def create_angular_summary_tables(step : int, omega_M : np.ndarray, omega_B : np.ndarray, omega_J: np.ndarray, omega_C: np.ndarray, Omega_K: np.ndarray, Omega_D: np.ndarray, Omega_E: np.ndarray, Omega_F: np.ndarray, Omega_G: np.ndarray, Omega_H: np.ndarray, Omega_I: np.ndarray, 
                                  alpha_M : np.ndarray, alpha_B : np.ndarray, alpha_J: np.ndarray, alpha_C: np.ndarray, Alpha_K: np.ndarray, Alpha_D: np.ndarray, Alpha_E: np.ndarray, Alpha_F: np.ndarray, Alpha_G: np.ndarray, Alpha_H: np.ndarray, Alpha_I: np.ndarray, decimals : int = 3) -> tuple[list, list]:
    """
    Creates angular velocity and angular acceleration summary tables for a specific step of the analysis.
    
    Args:
        step (int): The current step of the analysis for which the tables are being created.
        omega_M (np.ndarray): Angular velocity array for Link M.
        omega_B (np.ndarray): Angular velocity array for Link B.
        omega_J (np.ndarray): Angular velocity array for Link J.
        omega_C (np.ndarray): Angular velocity array for Link C.
        Omega_K (np.ndarray): Angular velocity array for Link K.
        Omega_D (np.ndarray): Angular velocity array for Link D.
        Omega_E (np.ndarray): Angular velocity array for Link E.
        Omega_F (np.ndarray): Angular velocity array for Link F.
        Omega_G (np.ndarray): Angular velocity array for Link G.
        Omega_H (np.ndarray): Angular velocity array for Link H.
        Omega_I (np.ndarray): Angular velocity array for Link I.
        alpha_M (np.ndarray): Angular acceleration array for Link M.
        alpha_B (np.ndarray): Angular acceleration array for Link B.
        alpha_J (np.ndarray): Angular acceleration array for Link J.
        alpha_C (np.ndarray): Angular acceleration array for Link C.
        Alpha_K (np.ndarray): Angular acceleration array for Link K.
        Alpha_D (np.ndarray): Angular acceleration array for Link D.
        Alpha_E (np.ndarray): Angular acceleration array for Link E.
        Alpha_F (np.ndarray): Angular acceleration array for Link F.
        Alpha_G (np.ndarray): Angular acceleration array for Link G.
        Alpha_H (np.ndarray): Angular acceleration array for Link H.
        Alpha_I (np.ndarray): Angular acceleration array for Link I.
        decimals (int, optional): Number of decimal places for formatting. Defaults to 3.
    
    Returns:
        table_path (list): A list of matplotlib path objects for the created tables.
        table_names (list): A list of names corresponding to each created table.
    """
    # Initialize lists to store table paths and names
    table_path = []
    table_names = []
    figure_number = 1
    
    # ? Angular Velocity Summary Table ?
    figure_number = append_angular_velocity_table(table_path, table_names, figure_number, step, omega_M, omega_B, omega_J, omega_C, Omega_K, Omega_D, Omega_E, Omega_F, Omega_G, Omega_H, Omega_I, decimals)
    
    # ? Angular Acceleration Summary Table ?
    figure_number = append_angular_acceleration_table(table_path, table_names, figure_number, step, alpha_M, alpha_B, alpha_J, alpha_C, Alpha_K, Alpha_D, Alpha_E, Alpha_F, Alpha_G, Alpha_H, Alpha_I, decimals)
    
    
    return table_path, table_names

