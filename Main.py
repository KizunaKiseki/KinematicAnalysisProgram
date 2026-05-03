# -*- coding: utf-8 -*-
"""
TITLE =[Insert Title]
DATE  = 2026.05.15
_____________________________________________________________________
DESCRIPTION:
1. [Insert Description]
_____________________________________________________________________
AUTHOR : Nicholas Heling
"""

# * IMPORTS *
# ? ================================================================ ?

# ! PYTHON TEMPLATES & LIBRARIES !
import os
import numpy as np
import matplotlib.pyplot as plt

# ! PROJECT MODULES !
import lib._Plot as _plot
import lib._Solve as _solve

# * VARIABLES *
# ? ================================================================ ?
# Scale Factor
SCALE_FACTOR = 1.5

# Link Lengths in [mm]
LINK_A = 38.00 * SCALE_FACTOR
LINK_B = 41.50 * SCALE_FACTOR   
LINK_C = 39.30 * SCALE_FACTOR
LINK_D = 40.10 * SCALE_FACTOR
LINK_E = 55.80 * SCALE_FACTOR
LINK_F = 39.40 * SCALE_FACTOR
LINK_G = 36.70 * SCALE_FACTOR
LINK_H = 65.70 * SCALE_FACTOR
LINK_I = 49.00 * SCALE_FACTOR
LINK_J = 50.00 * SCALE_FACTOR
LINK_K = 61.90 * SCALE_FACTOR
LINK_L = 7.80 * SCALE_FACTOR
LINK_M = 15.00 * SCALE_FACTOR

# ! Ground Link between A & M in [mm] !
LINK_N = np.sqrt(LINK_A ** 2 + LINK_L ** 2)

# Gear Ratio in [mm]
SMALL_GEAR_DIAMETER = 9     # Motor Gear
LARGE_GEAR_DIAMETER = 54    # Crank Gear
GEAR_RATIO = LARGE_GEAR_DIAMETER / SMALL_GEAR_DIAMETER

# Input Speed in [RPM]
MOTOR_SPEED = 30
CRANK_SPEED = MOTOR_SPEED / GEAR_RATIO

# Angular Velocity in [rad/s]
OMEGA_M = - (CRANK_SPEED * 2 * np.pi) / 60      # ↻ , Negative sign indicates clockwise rotation

# Angular Acceleration in [rad/s^2]
ALPHA_M = 0                                     # Assuming constant speed

# Input Crank Angle in [degrees]
CRANK_ANGLE = 0

# Single Test Angle in [radians]
THETA_M_TEST = np.deg2rad(CRANK_ANGLE)

# Crank Angle Array [radians]
NUM_STEPS = 361
CRANK_ANGLE_ARRAY = np.linspace(CRANK_ANGLE, CRANK_ANGLE - 360, NUM_STEPS)  # ↻ , from 0° to -360°
THETA_M_ARRAY = np.deg2rad(CRANK_ANGLE_ARRAY)

# Ground Points
O2 = np.array([0.0, 0.0])    
O4 = np.array([LINK_A, LINK_L]) 

# Figures Aesthetics Tweaks
CRANK_ANGLE_PLOT = np.linspace(0, CRANK_ANGLE - 360, NUM_STEPS)  


# * MAIN *
# ? ================================================================ ?

def main():
    """
    Summary of what the main does
    
    Args:
    
    
    Returns:
    
    
    Raises:
    """
    # Initialize figure_path & figure_names lists for saving figures
    figure_path = []
    figure_names = []
    
    # ! Solve across all crank angles !
    # Initialize array to store positions for each crank angle
    array_P1 = np.zeros((NUM_STEPS, 2))  
    array_P2 = np.zeros((NUM_STEPS, 2))
    array_P5 = np.zeros((NUM_STEPS, 2))
    array_P4 = np.zeros((NUM_STEPS, 2))
    
    # * Loop through each crank angle and solve for each position *
    for step, theta_m in enumerate(THETA_M_ARRAY):
        # ? Solve for Point P1 across all Crank Angles ?
        array_P1[step] = _solve.solve_point_1(O4, LINK_M, theta_m)
        
        # ? Solve for Point P2 across all Crank Angles ?
        array_P2[step] = _solve.solve_point_2(O2, array_P1[step], LINK_B, LINK_J)
        
        # ? Solve for Point P5 across all Crank Angles ?
        array_P5[step] = _solve.solve_point_5(O2, array_P1[step], LINK_C, LINK_K)
        
        # ? Solve for Point P4 across all Crank Angles ?
        array_P4[step] = _solve.solve_point_4(O2, array_P2[step], LINK_D, LINK_E)
    
    
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
            {"point" : O2, "label" : "O2", "x_offset" : -8.0, "y_offset" : -16.0},
            {"point" : O4, "label" : "O4", "x_offset" : -4.0, "y_offset" : -16.0},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 8.0, "y_offset" : -4.0},
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
            {"point" : O2, "label" : "O2", "x_offset" : -8.0, "y_offset" : -16.0},
            {"point" : O4, "label" : "O4", "x_offset" : -4.0, "y_offset" : -16.0},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 8.0, "y_offset" : -4.0},
        ],
        
        paths = [
            {
                "array" : array_P1,
                "label" : "P1 Path"
            }  
        ],
        
        padding = 20.0   
    )
    
    p1_x_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P1, 0, "P1", "Figure 3: Point P1 x-Position vs. Crank Angle")
    p1_y_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P1, 1, "P1", "Figure 4: Point P1 y-Position vs. Crank Angle")
    
    
    # Append P1 Figures to Figure Path
    figure_path.append(ground_figure)
    figure_path.append(p1_position_figure)
    figure_path.append(p1_x_figure)
    figure_path.append(p1_y_figure)
    
    # Append P1 Figure Names to Figure Names List
    figure_names.append("Ground_Link")
    figure_names.append("P1_Position")
    figure_names.append("P1_x_Position")
    figure_names.append("P1_y_Position")
    
    
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
            {"point" : O2, "label" : "O2", "x_offset" : -8.0, "y_offset" : -16.0},
            {"point" : O4, "label" : "O4", "x_offset" : -4.0, "y_offset" : -16.0},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 0.0, "y_offset" : -16.0},
            {"point" : array_P2[0], "label" : "P2", "x_offset" : -4.0, "y_offset" : 8.0},
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
            {"point" : O2, "label" : "O2", "x_offset" : -8.0, "y_offset" : -16.0},
            {"point" : O4, "label" : "O4", "x_offset" : -4.0, "y_offset" : -16.0},
            {"point" : array_P1[0], "label" : "P1", "x_offset" : 0.0, "y_offset" : -16.0},
            {"point" : array_P2[0], "label" : "P2", "x_offset" : 4.0, "y_offset" : 8.0},
        ],
        
        paths = [
            {   
                "array" : array_P2,
                "label" : "P2 Path"
            }
        ],
        
        padding = 20.0
    )

    P2_x_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P2, 0, "P2", "Figure 7: Point P2 x-Position vs. Crank Angle")
    P2_y_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P2, 1, "P2", "Figure 8: Point P2 y-Position vs. Crank Angle")
    
    
    # Append P2 Figures to Figure Path
    figure_path.append(nm_bj_figure)
    figure_path.append(p2_position_figure)
    figure_path.append(P2_x_figure)
    figure_path.append(P2_y_figure)
    
    # Append P2 Figure Names to Figure Names List
    figure_names.append("Closed_Loop_NM_BJ")
    figure_names.append("P2_Position")
    figure_names.append("P2_x_Position")
    figure_names.append("P2_y_Position")


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
    
    P5_x_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P5, 0, "P5", "Figure 11: Point P5 x-Position vs. Crank Angle")
    P5_y_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P5, 1, "P5", "Figure 12: Point P5 y-Position vs. Crank Angle")
    
    
    # Append P5 Figures to Figure Path
    figure_path.append(nm_ck_figure)
    figure_path.append(p5_position_figure)
    figure_path.append(P5_x_figure)
    figure_path.append(P5_y_figure)
    
    # Append P5 Figure Names to Figure Names List
    figure_names.append("Closed_Loop_NM_CK")
    figure_names.append("P5_Position")
    figure_names.append("P5_x_Position")
    figure_names.append("P5_y_Position")

    
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
                "point_2": O4,
                "label": "Link N",
                "color": _plot.LINK_N_COLOR,
                "linestyle": _plot.LINK_N_LINE_STYLE,
            },
            {
                "point_1": O4,
                "point_2": array_P1[0],
                "label": "Link M",
                "color": _plot.LINK_M_COLOR,
            },
            {
                "point_1": O2,
                "point_2": array_P2[0],
                "label": "Link B",
                "color": _plot.LINK_B_COLOR,
            },
            {
                "point_1": array_P1[0],
                "point_2": array_P2[0],
                "label": "Link J",
                "color": _plot.LINK_J_COLOR,
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
            {"point": O4, "label": "O4", "x_offset": -6, "y_offset": -14},
            {"point": array_P1[0], "label": "P1", "x_offset": -2, "y_offset": -14},
            {"point": array_P2[0], "label": "P2", "x_offset": 4, "y_offset": 6},
            {"point": array_P4[0], "label": "P4", "x_offset": -14, "y_offset": 6},
        ],

        paths=[
            {
                "array": array_P4,
                "label": "P4 Path"
            }
        ],

        padding=20.0
    )
    
    P4_x_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P4, 0, "P4", "Figure 15: Point P4 x-Position vs. Crank Angle")
    P4_y_figure = _plot.plot_position_figure(CRANK_ANGLE_PLOT, array_P4, 1, "P4", "Figure 16: Point P4 y-Position vs. Crank Angle")
    
    # Append P4 Figures to Figure Path
    figure_path.append(bde_rigid_body_figure)
    figure_path.append(p4_position_figure)
    figure_path.append(P4_x_figure)
    figure_path.append(P4_y_figure)
    
    # Append P4 Figure Names to Figure Names List
    figure_names.append("Rigid_Body_BDE")
    figure_names.append("P4_Position")
    figure_names.append("P4_x_Position")
    figure_names.append("P4_y_Position")
    
    

    # Create Figures Dictionary to save figures
    figures_dictionary = os.path.join(os.path.dirname(__file__), 'Figures')
    os.makedirs(figures_dictionary, exist_ok=True)
    
    # Save Figures to Figures Directory as PDF
    for figure, name in zip(figure_path, figure_names):
        figure_file_path = os.path.join(figures_dictionary, f'{name}.png')
        figure.savefig(figure_file_path, bbox_inches='tight', dpi=300)
        
        # Success Message for Saving Figure
        print(f"✅ {name} saved to {figure_file_path}")
    
       
# * EXECUTE *
# ? ================================================================ ?
if __name__ == "__main__":
    main()