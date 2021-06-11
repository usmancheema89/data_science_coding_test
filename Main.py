import cv2 as cv
import Utils


# Reading Images
print('Loading images...')
im1 = cv.imread('apple_1.png',cv.IMREAD_UNCHANGED)
im2 = cv.imread('apple_2.png',cv.IMREAD_UNCHANGED)
#changing Images to grey and saving them
print('Converting to gray scale...')
alpha_mask = im1[:,:,3] == 0
im1[alpha_mask] = [255, 255, 255, 255]
im1 = cv.cvtColor(im1, cv.COLOR_BGRA2BGR)
im1_grey =  cv.cvtColor(im1, cv.COLOR_BGR2GRAY) 

alpha_mask = im2[:,:,3] == 0
im2[alpha_mask] = [255, 255, 255, 255]
im2 = cv.cvtColor(im2, cv.COLOR_BGRA2BGR)
im2_grey =  cv.cvtColor(im2, cv.COLOR_BGR2GRAY)

cv.imwrite('./Result_Images/apple_1_grey.jpg', im1_grey)
cv.imwrite('./Result_Images/apple_2_grey.jpg', im2_grey)

#edge detection on Images and saving the results
im1 = cv.medianBlur(im1,7)
edge1 = cv.Canny(im1,200,400,5)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (11,11))
edge1= cv.morphologyEx(edge1, cv.MORPH_CLOSE, kernel)
cv.imwrite('./Result_Images/apple_1_edges.jpg', edge1)
im2 = cv.medianBlur(im2,7)
edge2 = cv.Canny(im2,300,400,11)
cv.imwrite('./Result_Images/apple_2_edges.jpg', edge2)
print('Gray scale images saved...')

#Calculating the area using a modified point in polygon method
print('Calculating area of the images...')
area1 = Utils.get_edge_area(edge1)
area2 = Utils.get_edge_area(edge2)
area_ratio = area1/area2
print('Area of Apple in image 1:', area1, ' px')
print('Area of Apple in image 2:', area2, ' px')
print('Area Ratio: %.2f' %(area_ratio))

#calculating the max distance between two points on the edges
dist1 = Utils.get_edge_dist(edge1)
dist2 = Utils.get_edge_dist(edge2)
dis_ratio = dist1/dist2
print('Max Edge distance in image 1: %.1f px' %(dist1))
print('Max Edge distance in image 2: %.1f px' %(dist2))
print('Distance Ratio: %.2f' %(dis_ratio))
