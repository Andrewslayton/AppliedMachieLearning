import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_template(main_image, find_image):
    h_temp1, w_temp1 = main_image.shape
    h_temp2, w_temp2 = find_image.shape
    result = np.zeros((h_temp1 - h_temp2 + 1, w_temp1 - w_temp2 + 1))
    for i in range(h_temp1 - h_temp2 + 1):
        for j in range(w_temp1 - w_temp2 + 1):
            calc_image = main_image[i:i+h_temp2, j:j+w_temp2]
            result[i, j] = np.sum((calc_image - find_image) ** 2)
    result = cv2.normalize(result, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return min_loc, result

find_image = cv2.imread(r'C:\Users\the tank\Downloads\powerpointBird.png', cv2.IMREAD_GRAYSCALE)
main_image = cv2.imread(r'C:\Users\the tank\Downloads\powerpointBirdTemplate.png', cv2.IMREAD_GRAYSCALE)
location, result_matrix = find_template(main_image, find_image)
print("Image Found:", location)
plt.imshow(result_matrix)
plt.show()
