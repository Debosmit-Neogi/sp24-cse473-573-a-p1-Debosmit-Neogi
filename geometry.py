import torch
from typing import Tuple

'''
Please do Not change or add any imports. 
'''

# --------------------------------------------------- task1 ----------------------------------------------------------

def findRot_xyz2XYZ(alpha: float, beta: float, gamma: float) -> torch.Tensor:
    '''
    Args:
        alpha, beta, gamma: They are the rotation angles along z, x and y axis of the 3 steps respectly 
        give in the project documentation. Note that they are angles, not radians.
    Return:
        A 3x3 tensor represents the rotation matrix from xyz to XYZ.
    '''
    rot_xyz2XYZ = torch.eye(3, dtype=torch.float32)

    # Your implementation starts from here ( Do not change anything above this line)
    

    return rot_xyz2XYZ


def findRot_XYZ2xyz(alpha: float, beta: float, gamma: float) -> torch.Tensor:
    '''
    Args:
        alpha, beta, gamma: They are the rotation angles along z, x and y axis of the 3 steps respectly 
        give in the project documentation. Note that they are angles, not radians.
    Return:
        A 3x3 tensor represents the rotation matrix from XYZ to xyz.
    '''
    rot_XYZ2xyz = torch.eye(3, dtype=torch.float32)

     # Your implementation starts from here ( Do not change anything above this line)

    return rot_XYZ2xyz

"""
If your implementation requires implementing other functions.
Please implement all the functions you design under here.
But remember the above "findRot_xyz2XYZ()" and "findRot_XYZ2xyz()"
functions are the only 2 function that will be called in task1.py.
"""
# Your functions for task1 goes below if necessary:






#---------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- task2 ----------------------------------------------------------

# for the find_corner_img_coord function implementation:
# You are able to use opencv to detect corners in this function, resulting in numpy arrays,
# but you have to convert numpy arrays back to torch.Tensor form.
# (findChessboardCorners, cornerSubPix can be used to find the corners as the image coordinates)
# (drawChessboardCorners can be used to see if you find the true corners) you can see the true corners in the project pdf - figure 2
# Comment out the following two lines to import and use the functions you need:

#import numpy as np
#from cv2 import TERM_CRITERIA_EPS, TERM_CRITERIA_MAX_ITER,findChessboardCorners, cornerSubPix, drawChessboardCorners

def find_corner_img_coord(image: torch.Tensor) -> torch.Tensor:
    '''
    Args: 
        image: Input image of size 3xMxN.
        M is the height of the image.
        N is the width of the image.
        3 is the channel of the image.

    Return:
        A tensor of size 32x2 that represents the 32 checkerboard corners' pixel coordinates. 
        The pixel coordinate is defined such that the of top-left corner is (0, 0)
        and the bottom-right corner of the image is (N, M). 
    '''
    img_coord = torch.zeros(32, 2, dtype=torch.float32)
    # You are able to use opencv to detect corners in this function, resulting in numpy arrays,
    # but you have to convert numpy arrays back to torch.Tensor form.
    # Your implementation starts here:
        
    
    
    return img_coord


def find_corner_world_coord(img_coord: torch.Tensor) -> torch.Tensor:
    '''
    You can output the world coord manually or through some algorithms you design.
    Your output should be the same order with img_coord.

    Args: 
        img_coord: The image coordinate of the corners.
        Note that you do not required to use this as input, 
        as long as your output is in the same order with img_coord.

    Return:
        A torch.Tensor of size 32x3 that represents the 32
        (36 detected points minus 4 points on the z axis) checkerboard corners' pixel coordinates. 
        The world coordinate or each point should be in form of (x, y, z). 
        The axis of the world coordinate system are given in the image.
        The output results should be in milimeters.
    '''
    world_coord = torch.zeros(32, 3, dtype=torch.float32)

    # You can only use torch in this function
    # Your implementation start here:
    
    return world_coord


def find_intrinsic(img_coord: torch.Tensor, world_coord: torch.Tensor) -> Tuple[float, float, float, float]:
    '''
    Use the image coordinates and world coordinates of the 32 point to calculate the intrinsic parameters.

    Args: 
        img_coord: The image coordinate of the 32 corners. This is a 32x2 tensor.
        world_coord: The world coordinate of the 32 corners. This is a 32x3 tensor.

    Returns:
        fx, fy: Focal length. 
        (cx, cy): Principal point of the camera (in pixel coordinate).
        NOTE: DO not forget to convert the return types to float after your computation
    '''

    fx: float = 0
    fy: float = 0
    cx: float = 0
    cy: float = 0

    # You can only use torch in this function
    # Your implementation starts here:
    

    return fx, fy, cx, cy


def find_extrinsic(img_coord: torch.Tensor, world_coord: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
    '''
    Use the image coordinates, world coordinates of the 32 point and the intrinsic
    parameters to calculate the extrinsic parameters.

    Args: 
        img_coord: The image coordinate of the 32 corners. This is a 32x2 tensor.
        world_coord: The world coordinate of the 32 corners. This is a 32x3 tensor.
    Returns:
        R: The rotation matrix of the extrinsic parameters.
            It is a 3x3 tensor.
        T: The translation matrix of the extrinsic parameters.
            It is a 1-dimensional tensor with length of 3.
    '''
    R = torch.eye(3, dtype=torch.float32)
    T = torch.zeros(3, dtype=torch.float32)

    # You can only use torch in this function
    # Your implementation start here:

    return R, T


"""
If your implementation requires implementing other functions.
Please implement all the functions you design under here.
But remember the above 4 functions are the only ones that will be called in task2.py.
"""

# Your functions for task2 goes below is necessary:




#---------------------------------------------------------------------------------------------------------------------
