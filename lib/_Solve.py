# -*- coding: utf-8 -*-
"""
TITLE = Kinematic Analysis Solvers
DATE  = 2026.05.15
_____________________________________________________________________
DESCRIPTION:
1. Solver to compute the position, velocity, and acceleration of the points for the Theo Jansen mechanism.
2. Solver to find the intersection of two circles, which is a common geometric problem in kinematic analysis.
3. Functions to solve for the position, velocity, and acceleration of points connected by two links.
4. Velocity and acceleration solvers for points in two-link loops.
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
    rhs_vector = velocity_base_2 - velocity_base_1
    
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
    rhs_vector = (acceleration_base_2 - acceleration_base_1) + (omega_1**2 * r_1 - omega_2**2 * r_2)
    
    # Solve for alpha_1 and alpha_2
    alpha_1, alpha_2 = np.linalg.solve(coefficient_matrix, rhs_vector)
    
    # Calculate acceleration of the target point using one of the acceleration equations
    acceleration_target = acceleration_base_1 + alpha_1 * perpendicular(r_1) - omega_1**2 * r_1
    
    
    return acceleration_target, alpha_1, alpha_2


def solve_position_P1(O4 : np.ndarray, link_m : float, theta_m : float) -> np.ndarray:
    """
    Solve the position of Point P1.
    """
    return O4 + link_m * np.array([np.cos(theta_m), np.sin(theta_m)])
    
def solve_velocity_P1(link_m : float, theta_m : float, omega_m : float) -> np.ndarray:
    """
    Solve the velocity of Point P1.
    """
    return link_m * omega_m * np.array([-np.sin(theta_m), np.cos(theta_m)])

def solve_acceleration_P1(link_m : float, theta_m : float, omega_m : float, alpha_m : float) -> np.ndarray:
    """
    Solve the acceleration of Point P1.
    """
    return alpha_m * link_m * np.array([-np.sin(theta_m), np.cos(theta_m)]) - omega_m**2 * link_m * np.array([np.cos(theta_m), np.sin(theta_m)])


def solve_position_P2(O2 : np.ndarray, P1 : np.ndarray, link_b : float, link_j : float) -> np.ndarray:
    """
    Solve the position of Point P2.
    """
    return solve_point_from_two_links(O2, P1, link_b, link_j, selection="max_y")

def solve_velocity_P2(O2 : np.ndarray, P1 : np.ndarray, P2 : np.ndarray, v_P1 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Solve the velocity of Point P2.
    """
    zero_velocity = np.zeros(2)
    
    
    return solve_velocity_two_link_loop(O2, P1, P2, zero_velocity, v_P1)

def solve_acceleration_P2(O2 : np.ndarray, P1 : np.ndarray, P2 : np.ndarray, a_P1 : np.ndarray, omega_B : float, omega_J : float) -> tuple[np.ndarray, float, float]:
    """
    Solve the acceleration of Point P2.
    """
    zero_acceleration = np.zeros(2)
    
    return solve_acceleration_two_link_loop(O2, P1, P2, zero_acceleration, a_P1, omega_B, omega_J)


def solve_position_P4(O2 : np.ndarray, P2 : np.ndarray, link_d : float, link_e : float) -> np.ndarray:
    """
    Solves the position of Point P4.
    """
    return solve_point_from_two_links(O2, P2, link_d, link_e, selection="min_x")

def solve_velocity_P4(O2 : np.ndarray, P2 : np.ndarray, P4 : np.ndarray, v_P2 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Solves the velocity of Point P4.
    """
    zero_velocity = np.zeros(2)
    
    return solve_velocity_two_link_loop(O2, P2, P4, zero_velocity, v_P2)

def solve_acceleration_P4(O2 : np.ndarray, P2 : np.ndarray, P4 : np.ndarray, a_P2 : np.ndarray, omega_D : float, omega_E : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P4.
    """
    zero_acceleration = np.zeros(2)
    
    return solve_acceleration_two_link_loop(O2, P2, P4, zero_acceleration, a_P2, omega_D, omega_E)


def solve_position_P5(O2 : np.ndarray, P1 : np.ndarray, link_c : float, link_k : float) -> np.ndarray:
    """
    Solves the position of Point P5.
    """
    return solve_point_from_two_links(O2, P1, link_c, link_k, selection="min_y")

def solve_velocity_P5(O2 : np.ndarray, P1 : np.ndarray, P5 : np.ndarray, v_P1 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Solves the velocity of Point P5.
    """
    zero_velocity = np.zeros(2)
    
    return solve_velocity_two_link_loop(O2, P1, P5, zero_velocity, v_P1)

def solve_acceleration_P5(O2 : np.ndarray, P1 : np.ndarray, P5 : np.ndarray, a_P1 : np.ndarray, omega_C : float, omega_K : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P5.
    """
    zero_acceleration = np.zeros(2)
    
    return solve_acceleration_two_link_loop(O2, P1, P5, zero_acceleration, a_P1, omega_C, omega_K)
  

def solve_position_P6(P4 : np.ndarray, P5 : np.ndarray, link_f : float, link_g : float) -> np.ndarray:
    """
    Solves the position of Point P6.
    """
    return solve_point_from_two_links(P4, P5, link_f, link_g, selection="min_x")

def solve_velocity_P6(P4 : np.ndarray, P5 : np.ndarray, P6 : np.ndarray, v_P4 : np.ndarray, v_P5 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Solves the velocity of Point P6.
    """
    return solve_velocity_two_link_loop(P4, P5, P6, v_P4, v_P5)

def solve_acceleration_P6(P4 : np.ndarray, P5 : np.ndarray, P6 : np.ndarray, a_P4 : np.ndarray, a_P5 : np.ndarray, omega_F : float, omega_G : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P6.
    """
    return solve_acceleration_two_link_loop(P4, P5, P6, a_P4, a_P5, omega_F, omega_G)


def solve_position_P7(P6: np.ndarray, P5 : np.ndarray, link_h : float, link_i : float) -> np.ndarray:
    """
    Solves the position of Point P7.
    """
    return solve_point_from_two_links(P6, P5, link_h, link_i, selection="min_y")

def solve_velocity_P7(P5 : np.ndarray, P6 : np.ndarray, P7 : np.ndarray, v_P5 : np.ndarray, v_P6 : np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Solves the velocity of Point P7.
    """
    return solve_velocity_two_link_loop(P6, P5, P7, v_P6, v_P5)

def solve_acceleration_P7(P5 : np.ndarray, P6 : np.ndarray, P7 : np.ndarray, a_P5 : np.ndarray, a_P6 : np.ndarray, omega_H : float, omega_I : float) -> tuple[np.ndarray, float, float]:
    """
    Solves the acceleration of Point P7.
    """
    return solve_acceleration_two_link_loop(P6, P5, P7, a_P6, a_P5, omega_H, omega_I)

def solve_velocity_foot(P5 : np.ndarray, P7 : np.ndarray, v_P5 : np.ndarray, omega_I : np.ndarray) -> np.ndarray:
    """
    Solves the velocity of the foot point P7.
    """
    r_I = P7 - P5
    
    return v_P5 + omega_I * perpendicular(r_I)

def solve_acceleration_foot(P5 : np.ndarray, P7 : np.ndarray, a_P5 : np.ndarray, omega_I : np.ndarray, alpha_I : np.ndarray) -> np.ndarray:
    """
    Solves the acceleration of the foot point P7.
    """
    r_I = P7 - P5
    
    return a_P5 + alpha_I * perpendicular(r_I) - omega_I**2 * r_I

