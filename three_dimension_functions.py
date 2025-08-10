# Functions Pertaining to 3D 

import math
import pygame

import settings

def project(point):
    t = - settings.FOCUS_POINT[2] / (point[2] - settings.FOCUS_POINT[2])

    x = settings.FOCUS_POINT[0] + t * (point[0] - settings.FOCUS_POINT[0])
    y = settings.FOCUS_POINT[1] + t * (point[1] - settings.FOCUS_POINT[1])

    projected_point = [x, y] 
    return projected_point

def rotate(point, rotation, center):
    # This function takes in a point in 3D space
    # as well as a rotation about Alpha, Beta, and Gamma (Roll, Pitch, and Yaw)
    # and returns a new point with the rotation applied
    x = point[0] - center[0]
    y = point[1] - center[1]
    z = point[2] - center[2]

    sinA = math.sin(rotation[0])
    cosA = math.cos(rotation[0])
    sinB = math.sin(rotation[1])
    cosB = math.cos(rotation[1])
    sinG = math.sin(rotation[2])
    cosG = math.cos(rotation[2])

    # 3D rotation matrix
    # [ cos(B)cos(G)  sin(A)sin(B)cos(G) - cos(A)sin(G)  cos(A)sin(B)cos(G) + sin(A)sin(G) ] [x]
    # [ cos(B)sin(G)  sin(A)sin(B)sin(G) + cos(A)cos(G)  cos(A)sin(B)sin(G) - sin(A)cos(G) ] [y]
    # [ -sin(B)       sin(A)cos(B)                       cos(A)cos(B)                      ] [z]

    new_x = x * (cosB * cosG)  +  y * (sinA * sinB * cosG - cosA * sinG)  +  z * (cosA * sinB * cosG + sinA * sinG) + center[0]
    new_y = x * (cosB * sinG)  +  y * (sinA * sinB * sinG + cosA * cosG)  +  z * (cosA * sinB * sinG - sinA * cosG) + center[1]
    new_z = x * (-sinB)        +  y * (sinA * cosB)                       +  z * (cosA * cosB)                      + center[2]

    new_point = [new_x, new_y, new_z]
    return new_point

def project_sphere(radius, center):
    distance = math.sqrt((center[0] - settings.FOCUS_POINT[0])**2 + (center[1] - settings.FOCUS_POINT[1])**2 + (center[2] - settings.FOCUS_POINT[2])**2)
    theta = math.asin(-radius / distance)
    circle_angular_diameter = 2 * math.atan((radius * math.cos(theta)) / (radius * math.sin(theta) + distance))
    screen_angular_diameter = 2 * math.atan((settings.SCREEN_WIDTH / 2) / - settings.FOCUS_POINT[2])

    projected_center = project(center)
    projected_radius = (settings.SCREEN_WIDTH / 2) * (circle_angular_diameter / screen_angular_diameter)

    return [projected_center[0] - projected_radius, projected_center[1] - projected_radius, 2 * projected_radius, 2 * projected_radius]