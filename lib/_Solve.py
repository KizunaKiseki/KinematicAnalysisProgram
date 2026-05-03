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


# * VARIABLES *
# ? ================================================================ ?


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