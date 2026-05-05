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


# * FUNCTION *
# ? ================================================================ ?


def circle_intersection(center_1 : np.ndarray, radius_1 : float, center_2 : np.ndarray, 
                        radius_2 : float) -> tuple[np.ndarray, np.ndarray]:
    """
    Solves the intersection points of two circles.
    
    ! Circle Equations:
        1. (x - x1)^2 + (y - y1)^2 = r1^2
        2. (x - x2)^2 + (y - y2)^2 = r2^2
    
    Args:
        center_1 (np.ndarray): Center of the first circle [x1, y1].
        radius_1 (float): Radius of the first circle.
        center_2 (np.ndarray): Center of the second circle [x2, y2].
        radius_2 (float): Radius of the second circle.
    
    Returns:
        intersection_1 (np.ndarray): First intersection point [x, y].
        intersection_2 (np.ndarray): Second intersection point [x, y].
    
    Raises:
        ValueError: If the circles do not intersect or are coincident.
    """
    # Extract center coordinates
    x1, y1 = center_1
    x2, y2 = center_2
    
    # Calculate distance between centers
    dx = x2 - x1
    dy = y2 - y1
    d = np.sqrt(dx**2 + dy**2)
    
    # Check for non-intersecting circles
    if d > radius_1 + radius_2:
        raise ValueError("Circles do not intersect.")
    
    # Check for one circle within the other
    if d < abs(radius_1 - radius_2):
        raise ValueError("One circle is contained within the other.")
    
    # Check for coincident circles
    if d == 0 and radius_1 == radius_2:
        raise ValueError("Circles are coincident.")

    # Calculate intersection points
    a = (radius_1**2 - radius_2**2 + d**2) / (2 * d)
    h = np.sqrt(radius_1**2 - a**2)
    
    # Calculate midpoint between the two centers along the line connecting them
    midpoint = center_1 + a * np.array([dx, dy]) / d
    offset = h * np.array([-dy, dx]) / d
    
    intersection_1 = midpoint + offset
    intersection_2 = midpoint - offset
    
    
    return intersection_1, intersection_2
    

def perpendicular(vector : np.ndarray) -> np.ndarray:
    """
    Returns the 2D perpendicular vector used for planar cross products.
    
    For planar motion:
        omega x r = omega * [-r_y, r_x]
        
    Args:
        vector (np.ndarray): A 2D vector [x, y].
        
    Returns:
        perpendicular_vector (np.ndarray): The perpendicular vector [-y, x].
    """
    
    return np.array([-vector[1], vector[0]])


def choose_intersection(option_1 : np.ndarray, option_2 : np.ndarray, selection : str) -> np.ndarray:
    """
    Selects the correct circle intersection point based on mechanism geometry.
    
    Args:
        option_1 (np.ndarray): First intersection point [x, y].
        option_2 (np.ndarray): Second intersection point [x, y].
        selection (str): Selection rule:
            "max_y" - Select the point with the larger y-value.
            "min_y" - Select the point with the smaller y-value.
            "max_x" - Select the point with the larger x-value.
            "min_x" - Select the point with the smaller x-value.
                
    Returns:
        selected_point (np.ndarray): The selected intersection point based on the selection rule.
        
    Raises:
        ValueError: If an unknown selection rule is provided.
    """
    if selection == "max_y":
        return option_1 if option_1[1] > option_2[1] else option_2
    elif selection == "min_y":
        return option_1 if option_1[1] < option_2[1] else option_2
    elif selection == "max_x":
        return option_1 if option_1[0] > option_2[0] else option_2
    elif selection == "min_x":
        return option_1 if option_1[0] < option_2[0] else option_2
    else:
        raise ValueError(f"Unknown selection rule: {selection}")


def solve_point_from_two_links(center_1 : np.ndarray, center_2 : np.ndarray, radius_1 : float, radius_2 : float, selection : str) -> np.ndarray:
    """
    General position solver for a point connected to two known points by two links.
    
    Args:
        center_1 (np.ndarray): First known point [x, y].
        center_2 (np.ndarray): Second known point [x, y].
        radius_1 (float): Length of the link connecting the point to center_1.
        radius_2 (float): Length of the link connecting the point to center_2.
        selection (str): Selection rule for choosing the correct intersection point.
    
    Returns:
        chosen_point (np.ndarray): The solved point position [x, y].
    """
    option_1, option_2 = circle_intersection(center_1, radius_1, center_2, radius_2)
    
    chosen_point = choose_intersection(option_1, option_2, selection)
    
    
    return chosen_point


def solve_velocity_two_link_loop(base_1 : np.ndarray, base_2 : np.ndarray, target : np.ndarray, velocity_base_1 : np.ndarray, velocity_base_2 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    General velocity solver for a point connected to two moving or fixed base points.
    
    ! Velocity Relationships:
        V_target = V_base_1 + omega_1 x r_1
        V_target = V_base_2 + omega_2 x r_2
        
        ? Where:
            r_1 = target - base_1
            r_2 = target - base_2
    
    ! Matrix Form:
        | -r_1_y   r_2_y | | omega_1 | = | Vx_base_1 - Vx_base_2 |
        | r_1_x   -r_2_x | | omega_2 | = | Vy_base_1 - Vy_base_2 |
    
    Args:
        base_1 (np.ndarray): First base point [x, y].
        base_2 (np.ndarray): Second base point [x, y].
        target (np.ndarray): Target point whose velocity is being solved [x, y].
        velocity_base_1 (np.ndarray): Velocity of the first base point [v_x, v_y].
        velocity_base_2 (np.ndarray): Velocity of the second base point [v_x, v_y].
    
    Returns:
        velocity_target (np.ndarray): Velocity of the target point [v_x, v_y].
        omega_1 (float): Angular velocity of the link connecting target to base_1.
        omega_2 (float): Angular velocity of the link connecting target to base_2.
    """
    # Position vectors from base points to target
    r_1 = target - base_1
    r_2 = target - base_2
    
    # Coefficient matrix for omega_1 and omega_2
    coefficient_matrix = np.array([[-r_1[1], r_2[1]], [r_1[0], -r_2[0]]])
    
    # RHS vector for velocity differences
    rhs_vector = velocity_base_1 - velocity_base_2
    
    # Solve for omega_1 and omega_2
    omega_1, omega_2 = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Calculate velocity of the target point using one of the velocity equations
    velocity_target = velocity_base_1 + omega_1 * perpendicular(r_1)
    
    
    return velocity_target, omega_1, omega_2


def solve_acceleration_two_link_loop(base_1 : np.ndarray, base_2 : np.ndarray, target : np.ndarray, acceleration_base_1 : np.ndarray, acceleration_base_2 : np.ndarray, omega_1 : float, omega_2 : float) -> tuple[np.ndarray, float, float]:
    """
    General acceleration solver for a point connected to two moving or fixed base points.
    
    ! Acceleration Relationships:
        A_target = A_base_1 + alpha_1 x r_1 - omega_1^2 * r_1
        A_target = A_base_2 + alpha_2 x r_2 - omega_2^2 * r_2
    
        ? Where:
            r_1 = target - base_1
            r_2 = target - base_2
            
    ! Matrix Form:
        | -r_1_y   r_2_y | | alpha_1 | = | A_target_x - A_base_1_x + omega_1^2 * r_1_x - A_base_2_x + omega_2^2 * r_2_x |
        | r_1_x   -r_2_x | | alpha_2 | = | A_target_y - A_base_1_y + omega_1^2 * r_1_y - A_base_2_y + omega_2^2 * r_2_y |
    
    Args:
        base_1 (np.ndarray): First base point [x, y].
        base_2 (np.ndarray): Second base point [x, y].
        target (np.ndarray): Target point whose acceleration is being solved [x, y].
        acceleration_base_1 (np.ndarray): Acceleration of the first base point [a_x, a_y].
        acceleration_base_2 (np.ndarray): Acceleration of the second base point [a_x, a_y].
        omega_1 (float): Angular velocity of the link connecting target to base_1.
        omega_2 (float): Angular velocity of the link connecting target to base_2.
    
    Returns:
        acceleration_target (np.ndarray): Acceleration of the target point [a_x, a_y].
        alpha_1 (float): Angular acceleration of the link connecting target to base_1.
        alpha_2 (float): Angular acceleration of the link connecting target to base_2.
    """
    # Position vectors from base points to target
    r_1 = target - base_1
    r_2 = target - base_2
    
    # Coefficient matrix for alpha_1 and alpha_2
    coefficient_matrix = np.array([[-r_1[1], r_2[1]], [r_1[0], -r_2[0]]])
    
    # RHS vector for acceleration differences and centripetal terms
    rhs_vector = (acceleration_base_1 - acceleration_base_2) + (omega_1**2 * r_1 - omega_2**2 * r_2)
    
    # Solve for alpha_1 and alpha_2
    alpha_1, alpha_2 = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Calculate acceleration of the target point using one of the acceleration equations
    acceleration_target = acceleration_base_1 + alpha_1 * perpendicular(r_1) - omega_1**2 * r_1
    
    
    return acceleration_target, alpha_1, alpha_2




def solve_point_1(O4 : np.ndarray, link_m : float, theta_m : float) -> np.ndarray:
    """
    Solve the position of Point P1.
    
    ! Vector Equation:
        1. r_P1 = r_O4 + r_m

    ! Position Equation:
        2. P1 = O4 + link_m * [cos(theta_m), sin(theta_m)]
        
    ! X & Y Components:
        3. x_P1 = x_O4 + link_m * cos(theta_m)
        4. y_P1 = y_O4 + link_m * sin(theta_m)
    
    Args:
        O4 (np.ndarray): Fixed crank origin.
        link_m (float): Length of input crank Link M.
        theta_m (float): The angle of the crank in radians.
    
    Returns:
        P1 (np.ndarray): Position of Point P1 [x_P1, y_P1].
    """
    P1 = O4 + link_m * np.array([np.cos(theta_m), np.sin(theta_m)])
    
    return P1   


def solve_velocity_1(link_m : float, theta_m : float, omega_m : float) -> np.ndarray:
    """
    Solves the velocity of Point P1.
    
    ! Position Equation:
        P1 = O4 + link_m * [cos(theta_m), sin(theta_m)]
        
    ! Velocity Equation:
        v_P1 = dP1/dt = link_m * [-sin(theta_m) * dtheta_m/dt, cos(theta_m) * dtheta_m/dt]
             = link_m * omega_m * [-sin(theta_m), cos(theta_m)]
             
    ! X & Y Components:
        v_x_P1 = -link_m * omega_m * sin(theta_m)
        v_y_P1 = link_m * omega_m * cos(theta_m)
            
    Args:
        link_m (float): Length of input crank Link M.
        theta_m (float): The angle of the crank in radians.
        omega_m (float): The angular velocity of the crank in radians per second.
    
    Returns:
        v_P1 (np.ndarray): Velocity of Point P1 [v_x_P1, v_y_P1].
    """
    # Calculate velocity of P1 using the velocity equation
    v_P1 = link_m * omega_m * np.array([-np.sin(theta_m), np.cos(theta_m)])
    
    
    return v_P1


def solve_acceleration_1(link_m : float, theta_m : float, omega_m : float, alpha_m : float) -> np.ndarray:
    """
    Solves the acceleration of Point P1.
    
    ! Position Equation:
        P1 = O4 + link_m * [cos(theta_m), sin(theta_m)]
        
    ! Velocity Equation:
        v_P1 = link_m * omega_m * [-sin(theta_m), cos(theta_m)]
        
        
    ! Acceleration Equation:
        a_P1 = alpha_m x r_m - omega_m^2 * r_m
        
    ! X & Y Components:
        a_x_P1 = -link_m * alpha_m * sin(theta_m) - link_m * omega_m**2 * cos(theta_m)
        a_y_P1 = link_m * alpha_m * cos(theta_m) - link_m * omega_m**2 * sin(theta_m)
    
    Args:
        link_m (float): Length of input crank Link M.
        theta_m (float): The angle of the crank in radians.
        omega_m (float): The angular velocity of the crank in radians per second.
        alpha_m (float): The angular acceleration of the crank in radians per second squared.
    
    Returns:
        a_P1 (np.ndarray): Acceleration of Point P1 [a_x_P1, a_y_P1].
    """
    # Calculate acceleration of P1 using the acceleration equation
    a_P1 = alpha_m * link_m * np.array([-np.sin(theta_m), np.cos(theta_m)]) - omega_m**2 * link_m * np.array([np.cos(theta_m), np.sin(theta_m)])
    
    
    return a_P1



def solve_point_2(O2 : np.ndarray, P1 : np.ndarray, link_b : float, link_j : float) -> np.ndarray:
    """
    Solves the position of Point P2.
    
    ! Known:
        1. O2 = Fixed ground pivot
        2. P1 = Crank pin
    
    ! Link Constraints:
        3. Distance from O2 to P2 = Link B
        4. Distance from P1 to P2 = Link J
        
    ! Circle Equations:
        5. (x_P2 - x_O2)^2 + (y_P2 - y_O2)^2 = link_b^2
        6. (x_P2 - x_P1)^2 + (y_P2 - y_P1)^2 = link_j^2
    
    ? Since P2 is the upper joint in the mechanism, the intersection with larger y-value is the correct solution.
    
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P1 (np.ndarray): Crank pin position.
        link_b (float): Length of Link B.
        link_j (float): Length of Link J.
    
    Returns:
        P2 (np.ndarray): Position of Point P2 [x_P2, y_P2].
    """
    # Use circle intersection to solve for P2
    option_P2_1, option_P2_2 = circle_intersection(O2, link_b, P1, link_j)
    
    # Choose the correct intersection point based on the mechanism configuration
    if option_P2_1[1] > option_P2_2[1]:  
        P2 = option_P2_1
    else:
        P2 = option_P2_2
    
    
    return P2


def solve_velocity_2(O2 : np.ndarray, P1 : np.ndarray, P2 : np.ndarray, v_P1 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Solve for the velocity of Point P2.
    
    ! Loop:
        N + M = B + J.
        
    ! Velocity Relationships:
        1. V_P2 = omega_B x r_B
        2. V_P2 = V_P1 + omega_J x r_J
        
        where :
        r_B = P2 - O2
        r_J = P2 - P1
        
    ! Planar Cross Product:
        omega x r = omega * [-r_y, r_x]
    
    ! Component Form:
        1. omega_B * rB_x = Vx_P1 - omega_J * rJ_x
        2. -omega_B * rB_y = Vy_P1 + omega_J * rJ_y

        
        Rearranging gives:
        1. omega_B * rB_x + omega_J * rJ_x = Vx_P1
        2. -omega_B * rB_y - omega_J * rJ_y = Vy_P1


    ! Matrix Form:
        | -r_B_y   r_J_y | | omega_B | = | Vx_P1 |
        | r_B_x   -r_J_x | | omega_J | = | Vy_P1 |
    
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P1 (np.ndarray): Crank pin position.
        P2 (np.ndarray): Upper joint position.
        v_P1 (np.ndarray): Velocity of Point P1 [v_x_P1, v_y_P1].
    
    Returns:
        omega_B (float): Angular velocity of Link B.
        omega_J (float): Angular velocity of Link J.
        v_P2 (np.ndarray): Velocity of Point P2 [v_x_P2, v_y_P2].
    """
    # Position vectors from O2 and P1 to P2
    r_B = P2 - O2
    r_J = P2 - P1
    
    # Coefficient matrix for omega_B and omega_J
    coefficient_matrix = np.array([[-r_B[1], r_J[1]], 
                                   [r_B[0], -r_J[0]]])
    
    # Right-hand side vector for v_P1 components
    rhs_vector = np.array([v_P1[0], v_P1[1]])
    
    # Solve for omega_B and omega_J using np.linalg.solve
    omega_B, omega_J = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Velocity of Point P2
    v_P2 = omega_B * np.array([-r_B[1], r_B[0]]) 
    
    return v_P2, omega_B, omega_J
    

def solve_acceleration_2(O2 : np.ndarray, P1 : np.ndarray, P2 : np.ndarray, a_P1 : np.ndarray, omega_B : float, omega_J : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P2.
    
    ! Acceleration Relationships:
        1. a_P2 = alpha_B x r_B - omega_B^2 * r_B
        2. a_P2 = a_P1 + alpha_J x r_J - omega_J^2 * r_J
        
        where :
        r_B = P2 - O2
        r_J = P2 - P1
        
    ! Planar Cross Product:
        alpha x r = alpha * [-r_y, r_x]
        
    ! Component Form:
        1. alpha_B * rB_x = a_x_P1 - alpha_J * rJ_x + omega_B^2 * rB_x - omega_J^2 * rJ_x
        2. -alpha_B * rB_y = a_y_P1 + alpha_J * rJ_y + omega_B^2 * rB_y - omega_J^2 * rJ_y
        
        Rearranging gives:
        1. -alpha_B * rB_x + alpha_J * rJ_x = a_x_P1 + omega_B^2 * rB_x - omega_J^2 * rJ_x
        2. alpha_B * rB_y - alpha_J * rJ_y = a_y_P1 + omega_B^2 * rB_y - omega_J^2 * rJ_y
        
    ! Matrix Form:
        | -rB_x   rJ_x | | alpha_B | = | a_x_P1 + omega_B^2 * rB_x - omega_J^2 * rJ_x |
        | rB_y   -rJ_y | | alpha_J | = | a_y_P1 + omega_B^2 * rB_y - omega_J^2 * rJ_y |
        
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P1 (np.ndarray): Crank pin position.
        P2 (np.ndarray): Upper joint position.
        a_P1 (np.ndarray): Acceleration of Point P1 [a_x_P1, a_y_P1].
        omega_B (float): Angular velocity of Link B.
        omega_J (float): Angular velocity of Link J.
        
    Returns:
        a_P2 (np.ndarray): Acceleration of Point P2 [a_x_P2, a_y_P2].
        alpha_B (float): Angular acceleration of Link B.
        alpha_J (float): Angular acceleration of Link J.
    """
    # Position Vectors
    r_B = P2 - O2
    r_J = P2 - P1
    
    # Build Coefficient Matrix
    coefficient_matrix = np.array([[-r_B[1], r_J[1]], 
                                   [r_B[0], -r_J[0]]])
    
    # Right-hand side vector
    rhs_vector = np.array([a_P1[0] + omega_B**2 * r_B[0] - omega_J**2 * r_J[0], 
                           a_P1[1] + omega_B**2 * r_B[1] - omega_J**2 * r_J[1]])
    
    # Solve for alpha_B and alpha_J
    alpha_B, alpha_J = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Acceleration of Point P2
    a_P2 = alpha_B * np.array([-r_B[1], r_B[0]]) - omega_B**2 * r_B
    
    
    return a_P2, alpha_B, alpha_J
    
    
def solve_point_4(O2 : np.ndarray, P2 : np.ndarray, link_d : float, link_e : float) -> np.ndarray:
    """
    Solves the position of Point P4.
    
    ! Known:
        1. O2 = Fixed ground pivot
        2. P2 = Upper joint position
        
    ! Link Constraints:
        3. Distance from O2 to P4 = Link D
        4. Distance from P2 to P4 = Link E
        
    ! Circle Equations:
        5. (x_P4 - x_O2)^2 + (y_P4 - y_O2)^2 = link_d^2
        6. (x_P4 - x_P2)^2 + (y_P4 - y_P2)^2 = link_e^2
        
    ? Since P4 is the  upper left joint in the mechanism, the intersection with smaller x-value is the correct solution.
    
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P2 (np.ndarray): Upper joint position.
        link_d (float): Length of Link D.
        link_e (float): Length of Link E.
    
    Returns:
        P4 (np.ndarray): Position of Point P4 [x_P4, y_P4].
    """
    # Use circle intersection to solve for P4
    option_P4_1, option_P4_2 = circle_intersection(O2, link_d, P2, link_e)
    
    # Choose the correct intersection point based on the mechanism configuration
    if option_P4_1[0] < option_P4_2[0]:
        P4 = option_P4_1
    else:
        P4 = option_P4_2
    
    
    return P4


def solve_velocity_4(O2 : np.ndarray, P2 : np.ndarray, P4 : np.ndarray, v_P2 : np.ndarray) -> np.ndarray:
    """
    Solves the velocity of Point P4.
    
    ! Velocity Relationships:
        1. V_P4 = omega_D x r_D
        2. V_P4 = V_P2 + omega_E x r_E
        
        where :
        r_D = P4 - O2
        r_E = P4 - P2
        
    ! Planar Cross Product:
        omega x r = omega * [-r_y, r_x]
        
    ! Component Form:
        1. omega_D * rD_x = Vx_P2 - omega_E * rE_x
        2. -omega_D * rD_y = Vy_P2 + omega_E * rE_y

        
        Rearranging gives:
        1. omega_D * rD_x + omega_E * rE_x = Vx_P2
        2. -omega_D * rD_y - omega_E * rE_y = Vy_P2
        
    ! Matrix Form:
        | -rD_y   rE_y | | omega_D | = | Vx_P2 |
        | rD_x   -rE_x | | omega_E | = | Vy_P2 |
    
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P2 (np.ndarray): Upper joint position.
        P4 (np.ndarray): Upper left joint position.
        v_P2 (np.ndarray): Velocity of Point P2 [v_x_P2, v_y_P2].
    
    Returns:
        v_P4 (np.ndarray): Velocity of Point P4 [v_x_P4, v_y_P4].
        omega_D (float): Angular velocity of Link D.
        omega_E (float): Angular velocity of Link E.
    """
    # Position vectors from O2 and P2 to P4
    r_D = P4 - O2
    r_E = P4 - P2
    
    # Coefficient matrix for omega_D and omega_E
    coefficient_matrix = np.array([[-r_D[1], r_E[1]], 
                                   [r_D[0], -r_E[0]]])
    
    # Right-hand side vector for v_P2 components
    rhs_vector = np.array([v_P2[0], v_P2[1]])
    
    # Solve for omega_D and omega_E using np.linalg.solve
    omega_D, omega_E = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Velocity of Point P4
    v_P4 = omega_D * np.array([-r_D[1], r_D[0]])
    
    
    return v_P4, omega_D, omega_E
    
    
def solve_acceleration_4(O2 : np.ndarray, P2 : np.ndarray, P4 : np.ndarray, a_P2 : np.ndarray, omega_D : float, omega_E : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P4.
    
    ! Acceleration Relationships:
        1. a_P4 = alpha_D x r_D - omega_D^2 * r_D
        2. a_P4 = a_P2 + alpha_E x r_E - omega_E^2 * r_E
        
        where :
        r_D = P4 - O2
        r_E = P4 - P2
        
    ! Planar Cross Product:
        alpha x r = alpha * [-r_y, r_x]
        
    ! Component Form:
        1. alpha_D * rD_x = a_x_P2 - alpha_E * rE_x + omega_D^2 * rD_x - omega_E^2 * rE_x
        2. -alpha_D * rD_y = a_y_P2 + alpha_E * rE_y + omega_D^2 * rD_y - omega_E^2 * rE_y
        
        Rearranging gives:
        1. -alpha_D * rD_x + alpha_E * rE_x = a_x_P2 + omega_D^2 * rD_x - omega_E^2 * rE_x
        2. alpha_D * rD_y - alpha_E * rE_y = a_y_P2 + omega_D^2 * rD_y - omega_E^2 * rE_y
        
    ! Matrix Form:
        | -rD_x   rE_x | | alpha_D | = | a_x_P2 + omega_D^2 * rD_x - omega_E^2 * rE_x |
        | rD_y   -rE_y | | alpha_E | = | a_y_P2 + omega_D^2 * rD_y - omega_E^2 * rE_y |
        
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P2 (np.ndarray): Upper joint position.
        P4 (np.ndarray): Upper left joint position.
        a_P2 (np.ndarray): Acceleration of Point P2 [a_x_P2, a_y_P2].
        omega_D (float): Angular velocity of Link D.
        omega_E (float): Angular velocity of Link E.
        
    Returns:
        a_P4 (np.ndarray): Acceleration of Point P4 [a_x_P4, a_y_P4].
        alpha_D (float): Angular acceleration of Link D.
        alpha_E (float): Angular acceleration of Link E.   
    """
    # Position Vectors
    r_D = P4 - O2
    r_E = P4 - P2
    
    # Build Coefficient Matrix
    coefficient_matrix = np.array([[-r_D[1], r_E[1]], 
                                   [r_D[0], -r_E[0]]])
    
    # Right-hand side vector
    rhs_vector = np.array([a_P2[0] + omega_D**2 * r_D[0] - omega_E**2 * r_E[0], 
                           a_P2[1] + omega_D**2 * r_D[1] - omega_E**2 * r_E[1]])
    
    # Solve for alpha_D and alpha_E
    alpha_D, alpha_E = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Acceleration of Point P4
    a_P4 = alpha_D * np.array([-r_D[1], r_D[0]]) - omega_D**2 * r_D
    
    
    return a_P4, alpha_D, alpha_E
    
    
def solve_point_5(O2 : np.ndarray, P1 : np.ndarray, link_c : float, link_k : float) -> np.ndarray:
    """
    Solves the position of Point P5.
    
    ! Known:
        1. O2 = Fixed ground pivot
        2. P1 = Crank pin
    
    ! Link Constraints:
        3. Distance from O2 to P5 = Link C
        4. Distance from P1 to P5 = Link K
        
    ! Circle Equations:
        5. (x_P5 - x_O2)^2 + (y_P5 - y_O2)^2 = link_c^2
        6. (x_P5 - x_P1)^2 + (y_P5 - y_P1)^2 = link_k^2
    
    ? Since P5 is the lower joint in the mechanism, the intersection with smaller y-value is the correct solution.
    
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P1 (np.ndarray): Crank pin position.
        link_c (float): Length of Link C.
        link_k (float): Length of Link K.
    
    Returns:
        P5 (np.ndarray): Position of Point P5 [x_P5, y_P5].
    """
    # Use circle intersection to solve for P5
    option_P5_1, option_P5_2 = circle_intersection(O2, link_c, P1, link_k)
    
    # Choose the correct intersection point based on the mechanism configuration
    if option_P5_1[1] < option_P5_2[1]:
        P5 = option_P5_1
    else:
        P5 = option_P5_2
        
        
    return P5


def solve_velocity_5(O2 : np.ndarray, P1 : np.ndarray, P5 : np.ndarray, v_P1 : np.ndarray) -> np.ndarray:
    """
    Solves the velocity of Point P5.
    
    ! Velocity Relationships:
        1. V_P5 = omega_C x r_C
        2. V_P5 = V_P1 + omega_K x r_K
        
        where :
        r_C = P5 - O2
        r_K = P5 - P1
        
    ! Planar Cross Product:
        omega x r = omega * [-r_y, r_x]
        
    ! Component Form:
        1. omega_C * rC_x = Vx_P1 - omega_K * rK_x
        2. -omega_C * rC_y = Vy_P1 + omega_K * rK_y

        
        Rearranging gives:
        1. omega_C * rC_x + omega_K * rK_x = Vx_P1
        2. -omega_C * rC_y - omega_K * rK_y = Vy_P1
        
    ! Matrix Form:
        | -rC_y   rK_y | | omega_C | = | Vx_P1 |
        | rC_x   -rK_x | | omega_K | = | Vy_P1 |
    
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P1 (np.ndarray): Crank pin position.
        P5 (np.ndarray): Position of Point P5.
        v_P1 (np.ndarray): Velocity of Point P1.
    
    Returns:
        v_P5 (np.ndarray): Velocity of Point P5.
        omega_C (float): Angular velocity of Link C.
        omega_K (float): Angular velocity of Link K.
    """
    # Position vectors from O2 and P1 to P5
    r_C = P5 - O2
    r_K = P5 - P1
    
    # Coefficient matrix for omega_C and omega_K
    coefficient_matrix = np.array([[-r_C[1], r_K[1]], 
                                   [r_C[0], -r_K[0]]])
    
    # Right-hand side vector
    rhs = np.array([v_P1[0], v_P1[1]])
    
    # Solve for angular velocities
    omega_C, omega_K = np.linalg.solve(coefficient_matrix, rhs)
    
    # Velocity of P5
    v_P5 = omega_C * np.array([-r_C[1], r_C[0]])
    
    
    return v_P5, omega_C, omega_K


def solve_acceleration_5(O2 : np.ndarray, P1 : np.ndarray, P5 : np.ndarray, a_P1 : np.ndarray, omega_C : float, omega_K : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P5.
    
    ! Acceleration Relationships:
        1. a_P5 = alpha_C x r_C - omega_C^2 * r_C
        2. a_P5 = a_P1 + alpha_K x r_K - omega_K^2 * r_K
        
        where :
        r_C = P5 - O2
        r_K = P5 - P1
        
    ! Planar Cross Product:
        alpha x r = alpha * [-r_y, r_x]
        
    ! Component Form:
        1. alpha_C * rC_x = a_x_P1 - alpha_K * rK_x + omega_C^2 * rC_x - omega_K^2 * rK_x
        2. -alpha_C * rC_y = a_y_P1 + alpha_K * rK_y + omega_C^2 * rC_y - omega_K^2 * rK_y
        
        Rearranging gives:
        1. -alpha_C * rC_x + alpha_K * rK_x = a_x_P1 + omega_C^2 * rC_x - omega_K^2 * rK_x
        2. alpha_C * rC_y - alpha_K * rK_y = a_y_P1 + omega_C^2 * rC_y - omega_K^2 * rK_y
        
    ! Matrix Form:
        | -rC_x   rK_x | | alpha_C | = | a_x_P1 + omega_C^2 * rC_x - omega_K^2 * rK_x |
        | rC_y   -rK_y | | alpha_K | = | a_y_P1 + omega_C^2 * rC_y - omega_K^2 * rK_y |
        
    Args:
        O2 (np.ndarray): Fixed ground pivot.
        P1 (np.ndarray): Crank pin position.
        P5 (np.ndarray): Position of Point P5.
        a_P1 (np.ndarray): Acceleration of Point P1.
        omega_C (float): Angular velocity of Link C.
        omega_K (float): Angular velocity of Link K.
    
    Returns:
        a_P5 (np.ndarray): Acceleration of Point P5.
        alpha_C (float): Angular acceleration of Link C.
        alpha_K (float): Angular acceleration of Link K.
    """
    # Position Vectors
    r_C = P5 - O2
    r_K = P5 - P1
    
    # Build Coefficient Matrix
    coefficient_matrix = np.array([[-r_C[1], r_K[1]], 
                                   [r_C[0], -r_K[0]]])
    
    # Right-hand side vector
    rhs_vector = np.array([a_P1[0] + omega_C**2 * r_C[0] - omega_K**2 * r_K[0], 
                           a_P1[1] + omega_C**2 * r_C[1] - omega_K**2 * r_K[1]])
    
    # Solve for alpha_C and alpha_K
    alpha_C, alpha_K = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Acceleration of Point P5
    a_P5 = alpha_C * np.array([-r_C[1], r_C[0]]) - omega_C**2 * r_C
    
    
    return a_P5, alpha_C, alpha_K


def solve_point_6(P4 : np.ndarray, P5 : np.ndarray, link_f : float, link_g : float) -> np.ndarray:
    """
    Solves the position of Point P6.
    
    ! Known:
        1. P4 = Upper left joint position
        2. P5 = Lower joint position
        
    ! Link Constraints:
        1. Distance from P4 to P6 = Link F
        2. Distance from P5 to P6 = Link G
    
    Args:
        P4 (np.ndarray): Upper left joint position.
        P5 (np.ndarray): Lower joint position.
        link_f (float): Length of Link F.
        link_g (float): Length of Link G.
    
    Returns:
        P6 (np.ndarray): Position of Point P6 [x_P6, y_P6].
    """
    # Use circle intersection to solve for P6
    option_P6_1, option_P6_2 = circle_intersection(P4, link_f, P5, link_g)
    
    # Choose the correct intersection point based on the mechanism configuration
    if option_P6_1[0] < option_P6_2[0]:
        P6 = option_P6_1
    else:
        P6 = option_P6_2
    
    
    return P6


def solve_velocity_6(P4 : np.ndarray, P5 : np.ndarray, P6 : np.ndarray, v_P4 : np.ndarray, v_P5 : np.ndarray) -> np.ndarray:
    """
    Solves the velocity of Point P6.
    
    ! Velocity Relationships:
        1. V_P6 = V_P4 + omega_F x r_F
        2. V_P6 = V_P5 + omega_G x r_G
        
        where :
        r_F = P6 - P4
        r_G = P6 - P5
        
    ! Planar Cross Product:
        omega x r = omega * [-r_y, r_x]
        
    ! Component Form:
        1. omega_F * rF_x = Vx_P4 - omega_G * rG_x
        2. -omega_F * rF_y = Vy_P4 + omega_G * rG_y

        
        Rearranging gives:
        1. omega_F * rF_x + omega_G * rG_x = Vx_P5 - Vx_P4
        2. -omega_F * rF_y - omega_G * rG_y = Vy_P5 - Vy_P4
        
    ! Matrix Form:
        | -rF_y   rG_y | | omega_F | = | V_x_P5 - Vx_P4 |
        | rF_x   -rG_x | | omega_G | = | Vy_P5 - Vy_P4 |
    
    Args:
        P4 (np.ndarray): Upper left joint position.
        P5 (np.ndarray): Lower joint position.
        P6 (np.ndarray): Position of Point P6.
        v_P4 (np.ndarray): Velocity of Point P4.
        v_P5 (np.ndarray): Velocity of Point P5.
    
    Returns:
        v_P6 (np.ndarray): Velocity of Point P6.
        omega_F (float): Angular velocity of Link F.
        omega_G (float): Angular velocity of Link G.
    """
    # Position vectors from P4 and P5 to P6
    r_F = P6 - P4
    r_G = P6 - P5
    
    # Coefficient matrix for omega_F and omega_G
    coefficient_matrix = np.array([[-r_F[1], r_G[1]], 
                                   [r_F[0], -r_G[0]]])
    
    # Right-hand side vector
    rhs = np.array([v_P5[0] - v_P4[0], 
                    v_P5[1] - v_P4[1]])
    
    # Solve for angular velocities
    omega_F, omega_G = np.linalg.solve(coefficient_matrix, rhs)
    
    # Velocity of P6
    v_P6 = omega_F * np.array([-r_F[1], r_F[0]])
    
    return v_P6, omega_F, omega_G


def solve_acceleration_6(P4 : np.ndarray, P5 : np.ndarray, P6 : np.ndarray, a_P4 : np.ndarray, a_P5 : np.ndarray, omega_F : float, omega_G : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P6.
    
    ! Acceleration Relationships:
        1. a_P6 = a_P4 + alpha_F x r_F - omega_F^2 * r_F
        2. a_P6 = a_P5 + alpha_G x r_G - omega_G^2 * r_G
        
        where :
        r_F = P6 - P4
        r_G = P6 - P5
        
    ! Planar Cross Product:
        alpha x r = alpha * [-r_y, r_x]
        
    ! Component Form:
        1. alpha_F * rF_x = a_x_P5 - a_x_P4 - alpha_G * rG_x + omega_F^2 * rF_x - omega_G^2 * rG_x
        2. -alpha_F * rF_y = a_y_P5 - a_y_P4 + alpha_G * rG_y + omega_F^2 * rF_y - omega_G^2 * rG_y
        
        Rearranging gives:
        1. -alpha_F * rF_x + alpha_G * rG_x = a_x_P5 - a_x_P4 + omega_F^2 * rF_x - omega_G^2 * rG_x
        2. alpha_F * rF_y - alpha_G * rG_y = a_y_P5 - a_y_P4 + omega_F^2 * rF_y - omega_G^2 * rG_y
        
    ! Matrix Form:
        | -rF_x   rG_x | | alpha_F | = | a_x_P5 - a_x_P4 + omega_F^2 * rF_x - omega_G^2 * rG_x |
        | rF_y   -rG_y | | alpha_G | = | a_y_P5 - a_y_P4 + omega_F^2 * rF_y - omega_G^2 * rG_y |
        
    Args:
        P4 (np.ndarray): Upper left joint position.
        P5 (np.ndarray): Lower joint position.
        P6 (np.ndarray): Position of Point P6.
        a_P4 (np.ndarray): Acceleration of Point P4.
        a_P5 (np.ndarray): Acceleration of Point P5.
        omega_F (float): Angular velocity of Link F.
        omega_G (float): Angular velocity of Link G.
        
    Returns:
        a_P6 (np.ndarray): Acceleration of Point P6.
        alpha_F (float): Angular acceleration of Link F.
        alpha_G (float): Angular acceleration of Link G.
    """
    # Position Vectors
    r_F = P6 - P4
    r_G = P6 - P5
    
    # Build Coefficient Matrix
    coefficient_matrix = np.array([[-r_F[1], r_G[1]], 
                                   [r_F[0], -r_G[0]]])
    
    # Right-hand side vector
    rhs_vector = np.array([a_P5[0] - a_P4[0] + omega_F**2 * r_F[0] - omega_G**2 * r_G[0], 
                           a_P5[1] - a_P4[1] + omega_F**2 * r_F[1] - omega_G**2 * r_G[1]])
    
    # Solve for alpha_F and alpha_G
    alpha_F, alpha_G = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Acceleration of Point P6
    a_P6 = a_P4 + alpha_F * np.array([-r_F[1], r_F[0]]) - omega_F**2 * r_F
    
    
    return a_P6, alpha_F, alpha_G

def solve_point_7(P6: np.ndarray, P5 : np.ndarray, link_h : float, link_i : float) -> np.ndarray:
    """
    Solves the position of Point P7.
    
    ! Known:
        1. P6 = Upper right joint position
        2. P5 = Lower joint position
        
    ! Link Constraints:
        1. Distance from P6 to P7 = Link H
        2. Distance from P5 to P7 = Link I
        
    ! Circle Equations:
        1. (x_P7 - x_P6)^2 + (y_P7 - y_P6)^2 = link_h^2
        2. (x_P7 - x_P5)^2 + (y_P7 - y_P5)^2 = link_i^2
        
    ? Since P7 is the foot point of the mechanism at the bottom, the intersection with smaller y-value is the correct solution.
    
    Args:
        P6 (np.ndarray): Upper right joint position.
        P5 (np.ndarray): Lower joint position.
        link_h (float): Length of Link H.
        link_i (float): Length of Link I.
    
    Returns:
        P7 (np.ndarray): Position of Point P7 [x_P7, y_P7].
    """
    # Use circle intersection to solve for P7
    option_P7_1, option_P7_2 = circle_intersection(P6, link_h, P5, link_i)
    
    # Choose the correct intersection point based on the mechanism configuration
    if option_P7_1[1] < option_P7_2[1]:
        P7 = option_P7_1
    else:
        P7 = option_P7_2
      
        
    return P7


def solve_velocity_7(P5 : np.ndarray, P6 : np.ndarray, P7 : np.ndarray, v_P5 : np.ndarray, v_P6 : np.ndarray) -> np.ndarray:
    """
    Solves the velocity of Point P7.
    
    ! Velocity Relationships:
        1. V_P7 = V_P6 + omega_H x r_H
        2. V_P7 = V_P5 + omega_I x r_I
        
        where :
        r_H = P7 - P6
        r_I = P7 - P5
        
    ! Planar Cross Product:
        omega x r = omega * [-r_y, r_x]
        
    ! Component Form:
        1. omega_H * rH_x = Vx_P6 - omega_I * rI_x
        2. -omega_H * rH_y = Vy_P6 + omega_I * rI_y

        
        Rearranging gives:
        1. omega_H * rH_x + omega_I * rI_x = Vx_P5 - Vx_P6
        2. -omega_H * rH_y - omega_I * rI_y = Vy_P5 - Vy_P6
        
    ! Matrix Form:
        | -rH_y   rI_y | | omega_H | = | V_x_P5 - Vx_P6 |
        | rH_x   -rI_x | | omega_I | = | Vy_P5 - Vy_P6 |
    
    Args:
        P5 (np.ndarray): Lower joint position.
        P6 (np.ndarray): Upper right joint position.
        P7 (np.ndarray): Position of Point P7.
        v_P5 (np.ndarray): Velocity of Point P5.
        v_P6 (np.ndarray): Velocity of Point P6.
    
    Returns:
        v_P7 (np.ndarray): Velocity of Point P7.
        omega_H (float): Angular velocity of Link H.
        omega_I (float): Angular velocity of Link I.
    """
    # Position vectors from P6 and P5 to P7
    r_H = P7 - P6
    r_I = P7 - P5
    
    # Coefficient matrix for omega_H and omega_I
    coefficient_matrix = np.array([[-r_H[1], r_I[1]], 
                                   [r_H[0], -r_I[0]]])
    
    # Right-hand side vector
    rhs = np.array([v_P5[0] - v_P6[0], 
                    v_P5[1] - v_P6[1]])
    
    # Solve for angular velocities
    omega_H, omega_I = np.linalg.solve(coefficient_matrix, rhs)
    
    # Velocity of P7
    v_P7 = omega_H * np.array([-r_H[1], r_H[0]])
    
    return v_P7, omega_H, omega_I


def solve_acceleration_7(P5 : np.ndarray, P6 : np.ndarray, P7 : np.ndarray, a_P5 : np.ndarray, a_P6 : np.ndarray, omega_H : float, omega_I : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P7.
    
    ! Acceleration Relationships:
        1. a_P7 = a_P6 + alpha_H x r_H - omega_H^2 * r_H
        2. a_P7 = a_P5 + alpha_I x r_I - omega_I^2 * r_I
        
        where :
        r_H = P7 - P6
        r_I = P7 - P5
        
    ! Planar Cross Product:
        alpha x r = alpha * [-r_y, r_x]
        
    ! Component Form:
        1. alpha_H * rH_x = a_x_P5 - a_x_P6 - alpha_I * rI_x + omega_H^2 * rH_x - omega_I^2 * rI_x
        2. -alpha_H * rH_y = a_y_P5 - a_y_P6 + alpha_I * rI_y + omega_H^2 * rH_y - omega_I^2 * rI_y
        
        Rearranging gives:
        1. -alpha_H * rH_x + alpha_I * rI_x = a_x_P5 - a_x_P6 + omega_H^2 * rH_x - omega_I^2 * rI_x
        2. alpha_H * rH_y - alpha_I * rI_y = a_y_P5 - a_y_P6 + omega_H^2 * rH_y - omega_I^2 * rI_y
        
    ! Matrix Form:
        | -rH_x   rI_x | | alpha_H | = | a_x_P5 - a_x_P6 + omega_H^2 * rH_x - omega_I^2 * rI_x |
        | rH_y   -rI_y | | alpha_I | = | a_y_P5 - a_y_P6 + omega_H^2 * rH_y - omega_I^2 * rI_y |
        
    Args:
        P5 (np.ndarray): Lower joint position.
        P6 (np.ndarray): Upper right joint position.
        P7 (np.ndarray): Position of Point P7.
        a_P5 (np.ndarray): Acceleration of Point P5.
        a_P6 (np.ndarray): Acceleration of Point P6.
        omega_H (float): Angular velocity of Link H.
        omega_I (float): Angular velocity of Link I.
        
    Returns:
        a_P7 (np.ndarray): Acceleration of Point P7.
        alpha_H (float): Angular acceleration of Link H.
        alpha_I (float): Angular acceleration of Link I.
    """
    # Position Vectors
    r_H = P7 - P6
    r_I = P7 - P5
    
    # Build Coefficient Matrix
    coefficient_matrix = np.array([[-r_H[1], r_I[1]], 
                                   [r_H[0], -r_I[0]]])
    
    # Right-hand side vector
    rhs_vector = np.array([a_P5[0] - a_P6[0] + omega_H**2 * r_H[0] - omega_I**2 * r_I[0], 
                           a_P5[1] - a_P6[1] + omega_H**2 * r_H[1] - omega_I**2 * r_I[1]])
    
    # Solve for alpha_H and alpha_I
    alpha_H, alpha_I = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Acceleration of Point P7
    a_P7 = a_P6 + alpha_H * np.array([-r_H[1], r_H[0]]) - omega_H**2 * r_H
    
    
    return a_P7, alpha_H, alpha_I


def solve_velocity_foot(P5 : np.ndarray, P7 : np.ndarray, v_P5 : np.ndarray, omega_I : np.ndarray) -> np.ndarray:
    """
    Solves the vertical velocity of the foot point P7.
    
    ! Foot Loop:
        r_c + r_I + r_P
    
    ! Velocity Relationships:
        1. V_P7 = V_P5 + omega_I x r_I
        
        where :
        r_I = P7 - P5
        
    ! Planar Cross Product:
        omega x r = omega * [-r_y, r_x]
        
    ! Component Form:
        1. Vx_P7 = Vx_P5 - omega_I * rI_x
        2. Vy_P7 = Vy_P5 + omega_I * rI_y
        
    Args:
        P5 (np.ndarray): Lower joint position.
        P7 (np.ndarray): Position of Point P7.
        v_P5 (np.ndarray): Velocity of Point P5.
        omega_I (float): Angular velocity of Link I.
    
    Returns:
        v_foot (np.ndarray): Velocity of the foot point P7.
    """
    # Position vector from P5 to P7
    r_I = P7 - P5
    
    # Velocity of P7 from link I
    v_foot = v_P5 + omega_I * np.array([-r_I[1], r_I[0]])
    
    return v_foot


def solve_acceleration_foot(P5 : np.ndarray, P7 : np.ndarray, a_P5 : np.ndarray, omega_I : np.ndarray, alpha_I : np.ndarray) -> np.ndarray:
    """
    Solves the vertical acceleration of the foot point P7.
    
    ! Foot Loop:
        r_c + r_I + r_P
    
    ! Acceleration Relationships:
        1. a_P7 = a_P5 + alpha_I x r_I - omega_I^2 * r_I
        
        where :
        r_I = P7 - P5
        
    ! Planar Cross Product:
        alpha x r = alpha * [-r_y, r_x]
        
    ! Component Form:
        1. a_x_P7 = a_x_P5 - alpha_I * rI_x + omega_I^2 * rI_x
        2. a_y_P7 = a_y_P5 + alpha_I * rI_y - omega_I^2 * rI_y
        
    Args:
        P5 (np.ndarray): Lower joint position.
        P7 (np.ndarray): Position of Point P7.
        a_P5 (np.ndarray): Acceleration of Point P5.
        omega_I (float): Angular velocity of Link I.
        alpha_I (float): Angular acceleration of Link I.
    
    Returns:
        a_foot (np.ndarray): Acceleration of the foot point P7.
    """
    # Position vector from P5 to P7
    r_I = P7 - P5
    
    # Acceleration of P7 from link I
    a_foot = a_P5 + alpha_I * np.array([-r_I[1], r_I[0]]) - omega_I**2 * r_I
    
    return a_foot


