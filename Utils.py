import cv2 as cv
import numpy as np
import math

def get_max_distances(boundary_matrix):
    max_dist = 0
    for i in range(len(boundary_matrix)):
        for j in range(len(boundary_matrix)):
            dist = math.dist(boundary_matrix[i], boundary_matrix[j])
            if dist > max_dist:
                max_dist = dist
    return max_dist

def get_edge_dist(image):
    x,y = image.shape[:2]
    area = 0
    boundary_matrix = []
    for j in range(y):
        x_list = []
        for i in range(x):    
            if image[i,j] != 0:
                boundary_matrix.append([i,j])
    
    np.array(boundary_matrix)

    max_dist = get_max_distances(boundary_matrix)
    
    return max_dist
    
def get_row_area(col):
    area = 0
    # print(len(col))
    for v in range(len(col)-1):
        area += abs(col[v]-col[v+1])

    return area
def get_edge_area(image):
    x,y = image.shape[:2]
    area = 0
    boundary_matrix = []
    for j in range(y):
        x_list = []
        for i in range(x):    
            if image[i,j] != 0:
                x_list.append(i)
        boundary_matrix.append(x_list)

    area = 0
    for col in boundary_matrix:
        if col:
            area += get_row_area(col)

    # print(area)
    return area